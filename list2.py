# Write a Python program to multiplies all the items in a list.

list_integers = [540, 986, 21, 263, 556, 689, 908, 421, 469, 536]

product = 1

for i in range(len(list_integers)):
    product = list_integers[i] * product
    i += 1
print(product)
print("check =",540* 986* 21* 263* 556* 689* 908* 421*469*536)
