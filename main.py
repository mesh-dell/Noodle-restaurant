n = int(input())
corner = []
product = 1
if 2 <= n <= 50:
    for i in range(n):
        s = input()
        s = s.split(' ')
        if i == 0 or i == n - 1:
            corner.append(s[0])
            corner.append(s[len(s) - 1])

    for i in corner:
        product *= int(i)

print(product)
