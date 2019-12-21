#Linux设置pip源
pip国内的一些镜像：
  阿里云 http://mirrors.aliyun.com/pypi/simple/
  中国科技大学 https://pypi.mirrors.ustc.edu.cn/simple/
  豆瓣(douban) https://pypi.douban.com/simple/
  清华大学 https://pypi.tuna.tsinghua.edu.cn/simple/
  中国科学技术大学 http://pypi.mirrors.ustc.edu.cn/simple/
临时使用：
　　在使用pip的时候在后面加上-i参数，指定pip源
　　eg: pip install scrapy -i https://pypi.douban.com/simple/
永久修改：
　　linux:
　　修改 ~/.pip/pip.conf (没有就创建一个)， 内容如下：
[global]
index-url = https://pypi.douban.com/simple/


#Linux环境安装jupyter
如果你是python3的就使用如下命令安装
python3 -m pip install --upgrade pip
sudo python3 -m pip install jupyter -i https://pypi.tuna.tsinghua.edu.cn/simple/

如果你的Python版本是Python 2
python -m pip install --upgrade pip
sudo python -m pip install jupyter -i https://pypi.tuna.tsinghua.edu.cn/simple/

选择适应你自己版本的安装方法后，在终端中输入以下语句，检测是否安装成功
jupyter notebook

报错：  Found existing installation: pyzmq 16.0.2
ERROR: Cannot uninstall 'pyzmq'. It is a distutils installed project and thus we cannot accurately determine which files belong to it which would lead to only a partial uninstall

在安装一些python的库的时候，经常会碰到这样的错误，例如在使用指令pip insall tensorlayer时，会出现如下的报错：
Cannot uninstall 'scikit-learn'. It is a distutils installed project and thus we cannot accurately determine which files belong to it which would lead to only a partial uninstall.
一般这种情况下，出错的东西其实是你已经安装过了的，然后你会发现你想卸载也卸载不掉。如果实在找不出别的方法来处理的话，可以试着忽略这个错误。所以可以这样处理：

pip install --ignore-installed scikit-learn

等它完成之后，再pip insall tensorlayer会发现顺利通过。其他的库要是遇到类似的错误，也可以这样解决。

可以采用virtual env的方式，单独为jupyter安装一个virtualenv

郁闷，没搞定，改成安装anaconda???

安装jupyter时报错：
ModuleNotFoundError: No module named 'setuptools'
解决方案：
sudo python3 -m pip install setuptools -i https://pypi.tuna.tsinghua.edu.cn/simple/

安装setuptools,命令如下：
    wget --no-check-certificate  https://pypi.python.org/packages/source/s/setuptools/setuptools-19.6.tar.gz#md5=c607dd118eae682c44ed146367a17e26
    tar -zxvf setuptools-19.6.tar.gz
    cd setuptools-19.6
    python3 setup.py build
    python3 setup.py install

#conda更改为国内镜像源。
终端中运行命令：<br>
(1)清华源(TUNA)<br>
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free/<br>
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main/<br>
conda config --setshow_channel_urls yes<br>

(2)中科大源(USTC)<br>
conda config --add channels https://mirrors.ustc.edu.cn/anaconda/pkgs/free/<br>
conda config --add channels https://mirrors.ustc.edu.cn/anaconda/pkgs/main/<br>
conda config --setshow_channel_urls yes<br>


#清华大学开源镜像站anaconda
安装命令：
sudo sh Anaxxxx.sh

网址：https://mirror.tuna.tsinghua.edu.cn/help/anaconda/
Anaconda 镜像使用帮助
Anaconda 是一个用于科学计算的 Python 发行版，支持 Linux, Mac, Windows, 包含了众多流行的科学计算、数据分析的 Python 包。
Anaconda 安装包可以到 https://mirrors.tuna.tsinghua.edu.cn/anaconda/archive/ 下载。
TUNA 还提供了 Anaconda 仓库的镜像，运行以下命令:
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free/
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main/
conda config --set show_channel_urls yes

