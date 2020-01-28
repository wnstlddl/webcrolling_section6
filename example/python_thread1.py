import threading

# 쓰레드(스레드) 실행
def thread_run():
    print('Thread Runnung - F')

def thread_run_msg(msg):
    print('Thread Runnung - F ', msg)

for i in range(1000):
    t1 = threading.Thread(target=thread_run)
    t2 = threading.Thread(target=thread_run_msg, args=('service',))

    t1.start()
    t2.start()
