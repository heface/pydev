#Linux使用技巧
[toc]
S
##1. 更新系统
由于linux默认apt源为国外源，网速太慢，所以不建议使用默认apt源，建议使用国内源。  
备份原文件：sudo cp /etc/apt/sources.list /etc/apt/sources.list.buckup  
编辑原文件：sudo gedit /etc/apt/sources.list  
国内源可以换成清华的，文件里保存的具体内容可以访问链接https://mirrors.tuna.tsinghua.edu.cn/help/ubuntu/，根据Linux版本选择对应的文件内容，  
如版本选择的是Ubuntu18.04 LTS，内容如下：  
```
# 默认注释了源码镜像以提高 apt update 速度，如有需要可自行取消注释
deb https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ bionic main restricted universe multiverse
# deb-src https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ bionic main restricted universe multiverse
deb https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ bionic-updates main restricted universe multiverse
# deb-src https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ bionic-updates main restricted universe multiverse
deb https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ bionic-backports main restricted universe multiverse
# deb-src https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ bionic-backports main restricted universe multiverse
deb https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ bionic-security main restricted universe multiverse
# deb-src https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ bionic-security main restricted universe multiverse
# 预发布软件源，不建议启用
# deb https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ bionic-proposed main restricted universe multiverse
# deb-src https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ bionic-proposed main restricted universe multiverse
```

第一件事情是重中之重，就是让系统保持时刻最新，终端中运行以下命令。  
    $ sudo apt-get update  
    $ sudo apt-get upgrade  
或者，你也可以使用更新管理器（mintUpdate）来干这事，你可以在菜单（Menu）> 管理（Administration）中找到它。

##2.安装常用工具
    $ sudo apt-get vim
    $ sudo apt-get emacs
    $ sudo apt-get retext
    $ sudo apt-get tldr
    $ sudo apt-get git

##3.配置git并获取最新代码
一 、
设置Git的user name和email：  
$ git config --global user.name "heface"  
$ git config --global user.email "heface@163.com"  

二、生成SSH密钥：  
1.查看是否已经有了ssh密钥：cd ~/.ssh  
如果没有密钥则不会有此文件夹，有则备份删除  
2.生成密钥：  
```
$ ssh-keygen -t rsa -C “email@email.com”
按3个回车，密码为空。
（email@email.com是github的账号，即上面的email）

Your identification has been saved in /home/tekkub/.ssh/id_rsa.
Your public key has been saved in /home/tekkub/.ssh/id_rsa.pub.
The key fingerprint is:
………………
```
最后得到了两个文件：id_rsa和id_rsa.pub

3.添加id_rsa密钥到ssh，命令为：ssh-add 文件名  
   如果出现error：Could not open a connection to your authentication agent.  
   则先执行：$ssh-agent bash  
   然后再执行：$ssh-add id_rsa  
   
4.在github上添加ssh密钥，这要添加的是“id_rsa.pub”里面的公钥。  
打开https://github.com/ ，登陆，复制id_rsa.pub里面的内容添加ssh。  
如果直接从Linux上复制id_rsa.pub的内容，可能会复制里面的换行符，而key是没有换行符的，直接复制可能会出现下面的错误提示：  
```
Key is invalid
Fingerprint has already been taken
Fingerprint cannot be generated
```
解决方案：  
       $cat id_rsa.pub  
然后复制里面的内容，就OK了！  
5.测试：ssh git@github.com  连接成功！
```
PTY allocation request failed on channel 0
Welcome to GitLab, ***!
Connection to github.com closed.
```

三、 开始使用github  
1.获取源码(在本地创建一个目录，进入目录git clone)：  
$ git clone git@github.com:heface/pydev.git  
其他git使用不再详述。  

##2. 多安装些浏览器
Linux Mint 17默认安装了firefox，你也可以获得更多的浏览器，如Chronium和Google Chrome。  
Chronium浏览器可以在仓库中获取。  
    $ sudo apt-get install chromium-browser  
至于Google Chrome，请访问google.com/chrome下载deb包，并使用gdebi来安装。  
```
    # 64 位
    $ wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
    $ sudo gdebi google-chrome-stable_current_amd64.deb     
    # 32 位
    $ wget https://dl.google.com/linux/direct/google-chrome-stable_current_i386.deb
    $ sudo gdebi google-chrome-stable_current_i386.deb
```
##3. 安装多媒体解码
受限的额外包可以帮你安装大多数基本的解码，可以让你播放像mp3这样的格式。它也会帮你安装微软字体。  
    $ sudo apt-get install ubuntu-restricted-extras

要启用加密dvd的回放，请安装以下包。  
    $ sudo apt-get install libdvdread4
    $ sudo /usr/share/doc/libdvdread4/install-css.sh

##4. 安装专有驱动
如果你有一张Nvidia或者ati的图形卡，或者broadcom的无线网卡，那么请安装厂商提供的专有驱动，这些驱动会为你带来最佳的硬件性能。  
要安装Nvidia驱动，你可以参照先前的这篇文章 ：如何在Linux Mint上安装最新的Nvidia驱动（http://www.binarytides.com/install-nvidia-drivers-linux-mint-16/）

##5. 安装Dropbox
Linux mint仓库已经提供了dropbox的客户端软件包，所以你不必满世界找了。
    $ sudo apt-get install dropbox python-gpgme
如果你还是比较喜欢从官方网站下载，那么翻墙可直达https://www.dropbox.com/install?os=lnx，请遵照说明下载用于Ubuntu的deb安装包。（LCTT译注：墙内用户还是忽视此条吧。）
Copy是另外一个云存储解决方案，它也有本地Linux客户端。详情可查阅copy.com，它也有ppa仓库。

##6. 安装rar和其它归档工具
要想在Nemo这样的文件管理器中通过上下文菜单创建rar归档，请安装rar工具。安装rar的同时，也可安装其它几个包以增加对其它归档格式的支持。
    $ 
    
##7. 安装剪贴板管理器
剪贴板管理器允许你维护和访问通过像Ctr+C这样的操作拷贝的项目历史，gnome下有很多的剪贴板管理器，像diodon，clipit，glipper，parcellite。  
Diodon在cinnamon桌面上似乎存在一些问题，在历史列表增长时会出现滚动条。Clipit和Gipper工作得很好，你也可以安装
```
    $ sudo apt-get install glipper
    # 或者
    $ sudo apt-get install clipit
```
然后，你可以从应用程序菜单中启动它们，它们应该会在你每次登录时启动。

##8. 修改Firefox的搜索引擎
你也许注意到，Firefox默认选择了Yahoo搜索引擎，而搜索引擎列表中并没有Google。点击“管理搜索引擎” > 获取更多搜索引擎，它会带你去 http://www.linuxmint.com/searchengines.php。  
向下拉动滚动条到商业搜索引擎部分，找到并点击Google图标。进入下一页后，再次点击搜索引擎列表，而这次你会看到“添加Google”选项，点击它就可以用上Google搜索了。（LCTT译注：墙内用户也请忽略此条。怒！）

##9. Uget下载管理器
Uget是一个简洁而健壮的跨平台下载管理器，在Linux上工作得很好。虽然它缺少分段下载文件功能，但是仍然是一个十分稳定的下载管理器。  
$ sudo apt-get install uget

##10. Deluge BitTorrent客户端
Linux Mint自带了Transmission，这是个简洁而高效的torrent客户端。如果正在寻找一个更有特色的torrent客户端，那么你可以试试deluge或者vuze（正式名称是azureus），还可以试试qbittorent。  
$ sudo apt-get install deluge-torrent

##11. Hardinfo - 系统信息工具
Hardinfo是一个十分便利的GUI工具，它可以用来报告大量完整的系统硬件信息。你可以通过它来集中查看处理器、内存、存储设备、网络配置、打印机、usb设备、声音/视频适配器等等信息。它具有测试和评估系统性能的功能。  
$ sudo apt-get install hardinfo

##12. 安装MATE桌面环境
除了Cinnamon，Linux Mint还自带了另一个流行的桌面环境MATE（Maatay）桌面。如果你想试试，那么就来安装吧。  
现在你可以在登陆屏幕选择MATE会话了。  
$ sudo apt-get install mint-meta-mate

##13. 让其它分区可写
如果你有其它ext分区，比如想用来存储和备份文件，那么你需要让它们可写，以免每次都要使用root特权。
首先，使用gksudo在文件管理器里打开分区挂载目录  
$ gksudo nemo
导航到分区目录，右击去往属性 > 权限标签  
赋予“目录访问” - 创建和删除文件权限给用户、组和其它。  
赋予“文件访问” - 读和写权限给用户、组和其它。  
对于NTFS分区，你不需要做此事。  

