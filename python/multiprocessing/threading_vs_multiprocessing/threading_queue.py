from threading import Thread, Lock, currentThread
from queue import Queue

global_value = 0


def worker(q, lock):
    while True:
        value = q.get()
        # processing...
        with lock:
            print(f'in {currentThread().name} got {value}')
        q.task_done()


if __name__ == '__main__':
    q = Queue()

    num_threads = 10
    lock = Lock()

    for _ in range(num_threads):
        thread = Thread(target=worker, args=(q, lock))
        thread.daemon = True
        thread.start()

    for i in range(1, 30):
        q.put(i)

    q.join()

    print('end main')
