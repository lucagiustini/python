#!/usr/bin/env python3
import time
import os
import sys
import NIC_Bonding_Configuration

# add parent folder to python path
sys.path.insert(1, os.path.realpath(os.path.pardir))
from tests import paramiko_library

""""""""""""""""""""""""""""""
# Local variables definition
HALeftFail = paramiko_library.CommandLineInterface()
HARightFail = paramiko_library.CommandLineInterface()
HALeft = paramiko_library.ParamikoHandler()
HARight = paramiko_library.ParamikoHandler()
SWITCH1 = paramiko_library.ParamikoHandler()
SWITCH2 = paramiko_library.ParamikoHandler()
""""""""""""""""""""""""""""""

class TestClass:

    # Initialize Test Result
    result = ""
    result_0 = ""
    result_1 = ""
    result_2 = ""
    result_3 = ""
    result_4 = ""
    result_5 = ""
    channel = ""
    output = ""
    
    
    ############# Testing the No Communication between HAs and CRD ####################
    #############             TESTING 1st CASE                     ####################

    ############# SWITCH_1 OFF PORTS A and B  ####################
    def test_SWITCH_1_OFF_A_B(self):

        channel1 = SWITCH1.test_sshConnection(
            NIC_Bonding_Configuration.TARGETS["SWITCH_1"]["ip_address"],
            NIC_Bonding_Configuration.TARGETS["SWITCH_1"]["user_name"],
            NIC_Bonding_Configuration.TARGETS["SWITCH_1"]["psw"])
        channel1 = SWITCH1.test_sendMessage(NIC_Bonding_Configuration.OFF_PORT_A, channel1)

        # sleep 2 seconds
        time.sleep(2)

        channel2 = SWITCH1.test_sshConnection(
            NIC_Bonding_Configuration.TARGETS["SWITCH_1"]["ip_address"],
            NIC_Bonding_Configuration.TARGETS["SWITCH_1"]["user_name"],
            NIC_Bonding_Configuration.TARGETS["SWITCH_1"]["psw"])
        channel2 = SWITCH1.test_sendMessage(NIC_Bonding_Configuration.OFF_PORT_B, channel2)

    # sleep 10 second
    time.sleep(10)

    ############# SWITCH_2 OFF PORTS A and B  ####################
    def test_SWITCH_2_OFF_A_B(self):

        channel1 = SWITCH2.test_sshConnection(
            NIC_Bonding_Configuration.TARGETS["SWITCH_2"]["ip_address"],
            NIC_Bonding_Configuration.TARGETS["SWITCH_2"]["user_name"],
            NIC_Bonding_Configuration.TARGETS["SWITCH_2"]["psw"])
        channel1 = SWITCH2.test_sendMessage(NIC_Bonding_Configuration.OFF_PORT_A, channel1)

        # sleep 2 seconds
        time.sleep(2)

        channel2 = SWITCH2.test_sshConnection(
            NIC_Bonding_Configuration.TARGETS["SWITCH_2"]["ip_address"],
            NIC_Bonding_Configuration.TARGETS["SWITCH_2"]["user_name"],
            NIC_Bonding_Configuration.TARGETS["SWITCH_2"]["psw"])
        channel2 = SWITCH2.test_sendMessage(NIC_Bonding_Configuration.OFF_PORT_B, channel2)

    # sleep 10 seconds
    time.sleep(10)

    # test ping CRD from HA Left
    def test_HA_Left_0(self):

        # connection ssh
        result_0 = HALeftFail.test_ssh_connection(
            NIC_Bonding_Configuration.TARGETS["HA_Left"]["ip_address"],
            NIC_Bonding_Configuration.TARGETS["HA_Left"]["user_name"],
            NIC_Bonding_Configuration.TARGETS["HA_Left"]["psw"]
            )

        # sleep 6 seconds before parsing the result
        time.sleep(6)

        if result_0 == False:
            print("Target : {} : SSH connection failed. Test successful!".format(NIC_Bonding_Configuration.TARGETS["HA_Left"]["ip_address"]))
            assert result_0
        else:
            print("Target : {} : SSH connection successful. Test failed!".format(NIC_Bonding_Configuration.TARGETS["HA_Left"]["ip_address"]))
            assert result_0
        print('=================================================================')
        return result_0

    # test ping CRD from HA Right
    def test_HA_Right_1(self):

        # connection ssh
        result_1 = HARightFail.test_ssh_connection(
            NIC_Bonding_Configuration.TARGETS["HA_Right"]["ip_address"],
            NIC_Bonding_Configuration.TARGETS["HA_Right"]["user_name"],
            NIC_Bonding_Configuration.TARGETS["HA_Right"]["psw"]
            )

        # sleep 6 seconds before parsing the result
        time.sleep(6)

        if result_1 == False:
            print("Target : {} : SSH connection failed. Test successful!".format(NIC_Bonding_Configuration.TARGETS["HA_Left"]["ip_address"]))
            assert result_1
        else:
            print("Target : {} : SSH connection successful. Test failed!".format(NIC_Bonding_Configuration.TARGETS["HA_Left"]["ip_address"]))
            assert result_1
        print('=================================================================')
        return result_1

    # sleep 15 seconds
    time.sleep(15)

    ############# SWITCH_1 ON PORTS A and B  ####################

    def test_SWITCH_1_ON_A_B(self):
            
            channel1 = SWITCH1.test_sshConnection(NIC_Bonding_Configuration.TARGETS["SWITCH_1"]["ip_address"],
                                                    NIC_Bonding_Configuration.TARGETS["SWITCH_1"]["user_name"],
                                                    NIC_Bonding_Configuration.TARGETS["SWITCH_1"]["psw"])
            channel1 = SWITCH1.test_sendMessage(NIC_Bonding_Configuration.ON_PORT_A, channel)

            # sleep 2 seconds
            time.sleep(2)

            channel2 = SWITCH1.test_sshConnection(NIC_Bonding_Configuration.TARGETS["SWITCH_1"]["ip_address"],
                                                    NIC_Bonding_Configuration.TARGETS["SWITCH_1"]["user_name"],
                                                    NIC_Bonding_Configuration.TARGETS["SWITCH_1"]["psw"])
            channel2 = SWITCH1.test_sendMessage(NIC_Bonding_Configuration.ON_PORT_B, channel2)

    # sleep 10 seconds
    time.sleep(10)

    ############# SWITCH_2 ON PORTS A and B  ####################

    def test_SWITCH_2_ON_A_B(self):
            
            channel1 = SWITCH2.test_sshConnection(NIC_Bonding_Configuration.TARGETS["SWITCH_2"]["ip_address"],
                                                    NIC_Bonding_Configuration.TARGETS["SWITCH_2"]["user_name"],
                                                    NIC_Bonding_Configuration.TARGETS["SWITCH_2"]["psw"])
            channel1 = SWITCH2.test_sendMessage(NIC_Bonding_Configuration.ON_PORT_A, channel1)

            # sleep 2 seconds
            time.sleep(2)

            channel2 = SWITCH2.test_sshConnection(NIC_Bonding_Configuration.TARGETS["SWITCH_2"]["ip_address"],
                                                    NIC_Bonding_Configuration.TARGETS["SWITCH_2"]["user_name"],
                                                    NIC_Bonding_Configuration.TARGETS["SWITCH_2"]["psw"])
            channel2 = SWITCH2.test_sendMessage(NIC_Bonding_Configuration.ON_PORT_B, channel2)

    # sleep 20 seconds before to test the 1st case
    time.sleep(20)
    

    ############# HA_Left + SWITCH_1 ####################
    ############# TESTING 2nd CASE   ####################

    # test ping CRD from HA Left
    def test_HA_Left_2(self):

        # connection ssh
        channel = HALeft.test_sshConnection(
            NIC_Bonding_Configuration.TARGETS["HA_Left"]["ip_address"],
            NIC_Bonding_Configuration.TARGETS["HA_Left"]["user_name"],
            NIC_Bonding_Configuration.TARGETS["HA_Left"]["psw"]
            )
        # sending command
        channel = HALeft.test_sendMessage(
            NIC_Bonding_Configuration.COMMAND_TO_SEND_HA_LEFT,
            channel)
        # receiving command
        self.output = HALeft.test_receiveMessage(
            NIC_Bonding_Configuration.COMMAND_TO_RECEIVE_TIME,
            channel)
        # sleep 15 seconds before parsing the result
        time.sleep(15)
        # parsing command
        result_time = HALeft.test_parseResult(
            self.output,
            NIC_Bonding_Configuration.COMMAND_TO_RECEIVE_TIME) # parsing the line_buffer output to get the time spent
        # result_time = 100 + result_time # FOR TEST FAILURE
        print(" {} [ms] required by the test ".format(result_time))
        result_packet = HALeft.test_parseResult(
            self.output,
            NIC_Bonding_Configuration.COMMAND_TO_RECEIVE_PACKET) # parsing the line_buffer output to get the packet loss
        # result_packet = 1 + result_packet # FOR TEST FAILURE
        print(" {} % packet loss by the test ".format(result_packet))
        print('=================================================================')
        if result_time <= NIC_Bonding_Configuration.TIME_LIMIT and result_packet == NIC_Bonding_Configuration.PACKET_LIMIT:
            result_2 = True
            print("Target : {} : Test Passed".format(NIC_Bonding_Configuration.TARGETS["HA_Left"]["ip_address"]))
            assert result_2
        else:
            result_2 = False
            print("Target : {} : Test Failed".format(NIC_Bonding_Configuration.TARGETS["HA_Left"]["ip_address"]))
            assert result_2
        print('=================================================================')
        return result_2

    # sleep 5 seconds
    time.sleep(5)

    ############# SWITCH_1 OFF PORT A  ####################
    def test_SWITCH_1_OFF_A(self):

        channel = SWITCH1.test_sshConnection(NIC_Bonding_Configuration.TARGETS["SWITCH_1"]["ip_address"],
                                                 NIC_Bonding_Configuration.TARGETS["SWITCH_1"]["user_name"],
                                                 NIC_Bonding_Configuration.TARGETS["SWITCH_1"]["psw"])
        channel = SWITCH1.test_sendMessage(NIC_Bonding_Configuration.OFF_PORT_A, channel)

    # sleep 10 seconds
    time.sleep(10)

    ############# SWITCH_1 ON PORT A   ####################
    def test_SWITCH_1_ON_A(self):

        channel = SWITCH1.test_sshConnection(NIC_Bonding_Configuration.TARGETS["SWITCH_1"]["ip_address"],
                                                 NIC_Bonding_Configuration.TARGETS["SWITCH_1"]["user_name"],
                                                 NIC_Bonding_Configuration.TARGETS["SWITCH_1"]["psw"])
        channel = SWITCH1.test_sendMessage(NIC_Bonding_Configuration.ON_PORT_A, channel)

    # sleep 20 seconds before to test the 2nd case
    time.sleep(20)


    ############# HA_Left + SWITCH_2 ####################
    ############# TESTING 3th CASE   ####################

    def test_HA_Left_3(self):

        # connection ssh
        channel = HALeft.test_sshConnection(
            NIC_Bonding_Configuration.TARGETS["HA_Left"]["ip_address"],
            NIC_Bonding_Configuration.TARGETS["HA_Left"]["user_name"],
            NIC_Bonding_Configuration.TARGETS["HA_Left"]["psw"]
            )
        # sending command
        channel = HALeft.test_sendMessage(
            NIC_Bonding_Configuration.COMMAND_TO_SEND_HA_LEFT,
            channel)
        # receiving command
        self.output = HALeft.test_receiveMessage(
            NIC_Bonding_Configuration.COMMAND_TO_RECEIVE_TIME,
            channel)
        # print (self.output)
        # sleep 15 seconds before parsing the result
        time.sleep(15)
        # parsing command
        result_time = HALeft.test_parseResult(
            self.output,
            NIC_Bonding_Configuration.COMMAND_TO_RECEIVE_TIME) # parsing the line_buffer output to get the time spent
        # result_time = 100 + result_time # FOR TEST FAILURE
        print(" {} [ms] required by the test ".format(result_time))
        result_packet = HALeft.test_parseResult(
            self.output,
            NIC_Bonding_Configuration.COMMAND_TO_RECEIVE_PACKET) # parsing the line_buffer output to get the packet loss
        # result_packet = 1 + result_packet # FOR TEST FAILURE
        print(" {} % packet loss by the test ".format(result_packet))
        print('=================================================================')
        if result_time <= NIC_Bonding_Configuration.TIME_LIMIT and result_packet == NIC_Bonding_Configuration.PACKET_LIMIT:
            result_3 = True
            print("Target : {} : Test Passed".format(NIC_Bonding_Configuration.TARGETS["HA_Left"]["ip_address"]))
            assert result_3
        else:
            result_3 = False
            print("Target : {} : Test Failed".format(NIC_Bonding_Configuration.TARGETS["HA_Left"]["ip_address"]))
            assert result_3
        print('=================================================================')

        return result_3

    # sleep 5 seconds
    time.sleep(5)

    ############# SWITCH_2 OFF   ####################
    def test_SWITCH_2_OFF_A(self):

        channel = SWITCH2.test_sshConnection(NIC_Bonding_Configuration.TARGETS["SWITCH_2"]["ip_address"],
                                                 NIC_Bonding_Configuration.TARGETS["SWITCH_2"]["user_name"],
                                                 NIC_Bonding_Configuration.TARGETS["SWITCH_2"]["psw"])
        channel = SWITCH2.test_sendMessage(NIC_Bonding_Configuration.OFF_PORT_A, channel)

    # sleep 10 seconds
    time.sleep(10)

    ############# SWITCH_2 ON   ####################
    def test_SWITCH_2_ON_A(self):

        channel = SWITCH2.test_sshConnection(NIC_Bonding_Configuration.TARGETS["SWITCH_2"]["ip_address"],
                                                 NIC_Bonding_Configuration.TARGETS["SWITCH_2"]["user_name"],
                                                 NIC_Bonding_Configuration.TARGETS["SWITCH_2"]["psw"])
        channel = SWITCH2.test_sendMessage(NIC_Bonding_Configuration.ON_PORT_A, channel)

    # sleep 20 seconds before to test the 3th case
    time.sleep(20)

    ############# HA_Right + SWITCH_1 ####################
    ############# TESTING 4th CASE    ####################

    def test_HA_Right_4(self):

        # connection ssh
        channel = HARight.test_sshConnection(
            NIC_Bonding_Configuration.TARGETS["HA_Right"]["ip_address"],
            NIC_Bonding_Configuration.TARGETS["HA_Right"]["user_name"],
            NIC_Bonding_Configuration.TARGETS["HA_Right"]["psw"]
            )
        # sending command
        channel = HARight.test_sendMessage(
            NIC_Bonding_Configuration.COMMAND_TO_SEND_HA_RIGHT,
            channel)
        # receiving command
        self.output = HARight.test_receiveMessage(
            NIC_Bonding_Configuration.COMMAND_TO_RECEIVE_TIME,
            channel)
        # print (self.output)
        # sleep 15 seconds before parsing the result
        time.sleep(15)
        # parsing command
        result_time = HARight.test_parseResult(
            self.output,
            NIC_Bonding_Configuration.COMMAND_TO_RECEIVE_TIME) # parsing the line_buffer output to get the time spent
        # result_time = 100 + result_time # FOR TEST FAILURE
        print(" {} [ms] required by the test ".format(result_time))
        result_packet = HARight.test_parseResult(
            self.output,
            NIC_Bonding_Configuration.COMMAND_TO_RECEIVE_PACKET) # parsing the line_buffer output to get the packet loss
        # result_packet = 1 + result_packet # FOR TEST FAILURE
        print(" {} % packet loss by the test ".format(result_packet))
        print('=================================================================')
        if result_time <= NIC_Bonding_Configuration.TIME_LIMIT and result_packet == NIC_Bonding_Configuration.PACKET_LIMIT:
            result_4 = True
            print("Target : {} : Test Passed".format(NIC_Bonding_Configuration.TARGETS["HA_Right"]["ip_address"]))
            assert result_4
        else:
            result_4 = False
            print("Target : {} : Test Failed".format(NIC_Bonding_Configuration.TARGETS["HA_Right"]["ip_address"]))
            assert result_4
        print('=================================================================')
        return result_4

    # sleep 5 seconds
    time.sleep(5)

    ############# SWITCH_1 OFF   ####################
    def test_SWITCH_1_OFF_B(self):

        channel = SWITCH1.test_sshConnection(NIC_Bonding_Configuration.TARGETS["SWITCH_1"]["ip_address"],
                                                 NIC_Bonding_Configuration.TARGETS["SWITCH_1"]["user_name"],
                                                 NIC_Bonding_Configuration.TARGETS["SWITCH_1"]["psw"])
        channel = SWITCH1.test_sendMessage(NIC_Bonding_Configuration.OFF_PORT_B, channel)

    # sleep 10 seconds
    time.sleep(10)

    ############# SWITCH_1 ON   ####################
    def test_SWITCH_1_ON_B(self):

        channel = SWITCH1.test_sshConnection(NIC_Bonding_Configuration.TARGETS["SWITCH_1"]["ip_address"],
                                                 NIC_Bonding_Configuration.TARGETS["SWITCH_1"]["user_name"],
                                                 NIC_Bonding_Configuration.TARGETS["SWITCH_1"]["psw"])
        channel = SWITCH1.test_sendMessage(NIC_Bonding_Configuration.ON_PORT_B, channel)

    # sleep 20 seconds before to test the 4th case
    time.sleep(20)


    ############# HA_Right + SWITCH_2 ####################
    ############# TESTING 5th CASE    ####################

    def test_HA_Right_5(self):

        # connection ssh
        channel = HARight.test_sshConnection(
            NIC_Bonding_Configuration.TARGETS["HA_Right"]["ip_address"],
            NIC_Bonding_Configuration.TARGETS["HA_Right"]["user_name"],
            NIC_Bonding_Configuration.TARGETS["HA_Right"]["psw"]
            )
        # sending command
        channel = HARight.test_sendMessage(
            NIC_Bonding_Configuration.COMMAND_TO_SEND_HA_RIGHT,
            channel)
        # receiving command
        self.output = HARight.test_receiveMessage(
            NIC_Bonding_Configuration.COMMAND_TO_RECEIVE_TIME,
            channel)
        # print (self.output)
        # sleep 15 seconds before parsing the result
        time.sleep(15)
        # parsing command
        result_time = HARight.test_parseResult(
            self.output,
            NIC_Bonding_Configuration.COMMAND_TO_RECEIVE_TIME) # parsing the line_buffer output to get the time spent
        # result_time = 100 + result_time # FOR TEST FAILURE
        print(" {} [ms] required by the test ".format(result_time))
        result_packet = HARight.test_parseResult(
            self.output,
            NIC_Bonding_Configuration.COMMAND_TO_RECEIVE_PACKET) # parsing the line_buffer output to get the packet loss
        # result_packet = 1 + result_packet # FOR TEST FAILURE
        print(" {} % packet loss by the test ".format(result_packet))
        print('=================================================================')
        if result_time <= NIC_Bonding_Configuration.TIME_LIMIT and result_packet == NIC_Bonding_Configuration.PACKET_LIMIT:
            result_5 = True
            print("Target : {} : Test Passed".format(NIC_Bonding_Configuration.TARGETS["HA_Right"]["ip_address"]))
            assert result_5
        else:
            result_5 = False
            print("Target : {} : Test Failed".format(NIC_Bonding_Configuration.TARGETS["HA_Right"]["ip_address"]))
            assert result_5
        print('=================================================================')

        return result_5

    # sleep 5 seconds
    time.sleep(5)

    ############# SWITCH_2 OFF   ####################
    def test_SWITCH_2_OFF_B(self):

        channel = SWITCH2.test_sshConnection(NIC_Bonding_Configuration.TARGETS["SWITCH_2"]["ip_address"],
                                                 NIC_Bonding_Configuration.TARGETS["SWITCH_2"]["user_name"],
                                                 NIC_Bonding_Configuration.TARGETS["SWITCH_2"]["psw"])
        channel = SWITCH2.test_sendMessage(NIC_Bonding_Configuration.OFF_PORT_B, channel)

    # sleep 10 seconds
    time.sleep(10)

    ############# SWITCH_2 ON   ####################
    def test_SWITCH_2_ON_B(self):

        channel = SWITCH2.test_sshConnection(NIC_Bonding_Configuration.TARGETS["SWITCH_2"]["ip_address"],
                                                 NIC_Bonding_Configuration.TARGETS["SWITCH_2"]["user_name"],
                                                 NIC_Bonding_Configuration.TARGETS["SWITCH_2"]["psw"])
        channel = SWITCH2.test_sendMessage(NIC_Bonding_Configuration.ON_PORT_B, channel)

    # sleep 20 seconds before to print the result
    time.sleep(20)


    #############       TEST RESULT        ####################
    """
    def test_NIC_Bonding(self):
        print('=================================================================')
        if result_0 and result_1 and result_2 and result_3 and result_4 and result_5:
            result = True
            print("The NICBONDING is SUCCESS.")
            assert result
        else:
            result = False
            print("The NICBONDING is FAILED.")
            assert result
        print('=================================================================')
    """


