x="hard"
def fun():
    global x
    x="easy"
    print(f"python is {x}")
fun()
print(f"Python is {x}")