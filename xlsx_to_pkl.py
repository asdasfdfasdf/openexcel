import os
import glob
import pandas as pd
from configparser import ConfigParser


# 定义批量将xlsx文件转换为pkl文件的函数
def xlsx_to_pkl(path):
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
            xlsx_to_pkl(cur_path)
        else:
            result.append(file)
            # 将xlsx文件转换为pkl文件
            pd.read_excel(cur_path).to_pickle(cur_path.replace('.xlsx', '.pkl'))
    print(result)
    print('Done!')


# 定义寻找文件并转换为pkl函数
def find_files(path, filename, save_path):
    # 定义保存结果的数组
    result = []
    # 首先遍历当前目录所有文件及文件夹
    file_list = os.listdir(path)
    # 循环判断每个元素是否是文件夹还是文件，是文件夹的话，递归
    for file in file_list:
        # 利用os.path.join()方法取得路径全名，并存入cur_path变量，否则每次只能遍历一层目录
        cur_path = os.path.join(path, file)
        i = len(cur_path.split('\\'))
        date = cur_path.split('\\')[i - 1]
        # 判断是否是文件夹
        if os.path.isdir(cur_path):
            find_files(cur_path)
        else:
            # 判断是否是特定文件名称
            if filename in file:
                result.append(file)
                pd.read_csv(cur_path).to_pickle(
                    save_path + '/' + filename + date + '.pkl')


if __name__ == '__main__':
    cfg = ConfigParser()
    cfg.read('config.ini', encoding='utf-8')
    # xlsx_to_pkl('E:/BaiduSyncdisk/微粒贷统计/每日数据/20220715')
    # 待搜索的文件夹路径
    path = cfg.get('all_path', 'path').replace('\\', '/')
    # 待搜索的文件名称
    filename = cfg.get('all_path', 'filename')
    # 保存结果的文件夹路径
    save_path = cfg.get('all_path', 'save_path').replace('\\', '/')
    find_files(path, filename, save_path)
