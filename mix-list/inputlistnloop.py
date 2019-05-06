#!/usr/bin/env python3
def main():
    # Read in out list data
    networklists = []
    with open('driverip.txt', 'r') as driverip:
        for sline in driverip: # single line from out dile is sline
            # append adds to the end of our lists
            # rstrip removes and special characters on the right of the str
            # the results is we add a list of driver and ip to networklists
            networklists.append(sline.rstrip("\n").split(' '))

    print(networklists) # display networklists to ensure we recreated

    for driveandip in networklists:
        print('SSH to ' + driveandip[1] + ' using driver ' + driveandip[0])

main()
