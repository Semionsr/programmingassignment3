import sys



import time

def main():
    data = sys.stdin.read().split('\n')



    idx = 0

    K = int(data[idx]); idx +=1

    values = {}
    for _ in range( K):
        parts = data[idx].split()
        values[parts[0]] =  int(parts[1])
        idx += 1

    A = data[idx]; idx += 1
    B = data[idx]; idx +=1

    n = len(A)
    m = len(B)

    dp = [[0] * (m +1) for _ in range(n + 1)]











    for i in range(1, n +  1 ):
        for j in range(1, m + 1):
            if A[i - 1] == B[j - 1]:



                dp[i][j] = dp[i - 1][j - 1] + values[A[i -1]]
            else:



                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    result = []
    i, j = n,  m
    while i >  0 and j > 0:
        if A[i - 1] ==B[j - 1]:














            result.append(A[i - 1])
            i -= 1
            j -= 1
        elif dp[i - 1][j] >= dp[i][j -1]:
            i -= 1
        else:
            j -= 1

    result.reverse()

    print(dp[n][m] )






    print(''.join(result))

if __name__ == '__main__':
    main()
