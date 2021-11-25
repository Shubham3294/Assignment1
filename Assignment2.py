import paramiko
import pytest

class Test_vm:

    host = "192.168.1.15"
    port = 22
    username = "shubham"
    password = 123
    command = "free | grep Mem | awk '{print ($2-$7)/$2 * 100}'"
    command1 = "df -h"
    command2 = "ls"
    command3 = "lscpu"

    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(host, port, username, password)


    def runSsh(self,cmd):
        userName = "shubham"
        password = 123
        hostname = "192.168.1.15"
        try:
            ssh = paramiko.SSHClient()
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            paramiko.util.log_to_file("filename.log")
            ssh.connect(hostname, username=userName, port=22, password=password)
            print("connected to host", self.host)
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


    def test_memory_util(self):

        self.memoryUtil = float(self.runSsh(self.command))
        print(self.runSsh(self.command))
        print(self.memoryUtil)

        assert self.memoryUtil > 90





