import subprocess
import random
import optparse
import re
import time

def get_user_input():
    parse_object = optparse.OptionParser()
    parse_object.add_option("-i","--interface",dest="interface",help="enter interface")
    return parse_object.parse_args()

def get_new_mac():
    charList = "123456789ABCDEF"
    new_mac = ""
    for i in range(12):
        new_mac += random.choice(charList)
        if (i+1)%2 == 0 and (i != 11):
            new_mac += ":"
    return new_mac

def change_mac_address(user_interface,user_mac_address):
    subprocess.call(["ifconfig",user_interface,"down"])
    subprocess.call(["ifconfig",user_interface,"hw","ether",user_mac_address])
    subprocess.call(["ifconfig",user_interface,"up"])
    time.sleep(1)

def control_mac_address(interface):
    try:
        result = subprocess.run(["ip", "link", "show", interface], capture_output=True, text=True, check=True)
        mac_address = re.search(r"ether\s+([0-9a-fA-F:]+)", result.stdout).group(1)
        return mac_address
    except Exception as e:
        print("Error:", e)
        return None

user_input,args = get_user_input()
generated_mac = get_new_mac()
change_mac_address(user_input.interface,generated_mac)
time.sleep(1)
finalized_mac = control_mac_address(user_input.interface)

if finalized_mac is not None:
    if finalized_mac == generated_mac:
        print("Success!!!")
    else:
        print("Error!!!",finalized_mac)
else:
    print("Error: MAC address couldn't be retrieved.")
