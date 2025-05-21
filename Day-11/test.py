
student = {
    "name": "John Doe",
    "age": 20,      
    "roll_no": 12345,
    "subjects": ["Math", "Science", "English"],
}

print(student["name"])
print(student.get("age"))

student["age"] = 25
print(student)

del student["roll_no"]
print(student)