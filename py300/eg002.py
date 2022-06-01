#!/usr/bin/env python
# coding=utf-8
'''
合并两个升序的整数数组A和B，形成一个新的数组，新数组也要有序。
输入A=[1]，B=[1]，输出[1，1]，返回合并后的数组。输入A=[1，2，3，4]，B=[2，4，5，6]，
输出[1，2，2，3，4，4，5，6]，返回合并所有元素后的数组。

!!!排序异常
'''


class Solution:
    def mergeSortedArray(self, A, B):
        i, j = 0, 0
        G = []
        while i < len(A) and j < len(B):
            if A[i] < B[j]:
                G.append(A[i])
                i += 1
            else:
                G.append(B[i])
                j += 1
            # while i < len(A):
            #     G.append(A[i])
            #     i += 1
            # while j < len(B):
            #     G.append(B[j])
            #     j += 1
        return G


if __name__ == '__main__':
    A = [50, 14]
    B = [18, 290, 3]
    C = [9, 2, 3, 4]
    D = [20, 4, 5, 6]
    solution = Solution()
    print("输入:", A, " ", B)
    print("输出:", solution.mergeSortedArray(A, B))
    print("输入:", C, " ", D)
    print("输出:", solution.mergeSortedArray(C, D))
