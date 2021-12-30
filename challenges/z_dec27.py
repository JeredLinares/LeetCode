###
27 Dec 2021

The complement of an integer is the integer you get when you flip all the 0's to 1's and all the 1's to 0's in its binary representation.

For example, The integer 5 is "101" in binary and its complement is "010" which is the integer 2.
Given an integer num, return its complement.


class Solution:
    def findComplement(self, num: int) -> int:
        int_2 = format(num,'b')
        output_value = ''
        for char_val in int_2:
            if char_val == '0':
                output_value += '1'
            else:
                output_value += '0'
        return int(output_value,2)

LEARNED: 


