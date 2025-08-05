# Electronic Shop

#!/bin/python3

import os
import sys

#
# Complete the getMoneySpent function below.
#
def getMoneySpent(keyboards, drives, b):
    #
    # Write your code here.
    #
    if(min(keyboards) > b):
        return -1
    elif(min(drives) > b):
        return -1
    elif((min(keyboards) + min(drives)) > b):
        return -1
    
    totals = []
    
    for keyboard in keyboards:
        for drive in drives:
            totalSpent = 0
            totalSpent = drive + keyboard
            if(totalSpent <= b):
                totals.append(totalSpent)
            
    if(max(totals) > b):
        return -1
    else:
        return max(totals)

# if __name__ == '__main__':
#     bnm = input().split()

#     b = int(bnm[0])
#     n = int(bnm[1])
#     m = int(bnm[2])

#     keyboards = list(map(int, input().rstrip().split()))
#     drives = list(map(int, input().rstrip().split()))

#     moneySpent = getMoneySpent(keyboards, drives, b)

#     # Just print the result in local machine
#     print(moneySpent)

## ////// -- Runs automatically without waiting for inputs -- /////////

if __name__ == '__main__':
    # Hardcoded test input
    bnm = "10 2 3".split()
    b = int(bnm[0])
    n = int(bnm[1])
    m = int(bnm[2])

    keyboards = list(map(int, "3 1".split()))
    drives = list(map(int, "5 2 8".split()))

    moneySpent = getMoneySpent(keyboards, drives, b)

    print(moneySpent)