即可添加 Anaconda Python 免费仓库。
运行 conda install numpy 测试一下吧。

Miniconda 镜像使用帮助
Miniconda 是一个 Anaconda 的轻量级替代，默认只包含了 python 和 conda，但是可以通过 pip 和 conda 来安装所需要的包。
Miniconda 安装包可以到 https://mirrors.tuna.tsinghua.edu.cn/anaconda/miniconda/ 下载。
Conda 三方源
当前tuna还维护了一些anaconda三方源。
Conda Forge
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/conda-forge/

msys2
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/msys2/

bioconda
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/bioconda/

menpo
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/menpo/

pytorch
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/pytorch/

 # for legacy win-64
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/peterjc123/

其他三方源
对于conda的其他三方源，如有需要请在这个issue中提出请求，我们会综合考虑多方因素来酌情增减。

#conda常用命令
conda update -n base conda        //update最新版本的conda
conda clean -p      //删除没有用的包
conda clean -t      //tar打包
conda --version  //检查conda版本
conda update conda  //升级conda版本
//假设你决定不再使用商业包IOPro。你可以在bunnies环境中移除它。
conda remove -n bunnies iopro
//我们不再需要snakes环境了，可以输入以下命令：
conda remove -n snakes --all


#Linux环境下VirtualENV安装和使用
virtualenv用于创建独立的Python环境，多个Python相互独立，互不影响，它能够：
1. 在没有权限的情况下安装新套件
2. 不同应用可以使用不同的套件版本
3. 套件升级不影响其他应用
安装
sudo apt-get install python-virtualenv
使用方法
virtualenv [虚拟环境名称]
如，创建**ENV**的虚拟环境
virtualenv ENV
默认情况下，虚拟环境会依赖系统环境中的site packages，就是说系统中已经安装好的第三方package也会安装在虚拟环境中，如果不想依赖这些package，那么可以加上参数 --no-site-packages建立虚拟环境
virtualenv --no-site-packages [虚拟环境名称]
启动虚拟环境
cd ENV
source ./bin/activate
注意此时命令行会多一个(ENV)，ENV为虚拟环境名称，接下来所有模块都只会安装到该目录中去。
退出虚拟环境
deactivate
在虚拟环境安装Python套件
Virtualenv 附带有pip安装工具，因此需要安装的套件可以直接运行：
pip install [套件名称]
如果没有启动虚拟环境，系统也安装了pip工具，那么套件将被安装在系统环境中，为了避免发生此事，可以在~/.bashrc文件中加上：
export PIP_REQUIRE_VIRTUALENV=true
或者让在执行pip的时候让系统自动开启虚拟环境：
export PIP_RESPECT_VIRTUALENV=true

Virtualenvwrapper
Virtaulenvwrapper是virtualenv的扩展包，用于更方便管理虚拟环境，它可以做：
1. 将所有虚拟环境整合在一个目录下
2. 管理（新增，删除，复制）虚拟环境
3. 切换虚拟环境
安装
sudo easy_install virtualenvwrapper
此时还不能使用virtualenvwrapper，默认virtualenvwrapper安装在/usr/local/bin下面，实际上你需要运行virtualenvwrapper.sh文件才行，先别急，打开这个文件看看,里面有安装步骤，我们照着操作把环境设置好。
1、创建目录用来存放虚拟环境
mkdir $HOME/.virtualenvs
2、在~/.bashrc中添加行： export WORKON_HOME=$HOME/.virtualenvs
3、在~/.bashrc中添加行：source /usr/bin/virtualenvwrapper.sh
4、运行： source ~/.bashrc
此时virtualenvwrapper就可以使用了。
列出虚拟环境列表
workon
也可以使用
lsvirtualenv
新建虚拟环境
mkvirtualenv [虚拟环境名称]
启动/切换虚拟环境
workon [虚拟环境名称]
删除虚拟环境
rmvirtualenv [虚拟环境名称]
离开虚拟环境
deactivate

