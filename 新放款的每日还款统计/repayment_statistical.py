import pandas as pd
import datetime

start = datetime.datetime.now()


# 定义将金额中的，去除，并转换成浮点数的函数
def money_to_float(money):
    money = money.replace(',', '')
    return float(money)


pd.set_option('display.max_columns', None)

# 读取放款csv文件
loan_datas = pd.read_csv('E:/BaiduSyncdisk/微粒贷统计/每日数据/20220720/放款20220720091610.csv')
loan_datas['借据号'] = loan_datas['借据号'].astype(str)
loan_datas['放款金额(元)'] = loan_datas['放款金额(元)'].apply(money_to_float)
loan_datas['贷款期次数'] = loan_datas['贷款期次数'].apply(int)

# 读取还款csv文件
repayment_datas = pd.read_csv('E:/BaiduSyncdisk/微粒贷统计/每日数据/20220720/还款20220720091813.csv')
repayment_datas['借据号'] = repayment_datas['借据号'].astype(str)
repayment_datas['本次实还总金额（元）'] = repayment_datas['本次实还总金额（元）'].apply(money_to_float)
repayment_datas['还款本金(元)'] = repayment_datas['还款本金(元)'].apply(money_to_float)

# 读取代偿csv文件
compensation_datas = pd.read_csv('E:/BaiduSyncdisk/微粒贷统计/每日数据/20220720/代偿20220720091904.csv')
compensation_datas['借据号'] = compensation_datas['借据号'].astype(str)

# 合并三个表
datas = pd.merge(loan_datas, repayment_datas, on='借据号', how='left')
datas = pd.merge(datas, compensation_datas, on='借据号', how='left')

datas.to_excel('E:/BaiduSyncdisk/微粒贷统计/每日数据/20220720/每日还款统计20220720.xlsx', index=False)

# 中间写代码块
end = datetime.datetime.now()
print('Running time: %s Seconds' % (end - start))
