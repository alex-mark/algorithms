from multiprocessing import Process
import os
import time


def square_numbers():
    for i in range(100):
        i * i
        time.sleep(0.1)


def test_processing():
    processes = []
    num_processes = os.cpu_count()
    print(num_processes)

    # create processes
    for i in range(num_processes):
        p = Process(target=square_numbers)
        processes.append(p)

    # start
    for p in processes:
        p.start()

    # join
    for p in processes:
        p.join()

    print('end main')


if __name__ == '__main__':
    test_processing()
