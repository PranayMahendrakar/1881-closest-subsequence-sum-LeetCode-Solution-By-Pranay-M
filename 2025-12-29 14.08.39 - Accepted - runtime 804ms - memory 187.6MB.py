class Solution:
    def minAbsDifference(self, nums: List[int], goal: int) -> int:
        from bisect import bisect_left
        n = len(nums)
        mid = n // 2
        def get_sums(arr):
            sums = {0}
            for x in arr:
                sums = sums | {s + x for s in sums}
            return sums
        left = sorted(get_sums(nums[:mid]))
        right = sorted(get_sums(nums[mid:]))
        ans = abs(goal)
        for s1 in left:
            t = goal - s1
            i = bisect_left(right, t)
            if i < len(right):
                ans = min(ans, abs(s1 + right[i] - goal))
            if i > 0:
                ans = min(ans, abs(s1 + right[i-1] - goal))
        return ans