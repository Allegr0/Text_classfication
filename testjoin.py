import threading, time  
def doWaiting():  
    print('start waiting1: ' + time.strftime('%H:%M:%S') + "\n"  )
    time.sleep(3)  
    print('stop waiting1: ' + time.strftime('%H:%M:%S') + "\n" )
def doWaiting1():  
    print('start waiting2: ' + time.strftime('%H:%M:%S') + "\n"   )
    time.sleep(8)  
    print('stop waiting2: ', time.strftime('%H:%M:%S') + "\n"  )
tsk = []   
for i in range(3):
    thread1 = threading.Thread(target = doWaiting)  
    thread1.start()  
    tsk.append(thread1)
for tt in tsk:
    tt.join()
for i in range(3):
    thread2 = threading.Thread(target = doWaiting1)  
    thread2.start()  
    tsk.append(thread2)
print('start join: ' + time.strftime('%H:%M:%S') + "\n")
for tt in tsk:
    tt.join()
print('end join: ' + time.strftime('%H:%M:%S') + "\n") 