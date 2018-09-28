# 从第一个元素开始，该元素可以认为已经被排序
# 取出下一个元素，在已经排序的元素序列中从后向前扫描
# 如果被扫描的元素（已排序）大于新元素，将该元素后移一位
# 重复步骤3，直到找到已排序的元素小于或者等于新元素的位置
# 将新元素插入到该位置后
# 重复步骤2~5


from random import randint
import time
l = [randint(1,10000)for i in range(10000)]
def charu(l):
    start = time.clock()
    for i in range(1,len(l)):
        for j in range(i):
            if l[i] < l[j]:
                l[i],l[j] = l[j],l[i]
    print(l)
    end = time.clock()
    print("running time : %s"%(end - start))

charu(l)
