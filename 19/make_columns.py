import re
with open('agaricus-lepiota.names', "r") as f:
    for line in f.readlines():
        matchWord = re.match(r'\s+\d{1,2}\.\s(.+):', line)
        if matchWord is not None:
                print(matchWord.group())