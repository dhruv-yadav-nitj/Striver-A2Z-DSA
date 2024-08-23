class Iteration:
    def countAndSay(self, n: int) -> str:
        curr = '1'
        for i in range(1, n):
            cnt = 1
            prev = curr[0]
            i = 1
            temp = ""
            while i < len(curr):
                if curr[i] == prev:
                    cnt += 1
                else:
                    temp += str(cnt) + prev
                    cnt = 1
                    prev = curr[i]
                i += 1
            temp += str(cnt) + prev
            curr = temp
        return curr


class Recursive:
    def helper(self, index: int, n: int, s: str):
        if index == n:
            return s
        cnt = 1
        prev = s[0]
        i = 1
        temp = ""
        while i < len(s):
            if s[i] == prev:
                cnt += 1
            else:
                temp += str(cnt) + prev
                cnt = 1
                prev = s[i]
            i += 1
        temp += str(cnt) + prev
        return self.helper(index + 1, n, temp)

    def countAndSay(self, n: int) -> str:
        return self.helper(1, n, "1")
