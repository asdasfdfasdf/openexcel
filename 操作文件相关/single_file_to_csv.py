import pandas as pd


# 将单个文件转换为csv文件
def single_file_to_csv(file_path, csv_path):
    df = pd.read_csv(file_path)
    df.to_csv(csv_path, index=False)
    print('Done!')


if __name__ == '__main__':
    file_path = r'E:\workdata\网商数据包\guarantee_business.selection\202208\20220804\bis_stdbook_daily__c883977e_d1e5_4440_a941_b87fb2f7145c'
    csv_path = r'E:\workdata\网商数据包\guarantee_business.selection\202208\20220804\bis_stdbook_daily__c883977e_d1e5_4440_a941_b87fb2f7145c.csv'
    single_file_to_csv(file_path, csv_path)
