
# STEAL FOR INTERNET
# Link: https://leetcode.com/explore/interview/card/top-interview-questions-medium/103/array-and-strings/776/

# Task
# Given an integer array nums, return all the triplets 
# [nums[i], nums[j], nums[k]] 
# such that i != j, i != k, 
# and j != k, and 
# nums[i] + nums[j] + nums[k] == 0.

# Notice that the solution set must not contain duplicate triplets.


class Solution:

    def threeSum(self, array: List[int]) -> List[List[int]]:
        if len(array) < 3:
            return []
        if (all(num == 0 for num in array)):
            return [[0, 0, 0]]
        size = len(array) 
        found = {}
        array = sorted(array)
        for index, value in enumerate(array):
            left = index + 1
            right = size - 1
            while left < right:
                total = value + array[left] + array[right]
                if total == 0:
                    current = (value, array[left], array[right])
                    if current not in found:
                        found[current] = True
                    right = right - 1
                elif total < 0:
                    left = left + 1
                else:
                    right = right - 1
        return list(found.keys())