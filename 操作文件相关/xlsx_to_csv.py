import myutils

# 获取所有文件名
file_names = myutils.get_all_file_path(r'E:\workdata\微粒贷下载数据\20220818')
print(file_names)
# 转换文件
for file_name in file_names:
    myutils.xlsx_to_csv(file_name, file_name.replace('.xlsx', '.csv'))
print('转换完成')
