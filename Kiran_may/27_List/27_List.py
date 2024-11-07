# 1.Accessing Nested List Elements:
l = [11, 22, 33, ["raj", "pavan"], 66, [99, 22]]
print(l[3][1])  # pavan

name = (l[3][1])
print(name)          # pavan
print(name.upper())  # PAVAN

# 2. **Slicing a List:**
s = [11, 22, 33, 44, 55, 66]
print(s[0:3:1])  # [11, 22, 33]
print(s[0:5:2])  # [11, 33, 55]

# 3. Reverse Slicing a List:
t = [12, 13, 14, 15, 16]  # 15, 14, 13
print(t[-2:-5:-1])

# 4. **Slicing Nested List Elements:**
u = [11, 22, 33, [44, 55, 66], 77, 88, 99]  # [44, 66]
print(u[3][0:3:2])

# 5. **Accessing and Slicing Nested List Elements:**
l2 = [12, 13, 14, [78, 79, 80, 81, [4, 6, 7, 8]]]
print(l2[0:3:2])          # [12, 14]
print(l2[3][1:4:2])       # [79, 81]
print(l2[3][4][0:4:3])    # [4, 8]


