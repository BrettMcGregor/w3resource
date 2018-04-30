# Write a Python function to get a string made of 4 copies of the last
# two characters of a specified string (length must be at least 2).
# Sample function and result :
# insert_end('Python') -> onononon
# insert_end('Exercises') -> eseseses

stringa = "Exercises"

if len(stringa) >= 2:
    print(stringa[-2:] * 4)
else:
    print("string too short")
