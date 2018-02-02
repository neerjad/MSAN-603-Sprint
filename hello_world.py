import time
start_time = time.time()

with open('~/Output/output_'+str(start_time), 'w') as f:
	f.write('Hello World'+"\n")
	f.write("Done!\n")