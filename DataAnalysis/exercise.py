import pandas as pd
from pandas import Series, DataFrame

data = {'chinese':[66,95,93,90,80],'english':[65, 85, 92, 88, 90], 'math':[30, 98, 96, 77, 90]}
df1 = DataFrame(data)
df2 = DataFrame(data, index=['ZhangFei','GuanYu', 'Zhaoyun','Huangzhong', 'DianWei'], columns=['english','math','chinese'])
print(df1)
print(df2)