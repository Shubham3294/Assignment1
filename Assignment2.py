import paramiko
import pytest


class Test_vm:
    
    memUtil_cmd = "free | grep Mem | awk '{print ($2-$7)/$2 * 100}'"  
    cpu_info_cmd = "lscpu"

    def runssh(self,cmd):
        userName = "shubham"
        password = "123"
        hostname = "192.168.1.15"
        try:
            ssh = paramiko.SSHClient()
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            
            ssh.connect(hostname, username=userName, port=22, password=password)
            
            stdin, stdout, stderr = ssh.exec_command(cmd, timeout=10)

            cmd_output = stdout.read()
            cmd_output_decoded = cmd_output.decode()
            
            error = stderr.read().decode('utf-8')

            if not error:
                ssh.close()
            return cmd_output_decoded
        except paramiko.AuthenticationException:
            print("Authentication failed, please verify your credentials: %s")

    
    def test_validate_memutil(self):

        self.memoryUtil = float(self.runssh(self.memUtil_cmd))
        assert self.memoryUtil < 90

    
    def test_validate_architecture(self):

        self.architecture = self.runssh(self.cpu_info_cmd).replace(" ","").split("\n")[0][-6:]
        assert self.architecture == "x86_64"


    def test_validate_model_name(self):

        self.modelname = self.runssh(self.cpu_info_cmd).replace(" ","").split("\n")[13][10:]
        assert self.modelname == "Intel(R)Core(TM)i5-8265UCPU@1.60GHz"
