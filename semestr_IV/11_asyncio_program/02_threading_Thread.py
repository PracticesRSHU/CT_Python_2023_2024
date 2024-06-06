# import threading
#
# def print_cube(num):
#     """
#     function to print cube of given num
#     """
#     print("\nCube: {}".format(num * num * num))
#
# def print_square(num):
#     """
#     function to print square of given num
#     """
#     print("\nSquare: {}".format(num * num))
#
# if __name__ == "__main__":
#     # creating thread
#     t1 = threading.Thread(target=print_square, args=(10,))
#     t2 = threading.Thread(target=print_cube, args=(10,))
#
#     # starting thread 1
#     t1.start()
#     # starting thread 2
#     t2.start()
#
#
#     # wait until thread 2 is completely executed
#     t2.join()
#     # wait until thread 1 is completely executed
#     t1.join()
#     # both threads completely executed
#     print("Done!")
#

import threading
import time
import random


def worker(number):
    sleep = random.randrange(1, 10)
    time.sleep(sleep)
    print("Я Worker {}, я спав {} секунд".format(number, sleep))


for i in range(5):
    t = threading.Thread(target=worker, args=(i,))
    t.start()
    # t.join()
print("Всі потоки запущено, давайте почекаємо поки вони виконаються!")
