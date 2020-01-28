import threading

#쓰레드 실행 - 클래스형

class Thread_Run(threading.Thread):
    def run(self):
        print('Thread runnuig - C')

for i in range(1000):
    t = Thread_Run()

    t.start()
