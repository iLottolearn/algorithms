#比较相邻的两个数，如果第一个数大于第二个数就交换位置，最大数就浮到了最后面



from random import randint
import time
l = [randint(1,10000)for i in range(10000)]

def maopao(l):
    start = time.clock()
    for i in range(1,len(l)):
        for j in range(len(l)-i):
            if l[j] > l[j+1]:
                l[j],l[j+1] = l[j+1],l[j]
    print(l)
    end = time.clock()
    print("running time : %s"%(end - start))

maopao(l)