import pandas as pd

df = pd.read_csv(r'E:\workdata\网商数据包\合并后\merge.csv')
# print(df.head())
# 读取错误数据
error = pd.read_table(r'E:\Code\pythonAuto\error.txt', header=None, encoding='GBK')
# print(error)
# 创建一个新的dataframe
new_df = pd.DataFrame()
# 遍历错误数据每一行数据
for i in error.index:
    # 获取每一行数据
    row = error.loc[i]
    # 将row按照‘ ’分割成list
    row = row[0].split(' ')
    # 添加到new_df中
    # ignore_index=True重新索引
    # axis=0纵向添加
    new_df = pd.concat([df[(df.name == row[1]) & (df.cert_no == row[3]) & (df.start_date == row[6]) & (
            df.paid_prin_amt == float(row[5]))]], ignore_index=True, axis=0)
new_df.to_csv(r'E:\workdata\网商数据包\合并后\error.csv', index=False)
