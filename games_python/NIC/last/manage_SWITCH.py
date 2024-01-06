############# Manage the Switch ###########

import time
import sys
import paramiko
import getopt

ip_address_SWITCH = 'WARNING !!!'
username_SWITCH = 'WARNING !!!'
password_SWITCH = 'WARNING !!!'
port_number_SWITCH = 'WARNING !!!'
action = 'WARNING !!!'
try:
    opts, args = getopt.getopt(sys.argv[1:],"s:u:p:n:a:",["SWITCH=","username=", "password=", "port_number=", "action="]) # the options of the script
except getopt.GetoptError:
    print('manage_SWITCH.py --SWITCH <ip_address_SWITCH> --username <username_SWITCH> --password <password_SWITCH> --port_number <port_number_SWITCH> --action <"enable" OR "disable">')
    sys.exit(2)
for opt, arg in opts:
    if opt in ("-s", "--SWITCH"):
        ip_address_SWITCH = arg
    if opt in ("-u", "--username"):
        username_SWITCH = arg
    if opt in ("-p", "--password"):
        password_SWITCH = arg
    elif opt in ("-n", "--port_number"):
        port_number_SWITCH = arg
    elif opt in ("-a", "--action"):
        action = arg

if action == 'enable':
    action = 'no shutdown'
elif action == 'disable':
    action = 'shutdown'

class sampleParamiko:
    ssh = "" # to initialise
    def __init__(self, host_ip, uname, psw):
        try:
            self.ssh = paramiko.SSHClient()
            self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            self.ssh.connect(host_ip, username=uname, password=psw, allow_agent=False)
        # in case there is an error while trying to establish the connection
        except (paramiko.BadHostKeyException, paramiko.AuthenticationException, paramiko.SSHException) as exception:
            print(str(exception))
            sys.exit(-1) # to exit the program

    def ececuteCmd(self):
        try:
            channel = self.ssh.invoke_shell() # you are using a blackbox where you see just the input and the output
            timeout = 10 # timeout is in seconds
            channel.settimeout(timeout) # to get the exit when timeout is over
            newline        = '\n'
            line_buffer    = ''
            channel_buffer = ''
            time.sleep(1)
            channel.send(cmd + newline) # the input for the blackbox
            time.sleep(6) # wait 6 seconds
            self.ssh.close() # to close the ssh connection with the Device
        except paramiko.SSHException as exception:
            print(str(exception))
            sys.exit(-1)
print('=================================================================')
print('connecting via SSH in the SWITCH ip:', ip_address_SWITCH)
print('to {} the port {}:'.format(action, port_number_SWITCH))
print('=================================================================')
print()
host_ip = ip_address_SWITCH # the Device IP where we want to connect
uname = username_SWITCH # the username of the Device
password = password_SWITCH # the password of the Device
cmd = 'enable \r configure \r interface 1/' + port_number_SWITCH + '\r ' + action + ' \r exit \r exit \r logout'
conn_obj = sampleParamiko(host_ip, uname, password)
conn_obj.ececuteCmd()


# python3 Scripts/execute_CMD.py --DEVICE 192.168.200.21 --username user --password user --command "sudo ping -i 0.005 -c 1000 192.168.1.216" & sleep 5
# python3 Scripts/manage_SWITCH.py --SWITCH 192.168.1.213 --username admin --password private --port_number 7 --action disable
# sleep 3s
# python3 Scripts/manage_SWITCH.py --SWITCH 192.168.1.213 --username admin --password private --port_number 7 --action enable
# sleep 8s
