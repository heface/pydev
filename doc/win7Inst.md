HP620开机启动设置:(F10)
开机出现惠普LOGO的时候点F9，会出现快捷设置菜单，使用上下方向键选择CD/DVD选项，回车确认即可

1 firefox浏览器下载安装 http://www.firefox.com.cn/
	firefox下载插件 ->工具 -> 附加组件 ，查找安装 DownThemAll
2 notepad++编辑器下载安装 https://notepad-plus-plus.org/
3 anaconda下载安装 https://www.anaconda.com/  清华镜像站 https://mirror.tuna.tsinghua.edu.cn/help/anaconda/
*4 emacs下载安装 
*5 git下载安装 https://git-scm.com/downloads/
6 realplayer播放器下载 https://hk.real.com/windows/  https://hk.real.com/windows/
7 foxmail下载 https://www.foxmail.com/
8 virtualbox下载 https://www.virtualbox.org/wiki/Downloads
9 python下载 https://www.python.org/downloads/
10 manjaro Linux下载 https://manjaro.org/download/    清华镜像站 https://tuna.moe/    https://mirrors.tuna.tsinghua.edu.cn/
11 火绒安全 https://www.huorong.cn
12 IDM下载工具 http://www.internetdownloadmanager.com/
13 sogo输入法 https://pinyin.sogou.com/
14 小狼毫输入法 https://rime.im/
15 显卡驱动 https://www.geforce.com/drivers    https://www.geforce.cn/drivers  nvidia官网
16 显卡检测工具 https://www.techpowerup.com/download/techpowerup-gpu-z/
17 福昕pdf阅读器


 在使用jupyter进行编程时，初始化目录可能不是自己想要的目录，那么下面讲解修改成自己想要的目录。
1） 在命令行中输入jupyter notebook --generate-config，会产生一个配置文件
　　我的会显示Writing default config to: C:\Users\allen\.jupyter\jupyter_notebook_config.py这样的提示。 
2） 找到对应的文件，搜索c.NotebookApp.notebook_dir
　　将前面的#注释去掉，在后面填上自己想要设置的初始化目录。比如我设置成c.NotebookApp.notebook_dir = u'D:\chengxu\ML'
　　以后就会将'D:\chengxu\ML'这个目录成为初始化的目录。 在使用jupyter进行编程时，初始化目录可能不是自己想要的目录，那么下面讲解修改成自己想要的目录。
1） 在命令行中输入jupyter notebook --generate-config，会产生一个配置文件
　　我的会显示Writing default config to: C:\Users\allen\.jupyter\jupyter_notebook_config.py这样的提示。 
2） 找到对应的文件，搜索c.NotebookApp.notebook_dir
　　将前面的#注释去掉，在后面填上自己想要设置的初始化目录。比如我设置成c.NotebookApp.notebook_dir = u'D:\chengxu\ML'
　　以后就会将'D:\chengxu\ML'这个目录成为初始化的目录。


conda更改为国内镜像源:
(base) C:\Users\HP>conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free
(base) C:\Users\HP>conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
(base) C:\Users\HP>conda config --set show_channel_urls yes

1）conda list 查看安装了哪些包。
2）conda env list 或 conda info -e 查看当前存在哪些虚拟环境

1 创建Python虚拟环境。
     使用 conda create -n your_env_name python=X.X（2.7、3.6等） 
anaconda 命令创建python版本为X.X、名字为your_env_name的虚拟环境。
your_env_name文件可以在Anaconda安装目录envs文件下找到。

# 指定python版本为2.7，注意至少需要指定python版本或者要安装的包# 后一种情况下，自动安装最新python版本
conda create -n env_name python=2.7
# 同时安装必要的包
conda create -n env_name numpy matplotlib python=2.7
conda create -n aistudy pandas keras python=3.6
2 使用激活(或切换不同python版本)的虚拟环境。
    打开命令行输入python --version可以检查当前python的版本。
 使用如下命令即可 激活你的虚拟环境(即将python的版本改变)。
    Linux:  source activate your_env_name(虚拟环境名称)
    Windows: activate your_env_name(虚拟环境名称)
   这是再使用python --version可以检查当前python版本是否为想要的。
3 对虚拟环境中安装额外的包。
    使用命令conda install -n your_env_name [package]即可安装package到your_env_name中
4 关闭虚拟环境(即从当前环境退出返回使用PATH环境中的默认python版本)。
   使用如下命令即可。
