class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        def mohit(data, val, low, high):
            if low > high:
                return low
            mid = (low + high)//2

            if data[mid] == val:
                return mid
            elif data[mid] < val:
                return mohit(data, val, mid + 1, high)
            elif data[mid] > val:
                return mohit(data, val, low, mid -1)
        return mohit(nums, target, 0, len(nums)-1)