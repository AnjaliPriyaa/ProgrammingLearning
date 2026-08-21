class Solution:
    def reverseBits(self, n: int) -> int:
        """
        result = 0
        FOR i from 0 to 31:
        # STEP 1: GET the bit at position i
        # >> moves the desired bit to the rightmost position
        # & 1 extracts only that bit
        bit = (n >> i) & 1
        # STEP 2: MOVE the bit to its reversed position
        # Original position i → Reversed position (31 - i)
        shifted_bit = bit << (31 - i)
        # STEP 3: ADD the bit to the result
        # | combines the new bit with the bits already stored
        # without losing the previous bits
        result = result | shifted_bit
        RETURN result
        """

        res = 0
        for i in range(32):
            bit = (n >> i) & 1
            res = res | (bit << (31 - i))
        return res