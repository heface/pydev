#Kali Linux 介绍：
http://cn.docs.kali.org/category/introduction-cn

#Kali Linux 下载：
http://www.kali.org/downloads/

#安装Kali Linux：
参考官方文档，以及在线搜索“Deiban Linux安装教程”或者 “Debian windows 双系统”。
http://wenku.baidu.com/view/2b5b3149767f5acfa1c7cd51.html

建议参考官方在线文档：
http://cn.docs.kali.org/category/installing-kali-linux-cn

#修改更新源
1 查看配置文件
cat /etc/apt/sources.list
看里面有没有一下三行kali官方源的地址（如果是断网安装，kali的默认源可能不会写入到这个文件里），如果没有，请在/etc/apt/sources.list中入这三行。
	deb http://http.kali.org/kali kali main non-free contrib
    deb-src http://http.kali.org/kali kali main non-free contrib
    deb http://security.kali.org/kali-security kali/updates main contrib non-free

#中科大kali源
deb http://mirrors.ustc.edu.cn/kali sana main non-free contrib
deb http://mirrors.ustc.edu.cn/kali-security/ sana/updates main contrib non-free
deb-src http://mirrors.ustc.edu.cn/kali-security/ sana/updates main contrib non-free
 
#阿里云kali源
deb http://mirrors.aliyun.com/kali sana main non-free contrib
deb http://mirrors.aliyun.com/kali-security/ sana/updates main contrib non-free
deb-src http://mirrors.aliyun.com/kali-security/ sana/updates main contrib non-free


2.加入之后就可以对系统进行更新了，终端中输入：	
apt-get update && apt-get upgrade 
apt-get update & apt-get upgrade
apt-get dist-upgrade 
apt-get clean 

3.把密码改一下

root@kali:~# passwd

#汉化
Kali Linux的国际化做得真心不错，安装时如果你选择了中文语言，进入系统之后已经发现汉化完成了。如果安装时没有选择中文那么请参考一下的方法吧系统语言设置成中文：
在命令行执行：
dpkg-reconfigure locales
进入选择语言的图形化界面之后，（空格是选择，Tab是切换，*是选中），选中en_US.UTF-8和zh_CN.UTF-8，确定后，将en_US.UTF-8选为默认。 

#安装中文字体
apt-get install xfonts-intl-chinese
apt-get install ttf-wqy-microhei

#安装中文输入法
apt-get install ibus ibus-pinyin

#汉化iceweasel
apt-get install iceweasel-l10n-zh-cn

#开启ssh服务
root@kali:~# service ssh start

#安装其他工具
apt-get install flashplugin-nonfree      #安装flash player
update-flashplugin-nonfree --install     #升级flash
apt-get install gnome-tweak-tool         #安装gnome管理软件
apt-get install synaptic                 #安装新立德
apt-get install file-roller              #安装解压缩软件
apt-get install clementine               #clementine音乐播放器
apt-get install smplayer                 #安装smplayer视频播放器
apt-get install terminator               #安装多窗口终端
apt-get install icedtea-7-plugin         #安装java

#运行 Metasploit Framework
依照kali linux网络服务策略，Kali没有自动启动的网络服务，包括数据库服务在内。所以为了让metasploit以支持数据库的方式运行有些必要的步骤。启动Kali的PostgreSQL服务：Metasploit 使用PostgreSQL作为数据库，所以必须先运行它。
service postgresql start
你可以用ss -ant的输出来检验PostgreSQL是否在运行，然后确认5432端口处于listening状态。

##启动Kali的Metasploit服务
随着PostgreSQL的启动和运行，接着我们要运行Metasploit服务。第一次运行服务会创建一个msf3数据库用户和一个叫msf3的数据库。还会运行Metasploit RPC和它需要的WEB 服务端。
service metasploit start
msf > db_status
[*] postgresql connected to msf3
msf >

##配置Metasploit随系统启动运行
如果你想PostgreSQL和Metasploit在开机时运行，你可以使用update-rc.d启用服务。
update-rc.d postgresql enable
update-rc.d metasploit enable

##启动metasploit
msfconsole

##更新
apt-get  install metasploit-framework
msfupdate