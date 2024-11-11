dicti = {}
name = "Shreyas"
list1 = [1,"Shreyas"]
list1[1] = "Varshini"
print(list1)
input("This was a list do you wanna try the frozen set: ")
list1 = frozenset(list1)
list1[1] = "Shreyas"
