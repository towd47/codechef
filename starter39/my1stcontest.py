nums = input()
n, a, b = nums.split()
n = int(n)
a = int(a)
b = int(b)

x = n - a
y = x - b
print(str(x) + " " + str(y))