class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:

        def canSplit(largest):
            # Number of times we need to create a new subarray.
            subarray = 0

            # Sum of the current subarray.
            cursum = 0

            for n in nums:
                cursum += n

                # Current subarray is too large.
                if cursum > largest:
                    # Start a new subarray.
                    subarray += 1

                    # Current number becomes the first
                    # element of the new subarray.
                    cursum = n

            # Number of subarrays = number of splits + 1.
            return subarray + 1 <= k

        # Smallest possible answer:
        # We cannot have a subarray sum smaller than
        # the largest individual number.
        l, r = max(nums), sum(nums)

        # Largest possible answer.
        res = r

        while l <= r:

            # Try the middle possible maximum sum.
            mid = l + ((r - l) // 2)

            if canSplit(mid):
                # mid works, so it is a possible answer.
                res = mid

                # Try to find a smaller valid answer.
                r = mid - 1

            else:
                # mid is too small.
                # We need a larger maximum sum.
                l = mid + 1

        return res