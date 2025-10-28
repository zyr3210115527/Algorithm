class Solution(object):
    def find(self, nums, target):
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        return -1

    def twoSum(self, numbers, target):
        i = 0
        while i < len(numbers):
            if find(self, numbers, target - numbers[i]) != -1 and find(self, numbers, target - numbers[i]) != i:
                if i + 1 < find(self, numbers, target - numbers[i]) + 1:
                    return [i + 1, find(self, numbers, target - numbers[i]) + 1]
                else:
                    return [find(self, numbers, target - numbers[i]) + 1, i + 1]
            i += 1

