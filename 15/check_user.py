import pykakasi
import glob
import datetime
import jaconv
import csv
import os
from numpy.lib.function_base import append
import pandas as pd
import configparser

# config.ini から顧客台帳ファイル名を取得
inifile = configparser.ConfigParser()
inifile.read('./config.ini', 'cp932')
FILE_DAITYO = inifile.get('Master', 'DAITYO')

OUT_COND_ALL = 'check_登録済.csv'
OUT_COND_PART = 'check_要確認.csv'
OUT_COND_NOT = 'check_未登録.csv'


def getfile_insensitive(path):
    '''
    pathの親ディレクトリを基準に、大文字小文字を無視して存在するPATHを返す。
    PATHは、大文字小文字を区別して返す。存在しない場合はNone
    '''
    directory, filename = os.path.split(path)
    directory, filename = (directory or '.'), filename.lower()
    for f in os.listdir(directory):
        newpath = os.path.join(directory, f)
        if os.path.isfile(newpath) and f.lower() == filename:
            return newpath


def isfile_insensitive(path):
    '''大文字を区別せずファイルの存在をTrue/Falseで返す。'''
    return getfile_insensitive(path) is not None


def henkan(column):
    list = df[column].values.tolist()
    new_list = []

    for li in list:
        li = jaconv.h2z(li)
        new_list.append(li)

    df[column] = new_list

    return df[column]


def df2list(data):
    return data.reset_index().T.reset_index().T.values.tolist()


def now_str():
    return datetime.datetime.now().strftime('%Y%m%d%H%M%S')


def select_order_file():
    '''
    最新の売上ファイルのファイル名取得
    '''
    orders = glob.glob("order_*.csv")
    if len(orders) == 0:
        print("売上データがありません")
        exit()
    return sorted(orders, reverse=True)[0]


def convert2romaji(text):
    """
    漢字かな混じり文をローマ字に変換する
    """
    kks = pykakasi.kakasi()
    result = kks.convert(text)
    return result[0]['hepburn']


# main

FILE_CSV = getfile_insensitive(FILE_DAITYO)
if FILE_CSV is None:
    print(f'{FILE_DAITYO} が見つかりません')
    exit()


df = pd.read_csv(FILE_CSV, encoding='cp932', delimiter=",")


# cleaning

# Hyphenを取り除く
df['得意先台帳.電話番号１'] = df['得意先台帳.電話番号１'].str.replace('-', '')
# df['得意先台帳.電話番号２'] = df['得意先台帳.電話番号２'].str.replace('-', '')
df['得意先台帳.ＦＡＸ番号'] = df['得意先台帳.ＦＡＸ番号'].str.replace('-', '')

# 先頭に0がない場合、0を付加する
df['得意先台帳.電話番号１'] = df['得意先台帳.電話番号１'].str.replace('^([1-9]+[0-9]+)', r'0\1', regex=True)
# df['得意先台帳.電話番号２'] = df['得意先台帳.電話番号２'].str.replace('^([1-9]+[0-9]+)', r'0\1', regex=True)
df['得意先台帳.ＦＡＸ番号'] = df['得意先台帳.ＦＡＸ番号'].str.replace('^([1-9]+[0-9]+)', r'0\1', regex=True)

# 半角スペース・全角スペースの除去
df['得意先台帳.得意先名'] = df['得意先台帳.得意先名'].str.replace("　", "")
df['得意先台帳.得意先名'] = df['得意先台帳.得意先名'].str.replace(" ", "")

# 変な記号が付加されているデータの除去
df['得意先台帳.得意先名'] = df['得意先台帳.得意先名'].str.replace("×", "")
df['得意先台帳.得意先名'] = df['得意先台帳.得意先名'].str.replace("ｘ", "")
df['得意先台帳.得意先名'] = df['得意先台帳.得意先名'].str.replace("X", "")
df['得意先台帳.得意先名'] = df['得意先台帳.得意先名'].str.replace("*", "", regex=False)
df['得意先台帳.得意先名'] = df['得意先台帳.得意先名'].str.replace("＊", "")

# H21... or 2019...という表記を削除
df['得意先台帳.得意先名'] = df['得意先台帳.得意先名'].str.replace("H[0-9].+$", "", regex=True)
df['得意先台帳.得意先名'] = df['得意先台帳.得意先名'].str.replace("[0-9].+$", "", regex=True)


# conda install -c conda-forge jaconv

henkan('得意先台帳.得意先名')
code = max(df['得意先台帳.得意先コード'])


FILE_CSV2 = select_order_file()

