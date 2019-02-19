dict={"name":"harsh","teach":"vivek","since":"2017"}
print(dict["name"])
print(dict.get('since'))
dict["name"]="ARunesh"
print(dict)
del dict["since"]
print("After deletion",dict)