##14. 安装Conky
Conky是一个轻量级系统监控工具，它通过桌面图形组件显示系统各种资源的统计数据，如cpu、内存、网络等。它不是必须的，但是可以让你的桌面更加绚丽夺目。  
从应用程序菜单启动Conky管理器，并添加组件到桌面。也可以选中开机启动选项来让Conky开机启动。  
```
    $ sudo apt-add-repository -y ppa:teejee2008/ppa
    $ sudo apt-get update
    $ sudo apt-get install conky-manager
```
##清除
做完这一切后，请为系统进行一次大扫除，移除一些不必要的包。
$ sudo apt-get autoremove

##更多应用程序
如果你正在为你的Mint盒子寻找更多的应用程序，那么这里列出了一部分更好的应用程序，所有这些都可以在软件管理器中安装。
    Opera - 网页浏览器pt
    Gnome Encfs Manager - 管理使用Encfs加密的文件和文件夹
    Smplayer - 多媒体播放器
    Rhythmbox, Clementine - 音乐播放器
    Openshot, Kdenlive - 视频编辑器
    Audacity - 音频编辑器
    Inkscape - 图形和图像编辑
    Gparted - 分区编辑器
    Gufw - 防火墙配置工具
    qBittorrent, Vuze - Torrent客户端
    Gwenview - 图像浏览
    Team viewer - 远程桌面
    Tv-maxe - 查看电视频道
    Grub Customizer - 修改GRUB启动菜单设置
    Linrunner TLP - 电源管理工具，对笔记本节电很有用
    Virtualbox - 虚拟化
    Kazam, recordMyDesktop - 桌面录像/演示
    Bleachbit - 通过删除旧的/临时文件释放磁盘空间
    Cheese - 使用网络摄像头拍照
    Shutter - 带有众多功能的屏幕截图工具

那么，请选择你喜欢的那些，并尽情享受Linux Mint吧！！


##1. 字体，永久的话题
    18.2默认安装的时楷体，而且这个楷体看着很不舒服，不知道是不是国外的人搞得，他们不适用中文，也没有看过中文状态下的样子
    开搞：
        先下载微软的微软雅黑，字体网站很多，18.2双击后点击安装，然后到到首选项》外观》字体中去设置，最后一个等宽可以使用 YaHei Consolas Hybrid 字体。我设置的尺寸位12，屏幕分辨率位1920*1080 15.6寸，所以看着正好
        设定好后可以注销或重启一下，不重启可能有些界面或浏览器无法获取到最新的字体设置
        这样设定后看上去就舒服多了，以前17.3时很嫌弃，但是当时 搜商 不行

##2. 输入法
输入法 17.3时 ibus有 google拼音，挺好用的，这次的版本中去除了，那个sun..不太好用，所以去下载了 搜过拼音，安装很简单，deb包都会自动将依赖安装好，双击就可以搞定，不够首先要去 首选项》输入法》安装简体中文，之后会自动安装fcitx和ibus，选择fcitx即可，安装好搜狗输入法后再fcitx设置中设置出来就可以了，无广告，真是良心之作啊

##3. 安装顺手的app

我常用的应用有一下几款：

    wps：文字处理，兼容office，再Windows下我也使用wps，要到wps网站上去下载
    #sudo apt-get install wps-office 注：下载并安装wps-office。
    calibre：gitbook上的书可以下载epub格式的，用这个看很不错，系统自带的被我卸载了，叫什么不记得了，这个软件直接在软件管理器搜索就有
    网易云音乐：音乐软件，百度搜索网易云音乐，下载linux版本就行
    visual studio code：代码编辑器，可以代替好多软件，简单写写代码还是不错的，很多人将他直接作为IDE使用
    phpstorm：php web应用开发神器 (1)
    webstorm：web前端和node开发，真是神器(2)
    pyCharm ：python开发神器(3)
    以上三款都出自 jetbeans公司，要去官网下载，搜索一下吧，感谢为我们带来这么好的软件，用支付宝就能购买正版，pyCharm有社区版免费的，我就用这个，够了。
    Remmina：远程桌面连接，可以控制Windows服务器，好用，软件管理器就有
    filezilla：FTP软件，软件管理器就有
    virtualbox：虚拟机，偶尔运行一下 xp win7 等可以用用，到网站上去下载最新版本的，顺便再去下扩展包
    Chrome：谷歌浏览器
    f.lux：屏幕色温调节，据说护眼的，官网有源，添加后就能apt了
    copyQ：剪辑版管理软件，以后复制文本图片时就不需要纠结是不是剪辑版内还有内容，官网下载
    shutter：截图软件，不错的，强大，软件管理器有
    坚果云：类似云盘，不过比较小，免费版每月可以上传1G资料，付费挺贵的，不过稳定安全第一么
    TomBoy：便签软件，系统自带，简单到爆，同步可以设置本地文件夹，我设置了坚果云同步目录，Windows平台也有，就可以同步了
    Gpick：拾取颜色用的
    Meld：文件对比工具，堪比Windows系统下的BeyondCompare收费软件，软件管理器有
    Pluma：文本文档编辑器，自带着色功能，默认位xed，应该都是从gedit源码编译过来的吧，长得都一样
    系统自带的好用软件还有：VLC、Firefox、GIMP

##4. 添加几个面板

    使用linuxmint的一个原因就是他的自由度非常大，不像Windows和Ubuntu，可调性太差
    Windows有且仅有一个任务栏，就是屏幕底部的那条，而且开始菜单越来越难用，越来越乱，再Windows系统下装了个rolan启动器，最近又搞强制更新，新版还不如旧版本好用，太恶心了
    在18.2下 MATE 面板程序 依然好用，给屏幕添加了三条，底部左侧一条放软件启动器（快捷图标），右侧放时间和托盘，还有多桌面切换器，顶部一条放当前的 窗口集合 、 显示桌面图标、笔记本温度传感指示器
    多个任务栏真心好用，如果Windows也有这样的原生软件就好了，而且linuxmint的多桌面真心不错，比目前的Windows10多桌面还要好，直接可以在指示器中拖动窗口到不同的桌面


#Wine

##安装Wine（来自官方安装命令）
1、对于64位系统，添加 32 位架构支持（对于32位的，似乎可以忽略此命令，不过加上也没有错）
终端下执行：sudo dpkg --add-architecture i386

2、添加软件源
终端下逐条执行（默认当前路径为～，执行以下命令过程中，请勿切换路径）：
sudo wget -nc https://dl.winehq.org/wine-builds/Release.key
sudo apt-key add Release.key
sudo apt-add-repository https://dl.winehq.org/wine-builds/ubuntu/

3、更新
终端下执行：sudo apt update
报错：
错误:13 https://dl.winehq.org/wine-builds/ubuntu bionic InRelease
  由于没有公钥，无法验证下列签名： NO_PUBKEY 76F1A20FF987672F
正在读取软件包列表... 完成    
W: GPG 错误：https://dl.winehq.org/wine-builds/ubuntu bionic InRelease: 由于没有公钥，无法验证下列签名： NO_PUBKEY 76F1A20FF987672F
E: 仓库 “https://dl.winehq.org/wine-builds/ubuntu bionic InRelease” 没有数字签名。
N: 无法安全地用该源进行更新，所以默认禁用该源。
解决：
sudo apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 76F1A20FF987672F
4、安装Wine
终端下执行：
稳定版：sudo apt install --install-recommends winehq-stable
开发版：sudo apt install --install-recommends winehq-devel
阶段版：sudo apt install --install-recommends winehq-staging
成功安装后，Wine对应的将安装到 /opt/winehq-stable，或/opt/wine-devel，或/opt/wine-staging路径下。（就个人而言，推荐安装稳定版，对于喜欢追求最新功能的网友，也可选择开发版或阶段版）


#办公软件-LibreOffice
1 install LibreOffice module:
yum install LibreOffice
2 select openoffice module
module add openoffice/4.0.4
3 view word/pdf document
soffice <file_name>
4 convert to pdf document
soffice --convert-to pdf:writer_pef_Export <word_file_name>


sudo add-apt-repository ppa:libreoffice/libreoffice-prereleases
sudo apt-get update
sudo apt-get install libreoffice libreoffice-style-breeze
LibreOffice 4.x 升级到 5.x 方法：

sudo apt-get dist-upgrade

#图像软件-FIM
##安装 FIM
基于 DEB 的系统，如 Ubuntu、Linux Mint， 可从默认的仓库中获取 FIM 图像查看器。因此，你可以使用如下命令安装fbi：
$ sudo apt-get install fim
如果它在你使用的 Linux 发行版的仓库中不包含 FIM，则可以下载源代码进行编译和安装，如下所示。
wget http://download.savannah.nongnu.org/releases/fbi-improved/fim-0.6-trunk.tar.gzwget http://download.savannah.nongnu.org/releases/fbi-improved/fim-0.6-trunk.tar.gz.siggpg --search 'dezperado autistici org'＃按照屏幕上的说明，从密钥服务器导入密钥
gpg --verify fim-0.6-trunk.tar.gz.sig

