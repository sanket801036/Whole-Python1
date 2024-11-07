num = 1234
original_num = num  # Save the original number
reversed_num = 0

while num != 0:
    digit = num % 10
    reversed_num = reversed_num * 10 + digit
    num //= 10

# After the loop, check if the reversed number is equal to the original number
print("Reversed Number: " + str(reversed_num))

if reversed_num == original_num:
    print("Palindrome: " + str(reversed_num))
else:
    print("Not a Palindrome: " + str(reversed_num))
