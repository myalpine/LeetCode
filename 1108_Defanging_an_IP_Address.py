# 2020年7月4日（土）

class Solution:
    def defangIPaddr(self, address: str) -> str:
        return address.replace(".","[.]")

# if __name__ == '__main__':
#    address = "1.1.1.1"
#    address2 = "255.100.50.0"
#    test = Solution()

#    print(f'Input: {address}')
#    print(f'Output: {test.defangIPaddr(address)}')
#    print(f'Input: {address2}')
#    print(f'Output: {test.defangIPaddr(address2)}')