tar xzf fim-0.6-trunk.tar.gzcd fim-0.6-trunk./configure --help=short＃阅读./configure --help=short 的输出：你可以在 ./configure 中添加选项./configuremake
su -c“make install”

##FIM用法
安装完成后，您可以使用以下命令以“自动缩放”显示的图像：
$ fim -a dog.jpg

如果当前目录中有多个 .jpg 文件，可以使用通配符打开所有文件，如下所示。
$ fim -a * .jpg

要打开目录中的所有图像，例如 Pictures，请运行：
$ fim Pictures/

我们也可以在文件夹及其子文件夹中递归地打开图像，然后像下面那样对列表进行排序。
$ fim -R Pictures/ --sort

要以 ASCII 格式渲染图像，可以使用 -t 标志。
$ fim -t dog.jpg

要退出 Fim，请按 ESC 或 q。

##键盘快捷键

您可以使用各种键盘快捷键来管理图像。例如，要加载下一张图像和之前的图像，请按下 PgUp / PgDown 键。成倍放大或缩小，请使用 + / - 键。以下是用于在FIM中控制图像的常用按键。
    PageUp / Down：上一张/下一张图片
    + / - ：放大/缩小
    a：自动缩放
    w：自适应宽度
    h：自适应高度
    j / k：平移/向上
    f / m：翻转/镜像
    r / R：旋转（顺时针/逆时针）
    ESC / q：退出

有关完整详细信息，请参阅手册页。
$ man fim

##安装Wine依赖环境
1、安装winetricks（Wine的辅助配置工具，超级便利）
终端下执行：sudo apt install --install-recommends winetricks

2、安装字体（解决Wine及初始配置界面乱码）
刚安装完Wine后，初始执行界面一般会出现诸如问号方块之类的乱码，为了便于阅读，需完善安装缺失的默认字体。
将以下simfang.ttf、simhei.ttf、simkai.ttf、simsun.ttc字体文件复制到Wine安装路径下的字体目录/opt/wine-stable/share/wine/fonts即可，你也可以将更多字体复制到该目录下。
就我个人而言，我将以上字体文件及微软雅黑字体文件msyh.ttf、msyhbd.ttf 复制到 Wine 字体目录即解决了界面乱码的问题。
sudo cp /usr/share/fonts/simfang.ttf /opt/wine-stable/share/wine/fonts
sudo cp /usr/share/fonts/simhei.ttf /opt/wine-stable/share/wine/fonts
sudo cp /usr/share/fonts/simkai.ttf /opt/wine-stable/share/wine/fonts
sudo cp /usr/share/fonts/simsun.ttf /opt/wine-stable/share/wine/fonts  --cp: 无法获取'/usr/share/fonts/simsun.ttf' 的文件状态(stat): 没有那个文件或目录
sudo cp /usr/share/fonts/msyh.ttf /opt/wine-stable/share/wine/fonts
sudo cp /usr/share/fonts/msyhbd.ttf /opt/wine-stable/share/wine/fonts

3、安装Wine依赖
一般而言，安装完Wine后，初始执行winecfg或wine或winetricks，会要求下载安装 wine-mono 和 wine-gecko，这是一个相对漫长的过程，并且中途还可能出错，有可能需要反复多次才能下载安装成功。这些依赖文件是下载安装在：~/.cache/wine 目录下的。
在此，我提供一个快速的解决办法：从其它人那里获取或用快速下载工具直接下载下来后，复制到 ~/.cache/wine 路径下即可，如果目录不存在，请自行创建。
最好是将包含wine-mono和wine-gecko的wine目录直接复制到~/.cache/下，合并或覆盖wine目录。

4、安装Wine中Windows程序依赖
在此处，必须借助winetricks这个强大的辅助工具了。
你可以在终端下执行 winetricks，在界面中选择相关的依赖库，但相对快捷的是直接将所需依赖作为参数传递给 winetricks ，如下：（对于网络上网友提供的安装方式，本人实际经验是逐个安装有更高的成功率）
终端下分别执行：
winetricks corefonts colorprofile
winetricks fontfix fontsmooth-gray fontsmooth-rgb fontsmooth-bgr
winetricks gdiplus
winetricks d3dx9
winetricks riched20 riched30
winetricks mfc40 mfc42
winetricks vcrun6 vb6run vcrun2003 vcrun2005 vcrun2008
winetricks msxml3 msxml4 msxml6

'''
---winetricks riched20 riched30---
Executing w_do_call msls31
Executing load_msls31 
Executing mkdir -p /home/he/.cache/winetricks/msls31
Executing cd /home/he/.cache/winetricks/msls31
Downloading ftp://ftp.hp.com/pub/softlib/software/msi/InstMsiW.exe to /home/he/.cache/winetricks/msls31
--2019-09-29 04:08:07--  ftp://ftp.hp.com/pub/softlib/software/msi/InstMsiW.exe
           => “InstMsiW.exe”
正在解析主机 ftp.hp.com (ftp.hp.com)... 15.73.48.57, 15.72.188.128
正在连接 ftp.hp.com (ftp.hp.com)|15.73.48.57|:21... 已连接。
正在以 anonymous 登录 ... 登录成功！
==> SYST ... 完成。    ==> PWD ... 完成。
==> TYPE I ... 完成。  ==> CWD (1) /pub/softlib/software/msi ... 完成。
==> SIZE InstMsiW.exe ... 1822848
==> PASV ... 
服务器响应时发生错误，正在关闭控制连接。
'''
'''
---winetricks mfc40 mfc42---
Executing load_msls31 
Executing cd /home/he/.cache/winetricks/msls31
Downloading ftp://ftp.hp.com/pub/softlib/software/msi/InstMsiW.exe to /home/he/.cache/winetricks/msls31
--2019-09-29 04:12:04--  ftp://ftp.hp.com/pub/softlib/software/msi/InstMsiW.exe
           => “InstMsiW.exe”
正在解析主机 ftp.hp.com (ftp.hp.com)... 15.72.236.27, 15.73.208.135
正在连接 ftp.hp.com (ftp.hp.com)|15.72.236.27|:21... 已连接。
Error in server response. Closing.
重试中。
'''


一般来说，以上依赖也够了，对于其它的依赖，请自行再安装。
这些依赖，将会下载安装到：~/.cache/winetricks
下载和安装将会花费不少时间，中途还可能出现各种问题，还需要反复多次才能成功，在此，分享一个最快速的方法：
即：从其它网友处获取这些依赖或用下载工具下载后复制到该目录下，便能省却过程中的诸多烦恼。
最好是将整个winetricks目录复制到~/.cache/下，合并或覆盖winetricks目录。
特别注意：以复制方式下载安装，是省却了下载过程中的诸多问题，仍然需要执行以上winetricks命令，将依赖信息合并到Windows的注册表中，路径是在：~/.wine，
另外，对于Windows应用程序所需的字体，是保存在：~/.wine/drive_c/windows/Fonts 路径中，你可以自行将所需的字体文件复制到该目录下即可。

注：终端下执行 sh winetricks 弹出窗口中选择，也可完成安装。

5、Wine设置
在终端下执行：winecfg，即可打开wine设置窗口界面。
Wine安装使用（适用Linux Mint 19与Ubuntu 18.04下）
6、至此，Wine 就完成了比较完善的安装了，就可以根据自己的喜好安装Windows应用程序了。
7、通过Wine安装Windows应用程序有多种方式，一般来说，可以通过鼠标右键点击Windows应用程序，在右键菜单中选择Wine来安装，但更推荐的方式是以Wine添加-删除程序去完成，如下：
终端下执行：wine uninstaller
Wine安装使用（适用Linux Mint 19与Ubuntu 18.04下）
稍等即可出现添加-删除程序的界面，如下：
通过界面中的“安装”按钮选择待安装的应用程序，根据安装向导逐步完成安装。


##其他说明
1，wine会创造一个虚拟的windows环境，默认在主目录的~/.wine/下(是隐藏目录)，并且可以通过winecfg设置其他盘符。
2，安装软件时，会牵扯到依赖关系问题，因为wine不能提供所有的dll文件和ocx文件，而且wine提供的有些dll文件和ocx文件功能不全，所以有些程序能够正常运行，有些程序会出现这样那样的问题，这时需要借助depends这样的工具分析依赖关系，并且拷贝windows下的文件到虚拟c盘，然后通过winecfg设置库文件为native来解决。
3，COM+、ODBC、ADO等问题：有些软件（特别是行业管理软件和erp软件）需要访问数据库，或者访问应用服务器，就牵扯到这些问题了，这时，就需要wine-doors等工具处理了，在这一点上我失败了。
4，drix 3d问题：wine自带drix3d，但是功能不全，有时需要拷贝d3d开头的dll文件到虚拟c盘window/system32下面去。
5，最复杂的加密狗等硬件访问问题：我碰到了，需要安装硬件驱动，不知道如何解决。

