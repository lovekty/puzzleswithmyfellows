# -*- coding: utf-8 -*-
# author: tony.zhuby
# date: 2018/3/8


def solution(N):
    count = 0
    index = 2
    while N / index - index / 2 > 0:
        if index % 2 != 0 and N % index == 0:
            count += 1
        elif index % 2 == 0 and N % index == (index / 2):
            count += 1
        index += 1
    return count


if __name__ == '__main__':
    print(solution(100))
    # print(solution2(15))
