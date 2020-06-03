def sentence_maker(string):
  if string.startswith(('how', 'who', 'what', 'why', 'when', 'where')):
    return '{}?'.format(string.capitalize())
  else:
    return '{}.'.format(string.capitalize())

# print(sentence_maker(input("Say something:")))

userList = []

while True:
  user_words = input("Say something:")
  new_words = sentence_maker(user_words)
  if user_words == "/end":
    print(" ".join(map(str, userList)))
    break
  else:
    userList.append(new_words)