QQ删除
1 进入qq目录，wine uninstall.exe  ；也可以直接在终端下输入:uninstaller
2 rm -rf ~/.local/share/applications/wine/

玩大航海，设置如下:
wine regedit d3d.reg
应用程式里面设置为 windows 2008R2(其他系统没测试过)
apt-get install winetricks
①winetricks dotnet40(如果卡住了,参考[1])
②winetricks -q vcrun6 vcrun6sp6
③sanwinetricks里面安装vcrun2012以及vcrun2012
①②③不确定是否绝对必要,因为我也是自己摸索出来的,在摸索的过程中安装了这三项,所以就记录了下来.

另外,必须全路径为英文

最后启动方法是:
wine DK4PK.exe

#Linux环境WPS安装
1.安装
下载地址：http://community.wps.cn/download/（去WPS官网下载）
执行安装命令：
sudo dpkg -i wps-office_10.1.0.5672~a21_amd64.deb
2.启动WPS for Linux后，出现提示"系统缺失字体" 。
出现提示的原因是因为WPS for Linux没有自带windows的字体，只要在Linux系统中加载字体即可。
具体操作步骤如下：
下载缺失的字体文件，然后复制到Linux系统中的/usr/share/fonts文件夹中。
国外下载地址：https://www.dropbox.com/s/lfy4hvq95ilwyw5/wps_symbol_fonts.zip
国内下载地址：https://pan.baidu.com/s/1eS6xIzo
下载完成后，解压并进入目录中，继续执行：
sudo cp * /usr/share/fonts
执行以下命令,生成字体的索引信息：
sudo mkfontscale
sudo mkfontdir
运行fc-cache命令更新字体缓存。
sudo fc-cache
重启wps即可，字体缺失的提示不再出现。

#Linux版WPS缺失字体解决方案
1 网上下载字体文件（多为百度网盘）
2 使用windows系统的字体文件
WIN7的字体安装路径：C:\Windows\Fonts，安装完成后重启WPS即可使用新安装的字体。
一、准备字体文件
windows的字体一般存放在c:/windows/fonts目录下，拷贝到linux下的字体有：
simfang.ttf 仿宋体
simhei.ttf 黑体
simkai.ttf 楷体
simsun.ttf 宋体和新宋体，原文件名simsun.ttc
tahoma.ttf tahoma字体
tahomabd.ttf tahoma字体的粗体形式
verdana.ttf verdana字体
verdanab.ttf verdana字体的粗体形式
verdanai.ttf verdana字体的斜体形式
verdanaz.ttf verdana字体的粗体＋斜体形式
拷贝过来的字体文件放在了/home/fwolf/tools/fonts目录下。
二、将字体加入到linux的可使用字体中
首先把字体文件链接到存放字体的目录中
cd /usr/share/fonts
ln -s /home/fwolf/tools/fonts xpfonts
cd xpfonts
mkfontscale
mkfontdir
这样作和把字体拷贝到/usr/share/fonts的一个目录下的效果是一样的。后面的两个mkfont命令是生成xpfonts目录下所包含的字体的索引信息。然后运行fc-cache命令更新字体缓存：
fc-cache

字体文件下载地址：https://pan.baidu.com/s/1cvrwCim8XUu_5b-ecL4BDg
https://www.dropbox.com/s/lfy4hvq95ilwyw5/wps_symbol_fonts.zip
解压后将整个wps_symbol_fonts目录拷贝到 /usr/share/fonts/ 目录下，注意wps_symbol_fonts目录要有可读可执行权限。
1、权限设置，执行命令如下
   #cd /usr/share/fonts/
   #chmod 755 wps_symbol_fonts
   #cd /usr/share/fonts/wps_symbol_fonts
   #chmod 644 *
2、生成缓存配置信息，进入字体目录
   #cd /usr/share/fonts/wps_symbol_fonts
   #mkfontdir
   #mkfontscale
   #fc-cache 

注：复制windows字体（fonts.zip）后，提示缺失MT Extra字体，下载MTExtra.zip并解压到/usr/share/fonts，执行fc-cache解决。

#LinuxMint设置apt源
1 点击菜单，点击首选项。
2 点击系统设置，点击软件源。
3 输入一个密码，然后点国旗这里。
4 选择为国内的上海，点击应用。
5 全部修改为国旗，然后点击确定，等待它自动更新就可以。


#Linux下操作json文件神器jq
##1 安装使用
yum install jq -y
apt install jq -y
查看一个 file.json 格式文件
$>jq . file.json

##2 JSON
(JavaScript Object Notation, JS 对象简谱) 是一种轻量级的数据交换格式。
简洁和清晰的层次结构使得 JSON 成为理想的数据交换语言。易于人阅读和编写，同时也易于机器解析和生成，并有效地提升网络传输效率。

JSON 语法格式：
JSON的结构基于这两点: "键/值对" ,
在不同的语言中,它可以被理解为对象(object)，记录(record)，结构(struct)，字典(dictionary)，哈希表(hash table)，键列表(keyed list)等 .
值的有序列表 多数语言中被理解为数组(array)

##3 JSON的基础结构说明：

对象是属性、值的集合。一个对象开始与”{” ,结束于”}”。每一个属性名和值间用”:”分隔。每个属性间用”，”分隔。
值可以是字符串，数字，逻辑值，数组，对象，null。 
数字：整数或浮点数 
字符串：在双引号中 
逻辑符：true和false 
数组：在方括号中 
对象：在花括号中 
null： 代表空

##4 JSON 键/值对
JSON 键值对是用来保存 JS 对象的一种方式，和 JS 对象的写法也大同小异，键/值对组合中的键名写在前面并用双引号 "" 包裹，使用冒号 : 分隔，然后紧接着值：
{"firstName": "Json"}
这很容易理解，等价于这条 JavaScript 语句：
{firstName : "Json"}

##5 JSON 与 JS 对象的关系
很多人搞不清楚 JSON 和 Js 对象的关系，甚至连谁是谁都不清楚。其实，可以这么理解：
JSON 是 JS 对象的字符串表示法，它使用文本表示一个 JS 对象的信息，本质是一个字符串。
如：
var obj = {a: 'Hello', b: 'World'}; //这是一个对象，注意键名也是可以使用引号包裹的
var json = '{"a": "Hello", "b": "World"}'; //这是一个 JSON 字符串，本质是一个字符串

JSON 和 JS 对象互转
要实现从对象转换为 JSON 字符串，使用 JSON.stringify() 方法：
var json = JSON.stringify({a: 'Hello', b: 'World'}); //结果是 '{"a": "Hello", "b": "World"}'

要实现从 JSON 转换为对象，使用 JSON.parse() 方法：
var obj = JSON.parse('{"a": "Hello", "b": "World"}'); //结果是 {a: 'Hello', b: 'World'}

##6 jq 命令允许直接在命令行下对JSON进行操作，包括分片、过滤、转换。
jq 命令的格式:
jq [options] filter [files]
options：
--version：输出jq的版本信息并退出
--slurp/-s：读入整个输入流到一个数组。
--raw-input/-R：不作为JSON解析，将每一行的文本作为字符串输出到屏幕。
--null-input/ -n：不读取任何输入，过滤器运行使用null作为输入。一般用作从头构建JSON数据。
--compact-output /-c：使输出紧凑，而不是把每一个JSON对象输出在一行。
--colour-output / -C：打开颜色显示
--monochrome-output / -M：关闭颜色显示
--ascii-output /-a：指定输出格式为ASCII
-raw-output /-r ：如果过滤的结果是一个字符串，那么直接写到标准输出（去掉字符串的引号）

filter：
. : 默认输出
.foo: 输出指定属性，foo代表属性。
.[foo] ：输出指定数组元素。foo代表数组下标。
.[]：输出指定数组中全部元素
， ：指定多个属性作为过滤条件时，用逗号分隔
| ： 将指定的数组元素中的某个属性作为过滤条件

files：
JOSN格式文件。

##7 格式化Json
cat json_test.txt
{"name":"WuDi","location":{"street":"ZhongShanLu","city":"BeiJing","age":"26","country":"CN"},"employees":[{"name":"Mark","division":"DevOps"},{"name":"Lucy","division":"HR"},{"name":"Elise","division":"Marketing"}]}

