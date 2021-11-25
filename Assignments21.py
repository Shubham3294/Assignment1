import paramiko
import pytest

host = "192.168.1.15"
port = 22
username = "shubham"
password = "123"
command = "free | grep Mem | awk '{print ($2-$7)/$2 * 100}'"
command1 = "df -h"
command2 = "ls"
command3 = "lscpu"

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(host, port, username, password)
#print("Connection Successful")


def runSsh(cmd):
    userName = "shubham"
    password = "123"
    hostname = "192.168.1.15"
    try:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        paramiko.util.log_to_file("filename.log")
        ssh.connect(hostname, username=userName, port=22, password=password)
        print("connected to host", host)
        stdin, stdout, stderr = ssh.exec_command(cmd, timeout=10)
        result = stdout.read()
        result1 = result.decode()
        print()
        error = stderr.read().decode('utf-8')

        if not error:
            ssh.close()
        return result1
    except paramiko.AuthenticationException:
        print("Authentication failed, please verify your credentials: %s")

memoryUtil = runSsh(command)
print("The Memory Utilization is : ", memoryUtil)
diskUtil = runSsh(command1)
print("The Disk Utilized is : \n", diskUtil)
fileList = runSsh(command2)
print("The Files present are : \n", fileList)
cpuinfo = runSsh(command3)
print("The CPU Information is : \n", cpuinfo)