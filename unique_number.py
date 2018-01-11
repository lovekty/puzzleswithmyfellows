# -*- coding: utf-8 -*-
# author: tony zhuby
# date: 2018-01-10


def solution(nums):
    ret = 0
    for num in nums:
        ret = ret ^ num
    return ret


if __name__ == '__main__':
    array = [1, 2, 3, 4, 5, 4, 7, 8, 7, 1, 3, 5, 8]
    print(solution(array))
