
userList = []

while True:
  user_words = input("Say something:")
  if user_words == "/end":
    print(" ".join(map(str, userList)))
    break
  else:
    userList.append(user_words)




