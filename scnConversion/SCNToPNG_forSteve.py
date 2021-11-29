import numpy as np
import os
#import boto3 #AWS
import json
import sys

#for scn to png processing
import re # Regular Expressions, https://docs.python.org/2/library/re.html
import xml.etree.ElementTree as ElementTree
import numpy as np
from PIL import Image

#location of scn file
filePath = 'CDMP_BSV_Gelred UNI.scn'

def main(filePath): #scn    
    #prep the image
    filePath = filePath
    theImage = filePath
    
    #load the scn image as binary
    file=open(theImage,'rb') #rb mode sets binary read, wb binary write
    try:
        file_boundary = read_until_boundary_definition(file)
    except UnicodeDecodeError:
        pass

    #Parse the header
    theHeader = image_header(file,file_boundary)
    
    #How many channels in image, which we now know, because we we created the dictionary above
    channel_count = int(theHeader['channel_count'])
    
    if (not channel_count) or channel_count <0 or channel_count > 3:
        channel_count = 1
    
    #this is a path with base file name.
    #the first pngImage is a folder, the second pngImag is a base file name
    pngPath = 'pngImage/pngImage'
    for current_channel in range(0,channel_count):
        image_channel(file, current_channel,theHeader,pngPath)   
            
    file.close()
    
    
   
# UTIL  FUNCTIONS REQUIRED FOR PROCESSING A SINGLE SCN FILE AND CONVERTING IT TO A PNG AT MAXIMUM RESOLUTION AND QUALITY

#string that is used when parsing the XML tree for keyword and values
IL_ATTRIBUTE_STRING = 'il_attribute_tag'

#one of the functions creates a variable that is used by a second function.  
#need to make that variable global so it can be defined in first function and used in the second
img_content_length = 1

# at the top of a bio-rad scn file, 'boundary = XXXXXX' is present
# this function outputs what the boundary value is
# important: this only works for files that were created from a Bio-Rad product, so I use a try exception
# that last cell of this notebook runs this function only, to get a sense of what it does.
def read_until_boundary_definition(file):
    boundary_reg_ex = 'boundary=\"(.+)\"'
    boundary_string = 'boundary'
    
    p = re.compile(boundary_reg_ex)
    while True:
        line = file.readline().decode()
        if line == '':
            return None
        if boundary_string not in line:
            continue
        matches = p.search(line)
        if not matches:
            continue
        return matches.group(1)

def string_to_boundary_line(file,file_boundary):
    total_str = ''
    while True:
        line = file.readline().decode()
        if line == '':
            return False
        if file_boundary not in line:
            total_str += line
        else:
            break
    return total_str

#step down the lines of the file until you arrive at the boundary
def go_to_boundary_line(file, file_boundary):
    while True:
        line = file.readline().decode()
        if line == '':
            return False
        if file_boundary in line:
            return True

#important point.  This is a recursive function, because some elements in the tree have children of children.
#the output of this function is also important for secondary machine learning problems, because it creates
# a dictionary of the header elements, which we could use for "tagging" at the moment of data upload at aihub
def parse_child_elements(element_tree):
    element_data = {}
    
    for child in element_tree:
        child_element = element_tree.find(child.tag)
        if not child_element:
            if child.text:
                element_data[child.tag] = child.text
            elif child_element.attrib:
                element_data[child.tag] = {}
                element_data[child.tag][IL_ATTRIBUTE_STRING] = child_element.attrib
            else:
                element_data[child.tag] =''
        else:
            element_data[child.tag] = parse_child_elements(child_element)
    
    return element_data
        
def parse_xml_data(file,file_boundary):
    #find begining of XML document
    for raw_line in file:
        line = raw_line.decode()
        if '<!DOCTYPE XML>' in line:
            break
    
    file_xml = string_to_boundary_line(file, file_boundary)
    if not file_xml:
        return None
    
    root = ElementTree.fromstring(file_xml)
    if not root:
        return None
    
    return parse_child_elements(root)

#important note.  This function updates the global img_content_length.  Needed for image redimension by x,y
def parse_image_channel_header(file):
    #find the image content length
    p= re.compile('Content-Length: (.+)')
    while True:
        line = file.readline().decode()
        if line == '':
            return False
        if 'Content-Length: ' not in line:
            continue
        matches = p.search(line)
        if not matches:
            continue
        content_length = matches.group(1)
        
        #saved the content length
        global img_content_length
        img_content_length = int(content_length)
        
        
        #now skip to the end of the header
        while True:
            line = file.readline().decode()
            if line == '':
                return False
            if line =='\r\n':
                return True
   

def parse_channel_image_channel_raw_data(file,raw_data_file_name,img_content_length):
    chunk_size = 128
    raw_file = open(raw_data_file_name, 'wb')
    
    #write the raw data in chunk_size chunks
    size_remaining = img_content_length
    while size_remaining > 0:
        chunk = file.read(chunk_size)
        size_remaining -= chunk_size
        if chunk == '':
            return False
        raw_file.write(chunk)
    raw_file.close()
    return True


