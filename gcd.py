class Solution:
    def findGCD(self, nums) -> int:
        min = max = nums[0]

        for i in nums:
            if i < min:
                min = i

            if i > max:
                 max = i

        while max and min:
            if max > min :
                max %= min 
            else:
                min %= max
        return max if max > min else min                        
    

solution = Solution()
num = [3,3,5,3,6,3,2,3,4,6,2,3,46,3,2,4]
print(solution.findGCD(num))
