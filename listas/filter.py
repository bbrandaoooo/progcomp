l = [1,3,2,5,8,14,7]

l2 = filter(lambda x: x % 2 == 0, l)

print(list(l2))  # Output: [2, 8, 14]

# só filtra os elementos de uma lista