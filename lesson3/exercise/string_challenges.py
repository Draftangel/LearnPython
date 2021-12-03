import re
from statistics import mean

# Вывести последнюю букву в слове
word = 'Архангельск'
print(word[-1])


# Вывести количество букв "а" в слове
word = 'Архангельск'
print(word.lower().count("а"))


# Вывести количество гласных букв в слове
word = 'Архангельск'
print(len(''.join([c for c in word.lower() if c in 'аиеёоуыэюя'])))


# Вывести количество слов в предложении
sentence = 'Мы приехали в гости'
print(len(sentence.split()))


# Вывести первую букву каждого слова на отдельной строке
sentence = 'Мы приехали в гости'
for word in sentence.split():
    print(word[0])


# Вывести усреднённую длину слова в предложении
sentence = 'Мы приехали в гости'
print(mean([len(w) for w in sentence.split()]))
