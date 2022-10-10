# Ethical Hacking Scripts

## 1. Portscanner
Scans open ports on targeted domain for a set number of ports
- targets: Targets to scan. Either I.P address or https 
- port_num: Number of ports to scan 

## 2. Vulnerability Scanner
Similar to Portscanner but it will return any open ports with vulnerabilities listed in vulbanners.txt

##  3 & 4.  SSH Bruteforcer and Web Bruteforcer
SSH bruteforcer targeting SSH domains with a list of common passwords (passwords.txt)
- host: Target address
- username: SSH username
- input_file: a list of passwords

Web bruteforcer consists of a password bruteforcer to log into web accounts with a list of common passwords (passwords.txt) and a /directories.py which searches for common hidden directories (common.txt) within URLs.
- target: URL
- username: verified username
- input_file: a list of passwords
- login_failed_string: Error message shown on website when incorrect password is input
- cookie_value (optional): For a secondary login page within the logged-in website

## 5. MTM Arspoofer
Performs man in the middle attack by spoofing MAC address of router and target to route TCP packets through machine.

    echo 1 >> /proc/sys/net/ipv4/ip_forward  

    python3 arpspoofer.py <router ip> <machine ip>

## 6. Password Sniffer
Detects username and password field inputs by reading TCP packets. It can be used as a package with  **MTM Arspoofer**.

## 7. Cracking Password
Able to decrypt passwords depending on it's hash type. Additionally, wireless cracker bruteforces any wireless networks connected to host.
- type_of_hash: MD5, SHA1, SHA256 etc.
- hash_to_decrypt: Hash value to bruteforce

## 8. Keylogger
Logs keyboard input of host machine. It is unfortunately detectable by Windows 11 Security.

## 9 & 10. Backdoor and Command & Control for multiple backdoors
Once backdoor is installed on target machine, it tries to connect with attacker every 20 seconds. Once connection is established, attacker can upload, download, take screenshots, track keyboard inputs and create persistence (backdoor runs in background undetected) on target machine.

command & control performs similar functions but it is able to control multiple targets  simultaneously 

## 11. Email Scraper
Scrapes target website for other domains and searches for any emails targets within domains.
- target: URL
