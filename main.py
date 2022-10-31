from itertools import count
import math
import os

###############################################################################
# Function Calls
###############################################################################


def hostAmountCalc(hostAmount):
    return math.log(hostAmount, 2)


def ipClass(ip):
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


def nNsShHNotation(netzwerkTeilBits, subnetTeilBits, hostTeilBits):
    # Calculates the NsShH Notation: n/N stand for a network bit, s/S for a subnet bit and h/H for a host bit
    nshNotation = []
    for i in range(netzwerkTeilBits):
        nshNotation.append("n")
    for i in range(subnetTeilBits):
        nshNotation.append("s")
    for i in range(hostTeilBits):
        nshNotation.append("h")
    nshNotation = "".join(nshNotation)
    nshNotation = [nshNotation[i:i+8] for i in range(0, len(nshNotation), 8)]
    nshNotation = ".".join(nshNotation)
    print("nsh Notation: ", nshNotation)
    nshNotation = nshNotation.replace("n" * 8, "N")
    nshNotation = nshNotation.replace("s" * 8, "S")
    nshNotation = nshNotation.replace("h" * 8, "H")
    print("nNsShH Notation: ", nshNotation)

    return nshNotation


def bitCalc(CIDR, requiredSubnetAmount):
    # Calculate the amount of bits for the network and subnet/host part
    netzwerkTeilBits = int(CIDR)
    subnetHostTeilBits = 32 - netzwerkTeilBits
    # SubnetBitCalculation
    notEnoughSubnets = True
    exponent = 0
    while notEnoughSubnets == True:
        if (2 ** exponent) >= int(requiredSubnetAmount):
            notEnoughSubnets = False
            # print("Sufficient subnets found with exponent:", exponent,
            #   "\nSubnet amount with exponent", exponent, "is", 2 ** exponent)
            requiredSubnetBitAmount = exponent

            # Calculate possible Subnets with the required SubnetBits in Binary
            possibleSubnets = []
            for i in range(0, 2**requiredSubnetBitAmount):
                possibleSubnets.append(
                    bin(i)[2:].zfill(requiredSubnetBitAmount))
            # Amount of items in possibleSubnets
            possibleSubnetsAmount = len(possibleSubnets)
        else:
            exponent = exponent + 1
            # print("Exponent:", exponent,  "-> not enough subnets")

    hostTeilBits = subnetHostTeilBits - requiredSubnetBitAmount
    subnetTeilBits = requiredSubnetBitAmount

    return netzwerkTeilBits, subnetHostTeilBits, subnetTeilBits, hostTeilBits, requiredSubnetBitAmount, possibleSubnets, possibleSubnetsAmount


def subnetmaskCalc(ip, requiredSubnetAmount, CIDR):
    print("Netzwerk Teil Bits: ", bitCalc(
        CIDR, requiredSubnetAmount)[0])
    print("Subnet/Host Teil Bits: ",
          bitCalc(CIDR, requiredSubnetAmount)[1])
    print("Subnet Teil Bits: ", bitCalc(CIDR, requiredSubnetAmount)[2])
    print("Host Teil Bits: ", bitCalc(CIDR, requiredSubnetAmount)[3])
    print("\nRequired Subnet Bit Amount: ",
          bitCalc(CIDR, requiredSubnetAmount)[4])
    print("Possible Subnet Amount: ", bitCalc(CIDR, requiredSubnetAmount)[6])
    print("Possible Subnets: ", bitCalc(CIDR, requiredSubnetAmount)[5])

    requiredSubnetBITAmount = bitCalc(CIDR, requiredSubnetAmount)[4]

    # Calculate SubnetStepWidth
    # Funktioniert mit 300 Subnets nicht
    STEP = 256 / (2 ** requiredSubnetBITAmount)
    print("\n\nSubnet STEP-Weite: ", STEP)

    # Calculate SubnetAdresses
    subnetAdresses = []
    for i in range(0, 2**requiredSubnetBITAmount):
        subnetAdresses.append(int(i * STEP))
    print("SubnetAdresses: ", subnetAdresses)

    for i in range(0, 2**requiredSubnetBITAmount):
        subnetAdresses.insert

    # Prepare IP-Adress in List
    print("\n\nIP-Adress: ", ip)
    ip = ip.split(".")
    ip = [int(i) for i in ip]
    # print("IP-Adress Octets: ", ip)

    # Calculate Binary IP-Adresses
    ipBin = []
    for i in range(0, 4):
        ipBin.append(bin(ip[i])[2:].zfill(8))
    ipBinString = ".".join(ipBin)
    print("IP Bin String: ", ipBinString)
    print("IP Bin: ", ipBin)

    nNsShHNotation(bitCalc(
        CIDR, requiredSubnetAmount)[0], bitCalc(CIDR, requiredSubnetAmount)[2], bitCalc(CIDR, requiredSubnetAmount)[3])


###############################################################################
    # Insert SubnetBits into IP-Adress
    # Given :
    # Possible Subnets:  ['00', '01', '10', '11']
    # IP Bin String:  11000000.10101000.00000000.00000000

    indexSBits = int(CIDR) + 1

    # 0-Amount of Subnets
    for i in range(0, len(bitCalc(CIDR, requiredSubnetAmount)[6])):
        ipSubnetBin =

    def insert(string, index):
        return string[:index] + '-' + string[index:]

    for i in len(ipBinString)-4:

        # ipBinSolo[] =

        # print insert("355879ACB6", 5)

        # IDK
        # for i in range(int(CIDR)+1, int(CIDR)+requiredSubnetBITAmount+1):
        #     print("HI", i)
        #     ipSubnetBinary[i] = ipBin[]

        ###############################################################################


def fullCalc():
    pass


def ipHostCidrMain():
    ip = input("IP-Adress: ")
    hostAmount = int(input("Host Amount: "))
    CIDR = int(input("CIDR: "))
    subnetmaskCalc(ip, hostAmount, CIDR)


def NetmaskCalc():
    pass


def HostAmountCalc():
    pass


###############################################################################
# Main
###############################################################################
def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("-----------------------------------------------------")
    print('       Welcome to the IP-Adress Programm!            ')
    print("-----------------------------------------------------")
    print("\n       What do you want to do?                     ")
    print("-----------------------------------------------------")
    print("1. Input: IP-Adress, Subnet Amount, Host Amount")
    print('2. Input: IP-Adress, Host Amount, CIDR')
    print("3. Input: IP-Adress, Netmask/CIDR")
    print("4. TEST")
    print("5. Input: IP-Adress")
    print("6. Exit")
    print("-----------------------------------------------------")
    choice = input("Your choice: ")
    os.system('cls' if os.name == 'nt' else 'clear')
    if choice == "1":
        fullCalc()
    elif choice == "2":
        ipHostCidrMain()
    elif choice == "3":
        exit()
    elif choice == "4":
        subnetmaskCalc("192.168.0.0", "4", "24")
    elif choice == "6":
        exit()
    else:
        print("Invalid input!")
        input("Press Enter to continue...")
        main()


if __name__ == "__main__":
    main()

# TODOS:
#
#
# Resourcen:
# https://networkengineering.stackexchange.com/questions/28121/maximum-number-of-subnets
#
# Aufgabe:
# 172.16.0.0/16 auf 300 Netze
# Bits/Hosts/Schema/Alle N+BC-Adressen!
#
#
#
# Host bits = Log2(Number-of-hosts) = Log2(100) = 6.643
#
#
#
#
