mapping = [
    {   "name" : "james" , "age" : 32  },
    {   "name" : "moneypenny" , "age" : 25 },
    {   "name" : "doom" , "age" : 46}
]


mapping.sort( key=lambda item : item["name"] )
print("---aplhabetically---")
print(mapping)

mapping.sort( key=lambda item : item["age"] )
print("---age wise---")
print(mapping)