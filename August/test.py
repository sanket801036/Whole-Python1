# Importing the necessary module for taking input
import sys

def even_odd_sum_difference(a):
    even_sum = 0
    odd_sum = 0

    # Loop from 1 to 'a'
    for i in range(1, a):
        if i % 2 == 0:
            even_sum += i
        else:
            odd_sum += i

    # Calculate the result
    result = even_sum - odd_sum
    return result

if __name__ == "__main__":
    a = int(input("Enter The Number: "))
    result = even_odd_sum_difference(a)
    print("Result:", result)
