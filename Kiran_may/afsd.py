address = input("Enter your address: ")
address_lines = address.split(',')
print("Address:")
for line in address_lines:
    print(line.strip())
 