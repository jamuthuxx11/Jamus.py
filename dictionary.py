#creating a dictionary
#data is stored in key value pairs
# ie key:value
cardata={
    "model":"BMW",
    "year":2016,
    "brand":"c200"
}

print(cardata["brand"])# accessing values in a dictionary we use the key
cardata["alloys"]="contains" #addingdata to a dictionary
print(cardata)

cardata["brand"]="c500" #modifying data in a dictionary
print(cardata)