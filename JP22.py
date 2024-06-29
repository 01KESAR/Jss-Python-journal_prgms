# write a python prgm to create data frame excel sheet using pandas & perform operation on data frames

import pandas as pd
from openpyxl import Workbook
marks_table={'rno':[1,2,3,4,5],
             'py':[98,97,45,80,67],
             'cma':[89,88,56,67,42],
             'ic':[67,78,45,56,89]}
df1 = pd.DataFrame(marks_table)
df1.to_excel('marks.xlsx',index=False)
df=pd.read_excel(io='marks.xlsx')
print(df)
print('highest marks  in python is',df['py'].max())
df['total']=df['py']+df['ic']+df['cma']
print('after calculating total dataframe is')
print(df)