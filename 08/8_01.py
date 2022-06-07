with open('sample.csv','r', encoding="utf-8") as f:
    lines = f.readlines()

with open('output.csv','w') as f:
    f.writelines(lines)