#linux下创建virtualenv时指定python版本
创建一个python3.x的虚拟环境
virtualenv -p /usr/bin/python3 py3env
其中，/usr/bin/python3为python3路径，可自行指定，py3env是虚拟环境的名称，可以根据自己的需求命名。
注意,前提是你已经安装了python3.x版本

当我们想用python2.x版本的时候,直接
virtualenv venv
或者
virtualenv -p /usr/bin/python py2env

#1 在Linux下安装virtualenv
本主使用的时python3.5环境
pip3 install virtualenv

##创建虚拟环境
这种操作会在你当前的环境下创建你的虚拟环境目录
~$：virtualenv  -p /usr/bin/python3.5(此处的版本是可以更改的）abc-env(这是本主给虚拟环境取的目录名）

##进入当前虚拟环境下
source abc-env/bin/activate  使用此命令，因为本主是将abc-env目录放在/home/tarena/下，找到abc-env目录下
有个bin目录下activate文件执行就可以

##显示已经进入
tarena@tedu:~$ source myproject-env/bin/activate
(abc-env) tarena@tedu:~$abc

##退出
~$:deactivate

#2 linux下安装virtualenvwrapper
安装virtualenvwrapper
yum install python-setuptools python-devel
apt install python-setuptools python3-dev
pip install virtualenvwrapper # linux下

********************************************
pip install virtualenvwrapper-win # windo
————————————————

pip3 install virtualenvwrapper

##查看是否安装上了 
pip3 list
1、上述工具装好后找不到mkvirtualenv命令，需要执行以下环境变量设置。
1.创建目录用来存放虚拟环境
    mkdir $HOME/.virtualenvs
2.在~/.bashrc中添加行：
    export WORKON_HOME=$HOME/.virtualenvs
    source /usr/local/bin/virtualenvwrapper.sh
3.运行:
    source ~/.bashrc
4.创建python虚拟环境
mkvirtualenv [虚拟环境名称]
workon [虚拟环境名称]

3.退出虚拟环境 离开 deactivate
4.删除(慎用) 
rmvirtualenv [虚拟环境名称]

#3 virtualenv和virtualenvwrapper的区别
virtualenv是你在当前路径下创建出来你给取名字的虚拟环境，这样不容易管理，这样你会在哪哪都是虚拟环境，除非你每一次
都切换到你当前下唯一的一个目录下创建虚拟环境，这样你就会特别麻烦 所以引出来了virtualenvwrapper
virtualenvwrapper会在你配置的环境下创建虚拟环境目录，不管你在当前哪个路径下，只要使用命令
mkvirtualenv -p /usr/bin/python3  虚拟环境名 都是创建在你配置的环境中的特定的文件目录下

#python tar.gz安装
1.使用setuptools工具安装xlrd模块
1) 安装setuptools工具
gunzip setuptools-2.0.tar.gz
tar -xvf setuptools-2.0.tar
python setup.py build
python setup.py install

2)安装xlrd模块
gunzip xlrd-1.1.0.tar.gz
tar -xvf xlrd-1.1.0.tar
python setup.py install

#virtualenv与virtualenvwrapper
当涉及到python项目开发时为了不污染全局环境，通常都会使用环境隔离管理工具virtualenv与virtualenvwrapper。
virtualenv是在项目底下执行生成venv环境目录以此来进行管理，这非常适合使用诸如pycharm这种集成环境配置的开发工具；那么当通过shell来运行virtualenv时便会显得非常麻烦，因为每次shell关闭再打开后都需要重新配置环境参数。
virtualenvwrapper是将所有的python项目虚拟环境环境都存放在一起，在使用shell配合小型开发工具就会非常方便。
virtualenvwrapper安装配置（MAC）

