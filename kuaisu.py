# 从数列中挑出一个元素作为基准数。
# 分区过程，将比基准数大的放到右边，小于或等于它的数都放到左边。
# 再对左右区间递归执行第二步，直至各区间只有一个数。

from random import randint
import time

l = [randint(1,10000)for i in range(10000)]
def kuaisu(l):
