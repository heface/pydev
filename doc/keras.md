#Linux机器学习开发环境搭建
[toc]
##安装pip安装tensorflow
首先将pip的版本升级
pip install --upgrade pip

然后下载下面链接对应的版本的tensorflow
tensorflow
https://developer.download.nvidia.cn/compute/redist/jp/v42/tensorflow-gpu/


cp36对应的是Python3.6版本，cp27对应的是Python2.7版本。
tensorflow_gpu后面对应的是版本号。选择Nano上面的cuda版本对应的版本安装。本人是cuda10.0,python2.7,然后就安装了1.13.0,cp27版本的tensorflow。
sudo pip install temnsorflow........


##安装keras

直接sudo pip install keras是不行的，要不就是卡着不动，要不就是失败。
需要先输入下面指令
sudo apt-get install python-scipy
sudo apt-get install libblas-dev liblapack-dev
sudo apt-get install gfortran

然后再输入安装指令sudo pip install keras

#keras基于theaolinux安装及问题解决
    安装是以theano为后端
    所选系统为Centos6 32位

    安装需要的包
conda install numpy scipy mkl <nose> <sphinx> <pydot-ng>
#<...>为可选的包
pip install parameterized

    GPU加速器没有安装，不过安装需要下载GPU下载
    Stable Installation

conda install theano pygpu
&
pip install  Theano    libgpuarray

git clone https://github.com/Theano/libgpuarray.git
cd libgpuarray
git checkout tags/v0.6.5 -b v0.6.9

    Bleeding-Edge Installation (recommended)

pip install <--user> <--no-deps> git+https://github.com/Theano/Theano.git#egg=Theano

    libgpuarray

conda install -c mila-udem pygpu

    Developer Installation

git clone git://github.com/Theano/Theano.git
cd Theano
<sudo> pip install <--user> <--no-deps> -e 

sudo yum install python-devel python-nose python-setuptools gcc gcc-gfortran gcc-c++ blas-devel lapack-devel atlas-devel
sudo easy_install pip


##Keras框架搭建

pip install -U --pre pip setuptools wheel
pip install -U --pre numpy scipy matplotlib scikit-learn scikit-image
pip install -U --pre tensorflow-gpu #可能执行不成功，没关系继续执行
pip install -U --pre keras

安装完毕后，输入python，然后输入：

>> import tensorflow
>> import keras

无错输出即可

    Keras中mnist数据集测试 下载Keras开发包

>>> git clone https://github.com/fchollet/keras.git
>>> cd keras/examples/
>>> python mnist_mlp.py

程序无错进行，至此，keras安装完成

#在linux ubuntu下搭建深度学习/机器学习开发环境

##一、安装Anaconda

1.下载

下载地址为：https://www.anaconda.com/download/#linux

2.安装anaconda，执行命令：
1 bash ~/Downloads/Anaconda3-5.1.0-Linux-x86_64.sh

3.在安装过程中会显示配置路径
Prefix=/home/jsy/anaconda2/

