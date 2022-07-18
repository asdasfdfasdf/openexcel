import pandas as pd

# pd.set_option('display.max_columns', None)
# 读取contract_daily.csv文件
contract_data = pd.read_csv('E:/workdata/数据上报/每日csv数据/20220718/bis_contract_daily/all_merge_bis_contract_daily.csv')
# 设置列名
# 读取remove_daily.csv文件
remove_data = pd.read_csv('E:/workdata/数据上报/每日csv数据/20220718/bis_remove_daily/all_merge_bis_remove_daily.csv')
# 左连接两个文件
result = pd.merge(contract_data, remove_data, how='left', on='contract_no')
# 设置表头名
# print(result.head())
result.prod_code_x = result.prod_code_x.astype(str)
result.prod_code_y = result.prod_code_y.astype(str)
# result.drop_duplicates(subset=['contract_no'], inplace=True)
# result.to_excel('E:/workdata/数据上报/每日csv数据/20220718/20220718_all_daily.xlsx', index=False)
result.to_csv('E:/workdata/数据上报/每日csv数据/20220718/20220718_all_daily.csv', index=False)
print('Done!')