deactivate env_name，也可以使用`activate root`切回root环境
Linux下使用 source deactivate 
5 删除虚拟环境。
移除环境
   使用命令conda remove -n your_env_name(虚拟环境名称) --all， 即可删除。
删除环境中的某个包。
   使用命令conda remove --name $your_env_name  $package_name 即可。

pip使用国内镜像源：
使用pip时在命令后面加上 -i参数，指定pip源
例: pip install scrapy -i https://pypi.douban.com/simple/
pip国内源：
	阿里：http://mirrors.aliyun.com/pypi/simple/
	中科大：https://pypi.mirrors.ustc.edu.cn/simple/
	清华：https://pypi.tuna.tsinghua.edu.cn/simple/



不安装anaconda，如何安装jupyter
命令行切换到 {PythonHome}\Scripts目录下
输入： pip install jupyter 
输入： jupyter notebook
jupyter notebook --generate-config 
打开“.jupyter”文件夹，可以看到里面有个配置文件。
修改jupyter_notebook_config.py配置文件
打开这个配置文件，找到“c.NotebookApp.notebook_dir=……”，把路径改成自己的工作目录。
## The directory to use for notebooks and kernels.
c.NotebookApp.notebook_dir = 'D:\PythonDev\jupyterCode'

前提，需要配置Python的环境变量。
如下：找到系统变量 path，编辑在最后加上 2 个路径，用分号隔开。
D:\Python36
D:\Python36\Scripts

安装python36时报错：计算机中丢失api-ms-win-crt-runtime-|1-1-0.dll
解决方案：
(1) 安装VC redit.exe
到微软官网下载这个软件：
    https://www.microsoft.com/zh-cn/download/details.aspx?id=48145
如果安装失败，请参照下面的博客的方法：
    http://blog.csdn.net/huqiao1206/article/details/50768481
(2) 安装KB2999226补丁程序
本人在上面的软件成功安装之后，依然没有解决问题，于是再次安装了下面这个补丁：
    Windows6.1-KB2999226-x64.msu   https://www.microsoft.com/zh-cn/download/details.aspx?id=49093
上面是64位的，32位的下载地址如下：
    Windows6.1-KB2999226-x86.msu   https://www.microsoft.com/zh-cn/download/details.aspx?id=49077
安装完这个补丁之后就解决问题了。
3 如何找补丁
如果你用的win10或者win8则要下载相应的补丁，找补丁的方法如下，先到微软官网：
    https://www.microsoft.com/zh-cn/download/details.aspx?id=49077
然后在搜索栏搜索补丁编号，根据自己的系统找到相应的补丁程序即可，如果要找64位的，则搜索 KB2999226 x64



如何从官网下载redhat enterprise iso镜像
1、登陆官网：www.redhat.com ，点击右上方的 LOGIN  。
当然网站会更新，总之找到登陆，如果你没有账号，就点击“register”注册一个，注意，是注册为“公司账户”！
填写注册信息：
注册完成后登陆，找到PRODUCTS（产品）选择Server（服务器）点击进入。
选择评估软件下载：
评估版本。就是有三十天的技术支持。点击“Download a free Red Hat Enterprise Linux 30-day evalution” 继续：
确认生成评估请求（我已经评估一次，所以提示existing，已存在。）点击“Back to Downloads”继续：
返回下载企业linux：
然后就可以看到各个版本的信息，找到自己需要的版本，点击进入，其中包含32位和64位，根据需求自行下载。


