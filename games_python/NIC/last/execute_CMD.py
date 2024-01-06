import time
import sys
import paramiko
import getopt
import re

ip_address = 'WARNING !!!'
username = 'WARNING !!!'
psw = 'WARNING !!!'
command = 'WARNING !!!'
try:
    opts, args = getopt.getopt(sys.argv[1:],"d:u:p:c:",["DEVICE=","username=", "password=", "command="]) # the options of the script
except getopt.GetoptError:
    print('execute_CMD.py --DEVICE <ip_address> --usersame <username> --password <psw> --command <command_to_execute>')
    sys.exit(2)
for opt, arg in opts:
    if opt in ("-d", "--DEVICE"):
        ip_address = arg
    elif opt in ("-u", "--username"):
        username = arg
    elif opt in ("-p", "--password"):
        password = arg
    elif opt in ("-c", "--command"):
        command = arg

# python3 execute_CMD.py --DEVICE 192.168.32.134 --username user --password user --command "sudo ping -i 0.005 -c 1000 127.0.0.1"

class ParamikoHandler:
    ssh = "" # to initialise
    def __init__(self, host_ip, uname, psw):
        try:
            self.ssh = paramiko.SSHClient()
            self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            self.ssh.connect(host_ip, username=uname, password=psw, look_for_keys=False, allow_agent=False)
        # in case there is an error while trying to establish the connection
        except (paramiko.BadHostKeyException, paramiko.AuthenticationException, paramiko.SSHException) as exception:
            print(str(exception))
            sys.exit(-1) # to exit the program

    def executeCmd(self):
        try:
            channel = self.ssh.invoke_shell() # you are using a blackbox where you see just the input and the output
            timeout = 20 # timeout is in seconds
            channel.settimeout(timeout) # to get the exit when timeout is over
            newline        = '\n'
            line_buffer    = ''
            channel_buffer = ''
            TIME_LIMIT = ''
            time.sleep(1)
            channel.send(cmd + newline) # the input for the blackbox
            time.sleep(7) # wait the creation of the output file.txt
            self.ssh.close() # to close the ssh connection with the Device
            while True:
                channel_buffer = channel.recv(1).decode("ISO-8859-1") # the output of the blackbox
                if len(channel_buffer) == 0:
                    break
                if channel_buffer != '\n':
                    line_buffer += channel_buffer
                else:
                    with open('RESULTS.txt', 'w') as f:
                        f.write(line_buffer) # to write the output in RESULTS.txt
                    with open('RESULTS.txt', 'r') as f:
                        TIME_LIMIT = re.search(r'time (\d+)ms', f.read())
                        if TIME_LIMIT:
                                print("--- " + host_ip + " ping statistics ---")
                                print(line_buffer)
                                print()
                                break
                    line_buffer = ''
        except paramiko.SSHException as exception:
            print(str(exception))
            sys.exit(-1)

print('=================================================================')
print('connecting via SSH in the HA ip : {}, with username = {} and password = {}'.format(ip_address, username, password))
print('executing this command:', command)
print()
host_ip = ip_address # the Device IP where we want to connect
uname = username # the username of the Device
psw = password # the password of the Device
cmd = command # the command that we send
print(cmd)
print('=================================================================')
print()
conn_obj = ParamikoHandler(host_ip, uname, password)
conn_obj.executeCmd()
