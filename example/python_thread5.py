#일정 시간 간격으로 반복 작업 가능한 예제(스크랩핑, 크롤링, 확인성 작업.....)
import time
import threading

def thread_run():
    print('======',time.ctime(),'======')
    #개발하고자 하는 코드
    for i in range(1,10000):
        print('Threading running - ',i)
    #############################
    threading.Timer(2.5,thread_run).start()

if __name__ == "__main__":
    thread_run()