with open(FILE_CSV2, encoding='cp932') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',', quotechar='"')
    header = next(csvreader)
    # print(header)

    out_rows_header = [
        '得意先台帳.得意先コード',
        '得意先台帳.イニシャルキーカナ（得意先）',
        '得意先台帳.得意先名',
        '得意先台帳.得意先名フリガナ',
        '得意先台帳.電話番号１',
        '得意先台帳.ＦＡＸ番号',
        '得意先台帳.得意先メールアドレス',
        '得意先台帳.郵便番号',
        '得意先台帳.住所１',
        '得意先台帳.住所２',
        '得意先台帳.性別等',
        '得意先台帳.生年月日',
        '得意先台帳.メモ',
        '得意先台帳.最終購買日',
        '得意先台帳.イニシャルキー英字（得意先）',
        '得意先台帳.敬称'
        # '得意先台帳.販売形態',
        # '得意先台帳.売値区分',
        # '得意先台帳.得意先用売値掛率',
        # '得意先台帳.税計算タイミング',
        # '得意先台帳.税端数処理',
        # '得意先台帳.簡易課税事業者'
    ]

    out1 = [out_rows_header[1:]]
    out2 = [out_rows_header[1:]]
    out3 = []

    for row in csvreader:
        # user_kana = jaconv.h2z(row[4] + row[5])
        user_kana = jaconv.z2h(row[4] + row[5])
        user_name = row[2] + row[3]
        user_name_sp = row[2] + "　" + row[3]
        # user_ini_kana = jaconv.h2z(row[4] + row[5])
        user_ini_kana = jaconv.z2h(row[4] + row[5])
        user_company = row[6]
        user_tel = row[14] + row[15] + row[16]
        user_tel_hy = row[14] + '-' + row[15] + '-' + row[16]
        if user_tel_hy == '--':
            user_tel_hy = ''
        user_fax = row[17] + row[18] + row[19]
        user_fax_hy = row[17] + '-' + row[18] + '-' + row[19]
        if user_fax_hy == '--':
            user_fax_hy = ''
        user_email = row[13]
        user_zip = row[7] + "-" + row[8]
        user_address1 = (row[10] + row[11]).replace(","," ").replace("'","")
        user_address2 = row[12].replace(","," ")
        user_gender = row[21]
        if user_gender == "男性":
            user_gender = 1
        elif user_gender == "女性":
            user_gender = 2
        user_birthday = row[24]
        user_memberid = "会員ID:" + row[1] + " 注文ID:" + row[0]
        user_lastbuy = row[36]
        user_ini_romaji = convert2romaji(user_kana)
        user_keisyo = '様'
        user_def1 = 1         # 1:小売のみ,2:掛売りのみ,3:小売主体,4:掛売り主体
        user_def2 = 1         # 1:標準小売単価
        user_def3 = 100       # 売値掛率
        user_def4 = 1         # 1:明細ごと,2:伝票ごと,3:締め時一括
        user_def5 = 1         # 1:切り捨て,2:切り上げ,3:四捨五入
        user_def6 = 1         # 1:事業者,2:消費者
        temp0 = df.loc[df['得意先台帳.得意先名'].str.contains(user_name), :]
        out_row = [
            user_kana[0:5], user_name_sp, user_kana, user_tel_hy, user_fax_hy, user_email, user_zip, user_address1,
            user_address2, user_gender, user_birthday, user_memberid, user_lastbuy,user_ini_romaji[0:5],user_keisyo
            # user_def1,user_def2,user_def3,user_def4,user_def5,user_def6
        ]
        # イニシャルキーは半角5桁まで

        if temp0.size > 0:
            temp1 = temp0.loc[temp0['得意先台帳.郵便番号'].str.contains(user_zip, na=False), :]
            temp2 = temp0.loc[temp0['得意先台帳.電話番号１'].str.contains(user_tel, na=False), :]
            if temp1.size > 0 and temp2.size > 0:
                out1.append(out_row)

            else:
                out2.append(out_row)
                out2.append(["=== 一部一致 ==="])
                for row in df2list(temp0.loc[:, ['得意先台帳.得意先コード', '得意先台帳.得意先名', '得意先台帳.電話番号１', '得意先台帳.郵便番号']]):
                    out2.append(row[1:])    # 内部的に持っているindexは出力しない
                out2.append(["---------------"])
                out2.append([])

        else:
            out3.append(out_row)

nowstr = now_str()
with open(nowstr + OUT_COND_ALL, "w", encoding='cp932', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(out1)

with open(nowstr + OUT_COND_PART, "w", encoding='cp932', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(out2)

# 重複の削除
duplicated_data = [tuple(d) for d in out3]
unique_data = set(duplicated_data)

out3 = []
for row_data in unique_data:
    row_data = list(row_data)
    code += 1
    row_data.insert(0, code)
    out3.append(row_data)

# out3 = [list(d) for d in unique_data]
out3.insert(0, out_rows_header)

with open(nowstr + OUT_COND_NOT, "w", encoding='cp932', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(out3)
