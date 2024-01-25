import configparser
import paramiko
import os
# import subprocess
# from subprocess import Popen, PIPE
import paramiko
from os.path import exists
    
class CheckPageaction():
    def checkruningfunction():
        config = configparser.ConfigParser()
        config.read('D:\\resetbackup\\python\\project\\mamautomation\\Tests\\config.ini')
        try:
            config.add_section("SUPPORT")
        except configparser.DuplicateSectionError:
            pass
        stored_exception = None
        path_items = config.items("paths")
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(hostname='192.168.15.245', username='root', password='pmsl@1234', port='1022')
        for key, path in path_items:
            commad = 'ps aux | grep ' + key
            si, so, se = ssh.exec_command(commad)
            readList = so.readlines()
            for n in readList:
                output = n.split('  ')
                # print(output[2])
                commadnew = 'pwdx' + output[2]
                si, so, se = ssh.exec_command(commadnew)
                readList = so.readlines()
                if not readList:
                    pass
                else:
                    outpunew = ''.join(readList)
                    outpunew = outpunew.split(':')
                    nout = outpunew[1].strip()
                    if path == nout:
                        print('Check done  Runing ', key)
                        
    def filecopyforopration():
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(hostname='192.168.15.245', username='root', password='pmsl@1234', port='1022')
        sftp_client = ssh.open_sftp()
        # filesssh = sftp_client.chdir('/var/mam/postproduction/testing/')
        isExisting = exists('C:\\Users\\Akash\\PycharmProjects\\mamautomation\\video')
        if not isExisting:
            return "sorece path does not exits"
        files = os.listdir('C:\\Users\\Akash\\PycharmProjects\\mamautomation\\video')
        os.chdir('C:\\Users\\Akash\\PycharmProjects\\mamautomation\\video')
        for f in files:
            sftp_client.put(f, "/Video1/testing/input/video_input1/" + f + "")
        sftp_client.chdir('/Video1/testing/input/video_input1/')
        print(sftp_client.getcwd())
        sftp_client.close()
        ssh.close()
                        
    #checkruningfunction()