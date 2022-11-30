from collections import Counter
class Solution(object):
    def uniqueOccurrences(self, arr):
        dct=Counter(arr)
        st=set()
        for i in dct:
            st.add(dct[i])
        if len(dct)==len(st):
            return True
        return False