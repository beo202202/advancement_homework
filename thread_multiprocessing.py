import threading
from multiprocessing import Process
import os


def foo():
    print('thread id', threading.get_native_id())
    print('process id', os.getpid())


def bar():
    print('This is bar')


def baz():
    print('This is baz')


if __name__ == '__main__':
    child1 = Process(target=foo).start()
    child2 = Process(target=bar).start()
    child3 = Process(target=baz).start()

    thread1 = threading.Thread(target=foo).start()
    thread2 = threading.Thread(target=foo).start()
    thread3 = threading.Thread(target=foo).start()

# thread id 22504
# process id 2036
# thread id 1600
# thread id 16980
# process id 2036
# process id 2036
# thread id 19696
# process id 15408
# This is bar
# This is baz
