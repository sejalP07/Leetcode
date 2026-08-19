class Solution:
    def myAtoi(self, s: str) -> int:
        i = 0
        n = len(s)

        INT_MIN = -2147483648
        INT_MAX = 2147483647

        # 1. Skip leading spaces
        while i < n and s[i] == ' ':
            i += 1

        # 2. Determine sign
        sign = 1

        if i < n and s[i] == '-':
            sign = -1
            i += 1

        elif i < n and s[i] == '+':
            i += 1

        # 3. Build number
        num = 0

        while i < n and s[i].isdigit():
            digit = int(s[i])
            num = num * 10 + digit
            i += 1

        # 4. Apply sign
        num *= sign

        # 5. Clamp to 32-bit range
        if num < INT_MIN:
            return INT_MIN

        if num > INT_MAX:
            return INT_MAX

        return num