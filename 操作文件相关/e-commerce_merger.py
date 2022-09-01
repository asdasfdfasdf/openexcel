import myutils
import pandas as pd
import os
import glob


# 定义获取文件夹下指定文件的函数
def get_file_name(file_path, file_name):
    # 创建一个空列表，用于存放文件的绝对路径
    file_path_list = []
    # 遍历file_path下所有文件夹
    for root, dirs, files in os.walk(file_path):
        # 遍历文件夹下所有文件
        for file in files:
            # 判断文件名是否包含指定字符串
            if file_name in file:
                # 将文件的绝对路径加入到列表中
                file_path_list.append(os.path.join(root, file))
    return file_path_list


# 将文件转为csv的函数
def file_to_csv(_file_path, file_save_path):
    # 将file_path切片存入列表中
    _file_path_list = _file_path.split('\\')
    # 将列表中的最后一个元素切片存入变量中
    file_name = _file_path_list[-2]
    # 读取文件
    df = pd.read_csv(_file_path, encoding='utf-8')
    df.to_csv(file_save_path + r'\bis_contract_daily' + file_name + '.csv', encoding='utf-8', index=False)


# 判断文件是否存在的函数
def file_exist(_file_path):
    # 如果文件不存在，则创建文件夹
    if not os.path.exists(_file_path):
        os.makedirs(_file_path)


# 合并文件夹下所有文件的函数
def merge_file(_file_path, file_save_path):
    df = pd.DataFrame()
    # 遍历文件夹下所有文件
    for file in _file_path:
        # 读取文件
        df1 = pd.read_csv(file, encoding='utf-8')
        # 将文件合并到df中
        df = pd.concat([df, df1], axis=0)
    df.to_csv(file_save_path, encoding='utf-8', index=False)


if __name__ == '__main__':
    save_path = r'E:\workdata\网商上报省系统数据包\20220815_20220827'
    bis_contract_daily = save_path + r'\bis_contract_daily'
    file_exist(bis_contract_daily)
    file_path_list = get_file_name(r'E:\workdata\网商上报省系统数据包\20220815_20220827', 'bis_contract_daily')
    for file_path in file_path_list:
        file_to_csv(file_path, save_path + r'\bis_contract_daily\\')
    # 获取bis_contract_daily文件夹下所有文件的绝对路径
    file_path_list = glob.glob(bis_contract_daily + '\\*.csv')
    df1 = pd.DataFrame()
    for file_path in file_path_list:
        df = pd.read_csv(file_path, encoding='utf-8')
        df1 = pd.concat([df1, df], axis=0)
    df1.to_csv(bis_contract_daily + r'\all_bis_contract_daily.csv', encoding='utf-8', index=False)

    bis_remove_daily = save_path + r'\bis_remove_daily'
    file_exist(bis_remove_daily)
    file_path_list = get_file_name(r'E:\workdata\网商上报省系统数据包\20220815_20220827', 'bis_remove_daily')
    for file_path in file_path_list:
        file_to_csv(file_path, save_path + r'\bis_remove_daily\\')
    # 获取bis_contract_daily文件夹下所有文件的绝对路径
    file_path_list = glob.glob(bis_remove_daily + '\\*.csv')
    df1 = pd.DataFrame()
    for file_path in file_path_list:
        df = pd.read_csv(file_path, encoding='utf-8')
        df1 = pd.concat([df1, df], axis=0)
    df1.to_csv(bis_remove_daily + r'\bis_remove_daily.csv', encoding='utf-8', index=False)
