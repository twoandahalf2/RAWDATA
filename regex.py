import re

data = 'Start a sentence and then bring it to an abcend84765Start a sentence and then bring it to an abcend'
data2= 'vladimir.kolev89@gmail.com'
pattern = re.compile(r'[0-9]{5}')
pattern2 = re.compile(r'[a-zA-Z0-9._]+@[a-zA-Z0-9]+\.[a-zA-Z]{2,3}')
matches = pattern.findall(data)
matches2 = pattern2.findall(data2)

for match in matches2:
    print(match)