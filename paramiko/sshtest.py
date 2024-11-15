import paramiko
import time

kf = r'C:\Users\Zichuan\Desktop\putty\centos7pri_putty02.pem'
prikey = paramiko.RSAKey.from_private_key_file(kf)
channel = paramiko.SSHClient()
channel.set_missing_host_key_policy(paramiko.AutoAddPolicy())
channel.connect(hostname="192.168.5.93",username="devops",pkey=prikey)
shell = channel.invoke_shell()
shell.send("whoami\n")
shell.send("nmcli -p dev\n")
time.sleep(2)
print(shell.recv(5000))
channel.close