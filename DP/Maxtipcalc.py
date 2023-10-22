def findmaxtip(a, b , x, y, n, ind):

    sum1=sum2=0
    if ind >= n:
        return 0
    
    if x > 0:
        sum1 += a[ind] + findmaxtip(a, b, x-1, y, n, ind+1)

    if y > 0:
        sum2 += b[ind] + findmaxtip(a, b, x, y-1, n, ind+1)

    return max(sum1, sum2)

if __name__ == "__main__":

    ind = 0
    n, x, y = map(int, input().split())
    a =  list(map(int, input().split()))
    b = list(map(int, input().split()))
    print(findmaxtip(a, b, x, y, n, ind))