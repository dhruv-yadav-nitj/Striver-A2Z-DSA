from typing import List
from queue import Queue
from collections import defaultdict, Counter

"""
Better watch the video!
"""


class Solution:
    def findLadders(self, begin: str, end: str, wordlist: List[str]) -> List[List[str]]:
        st = set(wordlist)
        q = Queue()
        q.put([begin])
        used_on_level = [begin]
        level = 0
        ans = []
        while not q.empty():
            curr: List[str] = q.get()
            if len(curr) > level:
                level += 1
                for item in used_on_level:
                    st.discard(item)
            word = curr[-1]
            if word == end:
                if len(ans) == 0:
                    ans.append(curr)
                elif len(ans[-1]) == len(curr):
                    ans.append(curr)
            for i in range(len(word)):
                for c in range(ord('a'), ord('z') + 1):
                    ch = chr(c)
                    temp = word[:i] + ch + word[i + 1:]
                    if temp in st:
                        curr_copy = curr[:] + [temp]  # we need to create the copy bcz Python sucks here you know!
                        q.put(curr_copy)
                        used_on_level.append(temp)
        return ans
