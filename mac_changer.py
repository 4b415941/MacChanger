import subprocess

import optparse

import re

#regex 101 kullanımı için



def get_user_input():

    parse_object = optparse.OptionParser()

    parse_object.add_option("-i","--interface",dest="interface",help="interface to change")

    parse_object.add_option("-m","--mac",dest="mac_address",help="get new mac address")



    return parse_object.parse_args()



#interface = "eth0"

#mac_address="00:22:33:55:77:88"



def change_mac_address(user_interface,user_mac_address):

    subprocess.call(["ifconfig",user_interface,"down"])

    subprocess.call(["ifconfig",user_interface,"hw","ether",user_mac_address])

    subprocess.call(["ifconfig",user_interface,"up"])



def control_new_mac(interface):

    ifconfig = subprocess.check_output(["ifconfig",interface])

    new_mac = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w",str(ifconfig))

    if new_mac:

        return new_mac.group(0) #bu grup içinde gelen ilk sonucu bana döndür "0" string olarak döndürmediği için.

    else:

        return None



print("MyMacChanger Started!")



(user_input,arguments) = get_user_input() #tuple olarak kaydettiği için.

change_mac_address(user_input.interface,user_input.mac_address)



finalized_mac = control_new_mac(str(user_input.interface))



if finalized_mac == user_input.mac_address:

    print("Success")

else:

    print("error")
