import pandas as pd
import glob

# 获取文件下的所有xlsx文件存入列表
xlsx_list = glob.glob(r'C:\Users\sunqh\Desktop\20220722微粒贷数据\*.xlsx')
# 将每个xlsx文件转换为csv文件
for i in xlsx_list:
    df = pd.read_excel(i)
    df.to_csv(i.replace('.xlsx', '.csv'), index=False)