##1、使用pip3安装
$ sudo pip3 install virtualenvwrapper
2、新建存放环境目录(笔者目录为Envs并放在Home下)
$ mkdir -p ~/Envs
3、配置virtualenvwrapper环境(使用python3)
i. 打开bash_profile，执行vim ~/.bash_profile并写入
设置virtualenvwrapper
export WORKON_HOME=~/Envs
export VIRTUALENVWRAPPER_PYTHON=/usr/local/bin/python3
打开终端自动启用
source /usr/local/bin/virtualenvwrapper.sh
ii. 打开.zshrc，执行vim ~/.zshrc并写入(如果有安装item2与oh-my-zsh)	
设置virtualenvwrapper
export WORKON_HOME=~/Envs
export VIRTUALENVWRAPPER_PYTHON=/usr/local/bin/python3
打开终端自动启用
source /usr/local/bin/virtualenvwrapper.sh

4、使配置生效
$ source ~/.bash_profile
$ source ~/.zshrc

##virtualenvwrapper 使用
1、新建虚拟环境test并指定python版本python3
$ mkvirtualenv test --python=python3
执行lsvirtualenv指令查看所有环境，环境test位于~/Envs/test
$ lsvirtualenv
test
====

2、在项目底下激活虚拟环境test
workon test
3、其他指令
退出环境test
deactivate
删除环境test
rmvirtualenv test
更多指令可以在shell中输入virtualenv回车会有提示
##virtualenvwrapper设置环境变量
当我们使用框架时经常需要执行pip install或者 export环境变量等额外的操作，这时就需要使用postactivate等钩子文件（当然钩子文件还有很多，具体感兴趣可以去查看官方文档）。
举个栗子：
想在test虚拟环境激活后设置环境变量
1、打开test的postactivate钩子文件vim ~/Envs/test/bin/postactivate
!/bin/zsh
This hook is sourced after this virtualenv is activated.
 
在当前会话加入环境变量
export ENV=dev

2、这时当执行workon test 激活虚拟环境后便会执行postactivate将项目环境变量Env设置为dev
3、在postactivate 中还可以执行诸如pip install -r requirements.txt，pip install -e conf等shell 操作
到目前为止基本的virtualenvwrapper使用就介绍完了


#pipenv安装使用
一、首先在python 官网安装推荐版的python
https://www.python.org/downloads/

二、新建项目目录并进入项目所在文件下，查看python是否安装成功,查看python 版本
python -V

三、用pip 安装pipenv，pip是python自带的
检查 pip的版本
pip -V
安装pipenv
pip install pipenv
如果提示 pipenv已经存在，则不用继续安装了
四、安装pipenv 虚拟环境，并生成 Pipfile 和Pipfile.lock文件
pipenv install
如果始终没有生成 Pipfile 和Pipfile.lock文件，则删除原来项目文件夹内或者外层文件夹的Pipfile 和Pipfile.lock文件，再执行pipenv install
五、进入pipenv 虚拟环境
pipenv shell
六、进入虚拟环境后，安装各种需要的包
pipenv install + 包名
pipenv install flask
七、查看已安装的包和依赖关系
pipenv graph
八、退出pipenv虚拟环境
exit

注意：Ubuntu在使用一些pip的时候会遇到：“Could not install packages due to an EnvironmentError: [Errno 13] 权限不够:”的问题。
在正常的命令后面加一个 --user即可：
在使用pip的相关命令时，使用国内源的速度更快：如下是使用了清华的国内源。
 pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple/ --user
这样会将Python 程序包安装到 $HOME/.local 路径下，其中包含三个字文件夹：bin，lib 和 share。


#conda更换kernel版本
1 python -m pip install ipykernel
python -m pip install ipykernel
2 sudo python -m ipykernel install --name etc

#pip升级已安装包
python -m pip install --upgrade setuptools

