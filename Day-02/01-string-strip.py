text="   Python is awesome       "
stripped_text = text.strip()
print("Original text:", text)
print("Stripped text:", stripped_text)


file_name="---my_file.txt-----"
file_name_stripped = file_name.strip("-")
print("Original file name:", file_name)
print("Stripped file name:", file_name_stripped)


messy = ".,!?Hello!.,"
cleaned = messy.strip(".,!?")
print(cleaned)