上面的JSON是PHP json_encode之后，echo出来的字符串，很明显，可读性太差。前一阵子写文档，需要将前后段JSON写入文档，我当时是用网上的JSON格式化工具做的。事实上，jq就可以检查JSON的合法性，并把JSON格式化成更友好更可读的格式：
cat json_test.txt | jq .

#linux常用命令

pwd date who last
ls -al   -a 显示隐藏文件， -l详细信息
cd
mkdir -p 递归创建
rmdir
rm -rf  -r 递归删除 -f强制删除
mv 修改文件名 移动
touch
echo "I am ralap" > 1.txt
echo "hello" >> 1.txt 追加
vi a 光标后开始插入
A 该行最后插入
I 在该行最前插入
gg 文件首行
G 未行
5dd 删除5行
3yy 复制3行
p 粘贴
v 进入选择模式，按y复制，p复制
%s/asd/111  查找文件所有asd，替换为111
/love 查找出现的love，按n下一个，N上一个
rwx 可读可写可执行
d-l 文件夹、 文件、链接
chmod g（所属组）-rw取消所属组rw权限，o（其他人），u（x）
chmod -R 递归修改所有权限
useradd
为用户配置sudo权限
vi /etc/sdoers 添加 root ALL=(ALL) ALL  ralap ALL=(ALL) ALL
hostname 主机名（/etc/sysconfig/network）
修改ip  ifconfig eth0 *********  /etc/sysconfig/network-scripts/ifcfg-eth0
mount -t iso9660 -o ro /dev/cdrom /mnt/cdrom/
umount /mnt/cdrom/
du -sh 统计文件大小
df -h 磁盘大小
halt 关机 reboot重启
ssh-keygen 生成密钥
ssh-copy-id ***  拷贝公钥到指定服务器 实现免密登录

#Linux连续执行多个命令
每条命令使用";"隔开，则无论前边的命令执行成功与否都会继续执行下一条命令
这里，故意将第二条命令中的echo多写了一个o，命令执行出错，但并不影响后续命令的执行
可以这么想，如果用分号来间隔命令，就相当于将命令分隔在了不同的行，无论前一行的命令成功或失败，都不影响下一行命令的执行。
$ echo 1; echoo 2; echo 3; echo 4
-bash: echoo: command not found

若命令间使用"&&"隔开，则只有前边的命令执行成功了再会继续执行后边的命令
这里，故意将第二条命令中的echo多写了一个o，命令执行出错，echo 3便没有执行，因此echo4也没执行
$ echo 1 && echoo 2 && echo 3 && echo 4
-bash: echoo: command not found

若命令间使用"||"隔开，则只有前边的命令执行失败了再回继续执行后边的命令
这里echo 1执行成功则没有继续执行后边的echo 2，继而没有执行echo 3，echo 4
echo 1 || echo 2 || echo 3 || echo 4
这里echoo 1执行失败，因此开始执行echo 2，执行成功，因而后边的echo 3， echo4都没执行
echoo 1 || echo 2 || echo 3 || echo 4
-bash: echoo: command not found

根据以上规则分析几个比较特殊的例子，也即混合了集中分隔符的例子
echo 1执行成功了，紧接着后边有两个"||"因此echo 2, echo 3都没执行，后边遇到了&&，而这之前的命令组合被认为是执行成功的，因此echo 4得以执行
$ echo 1 || echo 2 || echo 3 && echo 4 

echo 1执行成功了，继而执行echoo 2，执行失败，因此 echo 3不被执行，后边遇到了"||",而知之前的命令组合被认为是执行失败的，因此echo 4得以执行
$ echo 1 && echoo 2 && echo 3 || echo 4
-bash: echoo: command not found

echo 1执行成功了，继而执行echoo 2，执行失败，因此 echo 3不被执行，后边遇到了";",相当于把后边的命令放到了新行，这样的话无论如何后边的命令都会执行，因此echo 4得以执行
$ echo 1 && echoo 2 && echo 3 ; echo 4
-bash: echoo: command not found

echoo 1执行失败，后边为"||"因此echo 2得以执行，echo 2执行成功，紧接着后边有两个"||"因此echo 3，echo 4没有执行，后边遇到了&&，而之前的命令组合被认为是执行成功的，因此echoo5得以执行，执行发生错误，因此echo 6没有被执行，但后边是";"，所以无论如何echo 7都会被执行
$ echoo 1 || echo 2 || echo 3 || echo 4 && echoo 5 && echo 6 ; echo 7
-bash: echoo: command not found
-bash: echoo: command not found

#基础知识#

Debian是Linux的一个发行版，Linux对文件系统的权限管理的很严格，比如你在图形化下复制一个文件发现无法复制，使用命令sudo cp -r xx xx 就可以复制过去，这就是权限管理的问题。有的时候发现没办法运行记得加上sudo，总结一些必知必会的基础知识，方便在日常环境下使用。（这里插一句话，如果想使用Linux系统，但是决定ubuntu或者debian太麻烦了，建议使用国内相对来说比较好用的Linux发行版—deepin，安装过程比较简单，官方网站有很详细的介绍，小学生坐在马桶上都会安装。
###文件/文件夹管理###

1. ls       列出当前目录下所有文件
2. ls -a    列出当前目录所有文件（包括隐藏文件）
3. ls -l    列出每个文件的详细信息
4. cd ..    返回上级目录
5. cd -     返回上一次打开的目录
6. cd ~        返回主目录
7. cd //    返回根目录
8. mkdir test   创建名为test的文件夹
9. rm -rf test  删除test文件夹和其下所有文件（-r是递归，-f是强制）
10. mv test /var/test   把test文件夹移动到var目录下
11. mv  test test1      把test文件夹重命名为test1，该方法适用于文件重命名


###查看信息/开关服务###

1. sudo service apache start-stop-restart   开启-关闭-重启apache服务，记得加上sudo，不然权限不够无法启动，如果要开启别的服务比如mysql，直接把apache改成mysql即可（如果不记得mysql密码，cat /etc/mysql/debian.cnf 里面明文存储mysql密码）
2. sudo /etc/init.d/apahce start-stop-restart   同上，如果要开启别的服务比如mysql，直接把apache改成mysql即可
3. uname -a                 查看内核版本
4. cat /etc/issue           查看系统版本
5. hostname                 查看系统
6. cat /proc/cpuinfo        查看CPU信息
7. sudo ethtool eth0        查看网卡状态
8. sudo fdisk -l            查看磁盘信息
9. lshw                     查看硬件信息
10. df -h                   查看剩余空间
11. free -m                 查看内存使用情况
12. ps -A                   查看所有进程
13. kill pid&kill name      结束进程，pid是在ps -A查看对应的数字，name即是进程名
14. du -hs                  查看当前目录大小
15. find . -name 'xxx.py'   寻找文件，文件名可以使用通配符*
16. mysql \.                登陆mysql后，输入\\. var/sqlsetup.sql(sql文件路径)即可安装sql文件 
17. top/w                   查看负载，w后面三个值表示近1分钟，10,15分钟的负载，一般来说0.6是标准健康值
18. grep                    匹配文件
19. wc -l                   统计文件个数
20. |                       把上一个命令的值传递个下一个命令，比如grep '11' xxx.txt|wc -l


###打包/解压缩###

1. tar 
    1. tar -c 创建包
    2. tar -x 释放包
    3. tar -v 显示过程信息
    4. tar -z 代表压缩包
2. tar --zcvf dabao.tar.gz /var/bin      把/var/bin目录打包压缩成dabao.tar.gz
3. tar --zxvf dabao.tar.gz               把dabao.tar.gz解压出来


###安装软件###

Linux安装软件有两种方式，第一种是直接在线安装（使用apt-get），第二种是下载到本地然后手动安装（使用dpkg -i xxxx.deb）。

安装软件包

dpkg -i package.deb     //安装本地软件包，不解决依赖关系

apt-get install package  //在线安装软件包


软件安装后相关文件位置

1.下载的软件包存放位置

/var/cache/apt/archives

2.安装后软件默认位置

/usr/share

3.可执行文件位置

/usr/bin

4.配置文件位置

/etc

5.lib文件位置

/usr/lib


###详细命令###

1. apt-cache serach package             搜索包
2. apt-cache show package               显示这个包的详细信息，比如大小版本说明等
3. sudo apt-get install package         在线安装包
4. sudo apt-get install package --reinstall     重新在线安装这个包
5. sudo apt-get remove package          删除这个包
6. sudo apt-get remove package --purge  删除这个包和这个包的相关配置文件
7. sudo apt-get update                  更新源，在安装新的包之间要先编辑对应的源地址
8. sudo apt-get upgrade                 更新与源对应的所有文件包
9. apt-cache depends package            查看这个包需要依赖的包
10. apt-cache rdepends package          查看这个包被哪些包所依赖
11. sudo apt-get build-dep package      安装相关的编译环境
12. sudo apt-get clean && sudo apt-get autoclean    删除不用的包（清理/var/cacheapt/archive中的deb缓存文件）
13. sudo apt-get check                  检查室友有损坏的依赖包


