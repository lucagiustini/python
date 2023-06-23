############  Check the result of the test ##########

import os
import HA_NIC_Bonding_Configuration
import re # powerful tool for matching patterns in text

# function that allow to search in the file.txt the Time Spent
def getTime(filetxt_path):
    with open(filetxt_path, 'r') as f:
        Time_Spent_LIMIT = re.search(r'time (\d+)ms', f.read())
        if Time_Spent_LIMIT:
            return int(Time_Spent_LIMIT.group(1))
        else:
            return None

# function that allow to search in the file.txt the Packets Lost
def getPacketLoss(filetxt_path):
    with open(filetxt_path, 'r') as f:
        Packets_Lost_LIMIT = re.search(r'(\d+)% packet loss', f.read())
        if Packets_Lost_LIMIT:
            return int(Packets_Lost_LIMIT.group(1))
        else:
            return None

def test_check():
    print("=========================")
    print(getTime('RESULTS.txt'), "[ms] required")
    print(getPacketLoss('RESULTS.txt'), "% packet loss")
    if getTime('RESULTS.txt') <= HA_NIC_Bonding_Configuration.Time_Spent_LIMIT and getPacketLoss('RESULTS.txt') == HA_NIC_Bonding_Configuration.Packets_Lost_LIMIT:
        print("The NICBONDING is SUCCESS.")
        assert(True)
    if getTime('RESULTS.txt') > HA_NIC_Bonding_Configuration.Time_Spent_LIMIT or getPacketLoss('RESULTS.txt') != HA_NIC_Bonding_Configuration.Packets_Lost_LIMIT:
        print("The result is NOT OK.")
        assert(False)
    print("=========================")