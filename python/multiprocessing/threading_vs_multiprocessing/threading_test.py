from threading import Thread, Lock
import time

global_value = 0


def increase(lock):
    global global_value

    lock.acquire()
    local_copy = global_value

    # processing
    local_copy += 1
    time.sleep(0.1)

    global_value = local_copy
    lock.release()


if __name__ == '__main__':
    lock = Lock()
    print('start value', global_value)

    thread1 = Thread(target=increase, args=(lock,))
    thread2 = Thread(target=increase, args=(lock,))

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()

    print('end value', global_value)

    print('end main')
