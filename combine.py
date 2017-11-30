import pandas as pd

df = pd.read_excel('example.xlsx')
df[['operator', 'left_condition', 'equation_operator', 'right_condition']]=df[['operator', 'left_condition', 'equation_operator', 'right_condition']].fillna(value=' ')
df[['operator', 'left_condition', 'equation_operator', 'right_condition']]=df[['operator', 'left_condition', 'equation_operator', 'right_condition']].applymap(str)

def sql(DF, columns_To_Combine, new_Column_Name):
    DF[new_Column_Name] = ''
    for Col in columns_To_Combine:
        DF[new_Column_Name] += DF[Col].map(str) + ' '
    DF = DF.drop(columns_To_Combine, axis=1)
    DF = DF.groupby(by=['line_description']).sum()

    return DF

df = sql(df,df[['operator', 'left_condition', 'equation_operator', 'right_condition']],'SQLCode')
df.to_excel('output.xlsx')
