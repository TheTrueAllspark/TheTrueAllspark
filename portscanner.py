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
                print("\nInitiating scan... standby for super secret spy information!\n\n")
                scanner.scan(target, ports, '-vv -sS -T4')
                for host in scanner.all_hosts():
                    print(f'Host: {target:15} ({scanner[target].hostname()})')
                    print(f'State: {scanner[target].state():15}')
                    for proto in scanner[target].all_protocols():
                        print('----------')
                        print(f'Protocol: {proto:15}')                        
                        
                        for port in scanner[target][proto].keys():
                            print(f"Port: {port:5}\tState: {scanner[target][proto][port]['state']:5}\tService: {scanner[target][proto][port]['name']:20}")
                break
            elif response == '2':
                print("\nInitiating scan... standby for super secret spy information!\n\n")
                scanner.scan(target, ports, '-vv -sU -T4')
                for host in scanner.all_hosts():
                    print(f'Host: {target:15} ({scanner[target].hostname()})')
                    print(f'State: {scanner[target].state():15}')
                    for proto in scanner[target].all_protocols():
                        print('----------')
                        print(f'Protocol: {proto:15}')                        
                        
                        for port in scanner[target][proto].keys():
                            print(f"Port: {port:5}\tState: {scanner[target][proto][port]['state']:5}\tService: {scanner[target][proto][port]['name']:20}")
                break
            elif response == '3':
                print("\nInitiating scan... standby for super secret spy information!\n\n")
                scanner.scan(target, ports, '-vv -sS -sV -sC -A -O -T4')
                for host in scanner.all_hosts():
                    print(f'Host: {target:15} ({scanner[target].hostname()})')
                    print(f'State: {scanner[target].state():15}')
                    for proto in scanner[target].all_protocols():
                        print('----------')
                        print(f'Protocol: {proto:15}')                        
                        
                        for port in scanner[target][proto].keys():
                            print(f"Port: {port:5}\tState: {scanner[target][proto][port]['state']:5}\tService: {scanner[target][proto][port]['name']:20}")
                break
            elif response == '4':
                print("\nInitiating scan... standby for super secret spy information!\n\n")
                scanner.scan(target, ports, '-vv -T4')
                for host in scanner.all_hosts():
                    print(f'Host: {target:15} ({scanner[target].hostname()})')
                    print(f'State: {scanner[target].state():15}')
                    for proto in scanner[target].all_protocols():
                        print('----------')
                        print(f'Protocol: {proto:15}')                        
                        
                        for port in scanner[target][proto].keys():
                            print(f"Port: {port:5}\tState: {scanner[target][proto][port]['state']:5}\tService: {scanner[target][proto][port]['name']:20}")
                break
            elif response == '5':
                report = {}
                report['Scan'] = scanner.scan(target, arguments="-O")['scan'][target]['osmatch'][1]

                report_list.append(report)
                print(report_list)
                break
            elif response == '6':
                print("\nInitiating scan... standby for super secret spy information!\n\n")
                scanner.scan(target, ports, '-vv -sS -Pn -T4')
                for host in scanner.all_hosts():
                    print(f'Host: {target:15} ({scanner[target].hostname()})')
                    print(f'State: {scanner[target].state():15}')
                    for proto in scanner[target].all_protocols():
                        print('----------')
                        print(f'Protocol: {proto:15}')                        
                        
                        for port in scanner[target][proto].keys():
                            print(f"Port: {port:5}\tState: {scanner[target][proto][port]['state']:5}\tService: {scanner[target][proto][port]['name']:20}")
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
                print("\nInitiating scan... standby for super secret spy information!\n\n")
                scanner.scan(target,'1-1024', '-vv -sS -T4')
                for host in scanner.all_hosts():
                    print(f'Host: {target:15} ({scanner[target].hostname()})')
                    print(f'State: {scanner[target].state():15}')
                    for proto in scanner[target].all_protocols():
                        print('----------')
                        print(f'Protocol: {proto:15}')                        
                        
                        for port in scanner[target][proto].keys():
                            print(f"Port: {port:5}\tState: {scanner[target][proto][port]['state']:5}\tService: {scanner[target][proto][port]['name']:20}")
                break
            elif response == '2':
                print("\nInitiating scan... standby for super secret spy information!\n\n")
                scanner.scan(target,'1-65535', '-vv -sS -T4')
                for host in scanner.all_hosts():
                    print(f'Host: {target:15} ({scanner[target].hostname()})')
                    print(f'State: {scanner[target].state():15}')
                    for proto in scanner[target].all_protocols():
                        print('----------')
                        print(f'Protocol: {proto:15}')                        
                        
                        for port in scanner[target][proto].keys():
                            print(f"Port: {port:5}\tState: {scanner[target][proto][port]['state']:5}\tService: {scanner[target][proto][port]['name']:20}")
                break
            elif response == '3':
                print("\nInitiating scan... standby for super secret spy information!\n\n")
                scanner.scan(target,'1-1024', '-vv -sU -T4')
                for host in scanner.all_hosts():
                    print(f'Host: {target:15} ({scanner[target].hostname()})')
                    print(f'State: {scanner[target].state():15}')
                    for proto in scanner[target].all_protocols():
                        print('----------')
                        print(f'Protocol: {proto:15}')                        
                        
                        for port in scanner[target][proto].keys():
                            print(f"Port: {port:5}\tState: {scanner[target][proto][port]['state']:5}\tService: {scanner[target][proto][port]['name']:20}")
                break
            elif response == '4':
                print("\nInitiating scan... standby for super secret spy information!\n\n")
                scanner.scan(target,'1-65535', '-vv -sU -T4')
                for host in scanner.all_hosts():
                    print(f'Host: {target:15} ({scanner[target].hostname()})')
                    print(f'State: {scanner[target].state():15}')
                    for proto in scanner[target].all_protocols():
                        print('----------')
                        print(f'Protocol: {proto:15}')                        
                        
                        for port in scanner[target][proto].keys():
                            print(f"Port: {port:5}\tState: {scanner[target][proto][port]['state']:5}\tService: {scanner[target][proto][port]['name']:20}")
                break
            elif response == '5':
                print("\nInitiating scan... standby for super secret spy information!\n\n")
                scanner.scan(target,'1-1024', '-vv -sS -sV -sC -A -O -T4')
                for host in scanner.all_hosts():
                    print(f'Host: {target:15} ({scanner[target].hostname()})')
                    print(f'State: {scanner[target].state():15}')
                    for proto in scanner[target].all_protocols():
                        print('----------')
                        print(f'Protocol: {proto:15}')                        
                        
                        for port in scanner[target][proto].keys():
                            print(f"Port: {port:5}\tState: {scanner[target][proto][port]['state']:5}\tService: {scanner[target][proto][port]['name']:20}")
                break
            elif response == '6':
                print("\nInitiating scan... standby for super secret spy information!\n\n")
                scanner.scan(target,'1-65535', '-vv -sS -sV -sC -A -O -T4')
                for host in scanner.all_hosts():
                    print(f'Host: {target:15} ({scanner[target].hostname()})')
                    print(f'State: {scanner[target].state():15}')
                    for proto in scanner[target].all_protocols():
                        print('----------')
                        print(f'Protocol: {proto:15}')                        
                        
                        for port in scanner[target][proto].keys():
                            print(f"Port: {port:5}\tState: {scanner[target][proto][port]['state']:5}\tService: {scanner[target][proto][port]['name']:20}")
                break
            elif response == '7':
                print("\nInitiating scan... standby for super secret spy information!\n\n")
                scanner.scan(target,'1-1024', '-vv -T4')
                for host in scanner.all_hosts():
                    print(f'Host: {target:15} ({scanner[target].hostname()})')
                    print(f'State: {scanner[target].state():15}')
                    for proto in scanner[target].all_protocols():
                        print('----------')
                        print(f'Protocol: {proto:15}')                        
                        
                        for port in scanner[target][proto].keys():
                            print(f"Port: {port:5}\tState: {scanner[target][proto][port]['state']:5}\tService: {scanner[target][proto][port]['name']:20}")
                break
            elif response == '8':
                print("\nInitiating scan... standby for super secret spy information!\n\n")
                scanner.scan(target,'1-65535', '-vv -T4')
                for host in scanner.all_hosts():
                    print(f'Host: {target:15} ({scanner[target].hostname()})')
                    print(f'State: {scanner[target].state():15}')
                    for proto in scanner[target].all_protocols():
                        print('----------')
                        print(f'Protocol: {proto:15}')                        
                        
                        for port in scanner[target][proto].keys():
                            print(f"Port: {port:5}\tState: {scanner[target][proto][port]['state']:5}\tService: {scanner[target][proto][port]['name']:20}")
                break
            elif response == '9':
                print("\nInitiating scan... standby for super secret spy information!\n\n")
                report = {}
                report['Scan'] = scanner.scan(target, arguments="-O")['scan'][target]['osmatch'][1]

                report_list.append(report)
                print(report_list)
                break
            elif response == '10':
                print("\nInitiating scan... standby for super secret spy information!\n\n")
                scanner.scan(target,'1-1024', '-vv -sS -Pn -T4')
                for host in scanner.all_hosts():
                    print(f'Host: {target:15} ({scanner[target].hostname()})')
                    print(f'State: {scanner[target].state():15}')
                    for proto in scanner[target].all_protocols():
                        print('----------')
                        print(f'Protocol: {proto:15}')                        
                        
                        for port in scanner[target][proto].keys():
                            print(f"Port: {port:5}\tState: {scanner[target][proto][port]['state']:5}\tService: {scanner[target][proto][port]['name']:20}")
                break
            elif response == '11':
                print("\nInitiating scan... standby for super secret spy information!\n\n")
                scanner.scan(target,'1-65535', '-vv -sS -Pn -T4')
                for host in scanner.all_hosts():
                    print(f'Host: {target:15} ({scanner[target].hostname()})')
                    print(f'State: {scanner[target].state():15}')
                    for proto in scanner[target].all_protocols():
                        print('----------')
                        print(f'Protocol: {proto:15}')                        
                        
                        for port in scanner[target][proto].keys():
                            print(f"Port: {port:5}\tState: {scanner[target][proto][port]['state']:5}\tService: {scanner[target][proto][port]['name']:20}")
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



