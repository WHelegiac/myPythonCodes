'''
Author: WanHao
Date: 2022-02-12 21:40:27
LastEditors: Do not edit
LastEditTime: 2022-02-12 21:41:31
FilePath: \my_python_codes\multiProcess\demo01.py
FileDescription: Lazy~~~
'''
import time
import os
import multiprocessing

cnt = 

def consumer(queue):
    while True:
        cnt = queue.get()
        print(f"I am a consmer, cnt = {cnt} and process id = {os.getpid()}")
        time.sleep(1)


def producer(queue):
    while True:
        queue.put(cnt)
        print(f"I am a producer ,cnt = {cnt} and process id is{os.getpid()}")
        time.sleep(1)
        cnt += 1


if __name__ == "__main__":
        
    queue = multiprocessing.Queue()
    pro1 = multiprocessing.Process(target=producer, args=(queue,))
    pro2 = multiprocessing.Process(target=consumer, args=(queue,))

    pro1.start()
    pro2.start()
