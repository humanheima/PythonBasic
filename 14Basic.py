# 进程和线程

from multiprocessing import Process

from multiprocessing import Pool

import os, time, random


# fock子进程
# print("Process (%s) start ..." % os.getpid())

# pid = os.fork()
# if pid == 0:
#     print("I am child process (%s) and my parent is %s." % (os.getpid(), os.getppid()))
# else:
#     print("I (%s) just created a child process (%s)." % (os.getpid(), pid))


# 下面的例子演示了启动一个子进程并等待其结束


# def run_proc(name):
#     print("Run child process %s (%s)" % (name, os.getpid()))


# if __name__ == "__main__":
#     print("Parent process %s." % os.getpid())
#     p = Process(target=run_proc, args=("test",))
#     print("Child process will start.")
#     p.start()
#     p.join()
#     print("Child process end.")


# 进程池的方式批量创建子进程：

def long_time_task(name):
    print('Run task %s (%s)...' %(name,os.getpid()))
    start=time.time()
    time.sleep(random.random()*3)
    end=time.time()
    print('Task %s runs %0.2f seconds.'%(name,(end-start)))


if __name__=='__main__':
    print('Parent process %s.' %os.getpid())
    p=Pool(4)
    for i in range(5):
        p.apply_async(long_time_task,args=(i,))

    print('Waiting for all subprocesses done...')
    p.close()
    p.join()
    print('All subprocesses done.')