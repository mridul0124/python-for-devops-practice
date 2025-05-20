

names = ["Alice", "Bob", "Charlie"]
print(names[0])
print(names)

names[0] = "David"
print(names[0])
print(names)

names.append("Eve")
print(names)

names.remove("Bob")
print(names)

names.insert(1, "Frank")
print(names)

names.pop()
print(names)

if "Charlie" in names:
    print("Charlie is in the list")
    
print(len(names))

