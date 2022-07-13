import openpyxl


# 放款路径设置
loan_path = 'E:\\BaiduSyncdisk\\微粒贷统计\\每日数据\\20220713\\放款20220713134235.xlsx'
# 代偿路径设置
compensatory_path = 'E:\\BaiduSyncdisk\\微粒贷统计\\每日数据\\20220713\\代偿20220713134352.xlsx'


# 获取放款表借据号这一列的数据的方法
def get_loan_data(loan_path):
    wb = openpyxl.load_workbook(loan_path)
    sheet = wb.worksheets[0]
    # 获取放款表借据号这一列的数据
    _loan_id_list = [c.value for c in sheet['C']]
    return _loan_id_list


# 获取代偿表借据号这一列的数据的方法
def get_compensatory_data(compensatory_path):
    wb = openpyxl.load_workbook(compensatory_path)
    sheet = wb.worksheets[0]
    # 获取代偿表借据号这一列的数据
    _compensatory_id_list = [c.value for c in sheet['C']]
    return _compensatory_id_list


if __name__ == '__main__':
    # 获取放款表借据号list
    loan_id_list = get_loan_data(loan_path)[1:]
    # 获取代偿表借据号list
    compensatory_id_list = get_compensatory_data(compensatory_path)[1:]
    # 循环比较两个list的借据号是否相同
    for compensatory_id_list in compensatory_id_list:
        if compensatory_id_list in loan_id_list:
            print(compensatory_id_list)
        else:
            pass
