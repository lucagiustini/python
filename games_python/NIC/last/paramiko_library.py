import time
import sys
import paramiko
import subprocess
import getopt
import re


class CommandLineInterface:

    def test_ssh_connection(self, ip_address, username, password):
        ssh_command = f'ssh {username}@{ip_address} "echo successful"'
        try:
            subprocess.check_output(ssh_command, shell=True, timeout=5)
        except subprocess.CalledProcessError:
            # print("SSH connection failed. Test successful!")
            result = True
            return result
        except subprocess.TimeoutExpired:
            # print("SSH connection timed out. Test successful!")
            result = True
            return result
        else:
            # print("SSH connection successful. Test failed!")
            result = False
            return result


class ParamikoHandler:

    def test_sshConnection(self, host_ip, username, password):
        ssh = '' # to initialise
        #channel = None # to initialise
        try:
            self.ssh = paramiko.SSHClient()
            channel = self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            channel = self.ssh.connect(host_ip, username=username, password=password, look_for_keys=False, allow_agent=False)
            channel = self.ssh.invoke_shell() # you are using a blackbox where you see just the input and the output
            timeout = 20 # to exit from the ssh connection after 20 seconds
            channel.settimeout(timeout) # to get the exit when timeout is over
        except (paramiko.BadHostKeyException, paramiko.AuthenticationException, paramiko.SSHException, paramiko.ssh_exception.NoValidConnectionsError) as exception:
            print(f"SSH connection error: {exception}")
            sys.exit(-1)
        return channel

    def test_sendMessage(self, cmdtosend, channel):
        newline        = '\n'
        time.sleep(1)
        channel.send(cmdtosend + newline)
        return channel

    def test_manageSwitch(self, onoff, channel):
        newline        = '\n'
        time.sleep(1)
        channel.send(onoff + newline) # turn on or off the switch
        time.sleep(6) # wait 6 seconds
        channel.close() # to close the ssh connection with the switch

    def test_receiveMessage(self, cmdtoreceive, channel):
        result = None
        parse = None
        output    = ''
        channel_buffer = ''
        assertion = False
        time.sleep(7) # wait the end of the while cycle before the channel.close()
        channel.close() # to close the ssh connection with the Device before the loop
        while not result:
            channel_buffer = channel.recv(1).decode("ISO-8859-1") # the output of the blackbox
            if len(channel_buffer) == 0:
                break
            if channel_buffer != '\r':
                output += channel_buffer
            else:
                #result = re.search(r'time (\d+)ms', line_buffer) # parsing the line_buffer output
                result = re.search(r'{}'.format(cmdtoreceive), output) # parsing the line_buffer output
                if result:
                    print(output)
                    print()
                    break # to exit the while cycle when I reach result = True
                output = ''
        return output # assertion, parse, line_buffer

    def test_parseResult(self, output, cmdtoparse):
        print()
        result = re.search(r'{}'.format(cmdtoparse), output) # parsing the line_buffer output to get the time spent
        return int(result.group(1))
