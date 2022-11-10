import re
list = []
with open('agaricus-lepiota.names', "r") as f:
    for line in f.readlines():
        matchWord = re.match(r'\s+\d{1,2}\.\s(.+):', line)
        if matchWord is not None:
                list.append(matchWord.group(1))
                print(matchWord.group())
print(list)