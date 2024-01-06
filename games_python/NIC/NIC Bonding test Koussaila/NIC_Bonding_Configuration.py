#!/usr/bin/env python3
from os.path import join
import os
import sys

# add parent folder to python path
sys.path.insert(1, os.path.realpath(os.path.pardir))
sys.path.insert(1, join(os.path.realpath(os.path.pardir), ".."))
sys.path.insert(1, join(os.path.realpath(os.path.pardir), "..", ".."))

# add dedicated script locations
DEDICATED_SCRIPT_FOLDER = './Scripts'

# add dedicated script names
DEDICATED_SCRIPT_NAME = 'cpu_memory_measurements.py'

PERFORMANCE_RECORD_PERIOD = 1
PERFORMANCE_RECORD_TIME = 300

# # # # #  Configuration of the HA and CRD used for NIC Bonding  # # # # #

# I want to create a list of objects, each object containing the variables of each target
TARGETS = {
    "HA_Left" : {
        "ip_address": "192.168.200.23", "user_name": "user", "psw": "user"
        },
    "HA_Right" : {
        "ip_address": "192.168.200.24", "user_name": "user", "psw": "user"
        },
    "CRD" : {
        "ip_address": "192.168.1.216", "user_name": "user", "psw": "user"
        },
    "SWITCH_1" : {
        "ip_address": "192.168.1.213", "user_name": "admin", "psw": "private"
        },
    "SWITCH_2" : {
        "ip_address": "192.168.1.214", "user_name": "admin", "psw": "private"
        }
}

# command to send to the device
COMMAND_TO_SEND_HA_LEFT = 'sudo ping -i 0,005 -c 1000 ' + TARGETS["CRD"]["ip_address"]
COMMAND_TO_SEND_HA_RIGHT = 'sudo ping -i 0,005 -c 1000 ' + TARGETS["CRD"]["ip_address"]
COMMAND_TO_RECEIVE_TIME = 'time (\\d+)ms'
# command to send to the switch
COMMAND_TO_RECEIVE_PACKET = '(\\d+)% packet loss'


# list port number
PORT_NUMBER = ['3', '4', '5', '6', '7', '8'] 
# respectively HA 1 192.168.20.21, HA 2 192.168.20.22, HA 3 192.168.20.23, HA 4 192.168.20.24, CRD 192.168.1.216, Xcommunication between the Switches

ENABLE_SWITCH = 'no shutdown'
DISABLE_SWITCH = 'shutdown'
# command to send to the switch
# cmd = 'enable \\r configure \\r interface 1/' + PORT_NUMBER[7] + '\\r ' + ENABLE_SWITCH + ' \\r exit \\r exit \\r logout'
ON_PORT_A = 'enable \r configure \r interface 1/' + PORT_NUMBER[2] + '\r ' + ENABLE_SWITCH + ' \r exit \r exit \r logout'
OFF_PORT_A = 'enable \r configure \r interface 1/' + PORT_NUMBER[2] + '\r ' + DISABLE_SWITCH + ' \r exit \r exit \r logout'
ON_PORT_B = 'enable \r configure \r interface 1/' + PORT_NUMBER[3] + '\r ' + ENABLE_SWITCH + ' \r exit \r exit \r logout'
OFF_PORT_B = 'enable \r configure \r interface 1/' + PORT_NUMBER[3] + '\r ' + DISABLE_SWITCH + ' \r exit \r exit \r logout'
# print (cmd)

################## PARAMETERS TO CHECK RESULT ##################

# Time maximum spent to send packets in [ms]
TIME_LIMIT = 5100
# Packets lost in % at maximum
PACKET_LIMIT = 0  # 0,001
