unicode_1 = ("\u0123", "\u2665", "\U0001f638", "\u265E", "\u265F", "\u2168")
print(unicode_1)

def arm(n):
    d=len(str(n))
    sum_p=sum(int(i)**d for i in str(n))
    return n==sum_p
for n in range(1,1001):
    if arm(n):
        print(n)