###dkpg安装删除包###

1.  dpkg -i package-file-name       安装包
2.  sudo apt-get install -f根据经验，通常情况下会报依赖关系的错误，我们可以使用以下的命令修复安装。
2.  dpkg -r package-file-name       删除包
3.  sudo dpkg -l                    查看已经安装的软件
3.  dpkg -l | grep 'package-file-name'  检查这个包的状态
4.  dpkg -P package-file-name       表示彻底卸载软件包（包括配置文件）



###apt-get安装删除包###

1. 安装新的文件一般要编辑对应的源文件，比如：

        leafpad /etc/apt/sources.list  查看使用的源，更新编辑源
2. sudo apt-get update                  更新软件源
3. sudo apt-get upgrade                 更新对应源的所有文件
4. sudo apt-get install package         安装包
5. sudo apt-get --reinstall install package     重新安装这个包
5. sudo apt-get remove package          卸载删除包
6. sudo apt-get autoremove package      自动卸载软件但保留其配置文件
7. sudo apt-get autoremove --purge package  自动卸载软件其删除其配置文件

tips: 5 一般用于卸载本地安装的软件，6&7 一般用于在线安装的软件

 
###最佳方法删除与安装包###

通过上面的方法基本上都可以删除安装包，但是过程有些累赘，其中有一小步出错后后面就更加让人头疼，在Linux下有一个专门管理安装包的应用，aptitude。

aptitude在处理依赖问题上更佳一些。举例来说，aptitude在删除一个包时，会同时删除本身所依赖的包。这样，系统中不会残留无用的包，整个系统更为干净。

需要注意的是，与apt一样，安装新的软件之前要跟新源哦~

首先更新源文件

mv /etc/apt/sources.list /etc/apt/sources.list.bak   # 先备份一下

sudo nano /etc/apt/sources.list                      # 编辑文件

# 然后加上下面这些源地址
deb http://mirrors.163.com/debian/ jessie main non-free contrib
deb http://mirrors.163.com/debian/ jessie-updates main non-free contrib
deb http://mirrors.163.com/debian/ jessie-backports main non-free contrib
deb-src http://mirrors.163.com/debian/ jessie main non-free contrib
deb-src http://mirrors.163.com/debian/ jessie-updates main non-free contrib
deb-src http://mirrors.163.com/debian/ jessie-backports main non-free contrib
deb http://mirrors.163.com/debian-security/ jessie/updates main non-free contrib
deb-src http://mirrors.163.com/debian-security/ jessie/updates main non-free contrib
# 更新一下
apt-get update
apt-get upgrade
# 安装apttitude
sudo apt-get install apttitude
# 举个例子，检索并删除PHP
sudo aptitude purge `dpkg -l | grep php| awk '{print $2}' |tr "\n" " "`
# 这样，就完全删除了PHP
# 然后我在安装PHP，使用apt-get与apttitude一样，我使用apt-get....
sudo apt-get install php5 php-pear php5-mysql php5-gd



###aptitude常用命令###

aptitude update            更新可用的包列表
aptitude safe-upgrade      执行一次安全的升级
aptitude full-upgrade      将系统升级到新的发行版
aptitude install pkgname   安装包
aptitude remove pkgname    删除包
aptitude purge pkgname     删除包及其配置文件
aptitude search string     搜索包
aptitude show pkgname      显示包的详细信息
aptitude clean             删除下载的包文件
aptitude autoclean         仅删除过期的包文件

i: 安装软件包   
c: 软件包没有安装，但在系统中有软件包的残留配置   
p: 从系统彻底删除   
v: 虚拟软件包   
B: 已损坏的软件包   
u: 解压文件，但尚未配置软件包   
C: 半配置 - 配置失败需要修复   
H: 半安装 - 卸载失败需要修复  


tips:使用aptitude可以解决python使用pip安装包的时候包的依赖问题：，如安装scipy，matplotlib的时候出现依赖包，自己去安装比较麻烦的问题：
如：sudo aptitude install python-scipy ; sudo aptitude install python-matplotlib
文件权限问题
Linux对文件权限管理很严格，其所对应的概念如下：

w:可写
r：可读
x：可执行
a:可追加

使用ls -l可以查看每个文件的权限，如果需要修改权限可以这么做
chmod u+r xxx.py

这样xx.py就有了可读的权限，若要有读写权限使用u+wr即可，如果要删除相关的权限使用u-wr即可。另一种方式使用数字对应的u+r，比如最常见的chomd 777 xxx.py,r对应4，w对应2，有点麻烦不好记忆，使用u+r就可以了。

##快捷键##

Linux下使用鼠标机会不多，尽量多记住一些快捷键，在工作或者学习的时候能提高效率。  
    前一个后一个工作区的切换  
    如果你经常使用工作区，那你就可以用Ctrl + Alt +上/下方向键很容易地进行切换。左箭头切换到上一个工作区，右箭头切换到下一个工作区。  
    把当前窗口移到另一个工作区  
    快捷键Shift+ Ctrl + Alt +左/右方向键让你很容易把当前窗口移到指定的工作区。这个快捷键和上面的快捷键很好配合。如果你工作时常常打开很多窗口，但又不想看到桌面 和任务栏挤满程序，你可以用这个快捷键把程序移到另 一个工作区，这样你的桌面就整洁多了。  
    显示桌面  
    Ctrl + Alt + D快捷键让你很快地最小化所有窗口，看到桌面。当所有窗口都最小化后，你再按这个快捷键就可以恢复窗口原来的状态。  
    鼠标右击的键盘快捷键  
    在大多数程序里，你可以右击显示快捷菜单。其实键盘上 Shift + F10也能达到一样的效果。  
    重启会话以从崩溃中恢复  
    按下Ctrl + Alt + Backspace来重启会话，恢复的可能达90%。
    快速锁定屏幕
    如果你需要离开 电脑 一会儿，可以按下Ctrl + Alt + L很快地锁定屏幕，以防有人使用
    反向切换窗口
    Alt + Tab是切换窗口的快捷键。如果你再按下SHIft，你就可以反向切换窗口。这个快捷键很有用，当你Alt + Tab按得太快，错过了你想要切换的窗口，按一下shift就可以返回之前的窗口了。
    用方向键移动窗口
    Alt+F7会激活移动窗口 功能 ，用方向键（上，下，左，右）就可以移到窗口了。
    编辑文本快捷键使用
    1. ctrl + k  #从光标开始到文本末剪切所有文本
    2. ctrl + y  #粘贴文本
    3. ctrl + e  #将光标移动到本行末尾
    4. ctrl + a  #将光标移动到本行开头
    5. ctrl + w  #剪切前一个单词
    6. alt  + f  #跳转到下一个空格处
    7. alt  + b  #跳转到上一个空格处
    8. alt  + back  #删除前一个单词
    9. shfit + insert #粘贴一个词（在终端）


#linux下安装抓包工具fiddler
在linux上安装fiddler需要mono环境，所以先安装mono环境，
sudo apt-get install mono-complete

安装好环境后，下载fiddler，选择最新的
http://fiddler.wikidot.com/mono

把下载好的fiddler放在你自己喜欢的目录下解压，然后在目录上进入终端，解压，执行命令：
unzip -d fiddler ./fiddler-linux.zip 
mono Fiddler.exe

简化执行方式
上面每次都要进入Download文件夹,还得执行mono命令才能打开fiddler. 所以需要简化一下
移动到 ~/Tools (如果没有这个目录,需要创建)
mv ~/Downloads/fiddler ~/Tools
添加命令别名
alias fiddler="mono ~/Tools/fiddler/Fiddler.exe"
上面的alias在下次登录就会失效,所以需要设置永久生效
gedit ~/.bashrc
在末尾添加
alias fiddler="mono ~/Tools/fiddler/Fiddler.exe"
之后只要在终端输入fiddler就可以打开它了.

#借助rarlinux来解压rar格式文件

 下载地址：http://www.rarlab.com/download.htm
  打不开或者网速不好的可以到可以我的资源中的下载，免费：
  http://download.csdn.net/detail/alex_my/6731197 

  // 1 解压
  tar -zxvf rarlinux-3.6.0.tar.gz

  // 2 解压出一个rar文件夹，进入， 需要root权限
  cd rar
  make
  make install
  
使用方法
============================================

查看压缩包中的文档
$rar l XXX.rar  或  $rar v XXX.rar
查看压缩包中的文档(只看有什么文档)
$rar lb XXX.rar 或 $rar vb XXX.rar
查看压缩包中的文档(周详信息)
$rar lt XXX.rar 或 $rar vt XXX.rar

