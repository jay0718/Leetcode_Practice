class Solution(object):
    def numSquares(self, n):
        while( n % 4 == 0 ):
            n //= 4
        if n % 8 == 7:
            return 4
        for a in range( int(sqrt(n))+1 ):
            b = int( sqrt( n - a*a ) )
            if ( a**2 + b ** 2 ) == n:
                return (a>0) + (b>0)
        return 3