def build_lookup_table(min_value,max_value):
    lut_size = 2 ** 16
    lut = np.empty(lut_size, dtype='uint8')
    
    if min_value > 0:
        for x in range(0, min_value):
            lut[x] = 255
    
    lut_transition_size = max_value - min_value
    for x in range(min_value, max_value):
        #normally this does not include "255 -" i put this in to reverse image range 
        lut[x] =255 - int((255 * (x - min_value)) / lut_transition_size)
        
    if max_value < lut_size:
        for x in range(max_value, lut_size):
            lut[x] = 0
    return lut

def raw16_to_raw8(raw16_file_path, min_value, max_value):
    lut = build_lookup_table(min_value, max_value)
    
    rawfile16 = open(raw16_file_path, 'rb')
    data16 = np.fromfile(rawfile16, dtype=np.uint16)
    rawfile16.close()
    
    data8 = np.take(lut, data16,mode='clip')
    raw8_path = os.path.splitext(raw16_file_path)[0]+'.raw8'
    data8.tofile(raw8_path)
    return True

def raw8_to_pngs(raw8_file_path, width,height):
    base_png_path = os.path.join(os.path.dirname(raw8_file_path),os.path.basename(raw8_file_path))
    try:
        raw8_file = open(raw8_file_path, 'rb')
        raw8_data = raw8_file.read()
        raw8_file.close()
        
        img = Image.frombytes('L', (width,height),raw8_data,'raw','L')
        img.save(os.path.splitext(base_png_path)[0] + '.png',"PNG",quality=100)
        
        return True
    except Exception as e:
        print (e)
    return False

def create_pngs(file_path,size,transform_data):
    raw16_to_raw8(file_path,transform_data['min_value'],transform_data['max_value'])
    
    raw8_path = os.path.splitext(file_path)[0] + '.raw8'
    raw8_to_pngs(raw8_path, size[0], size[1])
                  

#important function that starts the process of reading the scn file
def image_header(file,file_boundary):
    #move to the first boundary line
    go_to_boundary_line(file, file_boundary)
    
    #now that you are at correct line, parse the header data and create dictionary called
    #header_data
    header_data = parse_xml_data(file,file_boundary)
    return (header_data)        
        
# big one that has a lot of error checking of prior functions when strung together
def image_channel(file,current_channel,header_data,pngPath):
    #print ('Begin processing Channel ', str(current_channel))
    channel_boundary = read_until_boundary_definition(file)
    if not channel_boundary:
        file.close()
        print('Failed to find Channel ', str(current_channel), ' boundary definition')
        return False
    #print (channel_boundary)
    
    if not go_to_boundary_line(file, channel_boundary):
        file.close()
        print('Failed to move to header boundary line')
        return False
    
    if not parse_image_channel_header(file):
        file.close()
        print('Failed to parse channel header')
        return False
        
    #raw_data_file_name = 'channel_'+str(current_channel + 1) + '.raw16'
    raw_data_file_name = pngPath + '.raw16'
    if not parse_channel_image_channel_raw_data(file,raw_data_file_name,img_content_length):
        file.close()
        print('Failed to parse raw data')
        return False
    
    #not sure if this try catch is necessary.  I put this in.  It's not a part of original code
    try:
        channel_data = parse_xml_data(file, channel_boundary)
    except UnicodeDecodeError:
        print ('failed to find file_boundary in',scnPathList[y])
        pass
    else:      
        size = (int(channel_data['size_pix'][IL_ATTRIBUTE_STRING]['width']),
               int(channel_data['size_pix'][IL_ATTRIBUTE_STRING]['height']))
        data_ceiling = float(channel_data['scanner'][IL_ATTRIBUTE_STRING]['data_ceiling'])
    
        transform_data = dict()
        transform_data['min_value']=int(float(header_data['scan_' + str(current_channel)]['transform'][IL_ATTRIBUTE_STRING]['low_frac'])* data_ceiling)
        transform_data['max_value']=int(float(header_data['scan_' + str(current_channel)]['transform'][IL_ATTRIBUTE_STRING]['high_frac'])* data_ceiling)
    
        scan_raw_image_to_png = create_pngs(raw_data_file_name, size, transform_data)
    
        return True

#I did not use this function
def image_protocol(file,file_boundary):
    #move to the next file boundary line
    if not go_to_boundary_line(file,file_boundary):
        file.close()
        print('Failed to find protocol boundary line')
        return False
    
    # get the XML text from here to the next boundary line
    image_protocol = parse_XML_data(file,file_boundary)
    if not image_protocol:
        file.close()
        print('Failed to parse protocol XML')
        return False
    
    # write the header data dictionary as a json file
    
    return True

if __name__ == '__main__':
    main(filePath)
