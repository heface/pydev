#数据读取
csv数据读取时需要先看一下csv文件中格式。主要看两点，一是第一列（也有可能是前几列）是不是索引，二是看第一行是数据还是feature的名称。 read_csv方法默认会将第一行当成feature来解析。
如果第一列是索引
pd.read_csv('data.csv', index_col=0)
如果是纯数据没有feature的话
pd.read_csv('data.csv', header=None)

#数据查看
查看数据的行数与列数， 一般来说行代表样本数， 列代表特征数
dataset.shape
查看数据的前5行、后5行
dataset.head()
dataset.tail()
查看每一列的计数及数据类型等信息
dataset.info()
查看统计信息
dataset.describe()
查看索引、列、底层的数据
dataset.index
dataset.columns
dataset.values

#查看几个样本数据
sampleA0 = cdataset[cdataset.cust_id == 2280163] #in ('2280163','1811083','2312623','2801129','2801101','2801097')]
sampleA1 = cdataset[cdataset.cust_id == 2576917] #in ('2576917','902589','87239','2801149','2801159','2801121')]
sampleB = pdataset[pdataset.cust_id == 11807333] #in ('11807333','11807829','11807749')]
print(sampleA0)
print('-'*80)
print(sampleA1)
print('-'*80)
print(sampleB)
sampleA0.to_csv('./etcSampleA0.csv')
sampleA1.to_csv('./etcSampleA1.csv')
sampleB.to_csv('./etcSampleB.csv')

#数据可视化
pandas提供了一个简单的函数让我们可以非常简单的查看各个column的分布直方图，当然仅限于该column的值的数字的时候，如果是离散值就没有用这个办法可视化了。值得注意的是该函数依赖于matplotlib， 须先导入该包。
import matplotlib.pyplot as plt
hr.hist(grid=False, figsize=(12,12))

#查看空值情况
a = pd.DataFrame(cdataset.count()-9025333)
b = pd.DataFrame(pdataset.count()-1048575)
print(a.info())
print(b.info())
print(a)
print(b)

#查看离散数据情况
labelSet = {}
catLabel = ['addr_type','prov_code','active_ind','newcus_ind','cust_type',  
    'channel_entry','fal_ind','emp_ind','country','sex',  
    'cust_type_ms','cust_type_me','reside_ind',
    'foreign_ind','spouse_ind','cust_segment' ]
for item in catLabel:
    labels = cdataset[item].unique().tolist()
    labelSet[item] = labels
    
    plabels = pdataset[item].unique().tolist()
    labelSet[item] = labels
    print('{}:{}'.format(item,labels))
    print('{}:{}'.format(item,plabels))

#目标值占比
data_1 = cdataset[cdataset.target==1]
print('-'*80)
print(data_1.head())
print('-'*80)
print(data_1.tail())
data_0 = cdataset[cdataset.target==0]
targetOccupy = data_1.shape[0]/(data_0.shape[0]+data_1.shape[0])*100 
print('目标值占比：{}%'.format(round(targetOccupy, 2)))

#分类数据空值填充（并画出各类占比）
def getOccupy(colName):
    target1 = pd.DataFrame(cdataset[cdataset.target==1][colName].value_counts())
    target1['index'] = target1.index
    target1.rename(columns = {colName : colName+'1'}, inplace = True)
    target0 = pd.DataFrame(cdataset[cdataset.target==0][colName].value_counts())
    target0['index'] = target0.index
    target0.rename(columns = {colName : colName+'0'}, inplace = True)
    targetA = pd.DataFrame(cdataset[colName].value_counts())
    targetA['index'] = targetA.index
    targetA.rename(columns = {colName : colName+'A'}, inplace = True)
    target = pd.merge(targetA,target1, how = 'outer', on = 'index')
    target = pd.merge(target,target0,how = 'outer', on = 'index')
    #target = pd.concat([targetA,target1,target0],axis = 1, join = 'outer', join_axes=[targetA.index])
    #index中如果有空值时，使用concat报错，猜测concat会把几个index拼接在一起，如果数据类型不同就抛异常
    target.set_index('index', inplace = True)
    target.fillna(0, inplace = True)
    target['targetOccupy'] = target[target.columns[:]].apply(
        lambda x : round(x[1]/x[0]*100, 2) , axis = 1
    )
    return target

def drawBar(df):
    name_list = [str(i) for i in df.index]
    plt.figure(figsize=(10,10))
    plt.barh([i for i in range(len(df.index))], df.targetOccupy, height =0.4, tick_label = name_list)
    plt.show()

fillMap = {'addr_type':0,'prov_code':0,'active_ind':-1,'newcus_ind':-1,'cust_type': 50,
    'channel_entry':'9999','fal_ind':'0','emp_ind':'0','country':'000','sex':'0', 
    'cust_type_me':'0','reside_ind':'0','foreign_ind':'0','spouse_ind':'0',
    'cust_segment':'00'}
cdataset.fillna(fillMap, inplace = True)

for item in catLabel:
    if item in ['cust_type_ms']:
        continue
    print('-'*30 + item + '-'*30)
    df = getOccupy(item)
    drawBar(df)

#查看连续数据情况
dataSet = cdataset[['family_dep','age','fcontract_date','employed_time','vip_final_date','target']]
print(dataSet.info())
print(dataSet.head())
print(dataSet.tail())
dataSet.describe()

#画出分布图
dataSet1 = dataSet[dataSet[target]==1]
dataSet0 = dataSet[dataSet[target]==0]
dataSet1.hist(grid=False, figsize=(12,12))
print('-'*80)
dataSet0.hist(grid=False, figsize=(12,12))


#查看特征的相关系数
dataSet.corr()

#转置
dataSet.T

#排序
df.sort_index(0) 按行名排序
df.sort_index(1) 按列名排序
df.sort_index(axis=1,ascending=False)

按行的值排序：
df.sort_values(by='20130101',axis=1)

按列的值排序：
df.sort_values(by='B')

按顺序进行多列降序排序
df.sort_values(['A','B'],ascending=False)

查看最大值的索引
df.idxmax(0)    #显示所有列最大值所对应的索引
df.A.idxmax(0)   #显示A列中最大值对应的索引
