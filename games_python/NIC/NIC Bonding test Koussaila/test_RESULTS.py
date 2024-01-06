############  Check the result of the test ##########

import os
import NIC_Bonding_Configuration
import re # powerful tool for matching patterns in text

# function that allow to search in the file.txt the Time Spent
def getTime(filetxt_path):
    with open(filetxt_path, 'r') as f:
        TIME_LIMIT = re.search(r'time (\d+)ms', f.read())
        if TIME_LIMIT:
            return int(TIME_LIMIT.group(1))
        else:
            return None

# function that allow to search in the file.txt the Packets Lost
def getPacketLoss(filetxt_path):
    with open(filetxt_path, 'r') as f:
        PACKET_LIMIT = re.search(r'(\d+)% packet loss', f.read())
        if PACKET_LIMIT:
            return int(PACKET_LIMIT.group(1))
        else:
            return None

def test_check():
    print()
    print('=================================================================')
    print(getTime('RESULTS.txt'), "[ms] required")
    print(getPacketLoss('RESULTS.txt'), "% packet loss")
    if getTime('RESULTS.txt') <= NIC_Bonding_Configuration.TIME_LIMIT and getPacketLoss('RESULTS.txt') == NIC_Bonding_Configuration.PACKET_LIMIT:
        print("The NICBONDING is SUCCESS.")
        assert(True)
    if getTime('RESULTS.txt') > NIC_Bonding_Configuration.TIME_LIMIT or getPacketLoss('RESULTS.txt') != NIC_Bonding_Configuration.PACKET_LIMIT:
        print("The result is NOT OK.")
        assert(False)
    print('=================================================================')
