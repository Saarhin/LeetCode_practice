# LeetCode_practice

My solutions to LeetCode problems

# 9. Palindrome Number

Given an integer x, return true if x is palindrome, and false otherwise

### Idea

Convert to str and compare with the str[::-1]

# 26. Remove Duplicates from Sorted Array

Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place

### Idea

Have a variable pointing at the index of nums array that the next value is inseted.

# 27. Remove Element

Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. The order of the elements may be changed. Then return the number of elements in nums which are not equal to val.

### Idea

have a pointer to show the position at which you should insert the next num != value

# 35. Search Insert Position

Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

### Idea

Use binary search

# 66. Plus One

You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's.

### Idea

Start from the end of the array and save the carry on each addition

# 88. Merge Sorted Array

Merge nums1 and nums2 into a single array sorted in non-decreasing order.

### Idea

Start from the end of arrays and check element by element

# 108. Convert Sorted Array to Binary Search Tree

Given an integer array nums where the elements are sorted in ascending order, convert it to a height-balanced binary search tree.

### Idea

User recursion to find middle as head and process the left and right array