#如何解决Python包依赖问题
##通过pip输出依赖  
pip freeze > requirements.txt  
这个命令可能是很多同学用来输出依赖的命令, 但它输出的是当前环境下的所有包, 也就是输出当前你安装的全部非Python标准库包  

对于按项目建环境的同学, 这种输出方式是没有多大问题的  
只要部署的时候在终端键入pip install -r requirements.txt就可以安装好依赖了, 但是对于没有严格区分项目环境的同学, 一次性安装了其他的包, 并不是一个好的解决方案.  
##通过pipreqs库输出依赖
如这个库的名称所示, 就是为了方便管理依赖而生.  
与pip直接导出全部不同, pipreqs只导出指定项目下Python文件import的库  
用法如下  
```
# 安装
pip install pipreqs
# 切换到项目目录
# 输出requirements.txt到项目根目录下
pipreqs --use-local ./
```
这里我切换到一个Django项目目录下, 打开requirements.txt, 内容是:  
```
pandas==0.22.0
django_debug_toolbar.egg==info
mongoengine==0.9.0
Django==1.11.8
```
瞬间清爽不少.  
#通过Pipenv管理依赖
Pipenv, 汇集了Pip，Pipfile和Virtualenv的功能，是一个强大的命令行工具。  
这里展示最简单的用法  

    pip install pipenv安装好库.  
    切换到项目根目录  
    终端键入Pipenv install  

如果你尚未建立requirements.txt那么将会得到一个空白的Pipfile文本文件, 此时我们在命令行中使用pipenv install 包名, 会在Pipefile写入对应包信息, 之后用户要安装依赖时, 使用pipenv install即可.
如果你已经建立, 终端上会输出以下信息:

requirements.txt found, instead of Pipfile! Converting…
Warning: Your Pipfile now contains pinned versions, if your requirements.txt did. 
We recommend updating your Pipfile to specify the "*" version, instead.
...

上面的输出意思是: 找到了requirements.txt, 但不是Pipfile, 正在转换...
Pipefile现在将包含固定版本信息, 如果你的requirements.txt中已包含.
我们推荐升级你的Pipefile到指定版本...

输出Pipenv文件, 得到以下内容:

[[source]]
url = "https://pypi.org/simple"
verify_ssl = true
name = "pypi"

[packages]
mongoengine = "==0.9.0"
"django-debug-toolbar.egg" = "==info"
django = "==1.11.8"
pandas = "==0.22.0"

[dev-packages]

[requires]
python_version = "3.6"

可以清楚的看到整个文件结构, 第一个是[source]是安装库所在源, 第二个是依赖库的信息, 第三个是当你开发环境所需要的包, 最后一个是Python版本.
当你需要区分开发环境和正式版本发布环境时, 可以使用以下命令:

pipenv install --dev 包名

如果正式版本发布时, 键入Pipenv install, 将不会安装dev标记的包
除非其他开发人员键入Pipenv install -dev, 才会安装所有包.

catboost req:
Requires: scipy, numpy, six, plotly, matplotlib, graphviz, pandas


#win7下virtualENV安装配置步骤
win7设置pip镜像源：
pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
注：pip配置文件位置-~/AppData/Romaing/pip/pip.ini

1 安装python（不详述）
2 安装virtualenvwrapper
pip install virtualenvwrapper -i https://pypi.tuna.tsinghua.edu.cn/simple/
pip install virtualenvwrapper-win -i https://pypi.tuna.tsinghua.edu.cn/simple/   # windows

3 新建虚拟环境test并指定python版本python3
$ mkvirtualenv test --python=C:\Python36  -i https://pypi.tuna.tsinghua.edu.cn/simple/
执行lsvirtualenv指令查看所有环境，环境test位于~/Envs/test
$ lsvirtualenv
test

4 在项目底下激活虚拟环境test
workon test
5 其他指令
退出环境test
deactivate
删除环境test
rmvirtualenv test
更多指令可以在shell中输入virtualenv回车会有提示



