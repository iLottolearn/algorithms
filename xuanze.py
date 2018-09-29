# 在未排序序列中找到最小（大）元素，存放到排序序列的起始位置。
# 再从剩余未排序元素中继续寻找最小（大）元素，然后放到已排序序列的末尾。
# 以此类推，直到所有元素均排序完毕

from random import randint
import time
l = [randint(1,10000)for i in range(10000)]


def xuanze(l):
    start = time.clock()
    for i in range(len(l)):
        for j in range(i,len(l)):
            if l[i] > l[j]:
                l[i],l[j] = l[j],l[i]
    print(l)
    end = time.clock()
    print('running time : %s'%(end-start))

xuanze(l)






