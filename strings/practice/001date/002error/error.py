x = 23 
y = 2

try:
    print(x/y)
except ZeroDivisionError as e:
    print("error is infinite")
else:
    print("no error")
finally:
    print("voila , finished")