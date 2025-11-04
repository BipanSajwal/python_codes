from tkinter.font import names

a=[]
for i in range(101): # This is normal way
    if i%2==0:
        a.append(i)
print(a)

# A list comprehension is a syntactic construct available in some programming languages
# for creating a list based on existing lists.

c=[d for d in range(101) if d%2==0] # here we use list comprehension
print(c)



e =[1,2,3,4,5,6,7,8,9]
squarred_numbers=[i**2 for i in e]
print(squarred_numbers)


names=["Bipan","Meena","Gun","Soniya","Sudesh","Anjal"]
first_Letters=[p[0] for p in names]
print(first_Letters)



#Generating list of squares of even numbers
hello=[even**2 for even in range (1,21) if even%2==0 ]
print(hello)



# Converting Strings to integers

hey='1','2','3','4','5'
ohh=[int(l) for l in hey]
print(ohh)


