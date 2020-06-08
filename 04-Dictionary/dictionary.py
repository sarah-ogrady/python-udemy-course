import json

data = json.load(open("data.json"))

def definition(word):
  if word in data:
    return data[word]
  else:
    return "This word is not in our dictionary, please check your spelling and try again"

word = input("Enter word:")
print(definition(word))
