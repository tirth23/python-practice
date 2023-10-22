def pow(base, exp):
    if exp == 1:
        return base
    if exp != 1:
        return base*pow(base, exp-1)

base = 2
exp = 4
print("value is ", pow(base, exp))

# Another method
base = 2
exp = 4
ans = 1
while exp >= 1:
    ans = base * ans
    exp -= 1
print(ans)
