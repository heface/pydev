#Pandas数据处理：12个使效率倍增的技巧  
```
import pandas as pd 
import numpy as np 
data = pd.read_csv("train.csv", index_col="Loan_ID")
```
##1 布尔索引(Boolean Indexing)
如何你想用基于某些列的条件筛选另一列的值，你会怎么做？例如，我们想要一个全部无大学学历但有贷款的女性列表。这里可以使用布尔索引。代码如下：  
data.loc[(data["Gender"]=="Female") & (data["Education"]=="Not Graduate") & (data["Loan_Status"]=="Y"), ["Gender","Education","Loan_Status"]]

##2 Apply函数
Apply是摆弄数据和创造新变量时常用的一个函数。Apply把函数应用于数据框的特定行/列之后返回一些值。这里的函数既可以是系统自带的也可以是用户定义的。例如，此处可以用它来寻找每行每列的缺失值个数：  
```
def num_missing(x):
    return sum(x.isnull())
#apply到每一列
print("Missing values pre column:")
print(data.apply(num_missing,axis=0) #axis=0代表函数应用于每一列
#apply到每一行
print("Missing values pre row:")
print(data.apply(num_missing,axis=1).head()#axis=1代表函数应用于每一行
```

注意：第二个输出使用了head()函数，因为数据包含太多行。

##3 替换缺失值
‘fillna()’ 可以一次解决这个问题。它被用来把缺失值替换为所在列的平均值/众数/中位数。  
```
from scipy.stats import mode
mode(data['Gender'])
```
输出: ModeResult(mode=array([‘Male’], dtype=object), count=array([489]))
返回了众数及其出现次数。记住，众数可以是个数组，因为高频的值可能不只一个。我们通常默认使用第一个：
mode(data['Gender']).mode[0]
'Male'
现在可以填补缺失值，并用上一步的技巧来检验。
```
data['Gender'].fillna(mode(data['Gender']).mode[0],inplace=True)
data['Gender'].fillna(mode(data['Married']).mode[0],inplace=True)
data['Gender'].fillna(mode(data['self_Employed']).mode[0],inplace=True)
#再次检查缺失值以确认
```
注意这是最基本的替换方式，其他更复杂的技术，如：  
缺失值建模   
用分组平均数（平均值/众数/中位数）   
填充  

##4 透视表
Pandas可以用来创建 Excel式的透视表。例如，“LoanAmount”这个重要的列有缺失值。
```
#Determine pivot table 
impute_grps = data.pivot_table(values=["LoanAmount"],
    index=["Gender","Married","Self_Employed"], aggfunc=np.mean)
```
print impute_grps
##5 多重索引
你可能注意到上一步骤的输出有个奇怪的性质。每个索引都是由三个值组合而成。这叫做多重索引。它可以帮助运算快速进行。
```
#只在带有缺失值的行中迭代： 
for i,row in data.loc[data['LoanAmount'].isnull(),:].iterrows(): 
  ind = tuple([row['Gender'],row['Married'],row['Self_Employed']]) 
  data.loc[i,'LoanAmount'] = impute_grps.loc[ind].values[0] 
#再次检查缺失值以确认： 
print data.apply(num_missing, axis=0)
```
注意：
多重索引需要在loc中用到定义分组group的元组(tuple)。这个元组会在函数中使用。
需要使用.values[0]后缀。因为默认情况下元素返回的顺序与原数据库不匹配。在这种情况下，直接指派会返回错误。

##6 二维表
这个功能可被用来获取关于数据的初始“印象”（观察）。这里我们可以验证一些基本假设。例如，本例中“Credit_History” 被认为对欠款状态有显著影响。可以用下面这个二维表进行验证：
```
pd.crosstab(data["Credit_History"],data["Loan_Status"],margins=True)
```
这些数字是绝对数值。不过，百分比数字更有助于快速了解数据。我们可以用apply函数达到目的：
```
def percConvert(ser): 
  return ser/float(ser[-1]) 
  pd.crosstab(data["Credit_History"],
    data["Loan_Status"],margins=True).apply(percConvert, axis=1)
```
现在可以很明显地看出，有信用记录的人获得贷款的可能性更高：有信用记录的人有80% 获得了贷款，没有信用记录的人只有 9% 获得了贷款。  
但不仅仅是这样，其中还包含着更多信息。由于我现在知道了有信用记录与否非常重要，如果用信用记录来预测是否会获得贷款会怎样？令人惊讶的是，在614次试验中我们能预测正确460次，足足有75%！  
如果此刻你在纳闷，我们要统计模型有什么用，我不会怪你。但相信我，在此基础上提高0.001%的准确率都是充满挑战性的。你是否愿意接受这个挑战？  
注：对训练集而言是75% 。在测试集上有些不同，但结果相近。同时，我希望这个例子能让人明白，为什么提高0.05% 的正确率就能在Kaggle排行榜上跳升500个名次。  
想了解更多请阅读Pandas Reference (crosstab)

##7 数据框合并

当我们有收集自不同来源的数据时，合并数据框就变得至关重要。假设对于不同的房产类型，我们有不同的房屋均价数据。让我们定义这样一个数据框：
```
prop_rates = pd.DataFrame([1000, 5000, 12000],
    index=['Rural','Semiurban','Urban'],columns=['rates'])     
    prop_rates
```
现在可以把它与原始数据框合并：
```
data_merged = data.merge(right=prop_rates, how='inner',
    left_on='Property_Area',right_index=True, sort=False) 
data_merged.pivot_table(values='Credit_History',
    index=['Property_Area','rates'], aggfunc=len)
```
这张透视表验证了合并成功。注意这里的 ‘values’无关紧要，因为我们只是单纯计数。
想了解更多请阅读Pandas Reference (merge)

##8 给数据框排序
Pandas可以轻松基于多列排序。方法如下：
```
    data_sorted = data.sort_values(['ApplicantIncome','CoapplicantIncome'], ascending=False)
    data_sorted[['ApplicantIncome','CoapplicantIncome']].head(10)

注：Pandas 的“sort”函数现在已经不推荐使用，我们用 “sort_values”函数代替。
想了解更多请阅读Pandas Reference (sort_values)

##9 绘图（箱型图&直方图）
许多人可能没意识到Pandas可以直接绘制箱型图和直方图，不必单独调用matplotlib。只需要一行代码。举例来说，如果我们想根据贷款状态Loan_Status来比较申请者收入ApplicantIncome：  
```
    data.boxplot(column="ApplicantIncome",by="Loan_Status")
    data.hist(column="ApplicantIncome",by="Loan_Status",bins=30)
```
可以看出获得/未获得贷款的人没有明显的收入差异，即收入不是决定性因素.
##10 用Cut函数分箱
有时把数值聚集在一起更有意义。例如，如果我们要为交通状况（路上的汽车数量）根据时间（分钟数据）建模。具体的分钟可能不重要，而时段如“上午”“下午”“傍晚”“夜间”“深夜”更有利于预测。如此建模更直观，也能避免过度拟合。
这里我们定义一个简单的、可复用的函数，轻松为任意变量分箱。
```
    #分箱:     
    def binning(col, cut_points, labels=None):     
      #Define min and max values:     
      minval = col.min()     
      maxval = col.max()     
      #利用最大值和最小值创建分箱点的列表     
      break_points = [minval] + cut_points + [maxval]     
      #如果没有标签，则使用默认标签0 ... (n-1)     
      if not labels:     
        labels = range(len(cut_points)+1)     
      #使用pandas的cut功能分箱     
      colBin = pd.cut(col,bins=break_points,labels=labels,include_lowest=True)     
      return colBin 
      
    #为年龄分箱:     
    cut_points = [90,140,190]     
    labels = ["low","medium","high","very high"]     
    data["LoanAmount_Bin"] = binning(data["LoanAmount"], cut_points, labels)     
    print pd.value_counts(data["LoanAmount_Bin"], sort=False)
