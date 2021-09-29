import time
from multiprocessing import Array, Lock, Process, Queue, Value


def add_100(number, numbers_array, lock):
    for _ in range(100):
        time.sleep(0.01)
        # with lock:
        #     number.value += 1
        for i in range(len(numbers_array)):
            with lock:
                numbers_array[i] += 1


if __name__ == '__main__':
    lock = Lock()
    shared_number = Value('i', 0)
    shared_array = Array('d', [0.0, 100.0, 200.0])
    print('Number at the beginning:', shared_number.value)
    print('Array at the beginning:', shared_array[:])

    p1 = Process(target=add_100, args=(shared_number, shared_array, lock))
    p2 = Process(target=add_100, args=(shared_number, shared_array, lock))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print('number at the end:', shared_number.value)
    print('array at the end:', shared_array[:])
