#manjaro软件源设置及软件安装
sudo pacman-mirrors -c China
sudo pacman-optimize && sync
sudo pacman -S gedit
sudo gedit /etc/pacman.conf

[archlinuxcn]
SigLevel = Optional TrustedOnly
Server = https://mirrors.tsinghua.edu.cn/archlinuxcn/$arch
Server = https://mirrors.ustc.edu.cn/archlinuxcn/$arch
sudo gedit /etc/pacman-mirrors.conf
OnlyCountry = China

sudo pacman -Syyu
sudo pacman -S archlinuxcn-keyring
sudo pacman -S fcitx-sogoupinyin fcitx-im fcitx-configtool
sudo gedit ~/.xprofile
export GTK_IM_MODULE=fcitx
export QT_IM_MODULE=fcitx
export XMODIFIERS="@im=fcitx"
sudo pacman -S fcitx-sogoupinyin fcitx-im fcitx-configtool shadowsocks-qt5 git google-chrome vivaldi visual-studio-code-bin atom android-studio eclipse-cpp electron-netease-cloud-music wps-office ttf-wps-fonts youdao-dict speedcrunch franz-bin virtualbox virtualbox-ext-oracle screenfetch deepin-wine-tim

git config --global user.name "liruya"
git config --global user.email "cylary1218@gmail.com"
git config --global http.proxy 'http://127.0.0.1:1080'
git config --global https.proxy 'https://127.0.0.1:1080'

安装 pacman -S
删除 pacman -R
移除已安装不需要软件包  pacman -Rs
删除一个包,所有依赖 pacman -Rsc
升级包 pacman -Syu
查询包数据库 pacman -Ss
搜索以安装的包 pacman -Qs
显示包大量信息 pacman -Si
本地安装包 pacman -Qi
清理包缓存 pacman -Sc

Android Studio空间不足
Help -> Edit Custom VM Options
-Djava.io.tmpdir=/var/tmp
//MPLABX && xc8
tar -xvf MPLABX-v5.05-linux-installer.tar
chmod u+x MPLABX-v5.05-linux-installer.sh
sudo ./MPLABX-v5.05-linux-installer.sh
chmod u+x xc8-v1.45-full-install-linux-installer.run
sudo ./xc8-v1.45-full-install-linux-installer.run
