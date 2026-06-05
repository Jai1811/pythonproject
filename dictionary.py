
#unordered mutable, no duplicate keys
dict = {
    "key":"value",
    "subject":["Maths","English"],
    "tup":(1.2,2,3,5,"Aj"),
    1:'s',
    13.5:'asa',
    "subdict":{
        "physics":78,
        "Maths":68
    }
}


dict["surname"] = 1

print (len(dict))

print(list(dict.keys()))

print(list(dict.values()))

print(dict["subdict"]["Maths"])

print(list(dict.items()))#returns all the key value pairs as tuples

print(dict.get("subdict"))

dict.update({"city":"sdfdfs"})#inserts specified items to dict

dict.update({"key":"Vales"})

print(dict)


dict2 = {
    "innerdict":{
        "data":1
    }
}

print(dict2["innerdict"]["data"])