============================================
把压缩包的内容解压到当前目录
$rar e XXX.rar
把压缩包的内容解压到指定目录，比如/home/yxd/tmp/下面
$rar e XXX.rar /home/yxd/tmp/
把压缩包解的内容压到指定目录，比如/home/yxd/tmp/下面，包含压缩包中的路径
$rar x XXX.rar /home/yxd/tmp/

============================================
压缩指定的一个文档，比如aaa，以默认压缩率
$rar a XXX.rar aaa
压缩指定的一个文档，比如aaa，以最大压缩率
$rar a -m5 XXX.rar aaa
压缩指定的一个目录下的任何文档，比如ddd目录下的任何文档
$rar a XXX.rar ddd/
压缩指定的一个目录下的任何文档，比如ddd目录下的任何文档和任何子目录
$rar a -r XXX.rar ddd/
压缩指定的一个目录下的任何文档，比如ddd目录下的任何文档和任何子目录，但是不包含空目录
$rar a -r -ed XXX.rar ddd/
压缩指定的一个目录下的任何文档，比如ddd目录，连目录也一起压缩，包括子目录
$rar a XXX.rar ddd

============================================
分卷压缩指定的一个文档，比如aaa，分卷大小为5000B
$rar a -v5 XXX.rar aaa
分卷压缩指定的一个文档，比如aaa，分卷大小为5k(5*1024B)
$rar a -v5k XXX.rar aaa
分卷压缩指定的一个文档，比如aaa，分卷大小为5B
$rar a -v5b XXX.rar aaa

#linux命令之解压缩tar,rar,zip
1. tar 命令
语法： tar [主选项 + 辅选项] 文件或目录

示例：
    # 压缩文件 file1 和目录 dir2 到 test.tar.gz
    tar -zcvf test.tar.gz file1 dir2
    # 解压 test.tar.gz（将 c 换成 x 即可）
    tar -zxvf test.tar.gz
    # 列出压缩文件的内容
    tar -ztvf test.tar.gz 

释义：
    -z : 使用 gzip 来压缩和解压文件
    -v : --verbose 详细的列出处理的文件
    -f : --file=ARCHIVE 使用档案文件或设备，这个选项通常是必选的
    -c : --create 创建一个新的归档（压缩包）
    -x : 从压缩包中解出文件

其它：
tar 命令其实并不是真的解压缩的处理者，而是使用了 gzip 或者 bzip2 等其它命令来达成，但是 gzip 等命令通常只能处理单个文件，并不方便，所以一般我们都是选择使用 tar 命令间接的完成解压缩。

2. rar 命令
示例：
    # 压缩文件
    rar a -r test.rar file
    # 解压文件
    unrar x test.rar

释义：
    a : 添加到压缩文件
    -r : 递归处理
    x : 以绝对路径解压文件

3. zip 命令
示例：
    # 压缩文件
    zip -r test.zip file
    # 解压文件
    zip test.zip

释义：
    -r : 递归处理

三、tar 命令详解
1. 语法：

tar [-ABcdgGhiklmMoOpPrRsStuUvwWxzZ][-b <区块数目>][-C <目的目录>][-f <备份文件>][-F <Script文件>][-K <文件>][-L <媒体容量>][-N <日期时间>][-T <范本文件>][-V <卷册名称>][-X <范本文件>][-<设备编号><存储密度>][--after-date=<日期时间>][--atime-preserve][--backuup=<备份方式>][--checkpoint][--concatenate][--confirmation][--delete][--exclude=<范本样式>][--force-local][--group=<群组名称>][--help][--ignore-failed-read][--new-volume-script=<Script文件>][--newer-mtime][--no-recursion][--null][--numeric-owner][--owner=<用户名称>][--posix][--erve][--preserve-order][--preserve-permissions][--record-size=<区块数目>][--recursive-unlink][--remove-files][--rsh-command=<执行指令>][--same-owner][--suffix=<备份字尾字符串>][--totals][--use-compress-program=<执行指令>][--version][--volno-file=<编号文件>][文件或目录...]
2. 参数详解：

-A或--catenate 新增文件到已存在的备份文件。
-b<区块数目>或--blocking-factor=<区块数目设置每笔记录的区块数目，每个区块大小为12Bytes。
-B或--read-full-records 读取数据时重设区块大小。
-c或--create 建立新的备份文件。
-C<目的目录>或--directory=<目的目录切换到指定的目录。
-d或--diff或--compare 对比备份文件内和文件系统上的文件的差异。
-f<备份文件>或--file=<备份文件指定备份文件。
-F<Script文件>或--info-script=<Script文件每次更换磁带时，就执行指定的Script文件。
-g或--listed-incremental 处理GNU格式的大量备份。
-G或--incremental 处理旧的GNU格式的大量备份。
-h或--dereference 不建立符号连接，直接复制该连接所指向的原始文件。
-i或--ignore-zeros 忽略备份文件中的0 Byte区块，也就是EOF。
-k或--keep-old-files 解开备份文件时，不覆盖已有的文件。
-K<文件>或--starting-file=<文件从指定的文件开始还原。
-l或--one-file-system 复制的文件或目录存放的文件系统，必须与tar指令执行时所处的文件系统相同，否则不予复制。
-L<媒体容量>或-tape-length=<媒体容量设置存放每体的容量，单位以1024 Bytes计算。
-m或--modification-time 还原文件时，不变更文件的更改时间。
-M或--multi-volume 在建立，还原备份文件或列出其中的内容时，采用多卷册模式。
-N<日期格式>或--newer=<日期时间只将较指定日期更新的文件保存到备份文件里。
-o或--old-archive或--portability 将资料写入备份文件时使用V7格式。
-O或--stdout 把从备份文件里还原的文件输出到标准输出设备。
-p或--same-permissions 用原来的文件权限还原文件。
-P或--absolute-names 文件名使用绝对名称，不移除文件名称前的"/"号。
-r或--append 新增文件到已存在的备份文件的结尾部分。
-R或--block-number 列出每个信息在备份文件中的区块编号。
-s或--same-order 还原文件的顺序和备份文件内的存放顺序相同。
-S或--sparse 倘若一个文件内含大量的连续0字节，则将此文件存成稀疏文件。
-t或--list 列出备份文件的内容。
-T<范本文件>或--files-from=<范本文件指定范本文件，其内含有一个或多个范本样式，让tar解开或建立符合设置条件的文件。
-u或--update 仅置换较备份文件内的文件更新的文件。
-U或--unlink-first 解开压缩文件还原文件之前，先解除文件的连接。
-v或--verbose 显示指令执行过程。
-V<卷册名称>或--label=<卷册名称建立使用指定的卷册名称的备份文件。
-w或--interactive 遭遇问题时先询问用户。
-W或--verify 写入备份文件后，确认文件正确无误。
-x或--extract或--get 从备份文件中还原文件。
-X<范本文件>或--exclude-from=<范本文件指定范本文件，其内含有一个或多个范本样式，让ar排除符合设置条件的文件。
-z或--gzip或--ungzip 通过gzip指令处理备份文件。
-Z或--compress或--uncompress 通过compress指令处理备份文件。
-<设备编号><存储密度设置备份用的外围设备编号及存放数据的密度。
--after-date=<日期时间此参数的效果和指定"-N"参数相同。
--atime-preserve 不变更文件的存取时间。
--backup=<备份方式>或--backup 移除文件前先进行备份。
--checkpoint 读取备份文件时列出目录名称。
--concatenate 此参数的效果和指定"-A"参数相同。
--confirmation 此参数的效果和指定"-w"参数相同。
--delete 从备份文件中删除指定的文件。
--exclude=<范本样式排除符合范本样式的问家。
--group=<群组名称把加入设备文件中的文件的所属群组设成指定的群组。
--help 在线帮助。
--ignore-failed-read 忽略数据读取错误，不中断程序的执行。
--new-volume-script=<Script文件此参数的效果和指定"-F"参数相同。
--newer-mtime 只保存更改过的文件。
--no-recursion 不做递归处理，也就是指定目录下的所有文件及子目录不予处理。
--null 从null设备读取文件名称。
--numeric-owner 以用户识别码及群组识别码取代用户名称和群组名称。
--owner=<用户名称把加入备份文件中的文件的拥有者设成指定的用户。
--posix 将数据写入备份文件时使用POSIX格式。
--preserve 此参数的效果和指定"-ps"参数相同。
--preserve-order 此参数的效果和指定"-A"参数相同。
--preserve-permissions 此参数的效果和指定"-p"参数相同。
--record-size=<区块数目此参数的效果和指定"-b"参数相同。
--recursive-unlink 解开压缩文件还原目录之前，先解除整个目录下所有文件的连接。
--remove-files 文件加入备份文件后，就将其删除。
--rsh-command=<执行指令设置要在远端主机上执行的指令，以取代rsh指令。
--same-owner 尝试以相同的文件拥有者还原问家你。
--suffix=<备份字尾字符串移除文件前先行备份。
--totals 备份文件建立后，列出文件大小。
--use-compress-program=<执行指令通过指定的指令处理备份文件。
--version 显示版本信息。
--volno-file=<编号文件使用指定文件内的编号取代预设的卷册编号。

