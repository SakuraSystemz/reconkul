#!/usr/bin/env python3
import subprocess
import os

def exec_nmap(options):
    nmap_command = f"nmap -vvv -Pn {options}"
    subprocess.run(nmap_command, shell=True)

def is_root_user():
    return os.geteuid() == 0

def run_help():
    print("""
        timing template:
          The default is -T3, but it should be set explicitly.
          This option controls the packets sent by Nmap to the target port in 6 steps,
          ranging from 0 to 5. For example, you can specify it as T3. T5 is the fastest option,
          but for high-speed scanning, it is recommended to use 4 as it balances packet volume and accuracy.
          On the other hand, for increased accuracy and to avoid detection by IPS/IDS defense systems, 
          you should use 0-1, which reduces the packet count and speed.
    """)

def main():
    art = """
==========================================================================
                                     /
                                    /
          o--o   o--o   o--o   o--o/  o   o   o   o  o / /o  o
          |   |  |     |      |   /|  |\  |   |  /   |    |  |
          o--o   o--o  o      o  / o  o \ o   o-o    o    o  o
          |   \  |     |      | /  |  |  \|   |  \   |    |  |
          o    o o--o   o--o   o--o   o   o   o   o   o--o   o---o
                              /
                             /            {v1.0.4/Apha}
==========================================================================
"""
    while True:
        print(art)
        print("//// Nmap Command Generator ////")
        print("0. Help")
        print("1. Quick Scan")
        print("2. Full Scan")
        print("3. Port Scan")
        print("4. SYN Scan(need root)")
        print("5. Vuln Scan")
        print("6. Exit")

        choice = input("set your choice -> ")

        if choice == "0":
            run_help()
            break

        elif choice == "1":
            host = input("set the host or IP -> ")
            tt = input("what choice timing template? [0...5] -> ")
            exec_nmap(f"-T{tt} -F {host}")

        elif choice == "2":
            host = input("set the host or IP -> ")
            tt = input("what choice timing template? [0...5] -> ")
            exec_nmap(f"-T{tt} -A {host}")
        elif choice == "3":
            host = input("set the host or IP -> ")
            ports = input("set ports -> ")
            tt = input("what choice timing template? [0...5] -> ")
            exec_nmap(f"-T{tt} -p {ports} {host}")
        elif choice == "4":
            if is_root_user():
                host = input("set the host or IP -> ")
                ports = input("set ports -> ")
                tt = input("what choice timing template? [0...5] -> ")
                exec_nmap(f"-T{tt} -p {ports} -sS {host}")
            else:
                print("SYN scan need root permission. try sudo")
                break
        elif choice == "5":
            if is_root_user():
              host = input("set the host or IP -> ")
              ports = input("set ports -> ")
              tt = input("what choice timing template? [0...5] -> ")
              exec_nmap(f"T{tt} -p {ports} -sSV --script vuln {host}")
            else:
                print("Vuln scan need root permission. try sudo")
                break

        elif choice == "6":
            break

        else:
            print("Invalid choice. Please try again.\n")

if __name__ == "__main__":
    main()
