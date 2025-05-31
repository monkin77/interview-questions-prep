from typing import *

DELIMITER = '#'

class Solution:

    def encode(self, strs: List[str]) -> str:
        final_str = ""

        for cur_str in strs:
            append_str = f"{len(cur_str)}#{cur_str}"

            final_str += append_str

        return final_str

    def decode(self, s: str) -> List[str]:
        str_list = []

        idx = 0
        next_str_len = ""
        while idx < len(s):
            if s[idx] == DELIMITER:
                str_len = int(next_str_len)
                next_str = s[idx+1:idx+1+str_len]
                str_list.append(next_str)

                # Increment the idx
                idx += (str_len + 1)
                next_str_len = ""
            else:
                # Concatenating the numbers corresponding to the next string length
                next_str_len += s[idx]
                idx += 1
        
        return str_list
