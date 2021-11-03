import nmap

scanner = nmap.PortScanner()
report_list = []
target = input("Enter target ip address: ")
portchoice = input("Would you like to specify a port?\n1. Yes\n2. No\n")


while True:
    if portchoice == "1":
        begin = input("Enter start port: ")
        end = input("Enter end port: ")
        ports = str(begin + '-' + end)
                       
        response = input("\nPlease enter the type of scan you want to run\
        \n1. SYN ACK Scan\
        \n2. UDP Scan\
        \n3. Comprehensive Scan\
        \n4. Regular Scan\
        \n5. OS Detection\
        \n6. Host Discovery Disabled Scan\n")

        while True:
            if response == '1':
                report = {}
                scanner.scan(target, ports, '-vv -sS -T4')
                report['Nmap Version: '] = scanner.nmap_version()
                report['IP Status: '] = scanner[target].state()
                report['Protocols: '] = scanner[target].all_protocols()
                report['Open Ports: '] = scanner[target]['tcp'].keys()

                report_list.append(report)
                print(report_list)
                break
            elif response == '2':
                report = {}
                scanner.scan(target, ports, '-vv -sU -T4')
                report['Nmap Version: '] = scanner.nmap_version()
                report['IP Status: '] = scanner[target].state()
                report['Protocols: '] = scanner[target].all_protocols()
                report['Open Ports: '] = scanner[target]['udp'].keys()

                report_list.append(report)
                print(report_list)
                break
            elif response == '3':
                report = {}
                scanner.scan(target, ports, '-vv -sS -sV -sC -A -O -T4')
                report['Nmap Version: '] = scanner.nmap_version()
                report['IP Status: '] = scanner[target].state()
                report['Protocols: '] = scanner[target].all_protocols()
                report['Open Ports: '] = scanner[target]['tcp'].keys()

                report_list.append(report)
                print(report_list)
                break
            elif response == '4':
                report = {}
                scanner.scan(target, ports, '-vv -T4')
                report['Nmap Version: '] = scanner.nmap_version()
                report['IP Status: '] = scanner[target].state()
                report['Protocols: '] = scanner[target].all_protocols()
                report['Open Ports: '] = scanner[target]['tcp'].keys()

                report_list.append(report)
                print(report_list)
                break
            elif response == '5':
                report = {}
                report['Scan'] = scanner.scan(target, arguments="-O")['scan'][target]['osmatch'][1]

                report_list.append(report)
                print(report_list)
                break
            elif response == '6':
                report = {}
                scanner.scan(target, ports, '-vv -sS -Pn -T4')
                report['Nmap Version: '] = scanner.nmap_version()
                report['IP Status: '] = scanner[target].state()
                report['Protocols: '] = scanner[target].all_protocols()
                report['Open Ports: '] = scanner[target]['tcp'].keys()

                report_list.append(report)
                print(report_list)
                break
            else:
                response = input("Invalid choice. Please try again.\n\nPlease enter the type of scan you want to run\
                    \n1. SYN ACK Scan\
                    \n2. UDP Scan\
                    \n3. Comprehensive Scan\
                    \n4. Regular Scan\
                    \n5. OS Detection\
                    \n6. Host Discovery Disabled Scan\n")
        break
    
    elif portchoice == "2":
        response = input("\nPlease enter the type of scan you want to run\
            \n1.  SYN ACK (Stealth)Scan(P 1-1024)\
            \n2.  SYN ACK (Stealth)Scan(All ports)\
            \n3.  UDP Scan(P 1-1024)\
            \n4.  UDP Scan(All ports)\
            \n5.  Comprehensive Scan(P 1-1024)\
            \n6.  Comprehensive Scan(All ports)\
            \n7.  Regular Scan(P 1-1024)\
            \n8.  Regular Scan(All ports)\
            \n9.  OS Detection\
            \n10. Host Discovery Disabled Scan(P 1-1024)\
            \n11. Host Discovery Disabled Scan(All ports)\n")

        while True:
            if response == '1':
                report = {}
                scanner.scan(target,'1-1024', '-vv -sS -T4')
                report['Nmap Version: '] = scanner.nmap_version()
                report['IP Status: '] = scanner[target].state()
                report['Protocols: '] = scanner[target].all_protocols()
                report['Open Ports: '] = scanner[target]['tcp'].keys()
                

                report_list.append(report)
                print(report_list)
                break
            elif response == '2':
                report = {}
                scanner.scan(target,'1-65535', '-vv -sS -T4')
                report['Nmap Version: '] = scanner.nmap_version()
                report['IP Status: '] = scanner[target].state()
                report['Protocols: '] = scanner[target].all_protocols()
                report['Open Ports: '] = scanner[target]['tcp'].keys()

                report_list.append(report)
                print(report_list)
                break
            elif response == '3':
                report = {}
                scanner.scan(target,'1-1024', '-vv -sU -T4')
                report['Nmap Version: '] = scanner.nmap_version()
                report['IP Status: '] = scanner[target].state()
                report['Protocols: '] = scanner[target].all_protocols()
                report['Open Ports: '] = scanner[target]['udp'].keys()

                report_list.append(report)
                print(report_list)
                break
            elif response == '4':
                report = {}
                scanner.scan(target,'1-65535', '-vv -sU -T4')
                report['Nmap Version: '] = scanner.nmap_version()
                report['IP Status: '] = scanner[target].state()
                report['Protocols: '] = scanner[target].all_protocols()
                report['Open Ports: '] = scanner[target]['udp'].keys()

                report_list.append(report)
                print(report_list)
                break
            elif response == '5':
                report = {}
                scanner.scan(target,'1-1024', '-vv -sS -sV -sC -A -O -T4')
                report['Nmap Version: '] = scanner.nmap_version()
                report['IP Status: '] = scanner[target].state()
                report['Protocols: '] = scanner[target].all_protocols()
                report['Open Ports: '] = scanner[target]['tcp'].keys()

                report_list.append(report)
                print(report_list)
                break
            elif response == '6':
                report = {}
                scanner.scan(target,'1-65535', '-vv -sS -sV -sC -A -O -T4')
                report['Nmap Version: '] = scanner.nmap_version()
                report['IP Status: '] = scanner[target].state()
                report['Protocols: '] = scanner[target].all_protocols()
                report['Open Ports: '] = scanner[target]['tcp'].keys()

                report_list.append(report)
                print(report_list)
                break
            elif response == '7':
                report = {}
                scanner.scan(target,'1-1024', '-vv -T4')
                report['Nmap Version: '] = scanner.nmap_version()
                report['IP Status: '] = scanner[target].state()
                report['Protocols: '] = scanner[target].all_protocols()
                report['Open Ports: '] = scanner[target]['tcp'].keys()

                report_list.append(report)
                print(report_list)
                break
            elif response == '8':
                report = {}
                scanner.scan(target,'1-65535', '-vv -T4')
                report['Nmap Version: '] = scanner.nmap_version()
                report['IP Status: '] = scanner[target].state()
                report['Protocols: '] = scanner[target].all_protocols()
                report['Open Ports: '] = scanner[target]['tcp'].keys()

                report_list.append(report)
                print(report_list)
                break
            elif response == '9':
                report = {}
                report['Scan'] = scanner.scan(target, arguments="-O")['scan'][target]['osmatch'][1]

                report_list.append(report)
                print(report_list)
                break
            elif response == '10':
                report = {}
                scanner.scan(target,'1-1024', '-vv -sS -Pn -T4')
                report['Nmap Version: '] = scanner.nmap_version()
                report['IP Status: '] = scanner[target].state()
                report['Protocols: '] = scanner[target].all_protocols()
                report['Open Ports: '] = scanner[target]['tcp'].keys()

                report_list.append(report)
                print(report_list)
                break
            elif response == '11':
                report = {}
                scanner.scan(target,'1-65535', '-vv -sS -Pn -T4')
                report['Nmap Version: '] = scanner.nmap_version()
                report['IP Status: '] = scanner[target].state()
                report['Protocols: '] = scanner[target].all_protocols()
                report['Open Ports: '] = scanner[target]['tcp'].keys()

                report_list.append(report)
                print(report_list)
                break
            else:
                response = input("Invalid choice. Please try again.\n\nPlease enter the type of scan you want to run\
                    \n1. SYN ACK (Stealth)Scan(P 1-1024)\
                    \n2. SYN ACK (Stealth)Scan(All ports)\
                    \n3. UDP Scan(P 1-1024)\
                    \n4. UDP Scan(All ports)\
                    \n5. Comprehensive Scan(P 1-1024)\
                    \n6. Comprehensive Scan(All ports)\
                    \n7. Regular Scan(P 1-1024)\
                    \n8. Regular Scan(All ports)\
                    \n9. OS Detection\
                    \n10. Host Discovery Disabled Scan(P 1-1024)\
                    \n11. Host Discovery Disabled Scan(All ports)\n")
        break
    else:
        portchoice = input("Invalid choice. Please try again.\nWould you like to specify a port?\n1. Yes\n2. No\n")


