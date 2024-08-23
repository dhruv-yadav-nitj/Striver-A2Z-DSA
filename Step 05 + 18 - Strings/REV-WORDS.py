class Solution:
    def reverseWords(self, s: str) -> str:
        s = " ".join((reversed(list(filter(lambda x: len(x) > 0, s.split(" "))))))
        return s
