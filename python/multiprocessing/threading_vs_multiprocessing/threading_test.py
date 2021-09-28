from threading import Thread
import time

global_value = 0


def increase():
    global global_value

    local_copy = global_value

    # processing
    local_copy += 1
    time.sleep(0.1)

    global_value = local_copy


if __name__ == '__main__':
    print('start value', global_value)

    thread1 = Thread(target=increase)
    thread2 = Thread(target=increase)

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()

    print('end value', global_value)

    print('end main')
