class Solution:


    def isValid(self, s):

        pairs = dict(['()','[]','{}'])

        stack = []

        for idx in s:

            if idx in '([{':

                stack.append(idx)

            elif len(stack) == 0 or idx != pairs[stack.pop()]: 
                return False


        return len(stack) == 0


solution = Solution()

result = solution.isValid('(){}[]')

print(result)           