1 前言
由于Python的版本众多，还有Python2和Python3的争论，因此有些软件包或第三方库就容易出现版本不兼容的问题。
通过 virtualenv 这个工具，就可以构建一系列 虚拟的Python环境 ，然后在每个环境中安装需要的软件包(配合 pip 使用)，这一系列的环境是相互隔离的。作为一个独立的环境就不容易出现版本问题，还方便部署。
2 安装
pip install virtualenv
3 virtualenv的基本使用
3.1 创建虚拟环境
virtualenv venv
为环境指定Python解释器:
virtualenv -p c:\Python36\python.exe venv
3.2 激活虚拟环境
activate venv
3.3 停止虚拟环境
deactivate
3.4 删除虚拟环境
直接删除目录即可.
rmvirtualenv venv
4 virtualenvwrapper
为了使用virtualenv更方便，可以借助 virtualenvwrapper
4.1 安装virtualenvwrapper
pip install virtualenvwrapper-win
4.2 创建虚拟环境
默认创建的虚拟环境位于C:\Users\username\envs,可以通过环境变量 WORKON_HOME 来定制。
通过计算机-->属性-->高级系统设置-->环境变量-->在系统变量中新建“变量名”：WORKON_HOME,变量值：“你自定义的路径”。
创建后，会自动激活环境，注意看Shell提示符的改变:
(venv)c:>
4.3列出所有虚拟环境
lsvirtualenv
4.4 激活虚拟环境
workon venv
4.5 进入虚拟环境目录
cdvirtualenv
4.6 进入虚拟环境的site-packages目录
cdsitepackages
4.7列出site-packages目录的所有软件包
lssitepackages
4.8 停止虚拟环境
deactivate
4.9 删除虚拟环境
rmvitualenv venv
5 重建Python环境
5.1 冻结环境
所谓 冻结(freeze) 环境，就是将当前环境的软件包等固定下来:
pip freeze >packages.txt　　# 安装包列表保存到文件requirements.txt中
5.2 重建环境
重建(rebuild) 环境就是在部署的时候，在生产环境安装好对应版本的软件包，不要出现版本兼容等问题:
pip install -r requirements.txt
配合pip，可以批量安装对应版本的软件包，快速重建环境，完成部署。

#不装anaconda安装jupyter notebook
命令行切换到 D:\Python34\Scripts目录下
窗口输入： pip install jupyter 
命令行窗口输入： jupyter notebook

jupyter notebook --generate-config 
打开“.jupyter”文件夹，可以看到里面有个配置文件。
修改jupyter_notebook_config.py配置文件
　　打开这个配置文件，找到“c.NotebookApp.notebook_dir=……”，把路径改成自己的工作目录。
## The directory to use for notebooks and kernels.
c.NotebookApp.notebook_dir = 'D:\PythonDev\jupyterCode'
这里有个前提，就是要配置Python34 的环境变量。方向如下：找到系统变量 path，编辑在最后加上 2 个路径，用分号隔开。
D:\Python34
D:\Python34\Scripts

1 pip install pandas
2 pip install jupyter
3 pip install keras
命令行输入:jupyter notebook 

#python一行命令开启http服务共享文件
一个可以非常方便实用的，用来共享文件或者临时测试的方式。实现一个微型的HTTP服务程序来说是很简单的事情，
在Python下，只需要一个命令行：
python -m SimpleHTTPServer

Python3的模块变了，Python3的用法：
python -m http.server 8000

这就行了，而python临时的HTTP服务在其默认的8000号端口上侦听。你会得到下面的信息：
Serving HTTP on 0.0.0.0 port 8000 ...

你可以打开你的浏览器，然后输入下面的IP+端口：
http: //IP:8000

如果你的目录下有一个叫 index.html 的文件名的文件，那么这个文件就会成为一个默认页，
如果没有这个文件，那么，目录列表就会显示出来。
