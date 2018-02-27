#!/usr/bin/env python

import paramiko
import time

def deploy(key, server, prefix):
	print "Connecting to box"
	ssh = paramiko.SSHClient()

	ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	ssh.connect(server, username = 'testtest', key_filename = key )

	ssh.exec_command('sudo yum install git -y')
	ssh.exec_command('rm -rf MSAN-603-Sprint; git clone https://github.com/neerjad/MSAN-603-Sprint.git;')

	ssh.exec_command("crontab -r") 
  
	print "Launching Flask Server"
	time.sleep(2)
	ssh.exec_command('sudo python $(pwd)/MSAN-603-Sprint/flask_server.py ' + prefix)

	print "Pull from Github successful"
	time.sleep(2)   

	print "Script fully executed ... exiting" 
	ssh.close()
	## EOF ##

#deploy('/Users/ryan/config/aws/sprint.pem', 'ec2-54-202-16-162.us-west-2.compute.amazonaws.com', 'hi')