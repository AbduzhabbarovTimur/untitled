def capitalize(line):
  return ' '.join(s[:1].upper() + s[1:] for s in line.split(' '))


line = input("Введите слово: ")
print(capitalize(line))