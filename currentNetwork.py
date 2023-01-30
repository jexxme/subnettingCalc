def currentNetwork():
    # Input: IP, CIDR
    # Output: Subnetmask, Broadcast, Network Adress, Host Range

    # Input
    IP = input("IP-Adress: ")
    if len(IP.split(".")) != 4:
        print("Bitte IP-Adress mit 4 Oktetten eingeben")
        currentNetwork()
    CIDR = int(input("CIDR: "))
    if CIDR < 9 or CIDR > 32:
        print("Bitte CIDR zwischen 9 und 32 eingeben")
        currentNetwork()
    IP = IP.split(".")

    # Convert to Int
    secondOktet = int(IP[1])
    thirdOktet = int(IP[2])
    fourthOktet = int(IP[3])

    # Calculate
    if CIDR >= 1 and CIDR <= 8:
        print("Bitte CIDR höher als 8 eingeben")
        currentNetwork()
    elif CIDR >= 9 and CIDR <= 16:
        print("Subnetting im 2. Oktet")
        eigentlicherCIDR = 8
        subnettingBits = CIDR - eigentlicherCIDR
        subnetAmount = 2 ** subnettingBits
        STEP = 256 / subnetAmount

        # Calculates the current Subnet in which the IP is in
        currentNumberInSubnet = secondOktet / STEP
        currentMask = 256 - STEP

        currentNetworkAdress = STEP * currentNumberInSubnet
        currentNetworkAdressDecimal = str(
            IP[0]) + "." + str(int(currentNetworkAdress)) + ".0.0"

        currentBroadcastAdress = STEP * (currentNumberInSubnet + 1) - 1
        currentBroadcastAdressDecimal = str(
            IP[0]) + "." + str(int(currentBroadcastAdress)) + ".255.255"

    elif CIDR >= 17 and CIDR <= 24:
        print("Subnetting im 3. Oktet")
        eigentlicherCIDR = 16
        subnettingBits = CIDR - eigentlicherCIDR
        subnetAmount = 2 ** subnettingBits
        STEP = 256 / subnetAmount

        # Calculates the current Subnet in which the IP is in
        currentNumberInSubnet = thirdOktet / STEP
        currentMask = 256 - STEP

        currentNetworkAdress = STEP * currentNumberInSubnet
        currentNetworkAdressDecimal = str(
            IP[0]) + "." + str(IP[1]) + "." + str(int(currentNetworkAdress)) + ".0"

        currentBroadcastAdress = STEP * (currentNumberInSubnet + 1) - 1
        currentBroadcastAdressDecimal = str(
            IP[0]) + "." + str(IP[1]) + "." + str(int(currentBroadcastAdress)) + ".255"

    elif CIDR >= 25 and CIDR <= 32:
        print("Subnetting im 4. Oktet")
        eigentlicherCIDR = 24
        subnettingBits = CIDR - eigentlicherCIDR
        subnetAmount = 2 ** subnettingBits
        STEP = 256 / subnetAmount

        # Calculates the current Subnet in which the IP is in
        currentNumberInSubnet = fourthOktet / STEP
        currentMask = 256 - STEP

        currentNetworkAdress = STEP * currentNumberInSubnet
        currentNetworkAdressDecimal = str(
            IP[0]) + "." + str(IP[1]) + "." + str(IP[2]) + "." + str(int(currentNetworkAdress))

        currentBroadcastAdress = STEP * (currentNumberInSubnet + 1) - 1
        currentBroadcastAdressDecimal = str(
            IP[0]) + "." + str(IP[1]) + "." + str(IP[2]) + "." + str(int(currentBroadcastAdress))

    else:
        print("CIDR muss größer als 0 sein!")
        currentNetwork()

    # Output
    print("-----------------------------------------------------")
    print("IP-Adress: ", IP)
    print("CIDR: ", CIDR)
    print("-----------------------------------------------------")
    print("Subnetmask: ", currentMask)
    print("Network Adress: ", currentNetworkAdressDecimal)
    print("Broadcast Adress: ", currentBroadcastAdressDecimal)
    print("-----------------------------------------------------")
