chars = "abcdefghijklmnopqrstuvwxyz"
str1 = "abcaba"

for char in chars:
  count = str1.count(char)
  if count >1:
    print(char,count)
