x="hard" #global variable
def fun():
    global x # it replaces loval variable value to global variable value
    x="easy" #local variable
    print(f"python is {x}") # this prints inside function
fun()
print(f"Python is {x}")# this prints outside function after changed local to global variable