4.安装完之后，运行python，仍是ubuntu自带的python信息，需自己设置下环境变量
5.在终端输入$sudo gedit /etc/profile，打开profile文件
6.在文件末尾添加一行：export PATH=/home/jsy/anaconda2/bin:$PATH，其中，将“/home/jsy/anaconda2/bin”替换为你实际的安装路径，保存。
7.重启Linux
8.打开终端，输入python，如果出现如下界面，表明设置成功。
你还可以用conda info 来查询安装信息
输入conda list 可以查询你现在安装了哪些库，常用的python, numpy, scipy名列其中。
如果你还有什么包没有安装上，可以运行conda install ***  来进行安装(***代表包名称），如果某个包版本不是最新的，运行conda update *** 就可以了。

###注意：安装其他包时报错 CondaHTTPError: HTTP 000 CONNECTION FAILED for url <https://repo.anaconda.com/pkgs/main/noarch/current_repodata.json>
解决方案1：
将C:\Users\<本机用户名>\.condarc文件修改为
channels:
  - http://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free/
ssl_verify: true
show_channel_urls: true
即可

注意：一定要是http而不能为https!!!

解决方案2：
具体操作如下:
1、快速创建channels配置文件的备份(保险起见)
cp ~/.condarc{,.bak}

查看配置文件的内容
cat ~/.condarc.bak 
channels:
  - https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free/
  - https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/conda-forge/
  - https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/msys2/
  - https://nanomirrors.tuna.tsinghua.edu.cn/anaconda/cloud
  - defaults
  - https://nanomirrors.tuna.tsinghua.edu.cn/anaconda/cloud/bioconda
  - https://nanomirrors.tuna.tsinghua.edu.cn/anaconda/cloud/bioconda/conda
  - bioconda
  - r
  - conda-forge
show_channel_urls: true

2、删除部分内容
修改后配置文件的内容如下：
vim ~/.condarc
channels:
  - https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free/
  - https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/conda-forge/
  - https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/msys2/
show_channel_urls: true
 
实际验证发现解决方案2比较靠谱


##二、安装scikit-learn 安装keras

执行命令：
1 conda install scikit-learn

安装Kras,执行命令：
1 conda install keras

安装keras过程中，会自动安装所需的TensorFlow

至此，深度学习，机器学习开发环境就已经安装完毕了，可以通过命令
1 spyder

或者
1 jupyter notebook

打开自己喜欢的IDE进行开发，输入以下代码，如果没有报错，就证明环境安装成功了。
import keras
import sklearn

##keras示例程序

import keras  
from keras.models import Sequential  
from keras.layers import Dense  
import numpy as np  
\# 输入训练数据 keras接收numpy数组类型的数据  
x=np.array([[0,1,0],  
            [0,0,1],  
            [1,3,2],  
            [3,2,1]])  
y=np.array([0,0,1,1]).T  
\#最简单的序贯模型，序贯模型是多个网络层的线性堆叠  
simple_model=Sequential()  
\#dense层为全连接层  
\#第一层隐含层为全连接层 5个神经元 输入数据的维度为3  
simple_model.add(Dense(5,input_dim=3,activation='relu'))  
\#第二个隐含层 4个神经元  
simple_model.add(Dense(4,activation='relu'))  
\#输出层为1个神经元  
simple_model.add(Dense(1,activation='sigmoid'))  
\#编译模型,训练模型之前需要编译模型  
\#编译模型的三个参数：优化器、损失函数、指标列表  
simple_model.compile(optimizer='sgd',loss='mean_squared_error')  
\#训练网络 2000次  
\#Keras以Numpy数组作为输入数据和标签的数据类型。训练模型一般使用fit函数  
simple_model.fit(x,y,epochs=2000)  
\#应用模型 进行预测  
y_=simple_model.predict_classes(x[0:1])  
print("[0,1,0]的分类结果："+str(y[0]))  

#conda中安装
##在Anaconda中配置tensorflow
1.打开终端
2.创建一个叫做tensorflow的conda环境并激活
conda create -n tensorflow python=3.5（这里注意，tensorflow目前只支持Python3.5）
--conda create -n keras python=3.6
activate tensorflow （ 激活，激活之后环境前面就是以这种形式显示的：(tensorflow)C:> ）
--conda activate keras
注意：由于新建的虚拟环境，所以没有numpy,pandas,matplotlib等，需要手动安装conda install xxx

3.CPU版本的tensorflow，如果需要安装GPU版本的自行搜索哦。输入以下命令：
pip install --ignore-installed --upgrade https://storage.googleapis.com/tensorflow/windows/cpu/tensorflow-1.1.0-cp35-cp35m-win_amd64.whl
--pip install --ignore-installed --upgrade https://storage.googleapis.com/tensorflow/linux/cpu/tensorflow-1.1.0-cp36-cp36m-linux_amd64.whl
不行，没装上
pip install tensorflow

如上方法并不能成功安装tensorflow...
conda install tensorflow
这样可以成功

4.至此，我们已经安装好了TensorFlow。接下来可以测试验证下是否可以使用。在命令行输入：Python，进入Python编程环境。 然后输入：

            import tensorflow as tf
            hello = tf.constant('Hello, TensorFlow!')
            sess = tf.Session()
            print(sess.run(hello))

正确的话，会输出： Hello, TensorFlow!
##在Jupyter中使用TensorFlow
1.首先，进入tensorFlow环境，安装ipython和jupyter。命令如下：
conda install ipython
conda install jupyter

2.然后，进去Jupyter，直接输入：
jupyter notebook （等待一下就会弹出浏览器，进入Jupyter）

3.最后，可以进行测试导入tensorflow，验证过程同上 import tensorflow as tf
。。。 可以成功运行啦！

#conda安装tensorflow
首先强烈建议大家用conda 管理python包，这里简单说下ubuntu 下conda的安装方法:
到这个网站上下载你想要的conda 版本，根据你自己环境下载。因为我是在ubuntu上安装的，我选择的Miniconda2-latest-Linux-x86_64.sh文件
然后一条命令搞定：sh Miniconda2-latest-Linux-x86_64.sh

这样就安装完成了。

加个国内的镜像源，直接上命令：
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free/
conda update -n base -c defaults conda
conda TensorFlow 包使用面向深度神经网络的英特尔数学核心函数库（Intel MKL-DNN），我们从 TensorFlow 1.9.0 版本开始。

与pip 安装相比，conda 安装可以带来超过 8 倍的速度提升。这对于经常使用 CPU
进行训练和推断的人来说非常棒！作为一名机器学习工程师，我在将代码 push 到 GPU 机器上之前，先使用 CPU
对代码运行测试训练。conda 安装带来的速度提升可以帮助快速迭代。我还在 CPU 上进行大量推断，因此这有助于我的模型性能。
MKL 库不仅加速 TensorFlow 包，还能加速其他广泛使用的库，如 NumPy、NumpyExr、SciPy 和 Scikit-Learn。

下面是使用 conda 安装所需的步骤。
pip uninstall tensorflow
安装好 conda 之后，尝试以下命令：
conda install tensorflow
In case your anaconda channel is not the highest priority channel by default(or you are not sure), use the following command to make sure you
get the right TensorFlow with Intel optimizations
conda install -c anaconda tensorflow
TensorFlowConda 安装详细参见：https://www.anaconda.com/blog/developer-blog/tensorflow-in-anaconda/
MKL 优化方面的详情参见：https://docs.anaconda.com/mkl-optimizations/。

GPU 版本的安装也更加简单
conda 安装将自动安装 GPU 支持所需的 CUDA 和 CuDNN 库。pip 安装则需要手动安装这些库。人人喜欢一步到位，尤其是在下载与安装库这方面。
使用 pip 安装 TensorFlow 时，GPU 支持所需的 CUDA 和 CuDNN 库必须单独手动安装，增加了大量负担。而使用 conda 安装 GPU 加速版本的 TensorFlow 时，只需使用命令 conda install tensorflow-gpu，这些库就会自动安装成功，且版本与 tensorflow-gpu 包兼容。此外，conda 安装这些库的位置不会与通过其他方法安装的库的其他实例产生冲突。不管使用 pip 还是 conda 安装 GPU 支持的 TensorFlow，NVIDIA 驱动程序都必须单独安装。
nvidia drive install
sudo apt-get --purge remove nvidia*
ctrl+alt+F4 logo in tty4
sudo  service lightdm stop
sudo ./Nvidia-version.sh
sudo dpkg --force all --remove   强制删除某个软件
sudo dpkg --configure -a
dpkg -l | grep ^ii | awk '{print $2}' | grep -v XXX | xargs sudo aptitude reinstall
sudo reboot

对于 TensorFlow 的多个版本，conda 包可使用多种 CUDA 版本。例如，对于 TensorFlow 1.10.0 版本，conda 包支持可用的 CUDA 8.0、9.0 和 9.2 库。而 pip 包仅支持 CUDA 9.0 库。在不支持 CUDA 库最新版本的系统上运行时，这非常重要。最后，由于这些库是通过 conda 自动安装的，用户可轻松创建多个环境，并对比不同 CUDA 版本的性能。


