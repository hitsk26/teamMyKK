import threading
import time
import sys
def f():
    i = 1
    while True:
        print(i)
        i += 1
        time.sleep(1)
        if i == 10:
            break

th = threading.Thread(target=f,name="th",args=())
th.setDaemon(True)
th.start()
while True:
    print('charcter')
    c = sys.stdin.read(1)
    print(c)
    if c == 'a':
        sys.exit()
