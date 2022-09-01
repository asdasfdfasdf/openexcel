import myutils
import pandas as pd
import os
import glob

# 定义执行模式常量
MODE_MERGE = 0

# 判断模式为1的话，执行bis_contract_daily合并
if MODE_MERGE == 1:
    # 获取符合条件的文件名
    myutils.find_files(r'E:\workdata\网商上报省系统数据包\20220815_20220827', 'bis_contract_daily',
                       r'E:\workdata\网商上报省系统数据包\20220815_20220827\bis_contract_merger')
    # 合并所有csv文件
    myutils.merge_files(r'E:\workdata\网商数据包\合并后\bis_contract_daily', r'E:\workdata\网商数据包\合并后\bis_contract_daily')
else:
    # 获取符合条件的文件名
    myutils.find_files(r'E:\workdata\网商数据包\guarantee_business.selection', 'bis_remove_daily',
                       r'E:\workdata\网商数据包\合并后\bis_remove_daily')
    # 遍历所有csv文件
    for file in glob.glob(r'E:\workdata\网商数据包\合并后\bis_remove_daily\*.csv'):
        # 读取文件
        df = pd.read_csv(file, header=None, low_memory=False)
        # 获取第一行数据
        row = df.loc[0].values
        # print(row)
        # 判断第一行数据是否有name
        if 'name' in row:
            # 如果有name，则删除第一行数据
            df = df.drop(0)
        # 写入文件
        df.to_csv(file, header=None, index=False)
