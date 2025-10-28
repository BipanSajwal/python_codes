# dictionary is mutable it stores data in curly bracket{}
# it needs key pair to perform
a={1,2,3,'bipan'} # here we have not given any key- pair that's why it is now set
print(type(a))
# unlike other data sets  we use key to call anything from dictionary no index number
b={    "Name":"Bipan Sajwal",
       "Country":"Nepal",
        "Contact No": 9762871188,
       "hey":[1,2,3,4],
       "Hello":{"Boy":"Bian","Girl":"Anbi"}
}
b["Name"]="Anjal"
print(b["Name"])
print(b,type(b))
print(b["Hello"]["Boy"])
del b["Country"]
print(b)