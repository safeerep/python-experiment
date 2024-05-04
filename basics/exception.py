a = 10
b = 0

try:
    result = a/b
    print('result after division'+ str(result))
except:
    print(str(a) +" can't be divided by zero")

# handling exception types
try:
    result = a/b
    print('result after division'+ str(result))
except: ZeroDivisionError