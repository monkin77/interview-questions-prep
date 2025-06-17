class Solution:
    def reverseBits(self, n: int) -> int:
        # obtain string representing the binary representation of n
        reversed_num = 0
        for i in range(32):
            # Obtain the current Least-Significant Bit
            cur_bit = n & 0b1

            # Shift n by one bit to the right
            n >>= 1

            # Shift the reversed num to the left
            reversed_num <<= 1
            # Include the current bit on the reverse num
            reversed_num |= cur_bit

        return reversed_num
