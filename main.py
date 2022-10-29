# IP-Adress Calculator
import os


def dec2bin(ip):
    ip = [bin(i)[2:].zfill(8) for i in ip]
    ip = "".join(ip)


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


def netmaskCalc(mask):
    # Calculate Binary Netmask and Wildcard
    netmask_bin = []
    netmask_dec = []
    for i in range(0, mask):
        netmask_bin.append("1")
    for i in range(mask, 32):
        netmask_bin.append("0")
    # Calculate Decimal Netmask
    for i in range(0, 4):
        netmask_dec.append(int("".join(netmask_bin[i*8:i*8+8]), 2))

    return netmask_bin


def main():
    # Initiate Input Variables
    ip = input("IP-Adress: ")

    # Prepare IP-Adress
    ip = ip.split(".")
    ip = [int(i) for i in ip]

    # Required Host Amount
    hostAmount = int(input("Required Host Amount (Optional): "))
    if hostAmount == 0:
        hostAmount = 1

    # Calculate Amount of Subnetbits needed
    subnetBits = 0
    while 2**subnetBits < hostAmount:
        subnetBits += 1

    # Prepare Netmask
    mask = int(input("Netmask/CIDR: "))
    # Calculate Binary Netmask and Wildcard
    netmask_bin = []
    for i in range(0, mask):
        netmask_bin.append("1")
    for i in range(mask, 32):
        netmask_bin.append("0")

    # TODO: Implement subnetting
    subnetAmount = input("Subnet Amount: ")
    if subnetAmount == "":
        subnetAmount = 1
    else:
        subnetAmount = int(subnetAmount)

    if mask > 32:
        print("Netmask is too big!")
        return

    # Calculate the number of hosts
    hosts = 2**(32-mask) - 2

    # Calculate the number of subnets
    subnets = 2**(mask-24)

    # Calculate the number of hosts per subnet
    hostsPerSubnet = hosts/subnets

    # Calculate the first and last IP-Adress of the subnet
    firstIP = ip[0:3]
    firstIP.append(0)
    lastIP = ip[0:3]
    lastIP.append(255)

    os.system('cls' if os.name == 'nt' else 'clear')
    print("Ip-Adress: ", ip)
    print("IP-Adress Class: ", IPClass(ip))
    print("Binary IP-Adress: ", dec2bin(ip))
    print("Number of hosts: ", hosts)
    print("Number of subnets: ", subnets)
    print("Number of hosts per subnet: ", hostsPerSubnet)
    print("First IP-Adress: ", firstIP)
    print("Last IP-Adress: ", lastIP)
    print("Binary Netmask: ", netmask_bin)
    input("Press Enter to continue...")
    start()


# Irgendwie sowas wie: Wenn keine Subnetanzahl angegeben ist -> Finde subnetzanzahl heraus und berechne die Subnetze
# https://networkengineering.stackexchange.com/questions/28121/maximum-number-of-subnets


def fullCalc():
    # INPUT: IP-Adress, Subnet Amount, Host Amount
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
    # TODO Inplement SNH Notation
    # OUTPUT: IP-Adress, Binary IP-Adress, IP-Adress Class, Subnet Amount, Host Amount, Netmask, Binary Netmask, Network Adress, IP-Adress Range, Broadcast Adress,

    print("Ip-Adress: ", ip)
    print("Binary IP-Adress: ", dec2bin(ip))
    print("IP-Adress Class: ", IPClass)
    print("Subnet Amount: ", subnetAmount)
    print("Host Amount: ", hostAmount)
    print("Netmask: ", netmaskCalc(subnetBits))


def halfCalc():
    mask = int(input("Netmask/CIDR: "))
    #####


def NetmaskCalc():
    pass


def HostAmountCalc():
    pass


def start():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("-----------------------------------------------------")
    print('       Welcome to the IP-Adress Programm!            ')
    print("-----------------------------------------------------")
    print("\n       What do you want to do?                     ")
    print("-----------------------------------------------------")
    print("0. Input: IP-Adress, Subnet Amount, Host Amount")
    print('1. Input: IP-Adress, Host Amount, Netmask/CIDR')
    print("2. Input: IP-Adress, Netmask/CIDR")
    print("3. Input: IP-Adress, Host Amount")
    print("4. Input: IP-Adress")
    print("5. Exit")
    print("-----------------------------------------------------")
    choice = input("Your choice: ")
    if choice == "1":
        main()
    elif choice == "2":
        main()
    elif choice == "3":
        main()
    elif choice == "4":
        main()
    elif choice == "5":
        exit()
    else:
        print("Invalid input!")
        input("Press Enter to continue...")
        start()


if __name__ == "__main__":
    start()
