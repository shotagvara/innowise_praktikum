"""Программа должна создать файл athlete.txt и записать туда три строки:

Name: Alex
Sport: Boxing
Weight: 80

Затем закрой файл, открой его заново для чтения и выведи содержимое в терминал."""
file=open("athlete.txt", "w")
file.write("Hello World!\n")
file.write("My name is Shota")
file.write("""
Name: Alex
Sport: Boxing
Weight: 80""")

<<<<<<< HEAD
file.close()
file=open("athlete.txt", "r")
print(file.read())
file.close()
=======
file.close
file=open("athlete.txt", "r")
print(file.read())
file.close()

>>>>>>> b70a066b10254d01e61bd840da8226b9170c8b26
