a = 10
b = 20

print('total is '+str(a+b))

# swapping by using temp variable
temp = a
a = b
b = temp
print('\n after first swap')
print(a)
print(b)

# swapping without an extra space
a = a+b
b = a - b
a = a - b
print('\n after last swap')
print(a)
print(b)