#linux制作启动U盘
    1.查看U盘对应的设备名称
        插入U盘后，使用下面的命令查看U盘对应的设备名称：
        fdisk -l
        可以看到，U盘对应的设备名称为/dev/sdb。
    2.卸载U盘
        使用如下命令卸载U盘：
        umount /dev/sdb
    3.格式化U盘（一定要慎重，仔细确认U盘是否挂载到/dev/sdb,如果有双硬盘通常sdb是你的第二块硬盘）
        使用如下命令格式化U盘：
        mkfs.fat /dev/sdb -I
    4.将ISO镜像文件写入到U盘
        使用如下命令将ISO文件写入到U盘：
        dd if=ubuntu-16.0.3-desktop-amd64.iso of=/dev/sdb
        (注意，/dev/sdb后面不要带1或者2的数字)
经过以上四步就制作好了U盘安装盘，重启PC，选择从U盘启动就可以开心地重装系统了。

#LinuxMint调节屏幕亮度
##方法〇
鼠标点击桌面右下角电池图标，有显示亮度滚动条，拖动调整即可。

##方法一
1.打开一个终端，查看本机最大亮度值。
输入命令：
cat /sys/class/backlight/acpi_video0/max_brightness
15
注：如果是双显卡，则/sys/class/backlight/下还有video1和intel_backlight目录，各自里面都有max_brightness和actual_brightness，表示最大亮度和实际亮度。默认一般使用video0下面的。
2.打开文本编辑器。一般是gedit或者pluma。把下面这几行代码复制到文本编辑器中，保存为.mybrt.sh。注意，这个文件名是以.开头的隐藏文件。这段代码的意思是把亮度设为7。前面我们查看了最大亮度是15，所以设置为7已经很不错。当然你可以修改这个数字为自己喜欢的亮度值。
\#!/bin/sh
\#change brightness setting on startup or resume
pkexec /usr/lib/gnome-settings-daemon/gsd-backlight-helper --set-brightness 7

3.为.mybrt.sh文件添加执行属性。打开终端，输入命令：chmod +x .mybrt.sh。
4.设置开机登录自动运行亮度脚本（即刚才新建的那个.mybrt.sh），这样就每次开机都可以恢复为我们需要的亮度了。在终端中输入命令：
gsettings set org.gnome.settings-daemon.peripherals.input-devices hotplug-command "/home/who/.mybrt.sh"
注意：把who换成你的用户名。
经过此番设置，你的笔记本电脑无论是重启、注销还是合上屏幕、待机等情况，一旦进入桌面后，屏幕亮度就会自动恢复为我们设置好的亮度值。这个方法很简单，也无需安装其他软件，或者修改系统配置文件。
值得注意的是，这个办法只对采用Gnome3桌面环境的Linux系统有效，如Ubuntu11.04以后的版本、Linuxdeepin12.06、Linuxmint13 Cinnamon版等。对Linuxmint13 mate版无效。

##方法二
我使用的Mint Linux的调整亮度的界面程序设置后亮度没有变化，那就只有玩儿一下有“深度”的了，直接修改配置文件的值就OK了，直接修改管理亮度的文件/sys/class/backlight/intel_backlight/brightness 中的值，
直接使用命令：echo 100 >/sys/class/backlight/intel_backlight/brightness   即是将屏幕的亮度调整到100,就是调暗的节奏了；
要亮度很高那就使用命令：echo 1000 >/sys/class/backlight/intel_backlight/brightness 调整到最亮了；

##方法三
xrandr的man文档解释是：
    primitive command line interface to RandR extension
    “原始的命令行下的RandR扩展”
但是什么是RandR呢？Wiki的定义如下：
    RandR (“resize and rotate”) is a communications protocol written as an extension to the X11 and Wayland protocols for display servers.
可以看出，RandR是一个调整显示用的协议。

xrandr最基本的用途是调整显示器的分辨率。在输入xrandr之后，会列出所有显示设备的状态和支持的分辨率。使用-s参数可以设置希望的分辨率。具体可见Linux下使用 xrandr 命令设置屏幕分辨率。
至于设置屏幕的亮度，可以有以下步骤：
输入xrandr，查看输出中状态是connected的显示设备，如LVDS。具体命令可以是：
xrandr | grep -v disconnected | grep connected

调整亮度：
xrandr --output LVDS --brightness 0.5
注：output后面的参数为上一步中查出的显示设备，不同主机结果可能不同。brightness后面的参数范围是0-1，0为全黑，1为最亮。

最后，将这个常用的功能写为一个脚本：
#! /bin/bash
if [ $# -ne 1 ] ; then
    echo "Usage: setbrightness <0.0-0.1>"
    exit 1
fi

xrandr --output LVDS --brightness $1

所有用户加入执行权限：
chmod a+x setbrightness
移至应用程序目录下，以便可以直接使用：
mv setbrightness /usr/local/bin
现在就可以直接设置显示器的亮度了！

#查看硬件信息
##1 hardinfo命令
此命令会以图形化方式显示硬件信息，如果没有可以用sudo apt install hardinfo安装
##2 查看CPU及内存信息
查看CPU：
cat /proc/cpuinfo
该命令可以查看系统CPU有多少个核，频率，特性等等。

查看cpu内核频率
cat /proc/cpuinfo |grep MHz|uniq
cpu MHz         : 27518.499

查看内存：
#cat /proc/meminfo
这个命令只能看当前内存大小，已用空间等等。

要查看内存型号、频率，使用命令(使用root才行)：
dmidecode -t memory
输出示例：
Memory Device
        Array Handle: 0x0012
        Error Information Handle: No Error
        Total Width: 64 bits
        Data Width: 64 bits
        Size: 4096 MB
        Form Factor: SODIMM
        Set: None
        Locator: DIMM0
        Bank Locator: BANK 0
        Type: DDR3
        Type Detail: Synchronous
        Speed: 1333 MHz
        Manufacturer: 00
        Serial Number: 00000000
        Asset Tag: Unknown
        Part Number:16KTF1G64HZ-1G6E1
        Rank: Unknown
        Configured Clock Speed: 1333 MHz

查看系统运行时间：
cat /proc/uptime
65923.93 65697.26

查看内核IO地址映射：
cat /proc/iomem

查看上一次登陆：
last /var/log/wtmp 
（如不存在，直接touch生成。可用rm删除 ）

内核版本：
cat /proc/version 


查看内核函数：
cat /proc/kallsyms


查看系统启动参数：
cat /proc/cmdline 
磁盘信息(这个文件一般人看不懂，有工具就是分析这个文件得到磁盘性能信息的)：
cat /proc/diskstats 


查看中断：
cat /proc/interrupts 
清空内存：
echo 2 > /proc/sys/vm/overcommit_memory  

#Linux下查看内存信息和查找DIMM型号的方法
    因为网站开发的需求，需要对单位的服务器内存进行升级。经过向HP的在线技术人员咨询后，得知HP Proliant DL160 G6(QP661A)这台服务器，最大能支持单条RDIMMs为16G，UDIMMs为4G。  
　　关于RDIMMs和UDIMMs的介绍在网上有大量的资料，在此就不在赘述了。  
```
dmidecode | grep -A16 "Memory Device"
he@he-X230:~/pydev/doc$ sudo dmidecode | grep -A16 "Memory Device"
Memory Device
	Array Handle: 0x0007
	Error Information Handle: Not Provided
	Total Width: 64 bits
	Data Width: 64 bits
	Size: 8192 MB
	Form Factor: SODIMM
	Set: None
	Locator: ChannelA-DIMM0
	Bank Locator: BANK 0
	Type: DDR3
	Type Detail: Synchronous
	Speed: 1600 MT/s
	Manufacturer: Samsung
	Serial Number: 0C84023B
	Asset Tag: None
	Part Number: 16KTF1G64HZ-1G6E1 
```
以上是LinuxMint系统上查询到的内存信息。其中，我们能得知，该内存是由Samsung生产的一条内存。那么内存到底是RDIMMs还是UDIMMs呢。我们可以根据Part Number：中那一串字符在集成电路的数据库中进行查找。网上也有很多免费资源。
　　在下载到的datasheet上，找到了该内存的所有信息如下：

附录：一个较好的IC资料查找网站：http://www.alldatasheet.com


