from multiprocessing import Pool
import threading

class A():
    def __init__(self,i):
        # super(A, self).__init__()
        self.tid = i

    def runa(self):
        print('done!')
        # thread.exit()
        sys.exit()

def process():
    pool = Pool(processes=4)
    queries = [[0 for j in range(0,10)] for i in range(0,10)]
    for i in range(0,10):
        y = A(i)
        pool.apply_async(y.runa, args=())
    pool.close()
    pool.join()
    print("exit")

if __name__=='__main__':
    process()