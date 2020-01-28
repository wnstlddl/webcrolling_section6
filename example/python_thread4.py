#로깅(logging)
import logging
import threading
import time

logging.basicConfig(
    level=logging.DEBUG,
    format='[%(levelname)s %(threadName)-8s %(message)s]',
)
def worker1():
    logging.debug('Starting')
    time.sleep(0.5)
    logging.debug('Existing')

def worker2():
    logging.debug('Starting')
    time.sleep(0.5)
    logging.debug('Existing')

#데몬쓰레 : (옵션 생략 시 기본 쓰레드)

t1 = threading.Thread(name='service-1',target=worker1)
t2 = threading.Thread(name='service-2',target=worker2,daemon=True)
t3 = threading.Thread(target=worker1,daemon=True)


if __name__=="__main__":
    t1.start()
    t2.start()
    t3.start()

    #Join 메소드 호출로 쓰레드 종료시 까지 대기
    t1.join() #join() 시간 동안 대기
    t2.join()
    t3.join()