```

##11 为分类变量编码
有时，我们会面对要改动分类变量的情况。原因可能是：  
有些算法（如罗吉斯回归）要求所有输入项目是数字形式。所以分类变量常被编码为0, 1….(n-1)
有时同一个分类变量可能会有两种表现方式。如，温度可能被标记为“High”， “Medium”， “Low”，“H”， “low”。这里 “High” 和 “H”都代表同一类别。同理， “Low” 和“low”也是同一类别。但Python会把它们当作不同的类别。
一些类别的频数非常低，把它们归为一类是个好主意。  
这里我们定义了一个函数，以字典的方式输入数值，用‘replace’函数进行编码。
```
    #使用Pandas replace函数定义新函数：     
    def coding(col, codeDict):     
      colCoded = pd.Series(col, copy=True)     
      for key, value in codeDict.items():     
        colCoded.replace(key, value, inplace=True)     
      return colCoded
    #把贷款状态LoanStatus编码为Y=1, N=0:     
    print 'Before Coding:'     
    print pd.value_counts(data["Loan_Status"])     
    data["Loan_Status_Coded"] = coding(data["Loan_Status"], {'N':0,'Y':1})     
    print '\nAfter Coding:'     
    print pd.value_counts(data["Loan_Status_Coded"])
```

编码前后计数不变，证明编码成功。

##12 在一个数据框的各行循环迭代
这不是一个常见的操作。但你总不想卡在这里吧？有时你会需要用一个for循环来处理每行。例如，一个常见的问题是变量处置不当。通常见于以下情况：  
带数字的分类变量被当做数值。
（由于出错）带文字的数值变量被当做分类变量。
所以通常来说手动定义变量类型是个好主意。如我们检查各列的数据类型：
``` 
    #检查当前数据类型：     
    data.dtypes
```
这里可以看到分类变量Credit_History被当作浮点数。对付这个问题的一个好办法是创建一个包含变量名和类型的csv文件。通过这种方法，我们可以定义一个函数来读取文件，并为每列指派数据类型。举例来说，我们创建了csv文件datatypes.csv。
```
    #载入文件:     
    colTypes = pd.read_csv('datatypes.csv')     
    print colTypes
```
载入这个文件之后，我们能对每行迭代，把用‘type’列把数据类型指派到‘feature’ 列对应的项目。
```
    #迭代每行，指派变量类型。     
    #注，astype用来指定变量类型。     
    for i, row in colTypes.iterrows(): #i: dataframe索引; row: 连续的每行       
      if row['feature']=="categorical":     
        data[row['feature']]=data[row['feature']].astype(np.object)     
      elif row['feature']=="continuous":     
        data[row['feature']]=data[row['feature']].astype(np.float)     
      print data.dtypes
```
现在信用记录这一列的类型已经成了‘object’ ，这在Pandas中代表分类变量。

#Pandas使用大全
1、首先导入pandas库，一般都会用到numpy库，所以我们先导入备用：
import numpy as np
import pandas as pd

2、导入CSV或者xlsx文件：
df = pd.DataFrame(pd.read_csv('name.csv',header=1))
df = pd.DataFrame(pd.read_excel('name.xlsx'))

3、用pandas创建数据表：
df = pd.DataFrame({"id":[1001,1002,1003,1004,1005,1006], 
 "date":pd.date_range('20130102', periods=6),
  "city":['Beijing ', 'SH', ' guangzhou ', 'Shenzhen', 'shanghai', 'BEIJING '],
 "age":[23,44,54,32,34,32],
 "category":['100-A','100-B','110-A','110-C','210-A','130-F'],
  "price":[1200,np.nan,2133,5433,np.nan,4432]},
  columns =['id','date','city','category','age','price'])

##2、数据表信息查看
1、维度查看：
df.shape

2、数据表基本信息（维度、列名称、数据格式、所占空间等）：
df.info()

3、每一列数据的格式：
df.dtypes

4、某一列格式：
df['B'].dtype

5、空值：
df.isnull()

6、查看某一列空值：
df.isnull()

7、查看某一列的唯一值：
df['B'].unique()

8、查看数据表的值：
df.values

9、查看列名称：
df.columns

10、查看前10行数据、后10行数据：
df.head() #默认前10行数据
df.tail()    #默认后10 行数据

11、数据信息被描述（数量，均值，方差，最小值，最大值，分位点，名字，数据类型）：
data['Existing_EMI'].describe()
Out[29]:
count    1.246260e+05
mean     3.636342e+03
std      3.369124e+04
min      0.000000e+00
25%      0.000000e+00
50%      0.000000e+00
75%      3.500000e+03
max      1.000000e+07
Name: Existing_EMI, dtype: float64

##三、数据表清洗
1、用数字0填充空值：
df.fillna(value=0)

2、使用列prince的均值对NA进行填充：
df['prince'].fillna(df['prince'].mean())

3、清除city字段的字符空格：
df['city']=df['city'].map(str.strip)

4、大小写转换：
df['city']=df['city'].str.lower()

5、更改数据格式：
df['price'].astype('int')       

6、更改列名称：
df.rename(columns={'category': 'category-size'}) 

7、删除后出现的重复值：
df['city'].drop_duplicates()

8、删除先出现的重复值：
df['city'].drop_duplicates(keep='last')

9、数据替换：
df['city'].replace('sh', 'shanghai')

10、计算每一列的取值数目:
for v in var:
    print '\nFrequency count for variable %s'%v
    print data[v].value_counts()
len(data['Employer_Name'].value_counts())

11、删除列：
data.drop('City',axis=1,inplace=True)

12、修改函数的应用：
data['Age'] = data['DOB'].apply(lambda x: 115 - int(x[-2:]))

##四、数据预处理
df1=pd.DataFrame({"id":[1001,1002,1003,1004,1005,1006,1007,1008], 
"gender":['male','female','male','female','male','female','male','female'],
"pay":['Y','N','Y','Y','N','Y','N','Y',],
"m-point":[10,12,20,40,40,40,30,20]})

1、数据表合并
df_inner=pd.merge(df,df1,how='inner')  # 匹配合并，交集
df_left=pd.merge(df,df1,how='left')        #
df_right=pd.merge(df,df1,how='right')
df_outer=pd.merge(df,df1,how='outer')  #并集

2、设置索引列
df_inner.set_index('id')

3、按照特定列的值排序：
df_inner.sort_values(by=['age'])

4、按照索引列排序：
df_inner.sort_index()

5、如果prince列的值>3000，group列显示high，否则显示low：
df_inner['group'] = np.where(df_inner['price'] > 3000,'high','low')

6、对复合多个条件的数据进行分组标记
df_inner.loc[(df_inner['city'] == 'beijing') & (df_inner['price'] >= 4000), 'sign']=1

7、对category字段的值依次进行分列，并创建数据表，索引值为df_inner的索引列，列名称为category和size
pd.DataFrame((x.split('-') for x in df_inner['category']),index=df_inner.index,columns=['category','size']))

8、将完成分裂后的数据表和原df_inner数据表进行匹配
df_inner=pd.merge(df_inner,split,right_index=True, left_index=True)

##五、数据提取
主要用到的三个函数：loc,iloc和ix，loc函数按标签值进行提取，iloc按位置进行提取，ix可以同时按标签和位置进行提取。
1、按索引提取单行的数值
df_inner.loc[3]

2、按索引提取区域行数值
df_inner.iloc[0:5]

3、重设索引
df_inner.reset_index()

4、设置日期为索引
df_inner=df_inner.set_index('date') 

5、提取4日之前的所有数据
df_inner[:'2013-01-04']

6、使用iloc按位置区域提取数据
df_inner.iloc[:3,:2] #冒号前后的数字不再是索引的标签名称，而是数据所在的位置，从0开始，前三行，前两列。

7、适应iloc按位置单独提起数据
df_inner.iloc[[0,2,5],[4,5]] #提取第0、2、5行，4、5列

8、使用ix按索引标签和位置混合提取数据
df_inner.ix[:'2013-01-03',:4] #2013-01-03号之前，前四列数据

9、判断city列的值是否为北京
df_inner['city'].isin(['beijing'])

10、判断city列里是否包含beijing和shanghai，然后将符合条件的数据提取出来
df_inner.loc[df_inner['city'].isin(['beijing','shanghai'])] 

11、提取前三个字符，并生成数据表
pd.DataFrame(category.str[:3])

##六、数据筛选
使用与、或、非三个条件配合大于、小于、等于对数据进行筛选，并进行计数和求和。
1、使用“与”进行筛选
df_inner.loc[(df_inner['age'] > 25) & (df_inner['city'] == 'beijing'), ['id','city','age','category','gender']]


2、使用“或”进行筛选
df_inner.loc[(df_inner['age'] > 25) | (df_inner['city'] == 'beijing'), ['id','city','age','category','gender']].sort(['age']) 


3、使用“非”条件进行筛选
df_inner.loc[(df_inner['city'] != 'beijing'), ['id','city','age','category','gender']].sort(['id']) 


4、对筛选后的数据按city列进行计数
df_inner.loc[(df_inner['city'] != 'beijing'), ['id','city','age','category','gender']].sort(['id']).city.count()

5、使用query函数进行筛选
df_inner.query('city == ["beijing", "shanghai"]')

6、对筛选后的结果按prince进行求和
df_inner.query('city == ["beijing", "shanghai"]').price.sum()

##七、数据汇总
主要函数是groupby和pivote_table
1、对所有的列进行计数汇总
df_inner.groupby('city').count()


2、按城市对id字段进行计数
df_inner.groupby('city')['id'].count()


3、对两个字段进行汇总计数
df_inner.groupby(['city','size'])['id'].count()


4、对city字段进行汇总，并分别计算prince的合计和均值
df_inner.groupby('city')['price'].agg([len,np.sum, np.mean]) 


##八、数据统计
数据采样，计算标准差，协方差和相关系数
1、简单的数据采样
df_inner.sample(n=3) 


2、手动设置采样权重
weights = [0, 0, 0, 0, 0.5, 0.5]
df_inner.sample(n=2, weights=weights) 


3、采样后不放回
df_inner.sample(n=6, replace=False) 


4、采样后放回
df_inner.sample(n=6, replace=True)


5、 数据表描述性统计
df_inner.describe().round(2).T #round函数设置显示小数位，T表示转置


6、计算列的标准差
df_inner['price'].std()


7、计算两个字段间的协方差
df_inner['price'].cov(df_inner['m-point']) 


8、数据表中所有字段间的协方差
df_inner.cov()


9、两个字段的相关性分析
df_inner['price'].corr(df_inner['m-point']) #相关系数在-1到1之间，接近1为正相关，接近-1为负相关，0为不相关


10、数据表的相关性分析
df_inner.corr()

##九、数据输出
分析后的数据可以输出为xlsx格式和csv格式
1、写入Excel
df_inner.to_excel('excel_to_python.xlsx', sheet_name='bluewhale_cc') 

2、写入到CSV
df_inner.to_csv('excel_to_python.csv') 

#pandas处理大数据的技巧
##大文本数据的读写
有时候我们会拿到一些很大的文本文件，完整读入内存，读入的过程会很慢，甚至可能无法读入内存，或者可以读入内存，但是没法进行进一步的计算，这个时候如果我们不是要进行很复杂的运算，可以使用read_csv提供的chunksize或者iterator参数，来部分读入文件，处理完之后再通过to_csv的mode='a'，将每部分结果逐步写入文件。
```
import pandas as pd
input = pd.read_csv('input.csv',chunksize=1000000)
for i in input:
    chunk = dosomethig(input) #进行一些操作
    chunk.to_csv('output.csv', mode='a', header=False) #header = False不会重复写入列名

