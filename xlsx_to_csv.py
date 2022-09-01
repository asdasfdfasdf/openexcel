import os
import glob
import pandas as pd
from configparser import ConfigParser


# 定义批量将xlsx文件转换为csv文件的函数
def xlsx_to_csv1(path):
    # 定义保存结果的数组
    result = []
    # 定义符合条件的csvlist
    csv_list = []
    # 循环遍历当前目录所有文件及文件夹
    for file in os.listdir(path):
        # 利用os.path.join()方法取得路径全名，并存入cur_path变量，否则每次只能遍历一层目录
        cur_path = os.path.join(path, file)
        # 判断是否是文件夹
        if os.path.isdir(cur_path):
            xlsx_to_csv1(cur_path)
        else:
            result.append(file)
            # 将xlsx文件转换为csv文件
            pd.read_excel(cur_path).to_csv(cur_path.replace('.xlsx', '.csv'))
            # 删除第一列
            df = pd.read_csv(cur_path + '.csv')
            df.drop(df.columns[0], axis=1, inplace=True)
    print(result)
    print('Done!')


# 定义寻找文件并转换为csv函数
def find_files(path, filename, save_path):
    # 定义保存结果的数组
    result = []
    # 首先遍历当前目录所有文件及文件夹
    file_list = os.listdir(path)
    # 循环判断每个元素是否是文件夹还是文件，是文件夹的话，递归
    for file in file_list:
        # 利用os.path.join()方法取得路径全名，并存入cur_path变量，否则每次只能遍历一层目录
        cur_path = os.path.join(path, file)
        # print(cur_path)
        i = len(cur_path.split('\\'))
        date = cur_path.split('\\')[i - 2]
        # 判断是否是文件夹
        if os.path.isdir(cur_path):
            find_files(cur_path, filename, save_path)
        else:
            # 判断是否是特定文件名称
            if filename in file:
                result.append(file)
                pd.read_csv(cur_path).to_csv(
                    save_path + '/' + filename + date + '.csv', index=False)


# 定义合并csv文件的函数
def merge_csv(path, save_path, filename):
    csv_list = glob.glob(path + '\\*.csv')
    dfs = []
    for i in csv_list:
        df = pd.read_csv(i)
        dfs.append(df)
    df = pd.concat(dfs)
    # df = df.drop(columns=['Unnamed: 0', 'business_variety', 'financing_purpose'])
    df.to_csv(save_path + '\\' + filename + '.csv', index=False)


# 根据contract_no去重
def drop_duplicates(path, save_path, filename):
    df = pd.read_csv(path + '\\' + filename + '.csv')
    df.drop_duplicates(subset=['contract_no'], inplace=True)
    df.to_csv(save_path + '\\' + filename + '.csv', index=False)


if __name__ == '__main__':
    cfg = ConfigParser()
    cfg.read('config.ini', encoding='utf-8')
    # 定义路径
    path = cfg.get('bis_contract_daily_path', 'path')
    save_path = cfg.get('bis_contract_daily_path', 'save_path')
    filename = cfg.get('bis_contract_daily_path', 'filename')
    find_files(path, filename, save_path)
    # 定义合并路径
    merge_path = cfg.get('contract_merge_path', 'path')
    merge_save_path = cfg.get('contract_merge_path', 'save_path')
    merge_filename = cfg.get('contract_merge_path', 'filename')
    # 合并csv文件
    merge_csv(merge_path, merge_save_path, merge_filename)
    drop_duplicates(merge_save_path, merge_save_path, merge_filename)
    # 定义remove_path
    remove_path = cfg.get('bis_remove_daily_path', 'path')
    remove_save_path = cfg.get('bis_remove_daily_path', 'save_path')
    remove_filename = cfg.get('bis_remove_daily_path', 'filename')
    find_files(remove_path, remove_filename, remove_save_path)
    # 定义remove合并路径
    merge_path = cfg.get('remove_merge_path', 'path')
    merge_save_path = cfg.get('remove_merge_path', 'save_path')
    merge_filename = cfg.get('remove_merge_path', 'filename')
    # 合并csv文件
    merge_csv(merge_path, merge_save_path, merge_filename)
