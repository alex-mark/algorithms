import multiprocessing
import concurrent.futures
import time


def do_something(seconds: int):
    print(f"Sleeping {seconds} second(s)...")
    time.sleep(seconds)
    print(f"Done Sleeping {seconds} second(s)...")


def do_something2(seconds: int):
    print(f"Sleeping {seconds} second(s)...")
    time.sleep(seconds)
    return f"Done Sleeping {seconds} second(s)..."


def oldway_main():
    start = time.perf_counter()

    processes = []

    # create processes
    for _ in range(10):
        p = multiprocessing.Process(target=do_something, args=[1.5])
        p.start()
        processes.append(p)

    # join makes script waiting for process to finish
    for p in processes:
        p.join()

    finish = time.perf_counter()
    print(f"Finished in {round(finish - start, 2)} seconds")


def modern_main():
    start = time.perf_counter()

    secs = [5, 4, 3, 2, 1]
    with concurrent.futures.ProcessPoolExecutor() as executor:
        # results = [executor.submit(do_something2, s) for s in secs]

        # for f in concurrent.futures.as_completed(results):
        #     print(f.result())

        results = executor.map(do_something2, secs)

        for res in results:
            print(res)

    finish = time.perf_counter()
    print(f"Finished in {round(finish - start, 2)} seconds")


if __name__ == "__main__":
    modern_main()
