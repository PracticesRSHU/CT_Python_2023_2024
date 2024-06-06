# from multiprocessing import Process
#
# def print_func(continent='Asia'):
#     print('The name of continent is : ', continent)
#
# if __name__ == "__main__":  # confirms that the code is under main function
#     names = ['America', 'Europe', 'Africa']
#     procs = []
#     proc = Process(target=print_func)  # instantiating without any argument
#     procs.append(proc)
#     proc.start()
#
#     # instantiating process with arguments
#     for name in names:
#         # print(name)
#         proc = Process(target=print_func, args=(name,))
#         procs.append(proc)
#         proc.start()
#
#     # complete the processes
#     for proc in procs:
#         proc.join()


import multiprocessing
import time
import random

def worker(number):
    sleep = random.randrange(1, 10)
    time.sleep(sleep)
    print("Я Worker {}, я спав {} секунд".format(number, sleep))

if __name__=='__main__':
    for i in range(5):
        t = multiprocessing.Process(target=worker, args=(i,))
        t.start()

    print("Всі процеси запущено, давайте почекаємо поки вони виконаються!")


# from multiprocessing import Pool

# def f(x):
#     return x*x

# if __name__ == '__main__':
#     p = Pool(5)
#     print(p.map(f, [1, 2, 3]))


from concurrent.futures import ThreadPoolExecutor
from time import sleep
 
# def return_after_5_secs(message):
#     sleep(5)
#     return message
#
# pool = ThreadPoolExecutor(3)
#
# future = pool.submit(return_after_5_secs, ("hello"))
# print(future.done())
# sleep(5)
# print(future.done())
# print(future.result())
