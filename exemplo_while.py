import os
import time

segundo = 0
minuto = 0

while True:
    os.system('clear')
    if segundo == 60:
        segundo = 0
        minuto = minuto + 1
    if segundo < 10:
        print(f'0{minuto}:0{segundo}')
    else:
        print(f'0{minuto}:{segundo}')
        
    time.sleep(1)
    segundo = segundo + 1