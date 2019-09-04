import re

sentence = 'Start a sentence and then bring it to an abcend'
pattern = re.compile(r'abc')
matches = pattern.findall(sentence)

for match in matches:
    print(match)