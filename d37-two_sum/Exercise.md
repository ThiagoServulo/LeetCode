# Two Sum

> Level: Easy

Given an array of integers, find two numbers such that they add up to a specific target number.

The function twoSum should return indices of the two numbers such that they add up to the target, where index1 < index2. Please note that your returned answers (both index1 and index2 ) are not zero-based. Put both these numbers in order in an array and return the array from your function ( Looking at the function signature will make things clearer ). Note that, if no pair exists, return an empty list.

If multiple solutions exist, output the one where index2 is minimum. If there are multiple solutions with the minimum index2, choose the one with minimum index1 out of them.

---

## Example 1:

**Input:**

    A: [2, 7, 11, 15]
    B: 9


**Output:**

    [1, 2]


**Explanation:** The elements present at index 1 and index 2 add up to 9. i.e. A[1] + A[2] = 9 (1-based indexing)