# class Solution: required by LeetCode format
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # Initialize both current and global maximum sums with the first element
        current_max = global_max = nums[0]

        # Start iterating from the second element
        for i in nums[1:]:
            # Decide whether to start a new subarray at i or continue the current one
            if i > current_max + i:
                current_max = i  # Start new subarray
            else:
                current_max += i  # Extend current subarray

            # Update global maximum if needed
            if global_max < current_max:
                global_max = current_max

        return global_max  # Return the largest subarray sum found




        '''
        # Brute force method using prefix sums and combinations
        # Generates all subarrays and finds the one with the maximum sum
        # This is correct but very slow for large inputs (O(n²))

        n = len(nums)

        # Build prefix sum array so we can get subarray sums in O(1)
        prefix = [0]
        for num in nums:
            prefix.append(prefix[-1] + num)
        # Example: for nums = [2, 4, 6], prefix = [0, 2, 6, 12]

        # Initialize max_sum to smallest possible value
        max_sum = float('-inf')

        # Loop over all possible subarrays using (start, end) pairs
        for i, j in combinations(range(n + 1), 2):
            sum = prefix[j] - prefix[i]  # Subarray sum from i to j-1
            if sum > max_sum:
                max_sum = sum
            # Uncomment to see all subarrays:
            # print(nums[i:j])

        return max_sum  # Final result (only for small arrays)
        '''

