class Solution:
    def isValid(self, s: str) -> bool:
        hash_value = {
            "(" : ")", "[" : "]", "{" : "}"
        }
        stack = []

        for i in s:
            if i in hash_value:
                stack.append(i)
            else:
                if not stack:
                    return False
                top = stack.pop()
                if hash_value[top] != i:
                    return False
        return len(stack) == 0