VirtualBox安装64位的系统需要满足以下条件：
1. 64位的cpu
2. cpu允许硬件虚拟化
先来看第一个条件，64位的CPU，这个嘛，现在的笔记本一般都是64位的了，所以不用担心，除非是好几年之间的电脑。如果你不清楚，可以打开命令行，输入systeminfo，在输出的信息中找到CPU这一行，如果是X86_64的，就是64位CPU；或者，也可以下载个CPU-Z软件查看（PS：这个软件很好用）。第一条分析完毕。
然后是第二条，是否开启CPU硬件虚拟化1，这个嘛，各大厂商的情况不大相同，有的电脑默认开启了（比如，我的HP），有的没有，所以需要自行开启，开启方法：开机时按某个键进入BIOS设置界面2。
然后，setup==>security==>cpu virtualization，将cpu virtualization这一项由Disable设置为Enable。保存，然后重启电脑，硬件虚拟化就开启成功了。
然后，按理说，经过这两步处理，VirtualBox中应该会出现64bit的选项了，然而，还是只有32位的选项，看来问题还真不是出在这里。
后面，又去查资料，终于发现了问题之所在，原来是因为Windows8.1自带的Hyper-V！我这个同学使用的是Win8.1系统，系统自带Hyper-V，这是微软自家的虚拟机软件。这么来说吧，VirtualBox和workstation与Hyper-v是可以共存的，但是，不是完美共存，Hyper-v是独占硬件虚拟化的，Windows 8.1下安装了Hyper-v后VirtualBox和VMware workstation是不能安装64位的操作系统的。这个问只会在Windows8.1/8上出现，Win7是不会出现这个问题的，因为Win7不自带Hyper-V！→_→
那么，我们就只要禁用Hyper-V就行了。禁用的步骤：
Ctrl+Shift+Esc，打开任务管理器： 
找到Hyper-V开头的8个服务，将Hyper-V虚拟机管理设置为手动开启，同时关闭该服务：
关闭Hyper-V之后，大功告成！
补充说明
1. 什么是硬件虚拟化？
硬件虚拟化其实就是CPU的虚拟化技术。intel的叫VT-x，amd的叫AMD-V。支持虚拟技术的CPU带有特别优化过的指令集来控制虚拟过程，通过这些指令集，VMM(Virtual Machine Monitor，虚拟机监视器)会很容易提高性能，相比软件的虚拟实现方式会很大程度上提高性能。虚 拟化技术可提供基于芯片的功能，借助兼容VMM软件能够改进纯软件解决方案。由于虚拟化硬件可提供全新的架构，支持操作系统直接在上面运行，从而无需进行 二进制转换，减少了相关的性能开销，极大简化了VMM设计，进而使VMM能够按通用标准进行编写，性能更加强大。
2. 如何判断是否支持硬件虚拟化呢？
Windows：
利用一个小工具 securable.exe 来帮助我们测试硬件对虚拟化技术的支持程度。我们程序运行结果中可以看到物理机支持 64 位运算，支持硬件 DEP，支持虚拟化技术。这样的结果表明我们可以放心测试 XP MODE，如果“ Hardware Virtualization ”显示的结果是“ Locked OFF ”，则表明 CPU 支持虚拟化技术，但主板的 BIOS 却禁止了对虚拟化的支持，这种情况我们就需要更改 BIOS 设定或升级 BIOS。如果三项检测结果中有一项显示了“NO”，那就表明您的硬件不能满足 XP MODE 的部署条件，就不用继续测试了。
Linux：
在Linux下，使用命令：grep -E ‘(vmx|svm)’ /proc/cpuinfo。如果有vmx或svm内容输出，则说明CPU支持虚拟化技术。
3. 安装还是出错，为什么呢？
新建虚拟电脑时，要安装64位的Ubuntu可是没有对应选择64位，更改设置即可。这里还要注意一点：要打开VirtualBox的vt-x/amd-v设置，这个其实会自动打开。重新安装，大功告成了！
还有一点，在上面所有操作都昨做完之后，最好重启一次，以免再次出错！


git获取源码:
git clone git@github.com:heface/pydev

jupyter修改端口和IP地址
jupyter notebook --no-browser --port 6000 --ip=192.168.1.103


#firefox更新问题
1 
{
    "policies": {
        "AppUpdateURL": "none",
        "DisableAppUpdate": true,
        "DisableFirefoxStudies": true,
        "DisableSystemAddonUpdate": true,
        "DisableTelemetry": true,
        "ExtensionUpdate": false
    }
}

将以上内容保存为polices.json, 再创建一个distribution目录, 移动polices.json到distribution中, 并放置在firefox安装目录, 即可 
https://github.com/mozilla/policy-templates/blob/master/README.md

2 
hosts文件末尾添加

---------------------------------------------------------------分割线
127.0.0.1     aus6.mozilla.org
127.0.0.1     aus5.mozilla.org
127.0.0.1     aus4.mozilla.org
127.0.0.1     aus3.mozilla.org
127.0.0.1     aus2.mozilla.org
---------------------------------------------------------------分割线

62.0.3测试可以屏蔽更新 

3 
彻底关掉更新的方法是安装esr版本，先安装esr版，打开esr版，再卸载掉正式版就可以无缝转换了，配置文件都在,选项里久违的never check for updates 又出现了。 