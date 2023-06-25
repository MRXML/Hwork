n = input("enter number")
print('it is a palindrome' if n[:len(n) // 2] == n[:len(n) // 2 - 1:-1] else print('it is not a palindrome'))