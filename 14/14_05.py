import re

def my_split(sentence, deleimiter=' '):
    # lists = []
    # word = ""
    # for s in sentence:
    #     if s == deleimiter:
    #         lists.append(word)
    #         word = ""
    #         continue
    #     else:
    #         word += s
    # lists.append(word)
    # return lists

    # split関数を使った場合
    # return sentence.split(" ")

    # re.split関数を使った場合
    return re.split(r'\s+', sentence)

if __name__ == '__main__':
    test_sentence = "this is a test sentence."
print(my_split(test_sentence))