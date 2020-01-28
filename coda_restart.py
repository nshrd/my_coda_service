#!/usr/bin/python

import psutil
import subprocess
import os
import time

while True:
        def checkIfProcessRunning(Coda):
            '''
            Check if there is any running process that contains the given name processName.
            '''
            #Iterate over the all the running process
            for proc in psutil.process_iter():
                try:
                    # Check if process name contains the given name string.
                    if Coda.lower() in proc.name().lower():
                        return True
                except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                    pass
            return False;

        if checkIfProcessRunning('coda'):
                print('Coda is running')
                time.sleep(5)
        else:
                
                print('coda is down attempting restart')
                os.system('CODA_PRIVKEY_PASS=12!@qw!@ coda daemon -discovery-port 8303 -peer /dns4/seed-one.genesis.o1test.net/tcp/10002/ipfs/12D3KooWP7fTKbyiUcYJGajQDpCFo2rDexgTHFJTxCH8jvcL1eAH -peer /dns4/seed-two.genesis.o1test.net/tcp/10002/ipfs/12D3KooWL9ywbiXNfMBqnUKHSB1Q1BaHFNUzppu6JLMVn9TTPFSA -run-snark-worker 4vsRCVi1g89BGiyWT4J7Ek3mGquYxSuxh8vCbxP4avqtjUv7Aywt3Jep6pSeAkUgx4SHBu6rUy2mCQEWEAbc3DmKk9WPPoaCAQ1ARbHuBvtN7H7oMoKerAATuZuGtReLkiHjcp88Qx4BXy8T -snark-worker-fee 1')
                time.sleep(5)
