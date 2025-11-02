#Format strings allows user to use variable between string place holders


Name="Bipan"
Surname="Sajwal"
Age=19
Course="Computing Science"
print(f"My name is {Name}{Surname}.",f"\n I am {Age} years old.",f" \n I am {Course} Student.")


#Next way to format is Here we can use indexing as well
a="Hello! My name is {2}.I am {3} years old".format("Bipan Sajwal",19 ,"Angel Lamichhane",18)
print(a)

b="Hello {b:^10}to {a:^20} Bipan".format(b="Bipan",a="Sajwal")
print(b)