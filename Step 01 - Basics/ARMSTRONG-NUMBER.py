class Solution:
    def armstrongNumber (self, n):
        n = str(n)
        temp = 0
        for i in n:
            temp += int(i)**3
        return str(temp == int(n)).lower()
