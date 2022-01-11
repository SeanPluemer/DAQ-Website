import time
import paramiko
import scp
import streamlit
import os

ssh = paramiko.client.SSHClient()
ssh.set_missing_host_key_policy(paramiko.client.AutoAddPolicy())
ssh.connect('192.168.0.170', username='pi',password='raspberry') #todo right now this is a static ip, need to find a way to "find" pi's
chan = ssh.invoke_shell()
scp = scp.SCPClient(ssh.get_transport())

def run_cmd(cmd, path):
    print('='*30)
    print('[CMD]', cmd)
    chan.send("cd " + path + '\n')
    chan.send(cmd + '\n')
    time.sleep(2)
    buff = ''
    while chan.recv_ready():
        print('Reading buffer')
        resp = chan.recv(9999)
        buff = resp.decode()
        print(buff)
        streamlit.write(buff)

        time.sleep(2)

    print('Command was successful: ' + cmd)


def copy_files_to_pi(test_config, signal_config, path):
    scp.put(test_config, path+"/test_config.csv")
    scp.put(signal_config, path+"/signal_config.csv")

def copy_files_from_pi(file_name, path, local_path):
    try:
        #os.chdir(local_path)
        scp.get( path+file_name,local_path)

    except Exception as e:
        streamlit.write(path+file_name, "not found")
        streamlit.write(e)



if __name__ == '__main__':
    # test1.py executed as scriptc
    # do something
    print("HELLO, I AM HERE")
    path = '/home/pi/'
    copy_files_to_pi("test1.txt","test2.txt", path )


    run_cmd('python3 demo.py')