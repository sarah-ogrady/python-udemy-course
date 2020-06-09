import json

from difflib import get_close_matches

data = json.load(open("data.json"))

def definition(word):
  word = word.lower()
  if word in data:
    return data[word]
  elif len(get_close_matches(word, data.keys())) > 0:
    answer = input("Did you mean %s instead? Type (y) for yes or (n) for no." % get_close_matches(word, data.keys())[0])
    if answer == "y":
      return "woop"
    else:
      return "oh no"
  else:
    return "This word is not in our dictionary, please check your spelling and try again"

word = input("Enter word:")
print(definition(word))