input = pd.read_csv('input.csv',iterator = True)
while loop:
    try:
        chunk = reader.get_chunk(1000000)
        chunk.to_csv('output.csv', mode='a', header=False) #和上面代码一样，只是通过iterator实现
    except StopIteration:
        break
'''
to_csv, to_excel的选择
在输出结果时统称会遇到输出格式的选择，平时大家用的最多的.csv, .xls, .xlsx，后两者一个是excel2003，一个是excel2007，我的经验是csv>xls>xlsx，大文件输出csv比输出excel要快的多，xls只支持60000+条记录，xlsx虽然支持记录变多了，但是，如果内容有中文常常会出现诡异的内容丢失。因此，如果数量较小可以选择xls，而数量较大则建议输出到csv，xlsx还是有数量限制，而且 大数据 量的话，会让你觉得python都死掉了

读入时处理日期列
我之前都是在数据读入后通过to_datetime函数再去处理日期列，如果数据量较大这又是一个浪费时间的过程，其实在读入数据时，可以通过parse_dates参数来直接指定解析为日期的列。它有几种参数，TRUE的时候会将index解析为日期格式，将列名作为list传入则将每一个列都解析为日期格式

关于to_datetime函数再多说几句，我们拿到的时期格式常常出现一些乱七八糟的怪数据，遇到这些数据to_datimetime函数默认会报错，其实，这些数据是可以忽略的，只需要在函数中将errors参数设置为'ignore'就可以了。

另外，to_datetime就像函数名字显示的，返回的是一个时间戳，有时我们只需要日期部分，我们可以在日期列上做这个修改，datetime_col = datetime_col.apply(lambda x: x.date())，用map函数也是一样的datetime_col = datetime_col.map(lambda x: x.date())

把一些数值编码转化为文字
前面提到了map方法，我就又想到了一个小技巧，我们拿到的一些数据往往是通过数字编码的，比如我们有gender这一列，其中0代表男，1代表女。当然我们可以用索引的方式来完成

其实我们有更简单的方法，对要修改的列传入一个dict，就会达到同样的效果。

通过shift函数求用户的相邻两次登录记录的时间差
之前有个项目需要计算用户相邻两次登录记录的时间差，咋看起来其实这个需求很简单，但是数据量大起来的话，就不是一个简单的任务，拆解开来做的话，需要两个步骤，第一步将登录数据按照用户分组，再计算每个用户两次登录之间的时间间隔。数据的格式很单纯，如下所示

如果数据量不大的，可以先unique uid，再每次计算一个用户的两次登录间隔，类似这样

这种方法虽然计算逻辑比较清晰易懂，但是缺点也非常明显，计算量巨大，相当与有多少量记录就要计算多少次。

那么为什么说pandas的shift函数适合这个计算呢?来看一下shift函数的作用

刚好把值向下错位了一位，是不是恰好是我们需要的。让我们用shift函数来改造一下上面的代码。

上面的代码就把pandas向量化计算的优势发挥出来了，规避掉了计算过程中最耗费时间的按uid循环。如果我们的uid都是一个只要排序后用shift(1)就可以取到所有前一次登录的时间，不过真实的登录数据中有很多的不用的uid，因此再将uid也shift一下命名为uid0，保留uid和uid0匹配的记录就可以了。

##数据预处理：使用Dask和Numba并行化加速
大数据
摘要： 本文是针对Python设计一种并行处理数据的解决方案——使用Dask和Numba并行化加速运算速度。案例对比分析了几种不同方法的运算速度，非常直观，可供参考。

如果你善于使用Pandas变换数据、创建特征以及清洗数据等，那么你就能够轻松地使用Dask和Numba并行加速你的工作。单纯从速度上比较，Dask完胜Python，而Numba打败Dask，那么Numba+Dask基本上算是无敌的存在。将数值计算分成Numba sub-function和使用Dask map_partition+apply，而不是使用Pandas。对于100万行数据，使用Pandas方法和混合数值计算创建新特征的速度比使用Numba+Dask方法的速度要慢许多倍。

Python：60.9x | Dask：8.4x | Numba：5.8x |Numba+Dask：1x

8be99f10ed908533e525b81fcd04bcdf3b27db2d

作为旧金山大学的一名数据科学硕士，会经常跟数据打交道。使用Apply函数是我用来创建新特征或清理数据的众多技巧之一。现在，我只是一名数据科学家，而不是计算机科学方面的专家，但我是一个喜欢捣鼓并使得代码运行更快的程序员。现在，我将会分享我在并行应用上的经验。

大多Python爱好者可能了解Python实现的全局解释器锁（GIL），GIL会占用计算机中所有的CPU性能。更糟糕的是，我们主要的数据处理包，比如Pandas，很少能实现并行处理代码。

Apply函数vs Multiprocessing.map

Tidyverse已经为处理数据做了一些美好的事情，Plyr是我最喜爱的数据包之一，它允许R语言使用者轻松地并行化他们的数据应用。Hadley Wickham说过：

“plyr是一套处理一组问题的工具：需要把一个大的数据结构分解成一些均匀的数据块，之后对每一数据块应用一个函数，最后将所有结果组合在一起。”

对于Python而言，我希望有类似于plyr这样的数据包可供使用。然而，目前这样的数据包还不存在，但我可以使用并行数据包构成一个简单的解决方案。

Dask

bbcc3ca9a96dc7ad7129d9047a2d58be57a4ed84

之前在Spark上花费了一些时间，因此当我开始使用Dask时，还是比较容易地掌握其重点内容。Dask被设计成能够在多核CPU上并行处理任务，此外也借鉴了许多Pandas的语法规则。

现在开始本文所举例子。对于最近的数据挑战而言，我试图获取一个外部数据源（包含许多地理编码点），并将其与要分析的一大堆街区相匹配。在计算欧几里得距离的同时，使用最大启发式将最大值分配给一个街区。

8809febd555c55a69522a58770971c8cf0c57af5

最初的apply：

Dask apply:

二者看起来很相似，apply核心语句是map_partitions，最后有一个compute()语句。此外，不得不对npartitions初始化。 分区的工作原理就是将Pandas数据帧划分成块，对于我的电脑而言，配置是6核-12线程，我只需告诉它使用的是12分区，Dask就会完成剩下的工作。

接下来，将map_partitions的lambda函数应用于每个分区。由于许多数据处理代码都是独立地运行，所以不必过多地担心这些操作的顺序问题。最后，compute()函数告诉Dask来处理剩余的事情，并把最终计算结果反馈给我。在这里，compute()调用Dask将apply适用于每个分区，并使其并行处理。

由于我通过迭代行来生成一个新队列（特征），而Dask apply只在列上起作用，因此我没有使用Dask apply，以下是Dask程序：

Numba、Numpy和Broadcasting

由于我是根据一些简单的线性运算（基本上是勾股定理）对数据进行分类，所以认为使用类似下面的Python代码会运行得更快一些。

d31908d0ecfefd263b3e5373461b34374de9adf5

Broadcasting用以描述Numpy中对两个形状不同的矩阵进行数学计算的处理机制。假设我有一个数组，我会通过迭代并逐个变换每个单元格来改变它

相反，我完全可以跳过for循环，并对整个数组执行操作。Numpy与broadcasting混合使用，用来执行元素智能乘积（对位相乘）。

Broadcasting可以实现更多的功能，现在看看骨架代码：

从本质上讲，代码的功能是改变数组。好的一方面是运行很快，甚至能和Dask并行处理速度比较。其次，如果使用的是最基本的Numpy和Python，那么就可以及时编译任何函数。坏的一面在于它只适合Numpy和简单Python语法。我不得不把所有的数值计算从我的函数转换成子函数，但其计算速度会增加得非常快。

将其一起使用

简单地使用map_partition()就可以将Numba函数与Dask结合在一起，如果并行操作和broadcasting能够密切合作以加快运行速度，那么对于大数据集而言，将会看到其运行速度得到大幅提升。

09e60c6e34586f4760449a2159928877d49958cf

d9d0d60dc749ba864cbb200bb05b60e71ff6adcf

上面的第一张图表明，没有broadcasting的线性计算其表现不佳，并行处理和Dask对速度提升也有效果。此外，可以明显地发现，Dask和Numba组合的性能优于其它方法。

上面的第二张图稍微有些复杂，其横坐标是对行数取对数。从第二张图可以发现，对于1k到10k这样小的数据集，单独使用Numba的性能要比联合使用Numba+Dask的性能更好，尽管在大数据集上Numba+Dask的性能非常好。

优化

为了能够使用Numba编译JIT，我重写了函数以更好地利用broadcasting。之后，重新运行这些函数后发现，平均而言，对于相同的代码，JIT的执行速度大约快了24%。

c9f6a34759b5b1298033c2e4ffd5d78a63994af5

可以肯定的说，一定有进一步的优化方法使得执行速度更快，但目前没有发现。Dask是一个非常友好的工具，本文使用Dask+Numba实现的最好成果是提升运行速度60倍。

#pandas数据处理清洗常用总结
利用pandas包进行数据分析时常见的操作有：
    1.创建对象
    2.查看对象
    3.选择
    4.缺失值处理
    5.相关操作
    6.合并
    7.分组和分段
    8.轴转换和数据透视表
    9.时间序列
    10.导入和保存数据

##创建对象

    创建Series
    创建DataFrame
    查看不同列的数据类型
    改变索引列名

1.通过传递一个 list 对象来创建一个 Series
s=pd.Series([1,2,3,np.nan,6,8])

2.通过传递一个 numpy array，时间索引以及列标签来创建一个 DataFrame
numpy.random.randn()是从标准正态分布中返回一个或多个样本值。
numpy.random.rand()的随机样本位于[0, 1)中。
np.random.randint(0,7,size=10)生成0到7的随机整数

dates=pd.date_range('20130101',periods=6)
df=pd.DataFrame(np.random.randn(6,4),index=dates,columns=list('ABCD'))

index和columns也可以在DataFrame创建后指定：
df.index=pd.date_range('20130101',periods=df.shape[0])
df.index=pd.date_range('20130101',periods=len(df))

另外，还可以指定某一列为索引
df = df.set_index('A', drop = True)

通过字典对象来创建一个 DataFrame

df2=pd.DataFrame({'A':1.,
                 'B':pd.Timestamp('20130102'),
                 'C':pd.Series(1,index=list(range(4)),dtype='float32'),
                 'D':np.array([3]*4,dtype='float32'),
                 'E':pd.Categorical(['test','train','test','train']),
                 'F':'foo'})

另外，在原有数据df的基础上，可以创建一个新的数据框df3
df3=pd.dataframe()
df3['min']=df.min()
df3['max']=df.max()
df3['std']=df.std()

或者按行进行汇总统计创建一个新的数据框df4

df4=pd.dataframe()
df4['min']=df.min(axis=1)
df4['max']=df.max(axis=1)
df4['std']=df.std(axis=1)

轴为0的时候是对列的数据进行统计运算，比如shape[0]是行的个数，相当于一个完整的列有多少数据，df.min(axis=0)，求每一列的最小值。轴为1是对行的数据量进行统计。

3.查看不同列的数据类型
df2.dtypes

4.改变索引列名
df.rename(index=lambda x:x+5,columns={'A':'newA','B':'newB'})

##二、查看数据

    查看头尾的行数据
    显示索引、列、底层的数据
    统计
    转置
    按轴排序
    按值排序
    查看最大值的索引
    格式化输出format
1.查看头尾的行数据
df.head()
df.tail(3)

2.显示索引、列、底层的数据
df.index
df.columns
df.values

注意，list(df)显示的是columns

3.统计
查看数据框的行数与列数:(shape[0]是行数shape[1]是列数)
df.shape
查看数据框 (DataFrame) 的索引、数据类型及内存信息:
df.info()
统计每一列非空个数
t.count()
统计某列有多少个不同的类用.nunique()或者len(set())，（统计某列不同类对应的个数用value_counts()，后面相关操作中会提到）
df.A..nunique()
len(set(df.A))
统计某列有哪些不同的类（使用value_counts()也可以显示，同时会显示各个类的个数）
df.A.unique()
统计某列是否有重复数据
df.A.is_unique
对于数据类型为数值型的列，查询其描述性统计的内容:
df.describe()
统计相关系数
df.corr()

4.转置
df.T

5.按轴排序
df.sort_index(0) 按行名排序
df.sort_index(1) 按列名排序
df.sort_index(axis=1,ascending=False)

6.按值排序
按行的值排序：
df.sort_values(by='20130101',axis=1)
按列的值排序：
df.sort_values(by='B')
按顺序进行多列降序排序
df.sort_values(['A','B'],ascending=False)

7.查看最大值的索引
df.idxmax(0)    #显示所有列最大值所对应的索引
df.A.idxmax(0)   #显示A列中最大值对应的索引

8.格式化输出format
“格式限定符”（语法是'{}'中带:号）,可以print相应格式的数据
print('{:.2%}'.format(0.12354))
金额千位分隔符
print('{:,}'.format(123456789))
print('{:.2f}'.format(31.31412))

##三、选择
    直接获取数据
    通过标签进行选择 .loc[]
    通过位置进行选择 .iloc[:,:]
    布尔索引
    设置赋值
    1.直接获取数据（用于获取整行或者整列的数据），此处注意列名一定要大小写对应，否则无法取出数据
df['B']
选择两列
df[['A','B']]
通过切片获取行数据
df[0:3]
df['20130101':'20130103']
2.通过标签进行选择 .loc[]
标签的优点是可以多轴交叉选择（注意：iloc内部只能单独使用行标签选择行数据，选择某一列标签时前面需加：，）：
df.loc[dates[0]]
位置加标签(注意只能用：，不能使用类似0:2的切片)：
df.loc[:,['A','B']]
标签加标签：
df.loc['20130101',['A','B']]
获取一个标量：
df.loc['20130101','A']
3.通过位置进行选择 .iloc[:,:]
通过传递数值进行位置选择（选择的是行）,特别是选择单行的时候（注意：iloc内部只有一个值得时候是选择的行，选择某一列时列号前面需加：，），另外-1代表最后一列：
df.iloc[3]
通过数值进行切片 位置加位置（区别于loc之处）
df.iloc[1:3,1:3]
通过制定一个位置的列表:
df.iloc[[1,2],[2,3]]
对行、列进行切片：
df.iloc[[0,1],:]
df.iloc[:,[0,1]]
获取特定的值:
df.iloc[1,1]
4.布尔索引
用一个单独列的值来选择数据:
df[df.A>0]
df[df>0]
选择A列中以a开头的行或列(假设此处的A列是字符串型数据)
df[df.A.str.startswith('a')]
使用 isin()方法来过滤:
df['E']=['one','one','two','there','four','there']
df[df.E.isin(['two','four'])]
5.赋值
①通过标签设置新的值
df.loc['20130101','A']=1
如果赋值的标签不存在，则产生新的列（行），未赋值的位置用空值填充
t.loc['20130101','H']=3
②通过位置设置新的值
df.iloc[0,0]=2
③设置整列值（len可以求表格数据的行数）：
df.loc[:,'D']=np.array([3]*len(df))
df['D']=np.array([3]*len(df))
④通过布尔索引赋值
df2=df.copy()
df2[df2>0]=-df2 #全部转化为负数
##四、缺失值处理
    删除列的方法
    去掉包含缺失值的行，不改变原来的值
    对缺失值进行填充
    对数据进行布尔填充
    查看每一列有多少缺失值：
df.isnull().sum()
查看每一列有多少完整的数据
df.shape[0]-df.isnull().sum()
1.删除列的方法:
df.drop(df.columns[4],axis=1,inplace=True)  #不知道列名时
df.drop(‘E’,axis=1,inplace=True)   #根据列名删除
或
del df['E']
2.去掉包含缺失值的行，不改变原来的值
df.dropna()   #不返回df还是原值
df.dropna(how='all')   #删除所有均为空值的行
df.dropna(inplace=True)   #返回删除后的
移除数据框 DataFrame 中包含空值的列
df.dropna(axis=1)
3.对缺失值进行填充（如果填充后需要保存，需加inplace=True）:
df.fillna(value=5)
将所有空值替换为平均值
df.fillna(df.mean())
4.对数据进行布尔填充
pd.isnull(df)
##五、相关操作
    统计行列平均值
    Apply – 对数据应用函数
    计数 value_counts()
    字符串大小写转换
    数据类型转换
    替换
1.统计行列平均值
按列统计平均
df.mean()
对平均值取整
round(df.mean())
按行统计平均
df.mean(1)
2.Apply – 对数据应用函数
其中注意临时函数lambda的使用
df.apply(lambda x:x.max()-x.min())
df.apply(np.mean)   按行统计axis=1
df.apply(np.max,axis=1)
另外可以通过def 定义函数，再使用apply，例如下面数据的第一列，时间为2061年，存在明显错误，可以通过创建函数去修复这个错误
data = pd.read_table(path6, sep = "\s+", parse_dates = [[0,1,2]]) 
data.head()

import datetime
def fix_century(x):
    year = x.year - 100 if x.year > 1989 else x.year
    return datetime.date(year, x.month, x.day)
data['Yr_Mo_Dy'] = data['Yr_Mo_Dy'].apply(fix_century)
data.head()

3.计数 value_counts()
s=pd.Series(np.random.randint(0,7,size=10))
s.value_counts()

DataFrame查看某一列类别数据各类的个数：
df2.E.value_counts()

DataFrame查看所有列的各类统计个数
df2.apply(pd.Series.value_counts)

4.字符串大小写转换
s=pd.Series(['One','Two'])
s.str.lower()

5.将DataFrame的格式转化为浮点数
df.astype(float)

6.替换
df.replace(4,'one')

##六、合并
    concat (不通过键值之间的连接)
    merge 类似于 SQL 类型的连接（ join）☆
    Append ---- 类似于 SQL 中 union
1.concat （默认上下连接，axis=1时左右连接）
df=pd.DataFrame(np.random.randn(10,4))

pieces=[df[:1],df[6:7]]
pd.concat(pieces)

2.merge 类似于 SQL 类型的连接（ join）
根据键连接
merge与concat的区别在于，merge需要依据某一共同的行或列来进行合并
left=pd.DataFrame({'key':['foo','foo1'], 'lval':[1,2]})
right=pd.DataFrame({'key':['foo','foo2'], 'rval':[4,5]})
pd.merge(left,right,on='key')

左连接left，右连接right，外连接outer 默认是inner
pd.merge(left,right,on='key',how='left')

3.Append 将一行连接到一个 DataFrame 上
专门用于上下按照同列名连接---- 类似于 SQL 中 union
append是concat的简略形式,只不过只能在axis=0上进行合并
df=pd.DataFrame(np.random.randn(5,4),columns=list('ABCD'))

s=df.iloc[1,:]
df.append(s,ignore_index=True)

##七、分组和分段
    分组（对数据进行分组汇总统计，类似数据透视表）
    通过多个列进行分组形成一个层次索引
    分段（对数据进行分段或者分箱切割，可用于连续变量的特征处理，例如woe）
df=pd.DataFrame({'A':['foo','bar','foo','bar','foo','bar','foo','bar'],
                'B':['one','two','three','four','two','two','one','three'],
                'C':np.random.randn(8),
                'D':np.random.randn(8)})
1.分组，并对每个分组执行 sum/count/mean/median（中位数）等函数
df.groupby('A').sum()
df.groupby('A').agg(np.sum)
df.groupby('A').agg({'C':sum,'D':sum})
分组求平均值、最大值、最小值
df.groupby('A').C.agg(['mean','max','min'])
按A中类的个数对C求平均值
df.groupby('A').agg({'C':sum})['C'].mean()
2.通过多个列进行分组形成一个层次索引
df.groupby(['A','B']).sum()
3.分段（分箱）
有两种：pd.qcut与pd.cut
按变量取值范围进行均匀分割cut
cut11=pd.cut(df1["可用额度比值"],4)
cut11.head()

按变量个数进行均匀分割qcut
cut11=pd.qcut(df1["可用额度比值"],4)

cut11=pd.qcut(df1["可用额度比值"],4,labels=False)
cut11.head()

##八、轴转换和数据透视表
    Stack堆栈
    数据透视表
1.Stack堆栈
tuples=list(zip(*[['bar','bar','baz','baz','foo','foo','qux','qux'],['one','two','one','two','one','two','one','two']]))
index=pd.MultiIndex.from_tuples(tuples,names=['first','ssecond'])
df=pd.DataFrame(np.random.randn(8,2),index=index,columns=['A','B'])

stacked=df.stack()
stacked2=stacked.unstack()

stacked4=stacked2=stacked.unstack(1)
2.数据透视表
pd.pivot_table()
df=pd.DataFrame({'A':['one','one','two','three']*3,
                'B':['A','B','C']*4,
                'C':['foo','foo','foo','bar','bar','bar']*2,
                'D':np.random.randn(12),
                'E':np.random.randn(12)})
                
pd.pivot_table(df,values='D',index=['A','B'],columns='C')

df.pivot_table(df,index=['A','B'],columns=['C'],aggfunc=np.sum)

##九、时间序列
    针对时间频率重采样
    时间类型转换
    时间采样分组
    时间筛选问题
1.针对时间频率重采样
首先创建一个采样后的时间序列：
rng=pd.date_range('20120101',periods=61,freq='S')
序列或者索引为时间时，可以使用.resample()重置采样频率
ts=pd.Series(np.random.randint(0,500,len(rng)),index=rng)
ts.resample('1Min',how=sum)

另外采样频率还有：
W weekly frequency
M 每月最后一天
BM 每个月最后一个工作日
2.将int64型数据转化成datetime数据
crime.info()
crime.head()

crime.Year = pd.to_datetime(crime.Year, format='%Y')
crime.info()
crime.head()
3.按时间采样结果分组
例如我们获得一组数据索引是每一年
按如果想按十年进行分组查看数据情况，即进行时间分组求和，可以使用重采样
crimes = crime.resample('10AS').sum()

另外，人口不能按十年的直接相加，使用10年内的最大值汇总，在上述基础上更新population列
population = crime['Population'].resample('10AS').max()
crimes['Population'] = population

4.时间筛选问题
通过创建时间分列字段，进行取样统计计算，此方法优点是配合query可以实现灵活取样
例如，如下，计算每一列一月份的平均值

可以先将时间字段分列，相当于创建了辅助列
data['date'] = data.index
data['month'] = data['date'].apply(lambda date: date.month)
data['year'] = data['date'].apply(lambda date: date.year)
data['day'] = data['date'].apply(lambda date: date.day)
data.head()
再筛选计算
january_winds = data.query('month == 1')
january_winds.loc[:,'RPT':"MAL"].mean()
按年进行取样
data.query('month == 1 and day == 1')
按月取样
data.query('day == 1')
时间差，两个日期之间可以相减，并求对应月数和天数
(data.max() - data.min()).days
##十、导入和保存数据
    CSV
    Excel
1.导出
df.to_csv('foo.csv')
df.to_excel('foo.xlsx')
df.to_sql(table_name,connection_object) # 将数据框 (DataFrame)中的数据导入SQL数据表/数据库中
df.to_json(filename) # 将数据框 (DataFrame)中的数据导入JSON格式的文件中

2.导入：
pd.read_csv('foo.csv')
pd.read_excel('foo.xlsx')
pd.read_sql(query, connection_object) # 导入SQL数据表/数据库中的数据
pd.read_json(json_string) # 导入JSON格式的字符，URL地址或者文件中的数据
另外一种常用导入方式
path3 ='../input/pandas_exercise/exercise_data/drinks.csv'    #'drinks.csv'
drinks = pd.read_csv(path3)

3.文件导入参数
在读取文件时考虑到格式问题，会使用一些参数进行调整。
参考：https://www.cnblogs.com/datablog/p/6127000.html
sep指定分隔符。如果不指定参数，则会尝试使用逗号分隔。
其中，会用到正则表达式，可以参考：https://baike.baidu.com/item/%E6%AD%A3%E5%88%99%E8%A1%A8%E8%BE%BE%E5%BC%8F/1700215?fr=aladdin
\s ->匹配任何空白字符，包括空格、制表符、换页符等
\f -> 匹配一个换页
\n -> 匹配一个换行符
\r -> 匹配一个回车符
\t -> 匹配一个制表符
\v -> 匹配一个垂直制表符
+->匹配前面的子表达式一次或多次(大于等于1次）。例如，“zo+”能匹配“zo”以及“zoo”，但不能匹配“z”。
“\s+”则表示匹配任意多个上面的字符。
data = pd.read_table(path6,sep = '\s+') 
data.head()
parse_dates 可以将指定的列转化为时间
data = pd.read_table(path6, sep = "\s+", parse_dates = [[0,1,2]]) 
data.head()

##pandas.read_csv参数整理 
读取CSV（逗号分割）文件到DataFrame
也支持文件的部分导入和选择迭代
更多帮助参见：http://pandas.pydata.org/pandas-docs/stable/io.html
参数：
filepath_or_buffer : str，pathlib。str, pathlib.Path, py._path.local.LocalPath or any object with a read() method (such as a file handle or StringIO)
可以是URL，可用URL类型包括：http, ftp, s3和文件。对于多文件正在准备中
本地文件读取实例：://localhost/path/to/table.csv
 
sep : str, default ‘,’
指定分隔符。如果不指定参数，则会尝试使用逗号分隔。分隔符长于一个字符并且不是‘\s+’,将使用python的语法分析器。并且忽略数据中的逗号。正则表达式例子：'\r\t'
 
delimiter : str, default None
定界符，备选分隔符（如果指定该参数，则sep参数失效）
 
delim_whitespace : boolean, default False.
指定空格(例如’ ‘或者’ ‘)是否作为分隔符使用，等效于设定sep='\s+'。如果这个参数设定为Ture那么delimiter 参数失效。
在新版本0.18.1支持
 
header : int or list of ints, default ‘infer’
指定行数用来作为列名，数据开始行数。如果文件中没有列名，则默认为0，否则设置为None。如果明确设定header=0 就会替换掉原来存在列名。header参数可以是一个list例如：[0,1,3]，这个list表示将文件中的这些行作为列标题（意味着每一列有多个标题），介于中间的行将被忽略掉（例如本例中的2；本例中的数据1,2,4行将被作为多级标题出现，第3行数据将被丢弃，dataframe的数据从第5行开始。）。
注意：如果skip_blank_lines=True 那么header参数忽略注释行和空行，所以header=0表示第一行数据而不是文件的第一行。
 
names : array-like, default None
用于结果的列名列表，如果数据文件中没有列标题行，就需要执行header=None。默认列表中不能出现重复，除非设定参数mangle_dupe_cols=True。
 
index_col : int or sequence or False, default None
用作行索引的列编号或者列名，如果给定一个序列则有多个行索引。
如果文件不规则，行尾有分隔符，则可以设定index_col=False 来是的pandas不适用第一列作为行索引。
 
usecols : array-like, default None
返回一个数据子集，该列表中的值必须可以对应到文件中的位置（数字可以对应到指定的列）或者是字符传为文件中的列名。例如：usecols有效参数可能是 [0,1,2]或者是 [‘foo’, ‘bar’, ‘baz’]。使用这个参数可以加快加载速度并降低内存消耗。
 
as_recarray : boolean, default False
不赞成使用：该参数会在未来版本移除。请使用pd.read_csv(...).to_records()替代。
返回一个Numpy的recarray来替代DataFrame。如果该参数设定为True。将会优先squeeze参数使用。并且行索引将不再可用，索引列也将被忽略。
 
squeeze : boolean, default False
如果文件值包含一列，则返回一个Series
 
prefix : str, default None
在没有列标题时，给列添加前缀。例如：添加‘X’ 成为 X0, X1, ...
 
mangle_dupe_cols : boolean, default True
重复的列，将‘X’...’X’表示为‘X.0’...’X.N’。如果设定为false则会将所有重名列覆盖。
 
dtype : Type name or dict of column -> type, default None
每列数据的数据类型。例如 {‘a’: np.float64, ‘b’: np.int32}
 
engine : {‘c’, ‘python’}, optional
Parser engine to use. The C engine is faster while the python engine is currently more feature-complete.
使用的分析引擎。可以选择C或者是python。C引擎快但是Python引擎功能更加完备。
 
converters : dict, default None
列转换函数的字典。key可以是列名或者列的序号。
 
true_values : list, default None
Values to consider as True
 
false_values : list, default None
Values to consider as False
 
skipinitialspace : boolean, default False
忽略分隔符后的空白（默认为False，即不忽略）.
 
skiprows : list-like or integer, default None
需要忽略的行数（从文件开始处算起），或需要跳过的行号列表（从0开始）。
 
skipfooter : int, default 0
从文件尾部开始忽略。 (c引擎不支持)
 
skip_footer : int, default 0
不推荐使用：建议使用skipfooter ，功能一样。
 
nrows : int, default None
需要读取的行数（从文件头开始算起）。
 
na_values : scalar, str, list-like, or dict, default None
一组用于替换NA/NaN的值。如果传参，需要制定特定列的空值。默认为‘1.#IND’, ‘1.#QNAN’, ‘N/A’, ‘NA’, ‘NULL’, ‘NaN’, ‘nan’`.
 
keep_default_na : bool, default True
如果指定na_values参数，并且keep_default_na=False，那么默认的NaN将被覆盖，否则添加。
 
na_filter : boolean, default True
是否检查丢失值（空字符串或者是空值）。对于大文件来说数据集中没有空值，设定na_filter=False可以提升读取速度。
 
verbose : boolean, default False
是否打印各种解析器的输出信息，例如：“非数值列中缺失值的数量”等。
 
skip_blank_lines : boolean, default True
如果为True，则跳过空行；否则记为NaN。
 
parse_dates : boolean or list of ints or names or list of lists or dict, default False

    boolean. True -> 解析索引
    list of ints or names. e.g. If [1, 2, 3] -> 解析1,2,3列的值作为独立的日期列；
    list of lists. e.g. If [[1, 3]] -> 合并1,3列作为一个日期列使用
    dict, e.g. {‘foo’ : [1, 3]} -> 将1,3列合并，并给合并后的列起名为"foo"

 
infer_datetime_format : boolean, default False
如果设定为True并且parse_dates 可用，那么pandas将尝试转换为日期类型，如果可以转换，转换方法并解析。在某些情况下会快5~10倍。
 
keep_date_col : boolean, default False
如果连接多列解析日期，则保持参与连接的列。默认为False。
 
date_parser : function, default None
用于解析日期的函数，默认使用dateutil.parser.parser来做转换。Pandas尝试使用三种不同的方式解析，如果遇到问题则使用下一种方式。
1.使用一个或者多个arrays（由parse_dates指定）作为参数；
2.连接指定多列字符串作为一个列作为参数；
3.每行调用一次date_parser函数来解析一个或者多个字符串（由parse_dates指定）作为参数。
 
dayfirst : boolean, default False
DD/MM格式的日期类型
 
iterator : boolean, default False
返回一个TextFileReader 对象，以便逐块处理文件。
 
chunksize : int, default None
文件块的大小， See IO Tools docs for more informationon iterator and chunksize.
 
compression : {‘infer’, ‘gzip’, ‘bz2’, ‘zip’, ‘xz’, None}, default ‘infer’
直接使用磁盘上的压缩文件。如果使用infer参数，则使用 gzip, bz2, zip或者解压文件名中以‘.gz’, ‘.bz2’, ‘.zip’, or ‘xz’这些为后缀的文件，否则不解压。如果使用zip，那么ZIP包中国必须只包含一个文件。设置为None则不解压。
新版本0.18.1版本支持zip和xz解压
 
thousands : str, default None
千分位分割符，如“，”或者“."
 
decimal : str, default ‘.’
字符中的小数点 (例如：欧洲数据使用’，‘).
 
float_precision : string, default None
Specifies which converter the C engine should use for floating-point values. The options are None for the ordinary converter, high for the high-precision converter, and round_trip for the round-trip converter.
指定
 
lineterminator : str (length 1), default None
行分割符，只在C解析器下使用。
 
quotechar : str (length 1), optional
引号，用作标识开始和解释的字符，引号内的分割符将被忽略。
 
quoting : int or csv.QUOTE_* instance, default 0
控制csv中的引号常量。可选 QUOTE_MINIMAL (0), QUOTE_ALL (1), QUOTE_NONNUMERIC (2) or QUOTE_NONE (3)
 
doublequote : boolean, default True
双引号，当单引号已经被定义，并且quoting 参数不是QUOTE_NONE的时候，使用双引号表示引号内的元素作为一个元素使用。
 
escapechar : str (length 1), default None
当quoting 为QUOTE_NONE时，指定一个字符使的不受分隔符限值。
 
comment : str, default None
标识着多余的行不被解析。如果该字符出现在行首，这一行将被全部忽略。这个参数只能是一个字符，空行（就像skip_blank_lines=True）注释行被header和skiprows忽略一样。例如如果指定comment='#' 解析‘#empty\na,b,c\n1,2,3’ 以header=0 那么返回结果将是以’a,b,c'作为header。
 
encoding : str, default None
指定字符集类型，通常指定为'utf-8'. List of Python standard encodings
 
dialect : str or csv.Dialect instance, default None
如果没有指定特定的语言，如果sep大于一个字符则忽略。具体查看csv.Dialect 文档
 
tupleize_cols : boolean, default False
Leave a list of tuples on columns as is (default is to convert to a Multi Index on the columns)
 
error_bad_lines : boolean, default True
如果一行包含太多的列，那么默认不会返回DataFrame ，如果设置成false，那么会将改行剔除（只能在C解析器下使用）。
 
warn_bad_lines : boolean, default True
如果error_bad_lines =False，并且warn_bad_lines =True 那么所有的“bad lines”将会被输出（只能在C解析器下使用）。
 
low_memory : boolean, default True
分块加载到内存，再低内存消耗中解析。但是可能出现类型混淆。确保类型不被混淆需要设置为False。或者使用dtype 参数指定类型。注意使用chunksize 或者iterator 参数分块读入会将整个文件读入到一个Dataframe，而忽略类型（只能在C解析器中有效）
 
buffer_lines : int, default None
不推荐使用，这个参数将会在未来版本移除，因为他的值在解析器中不推荐使用
 
compact_ints : boolean, default False
不推荐使用，这个参数将会在未来版本移除
如果设置compact_ints=True ，那么任何有整数类型构成的列将被按照最小的整数类型存储，是否有符号将取决于use_unsigned 参数
 
use_unsigned : boolean, default False
不推荐使用：这个参数将会在未来版本移除
如果整数列被压缩(i.e. compact_ints=True)，指定被压缩的列是有符号还是无符号的。
memory_map : boolean, default False
如果使用的文件在内存内，那么直接map文件使用。使用这种方式可以避免文件再次进行IO操作。

#预处理中的数据类型转换
##pandas中使用自定义函数进行数据类型转换
该方法特别适用于待转换数据列的数据较为复杂的情形，可以通过构建一个函数应用于数据列的每一个数据，并将其转换为适合的数据类型。
对于上述数据中的货币，需要将它转换为float类型，因此可以写一个转换函数：
```
def convert_currency(value):
    """
    转换字符串数字为float类型
     - 移除 ￥ ,
     - 转化为float类型
    """
    new_value = value.replace(',', '').replace('￥', '')
    return np.float(new_value)
```
现在可以使用Pandas的apply函数通过covert_currency函数应用于2016列中的所有数据中。
data['2016'].apply(convert_currency)

##利用Pandas的一些辅助函数进行类型转换
Pandas的astype()函数和复杂的自定函数之间有一个中间段，那就是Pandas的一些辅助函数。这些辅助函数对于某些特定数据类型的转换非常有用(如to_numeric()、to_datetime())。
所属组数据列中包含一个非数值，用astype()转换出现了错误，然而用to_numeric()函数处理就优雅很多。
pd.to_numeric(data['所属组'], errors='coerce').fillna(0)

Pandas中的to_datetime()函数可以把单独的year、month、day三列合并成一个单独的时间戳。
pd.to_datetime(data[['day', 'month', 'year']])

完成数据列的替换
data['new_date'] = pd.to_datetime(data[['day', 'month', 'year']]) #新产生的一列数据
data['所属组'] = pd.to_numeric(data['所属组'], errors='coerce').fillna(0)

##在读取数据时就对数据类型进行转换，一步到位
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
在这里也体现了使用自定义函数比lambda表达式要方便很多。(大部分情况下lambda还是很简洁的，笔者自己也很喜欢使用）

#pandas数据预处理
##查看统计数据
csv文件读取
拿到数据以后，一般都要先看看数据长啥样，有多大，都有什么特征，用pandas查看这些是非常方便的。针对本例子中的csv文件， 我们使用read_csv函数来读取， 读进来之后是pandas中的DataFrame格式。
```
import numpy as np
import pandas as pd
# 使用read_csv读取数据
hr = pd.read_csv("HR.csv")
```
但有一点要注意，读取的时候要先看一下csv文件中格式。主要看两点，一是第一列（也有可能是前几列）是不是索引，二是看第一行是数据还是feature的名称。 read_csv方法默认会将第一行当成feature来解析。
```
# 如果第一列是索引
pd.read_csv('data.csv', index_col=0)
# 如果是纯数据没有feature的话
pd.read_csv('data.csv', header=None)
```
实际上如果你用的是ipython，可以直接输入 pd.read_csv? 来查看这个函数的文档，非常方便。
查看数据
```
# 查看数据的行数与列数， 一般来说行代表样本数， 列代表feature数
hr.shape
# 查看数据的前5行
hr.head()
# 查看每一列的计数及数据类型等信息
hr.info()
# 查看统计信息
hr.describe()
```
一般来说我们都会看一下这些信息。 从而对数据有一定的概念。

## 简单的可视化
   pandas提供了一个简单的函数让我们可以非常简单的查看各个column的分布直方图，当然仅限于该column的值的数字的时候，如果是离散值就没有用这个办法可视化了。值得注意的是该函数依赖于matplotlib， 须先导入该包。
```
import matplotlib.pyplot as plt
hr.hist(grid=False, figsize=(12,12))
```
有两个参数值得一提
    grid : True 或者 False； 就是设不设置网格， 这个就看个人的需求了
    figsize： tuple；图的大小， 当你绘制的直方图有多个时， 就设置大一点，这个多尝试几次就好了
至于其他的参数，一般来说用的不多， 但如果有需求可以看一下文档，强烈建议用ipython，这用就可以直接用 hr.hist? 来查看该函数的文档了。

##去除重复项
pandas提供了duplicated 函数供我们查看是否有完全一样的两行，也就是重复的两行，返回的是一个Boolean值的Series，重复项那里就是True，无重复项的False
```
# 可以通过df.duplicated()查看是否有重复项
hr.duplicated(keep="last")
```
    keep: "first", "last", False. 默认是"first". 非常重要的参数，first的意思就是重复项里面第一个为False， 剩下的事True， last的意思则正好相反，最后一项是False， 其他重复项为True。指定为False则表示把所有重复项都设置为True
    subset: list, 要检查重复的项，默认是全部，也就是两行完全一样才判断为True。 如果只是像查看部分column是否一样的话就可以用subset这个参数了。

除了查看重复的项，我们还可以去除重复项。drop_duplicates提供了这一功能。

hr = hr.drop_duplicates()
    keep： "first", "last", False. 默认是“first”。 也就是默认保留最前面的重复项，将其他重复项去除。“last”则表示保留最后面的重复项，将其他重复项去除。False则表示将所有重复项全部去除。
    subset: list， 默认是全部列。如果只是要将其中几列相同就去除的话可以用这个参数。
    inplace: True or False。 默认是False，也就是不修改原来的DataFrame。设置为True则会改变原来的DataFrame。

##处理缺失值
缺失值的处理一直是数据处理的一个重点工作。根据数据的不同会做出不同的选择，有用均值填充的，中位数填充的，用0填充的，甚至直接去除的。再复杂一点的可以用autoencoder来训练预测缺失值，关于缺失值的处理可以写一本厚厚的书了。这里就简单的说明一下常见的处理方法。注意我这个数据没有缺失值，大家可以找找其他数据试一下。
# 用均值填充
hr.fillna(hr.mean())
# 用中位数填充
hr.fillna(hr.median())
# 用0填充
hr.fillna(0)

##离散的feature处理
包含离散的feature的数据无法直接作为输入进行机器学习。例如性别，男跟女，例如工资，low，medium，high。 需要做一个向量化处理。有人说不能直接用0,1,2来表示吗，例如0表示low，1表示medium， 2表示high。emmmm，当然不行。怎么向量化呢？以该数据中的工作岗位与工资为例， 001 表示low ，010表示medium，100表示表示high。
```
categorical_features = ['sales', 'salary']
hr_cat = pd.get_dummies(hr[categorical_features])
hr = hr.drop(categorical_features, axis=1)
hr = pd.concat([hr, hr_cat], axis=1)
```
很简单的代码，值得一提的事get_dummies这个函数。该函数的作用是将离散的变量转化为向量化，一两句说不清，这里只告诉你可以这么处理离散变量，想要细细了解看一下文档就明白了，我把文档贴过来也没有意思。

##数据归一化
向量归一化也是非常重要的。最常见的归一化方法有两种，一种是min-max归一化，就是每一个值除以最大值减去最小值的差，这样可以把数据归一化到[0,1]之间。另一种是z-score标准化，也就是经过处理后的数据符合标准正态分布，即均值为0，标准差为1。这两种都非常常见，具体使用哪种得看数据。可以用sklearn来进行处理，这样就不用自己来实现了。
```
from sklearn.preprocessing import StandardScaler
# 使用z-score标准化数据
ss = StandardScaler()
scale_features = ['number_project', 'average_monthly_hours', 'time_spend_company']
hr[scale_features] = ss.fit_transform(hr[scale_features])
```
如果是想用min-max归一化的话，sklearn也有现有的类实现。
```
from sklearn.preprocessing import MinMaxScaler
ss = MinMaxScaler()
scale_features = ['number_project', 'average_monthly_hours', 'time_spend_company']
hr[scale_features] = ss.fit_transform(hr[scale_features])
```

##去除缺失比例超过50%的行/列
这是我在处理其他数据的时候遇到的问题， 就是有时候并不只是单纯的根据一部分column来去除数据，而是要根据缺失比例来进行取舍。有可能是缺失比例超过30%，或者70%。我查了一下pandas好像没有现有的函数直接实现的。但不打紧，我写了两个函数来实现。
    去除缺失值比例超过一定程度的列
```
def drop_col(df, cutoff=0.4):
    n = len(df)
    for column in df.columns:
        cnt = df[column].count()
        if (float(cnt) / n) < cutoff:
            df = df.drop(column, axis=1)
    return df
hr = drop_col(hr)
```
当然本文中数据是没有缺失值的，因此没有什么效果。注意cutoff指的是有数据的比例。
    去除缺失值超过一定比例的行
```
def drop_row(df, cutoff=0.8):
    n = df.shape[1]
    for row in df.index:
        cnt = df.loc[row].count()
        if cnt / n < cutoff:
            df = df.drop(row, axis=0)
    return df
hr  = drop_row(hr)
```
同样的，这里的cutoff也是只有数据的比例

##根据条件给列数据重新赋值
这个应该也是非常常见的功能。举个简单的例子，现在要把Work_accident中大于2的值改为True，小于等于2的值改为False。例子要求可能不太合理，但意思应该表达出来了。这种要求怎么实现呢。非常简单，一句就可以搞定了。
hr['Work_accident'] = hr['Work_accident'].apply(lambda x: False if x<2 else True)
如果要求比较复杂，就不要用匿名函数了，自己写一个函数，然后像上面那样子就成了。非常简单的。
