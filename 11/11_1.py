import pandas as pd

df_sell = pd.read_csv('sell.csv')
df_user = pd.read_csv('user.csv')
df_item = pd.read_csv('item.csv')

df_sell_user = pd.merge(df_sell, df_user, left_on="user",
                        right_on="user_id", how="inner")
df_sell_user_item = pd.merge(
    df_sell_user, df_item, left_on="item", right_on="item_id", how="inner")


df_sell_user_item['total'] = df_sell_user_item['quantity'] * \
    df_sell_user_item['unit_price']
df_sell_user_item['profit'] = (df_sell_user_item['unit_price'] - 
    df_sell_user_item['purchase_price']) * df_sell_user_item['quantity']
df_sell_user_item.to_csv('result.csv')

# print('粗利合計=', df_sell_user_item['profit'].sum())
print('売上合計=',sum(df_sell_user_item['total']))
print('粗利合計=',sum(df_sell_user_item['profit']))
