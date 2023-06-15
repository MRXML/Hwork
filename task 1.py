first = int(input("enter number"))
second = int(input("enter number"))
third = int(input("enter number"))
fourth = int(input("enter number"))
fifth = int(input("enter number"))
if first > second and first > third and first > fourth and first > fifth:
    print(first)
elif second > first and second > third and second > fourth and second > fifth:
    print(second)
elif third > second and third > secпond and third > fourth and third > fifth:
    print(third)
elif fourth > second and fourth > third and fourth > first and fourth > fifth:
    print(fourth)
else:
    print(fifth)