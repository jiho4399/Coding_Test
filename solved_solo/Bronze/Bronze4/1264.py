while True:
  sentence = input()
  if sentence == '#':
    break

  count = 0
  for i in sentence:
    if i in ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']:
      count += 1
  print(count)