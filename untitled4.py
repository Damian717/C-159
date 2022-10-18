dictionary = {"fruit":"mango", 
              "color":"pink",
              "bird":"sparrow"}

try:
    print(dictionary["animal"])
except(KeyError):
    print("key animal is not present in dictionary")