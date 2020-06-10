import json

from difflib import get_close_matches

data = json.load(open("data.json"))

def definition(word):
  word = word.lower()
  if word in data:
    return data[word]
  elif word.title() in data:
    return data[word.title()]
  elif word.upper() in data:
    return data[word.upper()]
  elif len(get_close_matches(word, data.keys())) > 0:
    answer = input("Did you mean %s instead? Type (y) for yes or (n) for no: " % get_close_matches(word, data.keys())[0])
    if answer == "y":
      return data[get_close_matches(word, data.keys())[0]]
    elif answer == "n":
      return "Sorry, this word does not exist, please check it and try again."
    else:
      return "Sorry, this word does not exist, please check it and try again."
  else:
    return "This word is not in our dictionary, please check your spelling and try again"

word = input("Enter word:")

output = definition(word)

if type(output) == list:
  for item in output:
    print(item)
else:
  print(output)
