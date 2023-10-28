"""Practice with dictionaries."""

# constructing a new dictionary
ice_cream: dict[str, int] = {"chocolate": 12, "vanilla": 8, "strawberry": 5}

# adding a key-value pair to a dictionary
ice_cream["mint"] = 3
print(ice_cream)

# altering a value
ice_cream["mint"] = 4
print(ice_cream)

# removing a key-value pair
ice_cream.pop("mint")
print(ice_cream)

# print chocolate orders and update vanilla to 10
ice_cream["vanilla"] = 10
print(ice_cream["chocolate"])
print(ice_cream)

# len()
print(len(ice_cream))

# in 
if "mint" in ice_cream:
    print(ice_cream["mint"])
else: 
    print("mint is not in dict")

if "chocolate" in ice_cream:
    print(ice_cream["chocolate"])
else: 
    print("chocolate is not in dict")

print("\n\n")

# for loop
for key in ice_cream:
    print(ice_cream[key])

new_dct_1: dict[int, int] = dict()
print(new_dct_1)