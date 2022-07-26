import re
# 電話番号を取り出す正規表現
phone_pattern = "\d{3}-\d{3}-\d{4}"
# 名前を取り出す正規表現
name_pattern = r"^\d+,\"(.+?)\""

with open('sample.csv', encoding="utf-8") as f:
    for line in f:
        phone_list = re.findall(phone_pattern, line)
        name_list = re.findall(name_pattern, line)
        for name in name_list:
            for phone in phone_list:
                print(name + " ", phone)