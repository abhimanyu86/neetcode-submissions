class Solution:
    def reverseBits(self, n: int) -> int:
        result = 0
        for i in range(32):
            bit = (n >> i) & 1      # extract bit i from n (from the right)
            result = result | (bit << (31 - i))  # place it at the mirrored position
        return result