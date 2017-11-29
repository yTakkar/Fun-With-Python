list = ["First", "Second", "Third"]
another_list = [ e.upper() for e in list ]

print(list[0])
del list[2]
print(list)
list.insert(2, "Third")
print(list, another_list)
