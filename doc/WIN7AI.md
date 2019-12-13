WIN7下搭建人工智能开发环境
最近深度学习很火，本人也想了解下人工智能是怎么回事，所以在自己的电脑上搭建了一套学习环境。
因为不太喜欢anaconda，觉得它装的东西太多，就想自己配置一个相对干净的开发环境。
1 安装python ，这就不细说了，为了稳定考虑，装的是3.6.8版本。
2 设置pip镜像源：
pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
注：pip配置文件位置-~/AppData/Romaing/pip/pip.ini
3 安装虚拟环境管理器
pip install virtualenv
pip install virtualenvwrapper-win
4 为virtualenv创建目录，例如：D:\pyEnvs
创建环境变量WORKON_HOME，值为D:\pyEnvs
5 新建虚拟环境AIStudy并指定python版本python36:
mkvirtualenv AIStudy --python=C:\Python36\python.exe
6 执行lsvirtualenv指令查看所有虚拟环境，环境AIStudy 位于D:\pyEnvs
7 激活虚拟环境AIStudy:
workon AIStudy 
另：退出虚拟环境命令 deactivate
8 下边执行pip install安装各类需要的包：
pip install numpy,pandas,matplotlib
pip install keras
pip install catboost
pip install lightgbm
pip install sklearn
pip install jupyter
9 配置jupyter工作路径：
jupyter notebook --generate-config 
打开“.jupyter”文件夹，可以看到里面有个配置文件。
修改jupyter_notebook_config.py配置文件，找到“c.NotebookApp.notebook_dir=……”，
把路径改成自己的工作目录。
## The directory to use for notebooks and kernels.
c.NotebookApp.notebook_dir = 'D:\work'
10 启动jupyter(指定端口9000):
jupyter notebook --port 9000
这样就可以在浏览器中使用jupyter了。

CUDA Toolkit 10下载：
https://developer.nvidia.com/cuda-downloads?target_os=Windows&target_arch=x86_64&target_version=10&target_type=exelocal
pip install tensorflow

CUDA Toolkit for win7下载：
https://developer.nvidia.com/cuda-downloads?target_os=Windows&target_arch=x86_64&target_version=7&target_type=exelocal

Software requirements
The following NVIDIA® software must be installed on your system:

    NVIDIA® GPU drivers —CUDA 10.0 requires 410.x or higher.
    CUDA® Toolkit —TensorFlow supports CUDA 10.0 (TensorFlow >= 1.13.0)
	CUDA Toolkit for win7下载：
	https://developer.nvidia.com/cuda-downloads?target_os=Windows&target_arch=x86_64&target_version=7&target_type=exelocal
    CUPTI ships with the CUDA Toolkit.
    cuDNN SDK (>= 7.4.1)
    (Optional) TensorRT 5.0 to improve latency and throughput for inference on some models.


Make sure the installed NVIDIA software packages match the versions listed above. In particular, TensorFlow will not load without the cuDNN64_7.dll file. To use a different version, see the Windows build from source guide.

Add the CUDA, CUPTI, and cuDNN installation directories to the %PATH% environmental variable. For example, if the CUDA Toolkit is installed to C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v10.0 and cuDNN to C:\tools\cuda, update your %PATH% to match:

SET PATH=C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v10.0\bin;%PATH%
SET PATH=C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v10.0\extras\CUPTI\libx64;%PATH%
SET PATH=C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v10.0\include;%PATH%
SET PATH=C:\tools\cuda\bin;%PATH%



1 安装vs 2019 community版本，这从微软官网下载就可以，其实是为了用msvc编译器（CUDA安装需要），下载2015也可以。
勾选 使用C++的桌面开发 ，就这个占用空间6.75G

2 装显卡驱动，建议去官网下载最新的。CUDA 10.0 requires 410.x or higher. 

3 装CUDA Tookit

4 装cuDNN SDK

5 装tensorflow
pip install tensorflow-gpu
指定版本
pip install tensorflow-gpu==1.14

目前看CUDA10.1似乎只能安装tf-gpu1.13版本才行
conda install tensorflow-gpu安装的TF版本为1.13

conda设置镜像库
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free/
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main/
conda config --set show_channel_urls yes


Anaconda 管理包的指令

    conda list: 查看安装的所有包
    conda install <包名>: 安装指定包
    conda update <包名>: 更新指定包
    conda remove <包名>: 删除指定包

Anaconda 设置国内镜像源(Win)
1、通过 conda config 命令生成配置文件

    这里我们使用的是清华的镜像：https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free/
    在CMD命令行输入命令：

    conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free/
    conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main/
    conda config --set show_channel_urls yes

    其中conda config --set show_channel_urls yes 的意思是从channel中安装包时显示channel的url，这样就可以知道包的安装来源了。

此时，目录C:\Users下就会生成配置文件.condarc，内容如下：

channels:
    - https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free/
    - defaults
show_channel_urls: true

2、修改配置文件

    删除上述配置文件.condarc中的第三行，然后保存，最终版本文件如下：

    channels:
        - https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free/
    show_channel_urls: true

3、检查channels，查看是否设置成功

    通过命令 conda config --show channels 查看
    通过命令conda info 查看当前配置信息，

升级Anaconda需要先升级conda
    conda update conda
    conda update anaconda
    conda update anaconda-navigator    //update最新版本的anaconda-navigator
    conda update xxx   #更新xxx文件包

测试GPU
1 查看CUDA是否可用
import tensorflow as tf
a = tf.test.is_built_with_cuda()
print(a)
True表示CUDA可用
2 查看GPU是否可用
tf.test.is_gpu_available(cuda_only = False, min_cuda_compute_capability = None)
print(b)
True表示GPU可用

