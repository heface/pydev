#特征选择


#去重


#处理缺失值
缺失值的处理一直是数据处理的一个重点工作。根据数据的不同会做出不同的选择，有用均值填充的，中位数填充的，用0填充的，甚至直接去除的。再复杂一点的可以用autoencoder来训练预测缺失值。
1 去除缺失值比例超过一定程度的列
def drop_col(df, cutoff=0.4):
    n = len(df)
    for column in df.columns:
        cnt = df[column].count()
        if (float(cnt) / n) < cutoff:
            df = df.drop(column, axis=1)
    return df
hr = drop_col(hr)

2 去除缺失值超过一定比例的行
def drop_row(df, cutoff=0.8):
    n = df.shape[1]
    for row in df.index:
        cnt = df.loc[row].count()
        if cnt / n < cutoff:
            df = df.drop(row, axis=0)
    return df
hr  = drop_row(hr)

处理方法：
1、删除
2、补全：  常用补全方法有（1）用基本统计量填充（最大值、最小值、均值、中位数、众数）
                                         （2） 用表内临近值填充
                                         （3）用分类临界值、基本统计量填充
                                         （4）用回归模型填充，将缺失字段作为目标变量进行预测
                                         （5）多重插补
3、真值转换法：该方法将缺失值也作为数据分布规律的一部分，将缺失值和实际值都作为输入维度参与后续  数据处理和模型计算。
4、不处理：若后期的模型对缺失值有容忍度或有灵活的处理方法，则可不进行处理。常见的能够自动处理缺失值的模型包括：KNN、决策树、随机森林、神经网络、朴素贝叶斯、DBSCAN等。

#处理异常值
异常值是数据分布的常态，处于特定分布区域或范围之外的数据通常被定义为异常或噪声。异常分为两种：“伪异常”，由于特定的业务运营动作产生，是正常反应业务的状态，而不是数据本身的异常；“真异常”，不是由于特定的业务运营动作产生，而是数据本身分布异常。通常异常值会在数据的预处理中被删除掉。

判断异常值
1 z_score=(df-df.mean())/df.std()
2 df_zscore=z_score.abs()>2.2
3 print(df_zscore)

用中位数替换掉异常值
1 df_num=df.copy()
2 df_num=pd.DataFrame(np.where(df_zscore,df_num.median(),df_num),columns=['var_1','var_2'])
3 print(df_num)

删除异常值
1 df_drop=pd.DataFrame(np.where(df_zscore,np.nan,df),columns=['var_1','var_2'])
2 df_drop=df_drop.dropna()
3 print(df_drop)

#处理重复值
重复值处理的方法是去重，目的是保留能显示特征的唯一记录数据。
判断重复数据
1 df_isduplicated=df.duplicated(keep=False)  #只要不是唯一值都显示true
2 print(df_isduplicated)
3 print(df[df_isduplicated])
删除重复值
1 df_drop=df.drop_duplicates()
2 print(df_drop)



#离散数据处理
1 向量化

2 标签化

生成哑变量
1 df_dv=df.copy()
2 col=df.columns.delete(0)
3 for i in col:
4     new=pd.get_dummies(df_dv[i],prefix=i)
5     df_dv=df_dv.join(new)
6     df_dv=df_dv.drop(i,axis=1)
7 print(df_dv)

#数据归一化
常见的归一化方法有两种，一种是min-max归一化，就是每一个值除以最大值减去最小值的差，这样可以把数据归一化到[0,1]之间。另一种是z-score标准化，也就是经过处理后的数据符合标准正态分布，即均值为0，标准差为1。
1 使用z-score标准化数据
from sklearn.preprocessing import StandardScaler
ss = StandardScaler()
scale_features = ['number_project', 'average_monthly_hours', 'time_spend_company']
hr[scale_features] = ss.fit_transform(hr[scale_features])

2 min-max归一化
from sklearn.preprocessing import MinMaxScaler
ss = MinMaxScaler()
scale_features = ['number_project', 'average_monthly_hours', 'time_spend_company']
hr[scale_features] = ss.fit_transform(hr[scale_features])

#数据转换
1 使用astype()函数进行类型转换
如果数据中含有缺失值、特殊字符astype()函数可能失效。
2 使用自定义函数进行数据类型转换
该方法特别适用于待转换数据列的数据较为复杂的情形，可以通过构建一个函数应用于数据列的每一个数据，并将其转换为适合的数据类型。
data['2016'].apply(lambda x: x.replace('￥', '').replace(',', '')).astype('float')
为了转换状态列，可以使用Numpy中的where函数，把值为Y的映射成True,其他值全部映射成False。
data['状态'] = np.where(data['状态'] == 'Y', True, False)
3 利用Pandas的一些辅助函数进行类型转换
Pandas的astype()函数和复杂的自定函数之间有一个中间段，那就是Pandas的一些辅助函数。这些辅助函数对于某些特定数据类型的转换非常有用(如to_numeric()、to_datetime())。
所属组数据列中包含一个非数值，用astype()转换出现了错误，然而用to_numeric()函数处理就优雅很多。
pd.to_numeric(data['所属组'], errors='coerce').fillna(0)
4 在读取数据时就对数据类型进行转换，一步到位
            data2 = pd.read_csv("data.csv",
                   converters={
                               '客户编号': str,
                               '2016': convert_currency,
                               '2017': convert_currency,
                               '增长率': convert_percent,
                               '所属组': lambda x: pd.to_numeric(x, errors='coerce'),
                               '状态': lambda x: np.where(x == "Y", True, False)
                              },
                   encoding='gbk')


5 根据条件给列数据重新赋值
这个应该也是非常常见的功能。举个简单的例子，现在要把Work_accident中大于2的值改为True，小于等于2的值改为False。例子要求可能不太合理，但意思应该表达出来了。这种要求怎么实现呢。非常简单，一句就可以搞定了。
hr['Work_accident'] = hr['Work_accident'].apply(lambda x: False if x<2 else True)
