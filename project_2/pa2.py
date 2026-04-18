import os
import time

pid = os.fork() #Ask kernel to create a child process

if pid == 0: # Child id return 0 
    print("Child PID:", os.getpid()) # We get the child pid
    os._exit(0)  # Immediately terminate child process
else:
    print("Parent PID:", os.getpid()) # Gets the parent process id
    print("Parent Sleeping for 10 seconds...")
    for i in range(10,0,-1):
        time.sleep(1) # Count down for 10 seconds
        print(f'Time Remaining: {i}')
    print("Parent Exiting Now.")