# To check the logs of the test in debug mode

if __name__ == "__main__":

    result = ""
    result_0 = ""
    result_1 = ""
    result_2 = ""
    result_3 = ""
    result_4 = ""
    result_5 = ""

    # Call the class
    istance = TestClass()
    
    
    ############# Testing the No Communication between HAs and CRD ####################
    #############             TESTING 1st CASE                     ####################

    print("############# Testing the No Communication between HAs and CRD ####################")
    print("#############             TESTING 1st CASE                     ####################")

    print("   ############# SWITCH_1 OFF PORTS A and B  ####################   ")
    print()
    istance.test_SWITCH_1_OFF_A_B()
    time.sleep(1)

    print("   ############# SWITCH_2 OFF PORTS A and B  ####################   ")
    print()
    istance.test_SWITCH_2_OFF_A_B()

    time.sleep(1)

    print("   ############# HA_Left can't ping CRD   ####################   ")
    print()
    result_0 = istance.test_HA_Left_0()
    time.sleep(5)

    print("   ############# HA_Right can't ping CRD   ####################   ")
    print()
    result_1 = istance.test_HA_Right_1()
    time.sleep(15)

    print("   ############# SWITCH_1 ON PORTS A and B  ####################   ")
    print()
    istance.test_SWITCH_1_ON_A_B()
    time.sleep(1)

    print("   ############# SWITCH_2 ON PORTS A and B  ####################   ")
    print()
    istance.test_SWITCH_2_ON_A_B()

    time.sleep(20)
    
    

    ############# HA_Left + SWITCH_1 ####################
    ############# TESTING 2nd CASE   ####################

    print("   ############# HA_Left + SWITCH_1 ####################   ")
    print("   ############# TESTING 2nd CASE   ####################   ")

    print("   ############# HA_Left ping CRD   ####################   ")
    print()
    result_2 = istance.test_HA_Left_2()
    time.sleep(5)

    print("   ############# SWITCH_1 OFF PORT A   ####################   ")
    print()
    istance.test_SWITCH_1_OFF_A()
    time.sleep(5)

    print("   ############# SWITCH_1 ON PORT A  ####################   ")
    print()
    istance.test_SWITCH_1_ON_A()

    # sleep 20 seconds before to test the 2nd case
    time.sleep(20)


    ############# HA_Left + SWITCH_2 ####################
    ############# TESTING 3th CASE   ####################

    print("   ############# HA_Left + SWITCH_2 ####################   ")
    print("   ############# TESTING 3th CASE   ####################   ")

    print("   ############# HA_Right ping CRD   ####################   ")
    print()
    result_3 = istance.test_HA_Left_3()
    time.sleep(5)

    print("   ############# SWITCH_2 OFF PORT A  ####################   ")
    print()
    istance.test_SWITCH_2_OFF_A()
    time.sleep(3)

    print("   ############# SWITCH_2 ON PORT A  ####################   ")
    print()
    istance.test_SWITCH_2_ON_A()
    
    # sleep 20 seconds before to test the 3th case
    time.sleep(20)


    ############# HA_Right + SWITCH_1 ####################
    ############# TESTING 4th CASE    ####################

    print("   ############# HA_Right + SWITCH_1 ####################   ")
    print("   ############# TESTING 4th CASE    ####################   ")

    print("   ############# HA_Right ping CRD   ####################   ")
    print()
    result_4 = istance.test_HA_Right_4()
    time.sleep(5)

    print("   ############# SWITCH_1 OFF PORT B  ####################   ")
    print()
    istance.test_SWITCH_1_OFF_B()
    time.sleep(3)

    print("   ############# SWITCH_1 ON PORT B  ####################   ")
    print()
    istance.test_SWITCH_1_ON_B()

    # sleep 20 seconds before to test the 4th case
    time.sleep(20)


    ############# HA_Right + SWITCH_2 ####################
    ############# TESTING 5th CASE   ####################

    print("   ############# HA_Right + SWITCH_2 ####################   ")
    print("   ############# TESTING 5th CASE   ####################   ")

    print()
    result_5 = istance.test_HA_Right_5()
    time.sleep(5)

    print("   ############# SWITCH_2 OFF PORT B  ####################   ")
    print()
    print(NIC_Bonding_Configuration.OFF_PORT_B)
    istance.test_SWITCH_2_OFF_B()
    time.sleep(3)

    print("   ############# SWITCH_2 ON PORT B  ####################   ")
    print()
    print(NIC_Bonding_Configuration.ON_PORT_B)
    istance.test_SWITCH_2_ON_B()
    # sleep 20 seconds before to print the result
    time.sleep(20)

    ############# TEST RESULT   ####################
    print("   ############# TEST RESULT   ####################   ")
    print('=================================================================')
    if result_0 and result_1 and result_2 and result_3 and result_4 and result_5:
    #if result_2 and result_3 and result_4 and result_5:
        result = True
        print("The NICBONDING is SUCCESS.")
        assert result
    else:
        result = False
        print("The NICBONDING is FAILED.")
        assert result
    print('=================================================================')
    
    pass
