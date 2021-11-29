#Dependencies:
#Python 3.7 32 bit
#PyVisa 1.7
#
#JAC: 03/31/2020
#-Added \n to write and read terminations
 
import visa
import time # for sleep
import binascii

#################################################################################################
# Command list can be found here, sec 3.3
#     https://int.siglent.com/upload_file/user/SPD1000X/SPD1000X_UserManual_UM0501X-E02A.pdf
#################################################################################################
 
def main():
    rm = visa.ResourceManager()
   
    # Go to Device Manager, Events tab, Information section
    # VID and PID from stock code were correct, needed the last string
    instadd = 'USB0::0xF4EC::0x1410::SPD13CBD3R0312::INSTR'
    
    inst = rm.open_resource(instadd)
    inst.write_termination='\n'
    inst.read_termination='\n'
    print (rm.list_resources())
    time.sleep(0.04)
    inst.write('VOLTage 11')
    time.sleep(0.04)    #Need to have a pause between commands or 
    #                   subsequent ones won't execute.
    inst.write('OUTP CH1,ON')
    time.sleep(2)
    inst.write('OUTP CH1,OFF')
    time.sleep(2)
    inst.write('*IDN?')
    #print ("here")
    time.sleep(1)
    qStr = inst.read()
    print (str(qStr))
    inst.close()
    
if __name__ == '__main__':
    main()