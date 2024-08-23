class Solution:

    # Function to return a list containing the union of the two arrays.
    def findUnion(self, arr1, arr2, n, m):
        """
        :param arr1: given sorted array a
        :param n: size of sorted array a
        :param arr2: given sorted array b
        :param m: size of sorted array b
        :return:  The union of both arrays as a list
        """
        i = j = 0
        ans = []
        while i < n and j < m:
            while i+1 < n and arr1[i] == arr1[i+1]:
                i += 1
            while j+1 < m and arr2[j] == arr2[j+1]:
                j += 1
            if arr1[i] < arr2[j]:
                ans.append(arr1[i])
                i += 1
            elif arr2[j] < arr1[i]:
                ans.append(arr2[j])
                j += 1
            else:
                ans.append(arr1[i])
                i += 1
                j += 1
        while i < n:
            while i+1 < n and arr1[i] == arr1[i+1]:
                i += 1
            ans.append(arr1[i])
            i += 1
        while j < m:
            while j+1 < m and arr2[j] == arr2[j+1]:
                j += 1
            ans.append(arr2[j])
            j += 1
        return ans
