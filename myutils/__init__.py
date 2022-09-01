import pandas as pd
import os
import glob


# 获取文件夹下所有文件的绝对路径的函数
def get_all_file_path(path):
    file_paths = []
    for root, dirs, files in os.walk(path):
        for file in files:
            file_paths.append(os.path.join(root, file))
    return file_paths


# 定义xlsx转为csv文件的函数
def xlsx_to_csv(xlsx_file, csv_file):
    df = pd.read_excel(xlsx_file)
    df.to_csv(csv_file, index=False)
    print('{}转为{}成功'.format(xlsx_file, csv_file))
    return df


# 定义寻找文件并转换为csv函数
def find_files(path, filename, save_path):
    # 判断保存路径是否存在，不存在则创建
    if not os.path.exists(save_path):
        os.makedirs(save_path)
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


# 合并文件夹下所有csv文件的函数
def merge_files(path, save_path):
    # 判断保存路径是否存在，不存在则创建
    if not os.path.exists(save_path):
        os.makedirs(save_path)
    # 合并所有csv文件
    file_list = glob.glob(path + '/*.csv')
    # print(file_list)
    df = pd.DataFrame()
    df = pd.concat([pd.read_csv(file, header=None) for file in file_list], ignore_index=True)
    df.to_csv(save_path + '/' + 'merge.csv', index=False)
