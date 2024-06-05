"""
read_csv  https://cloud.tencent.com/developer/article/1856554
write_csv  https://cloud.tencent.com/developer/article/2353604

new, store_nem, name, phone, address, create_time, other
"""

import csv
import numpy as np
import pandas as pd


class Test():
    def read_csv(self):
        with open('txt/camp_store.txt', newline='') as f:
            reader = csv.reader(f, delimiter='\t', quoting=csv.QUOTE_NONE)
            for row in reader:
                print(row)

    def numyp_csv(self):
        arr3 = np.array(np.loadtxt('C:/Users/hhx/Desktop/某门课程平时成绩和期末考试成绩.csv', dtype=str, delimiter=',', skiprows=1, usecols=0, encoding='utf-8'))

    def pandas_csv(self):
        pass

    def test(self):
        data = {'姓名': ['张三', '李四', '王五'],
                '年龄': [18, 19, 17],
                '成绩': [85, 90, 95]}
        # 创建DataFrame
        df = pd.DataFrame(data)
        # 将DataFrame保存为CSV文件
        # df.to_csv('student_data.csv', index=False)
        df.to_excel('789.xlsx', sheet_name='Sheet1', index=False, header=True)

    def read_excel(self,path):
        data_xls = pd.ExcelFile(path)
        print(data_xls.sheet_names)
        data = {}
        for name in data_xls.sheet_names:
            df = data_xls.parse(sheetname=name, header=None)
            data[name] = df
            # print(df)
            # print(name)
        return data


if __name__ == '__main__':
    t = Test()
    t.test()