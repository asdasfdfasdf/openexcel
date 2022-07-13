import openpyxl
import datetime


# 定义打印方法
def print_func():
    print('Hello World')


# 将金额中的‘,’替换为‘’，并转换为float类型
def change_money(money):
    return float(money.replace(',', ''))


# 将-连接的时间转换为datetime类型
def change_time(time):
    return datetime.datetime.strptime(time, '%Y-%m-%d')
