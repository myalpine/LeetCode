# 2020年7月4日（土）

# 最初の解答

class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        TargetArray = []
        for i in range(len(index)):
            TargetArray.insert(index[i], nums[i])
        return TargetArray

# zip関数を使うと速い。

    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        TargetArray=[]
        for i,v in zip(index,nums):
            TargetArray.insert(i,v)
        return TargetArray

# ローカルで実行する場合は以下のように記述する。

# from typing import List

# class Solution:
#    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
#        TargetArray=[]
#        for i,v in zip(index,nums):
#            TargetArray.insert(i,v)
#        return TargetArray

#if __name__ == '__main__':
#    nums = [0,1,2,3,4]
#    index = [0,1,2,2,1]

#    test = Solution()
#    print(test.createTargetArray(nums, index))