# python 2.7
#
# this is the windows version of ssh_n_move as pxssh does not exist for windows
#
# required modules: paramiko and pycrypto
#
# the later can apparently be a pain to install and so instead of installing python, have installed anaconda, then run:
# conda install paramiko
# conda install pycrytpo (although this should be installed automatically)
#
# todo: find a secure method for storing the password
# todo: log successful mv

import paramiko

# ssh client
ssh = paramiko.SSHClient()
# auto accept host key without prompting and requiring response from a user
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
# connect to server
# ssh.connect('athena.kcl.ac.uk', username='ryank', password='password')
ssh.connect('5.2.65.31', port=400, username='wook', password='password')
# send move command
# stdin, stdout, stderr = ssh.exec_command('mv /gpfs/home/ryank/NGS_runs/testdir2/* /gpfs/home/ryank/NGS_runs/testdir')
stdin, stdout, stderr = ssh.exec_command('mv /home/wook/t1/* /home/wook/t2')
