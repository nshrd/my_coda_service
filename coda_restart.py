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
                os.system('CODA_PRIVKEY_PASS=yourPass coda daemon -discovery-port 8303 -peer /dns4/seed-one.genesis.o1test.net/tcp/10002/ipfs/12D3KooWP7fTKbyiUcYJGajQDpCFo2rDexgTHFJTxCH8jvcL1eAH -peer /dns4/seed-two.genesis.o1test.net/tcp/10002/ipfs/12D3KooWL9ywbiXNfMBqnUKHSB1Q1BaHFNUzppu6JLMVn9TTPFSA -run-snark-worker 4vsRCVwLWZAxAj7ueZeW3j8ddFTvu23oWFLZVdPbv8tSdqJ3h28jgWMF15jn368jqhBNAKE8xmrmjanjYL3Z65oEMo262A7beF7bin5yMDkCoGHpKcSdkdSrCXPoZ6A8xNVVeTR3b8YhrHZZ -snark-worker-fee 1')
                time.sleep(5)
