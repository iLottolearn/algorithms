# 从数列中挑出一个元素作为基准数。
# 分区过程，将比基准数大的放到右边，小于或等于它的数都放到左边。
# 再对左右区间递归执行第二步，直至各区间只有一个数。

from random import randint
import time

ary = [randint(1,10000)for i in range(10000)]

def quick_sort(ary):
    return qs(ary,0,len(ary)-1)

def qs(ary,left,right):
    if left >= right: return ary
    key = ary[left]
    lp = left
    rp = right
    while lp < rp:
        while ary[rp] >= key and lp < rp:
            rp -= 1
        while ary[lp] <= key and lp < rp:
            lp += 1
        ary[lp],ary[rp] = ary[rp],ary[lp]
    ary[lp],ary[left] = ary[left],ary[lp]
    qs(ary,left,lp-1)
    qs(ary,rp+1,right)
    return ary

def main():
    start = time.clock()
    reslut = quick_sort(ary)
    print(reslut)
    end = time.clock()
    print("running time : %s"%(end -start))

if __name__ == '__main__':
    main()


