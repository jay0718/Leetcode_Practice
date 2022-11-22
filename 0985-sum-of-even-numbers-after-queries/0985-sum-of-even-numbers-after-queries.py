class Solution(object):
    def sumEvenAfterQueries(self, A, queries):
        S = sum(x for x in A if x % 2 == 0)
        answer = [ ]

        for x, i in queries:
            if A[i] % 2 == 0: S -= A[i]
            A[i] += x
            if A[i] % 2 == 0: S += A[i]
            answer.append(S)

        return answer