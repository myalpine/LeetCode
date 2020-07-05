# 2020年7月5日（日）

from typing import List

class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        ans = []
        for i in range(0, len(nums), 2):
            ans += [nums[i + 1]] * nums[i]
        return ans

if __name__ == '__main__':
    nums = [1,2,3,4]
    test = Solution()

    print(f'Input:{nums}')
    print(f'Output:{test.decompressRLElist(nums)}')