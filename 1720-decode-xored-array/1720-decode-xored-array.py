class Solution:
    def decode(self, encoded: list[int], first: int) -> list[int]:
        arr = [first]

        for num in encoded:
            next_num = arr[-1] ^ num
            arr.append(next_num)

        return arr