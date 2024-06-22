n ={
    "Arei": {"name":"Areiahna", "age": 22, "number": 2695193581},
    "Yamah": {"name": "Qiyamah", "age": 22, "number": 2697572324},
    "Moomoo": {"name": "Elijah", "age": 22, "number":3176465432}
}

stuff = sorted(n.items(),key = lambda x : x[1]["name"])

for name, details in stuff:
    print(name, details)
