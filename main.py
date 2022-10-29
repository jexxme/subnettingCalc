import math
import os
###############################################################################
# Function Calls
###############################################################################


def dec2bin(ip):
    ip = [bin(i)[2:].zfill(8) for i in ip]
    ip = "".join(ip)

# Idk what to do with this


def hostAmountCalc(hostAmount):
    return math.log(hostAmount, 2)


def IPClass(ip):
    if ip[0] < 128:
        return "A"
    elif ip[0] < 192:
        return "B"
    elif ip[0] < 224:
        return "C"
    elif ip[0] < 240:
        return "D"
    else:
        return "E"


def netmaskCalc(ip, mask):
    # Calculate Binary Subnetmask
    # FULL IP = 32 Bits
    #Hostbits = 32 - Subnetbits
    #Subnetbits = 32 - Hostbits
    # Example:
    # IP-Adress: 10.10.0.0/16
    # Subnetbits: 16
    # Hostbits: 16
    # Netmask: 255.255.0.0

    netmask_bin = []
    for i in range(0, mask):
        netmask_bin.append("1")
    for i in range(mask, 32):
        netmask_bin.append("0")
    netmask_bin = "".join(netmask_bin)

    # Calculate Decimal Netmask
    netmask_dec = []
    for i in range(0, 4):
        netmask_dec.append(int("".join(netmask_bin[i*8:i*8+8]), 2))

    netmask_dec = ".".join([str(i) for i in netmask_dec])

    # Split Binary Netmask into 4 octets in a String
    netmask_bin = [netmask_bin[i:i+8] for i in range(0, len(netmask_bin), 8)]
    netmask_bin = ".".join(netmask_bin)

    return netmask_dec, netmask_bin


def subnetmaskCalc(ip, subnetAmount, mask):
    # Calculate Binary Subnetmask
    # FULL IP = 32 Bits
    #Hostbits = 32 - Subnetbits
    #Subnetbits = 32 - Hostbits
    # Example:
    # IP-Adress: 10.10.0.0/16
    # Subnetbits: 16
    # Hostbits: 16
    # Netmask: 255.255.0.0

    # Calculate

    # Calculate Decimal subnetmask
    subnetmask_dec = []
    for i in range(0, 4):
        subnetmask_dec.append(int("".join(subnetmask_bin[i*8:i*8+8]), 2))

    subnetmask_dec = ".".join([str(i) for i in subnetmask_dec])

    # Split Binary subnetmask into 4 octets in a String
    subnetmask_bin = [subnetmask_bin[i:i+8]
                      for i in range(0, len(subnetmask_bin), 8)]
    subnetmask_bin = ".".join(subnetmask_bin)

    return subnetmask_dec, subnetmask_bin


def NaIPRangeBaCalc(ip):
    # # Calculate the first and last IP-Adress of the subnet
    # firstIP = ip[0:3]
    # firstIP.append(0)
    # lastIP = ip[0:3]
    # lastIP.append(255)
    # ipRange = str(firstIP) + " - " + str(lastIP)

    # Calculate the Network Adress
    networkAdress = ip[0:3]
    networkAdress.append(0)

    # Calculate the Broadcast Adress
    broadcastAdress = ip[0:3]
    broadcastAdress.append(255)

    return networkAdress, broadcastAdress


def fullCalc():
    # INPUT: IP-Adress, Subnet Amount, Host Amount
    # OUTPUT: IP-Adress, Binary IP-Adress, IP-Adress Class, Subnet Amount, Host Amount, Netmask, Binary Netmask, Network Adress, IP-Adress Range, Broadcast Adress

    ip = input("IP-Adress: ")
    # Prepare IP-Adress
    ip = ip.split(".")
    ip = [int(i) for i in ip]
    # Required Host Amount
    hostAmount = int(input("Required Host Amount: "))
    if hostAmount == 0:
        hostAmount = 1

    # Calculate Amount of Subnetbits needed
    subnetBits = 0
    while 2**subnetBits < hostAmount:
        subnetBits += 1

    # Input Subnet Amount
    subnetAmount = input("Subnet Amount: ")
    if subnetAmount == "":
        subnetAmount = 1
    else:
        subnetAmount = int(subnetAmount)
    print("Binary IP-Adress: ", dec2bin(ip))
    print("IP-Adress Class: ", IPClass(ip))
    print("\n")
    print("Netmask: ", netmaskCalc(ip, subnetBits)[0])
    print("Binary Netmask: ", netmaskCalc(ip, subnetBits)[1])
    print("\n")
    print("Subnetmask: ", subnetmaskCalc(ip, subnetAmount, subnetBits)[0])
    print("Network Adress: ", NaIPRangeBaCalc(ip)[0])
    print("IP-Adress Range: ", NaIPRangeBaCalc(ip)
          [0], " - ", NaIPRangeBaCalc(ip)[1])
    print("Broadcast Adress: ", NaIPRangeBaCalc(ip)[1])


def halfCalc():
    mask = int(input("Netmask/CIDR: "))
    #####


def NetmaskCalc():
    pass


def HostAmountCalc():
    pass


###############################################################################
# Main
###############################################################################

# TODOS:
# SHN Notation
# Resourcen:
# https://networkengineering.stackexchange.com/questions/28121/maximum-number-of-subnets
#
# Aufgabe:
# 172.16.0.0/16 auf 300 Netze
# Bits/Hosts/Schema/Alle N+BC-Adressen!
#


def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("-----------------------------------------------------")
    print('       Welcome to the IP-Adress Programm!            ')
    print("-----------------------------------------------------")
    print("\n       What do you want to do?                     ")
    print("-----------------------------------------------------")
    print("1. Input: IP-Adress, Subnet Amount, Host Amount")
    print('2. Input: IP-Adress, Host Amount, Netmask/CIDR')
    print("3. Input: IP-Adress, Netmask/CIDR")
    print("4. Input: IP-Adress, Host Amount")
    print("5. Input: IP-Adress")
    print("6. Exit")
    print("-----------------------------------------------------")
    choice = input("Your choice: ")
    os.system('cls' if os.name == 'nt' else 'clear')
    if choice == "1":
        fullCalc()
    elif choice == "2":
        halfCalc()
    elif choice == "3":
        exit()
    elif choice == "4":
        exit()
    elif choice == "6":
        exit()
    else:
        print("Invalid input!")
        input("Press Enter to continue...")
        main()


if __name__ == "__main__":
    main()
