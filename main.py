import os

###############################################################################
# Function Calls
###############################################################################


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
    STEP = 256 / (2 ** requiredSubnetBITAmount)
    print("\nSubnet STEP-Weite: ", STEP)

    # Calculate SubnetAdresses
    subnetAdresses = []
    for i in range(0, 2**requiredSubnetBITAmount):
        subnetAdresses.append(int(i * STEP))
    print("SubnetAdresses: ", subnetAdresses)

    for i in range(0, 2**requiredSubnetBITAmount):
        subnetAdresses.insert

    # Prepare IP-Adress in List
    ip = ip.split(".")
    ip = [int(i) for i in ip]
    # print("IP-Adress Octets: ", ip)

    # Calculate Binary IP-Adresses
    ipBin = []
    for i in range(0, 4):
        ipBin.append(bin(ip[i])[2:].zfill(8))
    ipBinString = ".".join(ipBin)

    nNsShHNotation(bitCalc(
        CIDR, requiredSubnetAmount)[0], bitCalc(CIDR, requiredSubnetAmount)[2], bitCalc(CIDR, requiredSubnetAmount)[3])
    print()

###############################################################################
    # Insert SubnetBits into IP-Adress
    possibleSubnets = bitCalc(CIDR, requiredSubnetAmount)[5]

    # Prepare IP-Adress for Subnet Insertion
    ipBinString = ipBinString.replace(".", "")
    ipBinString = list(ipBinString)
    print("IP Bin String: ", ipBinString)

    # Calculate Index of SubnetBits
    firstIndexOfSubnet = int(CIDR) + 1
    lastIndexOfSubnet = int(CIDR) + int(requiredSubnetBITAmount)

    # Insert SubnetBits into IP-Adress
    ipSubnetBinary = []
    ipSubnetBinary = ipBinString

    ipSubnetBinarySplitted = []
    for i in range(0, len(possibleSubnets)):
        ipSubnetBinary[firstIndexOfSubnet -
                       1:lastIndexOfSubnet] = possibleSubnets[i]
        ipSubnetBinarySplitted.append(ipSubnetBinary[:])

    # Convert ipSubnetBinarySplitted to String
    ipSubnetBinarySplittedString = []
    for i in range(0, len(possibleSubnets)):
        ipSubnetBinarySplittedString.append(
            "".join(ipSubnetBinarySplitted[i]))

    # Add "." after every 8 Bits
    for i in range(0, len(possibleSubnets)):
        ipSubnetBinarySplittedString[i] = ipSubnetBinarySplittedString[i][0:8] + \
            "." + ipSubnetBinarySplittedString[i][8:16] + \
            "." + ipSubnetBinarySplittedString[i][16:24] + \
            "." + ipSubnetBinarySplittedString[i][24:32]
        print("IP Subnet Binary Splitted String (Subnet:", i, "):",
              ipSubnetBinarySplittedString[i])

    # Convert Binary Ip Adress to Decimal Ip Adress
    ipSubnetDecimal = []
    for i in range(0, len(possibleSubnets)):
        ipSubnetDecimal.append(
            [int(ipSubnetBinarySplittedString[i][0:8], 2),
             int(ipSubnetBinarySplittedString[i][9:17], 2),
             int(ipSubnetBinarySplittedString[i][18:26], 2),
             int(ipSubnetBinarySplittedString[i][27:35], 2)
             ])
        print("IP Subnet Decimal (Subnet:", i, "):", ipSubnetDecimal[i])

    # Calculate Network Adress
    networkAdress = []
    for i in range(0, len(possibleSubnets)):
        networkAdress.append(
            [ipSubnetDecimal[i][0], ipSubnetDecimal[i][1], ipSubnetDecimal[i][2], ipSubnetDecimal[i][3]])
        print("Network Adress (Subnet:", i, "):", networkAdress[i])

    # Calculate Broadcast Adress


def ipHostCidrMain():
    ip = input("IP-Adress: ")
    hostAmount = int(input("Host Amount: "))
    CIDR = int(input("CIDR: "))
    subnetmaskCalc(ip, hostAmount, CIDR)


###############################################################################
# Main
###############################################################################
def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("-----------------------------------------------------")
    print('       Welcome to the IP-Adress Programm!            ')
    print("-----------------------------------------------------")
    print("            What do you want to do?                  ")
    print("-----------------------------------------------------")
    print("1. Input: IP-Adress, Host Amount, CIDR")
    print('\n2. TEST: 192.168.178.0, 4, 24')
    print("\n3. Unmögliche Aufgabe")
    print("\n\n0. Exit")
    print("-----------------------------------------------------")
    choice = input("Your choice: ")
    os.system('cls' if os.name == 'nt' else 'clear')
    if choice == "1":
        ipHostCidrMain()
    elif choice == "2":
        subnetmaskCalc("192.168.178.0", "4", "24")
    elif choice == "3":
        subnetmaskCalc("172.16.0.0", "300", "17")
    elif choice == "0":
        exit()
    else:
        print("Invalid input!")
        input("Press Enter to continue...")
        main()


if __name__ == "__main__":
    main()
