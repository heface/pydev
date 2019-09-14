#Emac使用技巧
[toc]
#Emacs快捷键

C = Control<br>
M = Meta = Alt | Esc<br>
Del = Backspace<br>
RET = Enter<br>

每个按键都去试验下，注意观察所有窗口的变化

emacs中最常用的快捷键绑定为“C+n" 其中 n为任意字符;<br>
次常用绑定为“ESC n";<br>
文件操作通常为“C-x n";<br>
与编辑模式相关通常为“C-n n"<br>

##基本命令<br>
C-x C-c : 退出Emacs<br>
C-x C-f : 打开一个文件，如果文件不存在，则创建一个文件<br>
C-g : 取消未完成的命令<br>
emacs -nw :不以gui形式启动

##移动光标

C-v : 向前翻页<br>
M-v : 向后翻页<br>
M-r : 将光标移动到屏幕中间那行<br>
C-a : 移到行首<br>
M-a : 移到句首，从行首到句首之间可能有空格<br>
C-e : 移到行尾<br>
M-e : 移到句尾<br>
M-{ : 向上移动一段<br>
M-} : 向下移动一段<br>
C-right,esc-f : 向前移动一个单词<br>
C-left ,esc-b: 向后移动一个单词<br>
C-up : 向前移动一段<br>
C-down : 向后移动一段<br>
M-< : 移到整个文本开头<br>
M-> : 移到整个文本末尾<br>
M-r ： 将游标移到目前视窗的中央<br>
C-u 数字 命令 : 执行多次(数字表示次数)该命令；“M-数字 命令” 也可以<br>
M-gg(M-x goto-line) : 移动到某一行<br>
C-l : 重绘屏幕，效果就是当前编辑行移动窗口中央<br>

##窗口操作
C-x 0 : 关闭当前窗口<br>
C-x 1 : 将当前窗口最大化<br>
C-x 2 : 垂直分割窗口<br>
C-x 3 : 水平分割窗口C-u)<br>
C-x ^ : 加高当前窗口，如果有C-u，则每次加高4行<br>
(C-u) C-x } : 加宽当前窗口<br>
(C-u) C-x { : 压窄当前窗口<br>
ESC C-v : 在其它窗口进行卷屏操作搜索和替换<br>

##搜索和替换
C-s : 向前搜索（增量式搜索）；连续C-s，跳到下一个搜索到的目标<br>
C-s RET : 普通搜索<br>
C-r : 向前搜索<br>
C-s RET C-w : 按单词查询<br>
M-% : 查询替换，也就是替换前会询问一下<br>
M-x replace-string : 普通替换<br>

##Bookmark
C-x r m : 设置书签bookmark<br>
C-x r b : 跳到bookmark处<br>
esc c-n(c-m-n):调到后面对应的括号<br>
esc c-p(c-m-p):调到前面对应的括号<br>

##帮助
C-h ? : 查看帮助信息<br>
C-h f : 查看一个函数,此处的函数是指lisp语言中的某个函数的意思;<br>
C-h v : 查看一个变量<br>
C-h k : 查看一个键绑定 (C－h c 也是查看键绑定，但是信息较简略)<br>
C-h C-f : 查看一个函数的Info，非常有用<br>
C-h i : 看Info<br>

##删除命令
<Delback> 删除光标前的一个字符<br> 
C-d 删除光标后的一个字符 <br>
M-<Delback> 移除光标前的一个词<br> 
M-d 移除光标后的一个词<br>

##C模式快捷键

C-M-\ : 对选中区域，按照某种格式(比如C程序)进行格式化<br>
C-x h : 全部选中<br>
M-! : 执行外部shell命令<br>
M-x shell : 模拟shell的buffer<br>
ALT-/ : 快速补全<br>
ESC-m :把光标移到当前行的第一个非空字符上<br>
ESC-^:把当前行合并到上一行<br>
ESC ; :添加注释<br>
ESC j :下一行添加注释<br>
C-c C-a:自动换行<br>

##基本快捷键(Basic)
C-x C-f “find”文件, 即在缓冲区打开/新建一个文件<br>
C-x C-s 保存文件<br>
C-x C-w 使用其他文件名另存为文件<br>
C-x C-v 关闭当前缓冲区文件并打开新文件<br>
C-x i 在当前光标处插入文件<br>
C-x b 新建/切换缓冲区<br>
C-x C-b 显示缓冲区列表<br>
C-x k 关闭当前缓冲区<br>
C-z 挂起emacs<br>
C-x C-c 关闭emacs<br>

##光标移动基本快捷键(Basic Movement)
C-f 后一个字符<br>
C-b 前一个字符<br>
C-p 上一行<br>
C-n 下一行<br>
M-f 后一个单词<br>
M-b 前一个单词<br>
C-a 行首<br>
C-e 行尾<br>
C-v 向下翻一页<br>
M-v 向上翻一页<br>
M-< 到文件开头 注意这里是‘<’不是‘,’需要按shift，遇到相同情况下同<br>
M-> 到文件末尾<br>

##编辑(Editint)
M-n 重复执行后一个命令n次<br>
C-u 重复执行后一个命令4次<br>
C-u n 重复执行后一个命令n次<br>
C-d 删除(delete)后一个字符<br>
M-d 删除后一个单词<br>
Del 删除前一个字符<br>
M-Del 删除前一个单词<br>
C-k 移除(kill)一行<br>

C-Space 设置开始标记 (例如标记区域)<br>
C-@ 功能同上, 用于C-Space被操作系统拦截的情况<br>
C-w 移除(kill)标记区域的内容<br>
M-w 复制标记区域的内容<br>
C-y 召回(yank)复制/移除的区域/行<br>
M-y 召回更早的内容 (在kill缓冲区内循环)<br>
C-x C-x 交换光标和标记<br>

C-t 交换两个字符的位置<br>
M-t 交换两个单词的位置<br>
C-x C-t 交换两行的位置<br>
M-u 使从光标位置到单词结尾处的字母变成大写<br>
M-l 与M-u相反<br>
M-c 使从光标位置开始的单词的首字母变为大写<br>

##重要快捷键(Important)<br>
C-g 停止当前运行/输入的命令<br>
C-x u 撤销前一个命令<br>
M-x revert-buffer RETURN (照着这个输入)撤销上次存盘后所有改动<br>
M-x recover-file RETURN 从自动存盘文件恢复<br>
M-x recover-session RETURN 如果你编辑了几个文件, 用这个恢复<br>

##在线帮助(Online-Help)
C-h c 显示快捷键绑定的命令<br>
C-h k 显示快捷键绑定的命令和它的作用<br>
C-h l 显示最后100个键入的内容<br>
C-h w 显示命令被绑定到哪些快捷键上<br>
C-h f 显示函数的功能<br>
C-h v 显示变量的含义和值<br>
C-h b 显示当前缓冲区所有可用的快捷键<br>
C-h t 打开emacs教程<br>
C-h i 打开info阅读器<br>
C-h C-f 显示emacs FAQ<br>
C-h p 显示本机Elisp包的信息<br>

##搜索/替换(Seach/Replace)<br>
C-s 向后搜索<br>
C-r 向前搜索<br>
C-g 回到搜索开始前的位置(如果你仍然在搜索模式中)<br>
M-% 询问并替换(query replace)<br>

Space或y 替换当前匹配<br>
Del或n 不要替换当前匹配<br>
. 仅仅替换当前匹配并退出(替换)<br>
, 替换并暂停(按Space或y继续)<br>
! 替换以下所有匹配<br>
^ 回到上一个匹配位置<br>
RETURN或q 退出替换<br>

##使用正则表达式(Regular expression)搜索/替换
可在正则表达式中使用的符号:<br>
^ 行首<br>
$ 行尾<br>
. 单个字符<br>
.* 任意多个(包括没有)字符<br>
\< 单词开头<br>
\> 单词结尾<br>
[] 括号中的任意一个字符(例如[a-z]表示所有的小写字母)<br>

M C-s RETURN 使用正则表达式向后搜索<br>
M C-r RETURN 使用正则表达式向前搜索<br>
C-s 增量搜索<br>
C-s 重复增量搜索<br>
C-r 向前增量搜索<br>
C-r 重复向前增量搜索<br>
M-x query-replace-regexp 使用正则表达式搜索并替换<br>

##窗口命令(Window Commands)
C-x 2 水平分割窗格<br>
C-x 3 垂直分割窗格<br>
C-x o 切换至其他窗格<br>
C-x 0 关闭窗格<br>
C-x 1 关闭除了光标所在窗格外所有窗格<br>
C-x ^ 扩大窗格<br>
M-x shrink-window 缩小窗格<br>
M C-v 滚动其他窗格内容<br>
C-x 4 f 在其他窗格中打开文件<br>
C-x 4 0 关闭当前缓冲区和窗格<br>
C-x 5 2 新建窗口(frame)<br>
C-x 5 f 在新窗口中打开文件<br>
C-x 5 o 切换至其他窗口<br>
C-x 5 0 关闭当前窗口<br>

##书签命令(Bookmark commands)
C-x r m 在光标当前位置创建书签<br>
C-x r b 转到书签<br>
M-x bookmark-rename 重命名书签<br>
M-x bookmark-delete 删除书签<br>
M-x bookmark-save 保存书签<br>
C-x r l 列出书签清单<br>

d 标记等待删除
Del 取消删除标记<br>
x 删除被标记的书签<br>
r 重命名<br>
s 保存列表内所有书签<br>
f 转到当前书签指向的位置<br>
m 标记在多窗口中打开<br>
v 显示被标记的书签(或者光标当前位置的书签)<br>
t 切换是否显示路径列表<br>
w 显示当前文件路径<br>
q 退出书签列表<br>

M-x bookmark-write 将所有书签导出至指定文件<br>
M-x bookmark-load 从指定文件导入书签<br>

##Shell
M-x shell 打开shell模式<br>
C-c C-c 类似unix里的C-c(停止正在运行的程序)<br>
C-d 删除光标后一个字符<br>
C-c C-d 发送EOF<br>
C-c C-z 挂起程序(unix下的C-z)<br>
M-p 显示前一条命令<br>
M-n 显示后一条命令<br>

##DIRectory EDitor (dired)<br>
C-x d 打开dired<br>
C(大写C) 复制<br>
d 标记等待删除<br>
D 立即删除<br>
e或f 打开文件或目录<br>
g 刷新当前目录<br>
G 改变文件所属组(chgrp)<br>
k 从屏幕上的列表里删除一行(不是真的删除)<br>
m 用*标记<br>
n 光标移动到下一行<br>
o 在另一个窗格打开文件并移动光标<br>
C-o 在另一个窗格打开文件但不移动光标<br>
P 打印文件<br>
q 退出dired<br>
Q 在标记的文件中替换<br>
R 重命名文件<br>
u 移除标记<br>
v 显示文件内容<br>
x 删除有D标记的文件<br>
Z 压缩/解压缩文件<br>
M-Del 移除标记(默认为所有类型的标记)<br>
~ 标记备份文件(文件名有~的文件)等待删除<br>
# 标记自动保存文件(文件名形如#name#)等待删除<br>
*/ 用*标记所有文件夹(用C-u */n移除标记)<br>
= 将当前文件和标记文件(使用C-@标记而不是dired的m标记)比较<br>
M-= 将当前文件和它的备份比较<br>
! 对当前文件应用shell命令<br>
M-} 移动光标至下一个用*或D标记的文件<br>
M-{ 移动光标至上一个用*或D标记的文件<br>
% d 使用正则表达式标记文件等待删除<br>
% m 使用正则表达式标记文件为*<br>
+ 新建文件夹<br>
> 移动光标至后一个文件夹<br>
< 移动光标至前一个文件夹<br>
s 切换排序模式(按文件名/日期)<br>

或许把这个命令归入这一类也很合适:<br>
M-x speedbar 打开一个独立的目录显示窗口<br>

##Telnet（大致了解）<br>
M-x telnet 打开telnet模式<br>
C-d 删除后一个字符或发送EOF<br>
C-c C-c 停止正在运行的程序(和unix下的C-c类似)<br>
C-c C-d 发送EOF<br>
C-c C-o 清除最后一个命令的输出<br>
C-c C-z 挂起正在运行的命令<br>
C-c C-u 移除前一行<br>
M-p 显示前一条命令<br>

##Text
只能在text模式里使用<br>
M-s 使当前行居中<br>
M-S 使当前段落居中<br>
M-x center-region 使被选中的区域居中<br>

##宏命令(Macro-commands)（大致了解）
C-x ( 开始定义宏<br>
C-x ) 结束定义宏<br>
C-x e 运行最近定义的宏<br>
M-n C-x e 运行最近定义的宏n次<br>
M-x name-last-kbd-macro 给最近定义的宏命名(用来保存)<br>
M-x insert-kbd-macro 将已命名的宏保存到文件<br>
M-x load-file 载入宏<br>

##编程(Programming)
M C-\ 自动缩进光标和标记间的区域<br>
M-m 移动光标到行首第一个(非空格)字符<br>
M-^ 将当前行接到上一行末尾处<br>
M-; 添加缩进并格式化的注释<br>
C, C++和Java模式<br>
M-a 移动光标到声明的开始处<br>
M-e 移动光标到声明的结尾处<br>
M C-a 移动光标到函数的开始处<br>
M C-e 移动光标到函数的结尾处<br>
C-c RETURN 将光标移动到函数的开始处并标记到结尾处<br>
C-c C-q 根据缩进风格缩进整个函数<br>
C-c C-a 切换自动换行功能<br>
C-c C-d 一次性删除光标后的一串空格(greedy delete)<br>

为了实现下面的一些技术, 你需要在保存源代码的目录里运行”etags<br>
*.c *.h *.cpp”(或者源代码的其他的扩展名)<br>
M-.(点) 搜索标签<br>
M-x tags-search ENTER 在所有标签里搜索(使用正则表达式)<br>
M-,(逗号) 在tags-search里跳至下一个匹配处<br>
M-x tags-query-replace 在设置过标签的所有文件里替换文本<br>

##GDB(调试器)（大致了解）
M-x gdb 在另一个的窗格中打开gdb<br>

版本控制(Version Control)（以后会用到现在大致了解就可以了）
C-x v d 显示当前目录下所有注册过的文件(show all registered files in this dir)<br>
C-x v = 比较不同版本间的差异(show diff between versions)<br>
C-x v u 移除上次提交之后的更改(remove all changes since last checkin)<br>
C-x v ~ 在不同窗格中显示某个版本(show certain version in different window)<br>
C-x v l 打印日志(print log)<br>
C-x v i 标记文件等待添加版本控制(mark file for version control add)<br>
C-x v h 给文件添加版本控制文件头(insert version control header into file)<br>
C-x v r 获取命名过的快照(check out named snapshot)<br>
C-x v s 创建命名的快照(create named snapshot)<br>
C-x v a 创建gnu风格的更改日志(create changelog file in gnu-style)<br>

##文件操作：
C+x C+f<br>
打开文件<br>
C+x C+r<br>
以只读的方式打开文件<br>
C+x C+q<br>
进行 只读/读写 模式切换<br>
C+x C+v<br>
切换缓冲区<br>
C+x C+s<br>
保存文件<br>
C+x C+w<br>
文件另存为<br>
C+x i<br>
 向缓冲区中插入文件<br>
<br>
移动操作：C+f  <br>
前进一个字符C+b <br>
后退一个字符M+f  <br>
前进一个单词M+b <br>
后退一个单词C+a  <br>
移动到行首C+e  <br>
移动到行尾M+a  <br>
移动到句首M+e  <br>
移动到句尾C+p  <br>
后退一行C+n  <br>
前进一行M+g g <br>
跳到指定行C+v  <br>
向下翻页M+v  <br>
向上翻页M+< 移动到缓冲区首M+> <br>
移动到缓冲区尾C+M+f <br>
向前匹配括号C+M+b<br>
向后匹配括号标记/复制/剪切/粘贴：C+xh <br>
全选C+@   <br>
标记开始M+w   <br>
复制区域到kill ring中，但不删除C+w    <br>
删除区域C+y    <br>
将kill ring 中的内容粘贴到缓冲区C+Del <br>
剪切光标到单词结束M+Del <br>
剪切光标到单词开始C+k    <br>
剪切光标到行结尾M+k    <br>
剪切光标到句结尾(C+d)/Del   <br>
删除光标上的字M+d   <br>
剪切光标到下一个单词结尾ctrl-S(shift+s)-Backspace  <br>
删除当前行<br>

##缓冲区操作：

C+x C+f 打开/创建一个文件，并创建一个新的缓冲区<br>
C+x C+s  保存缓冲区内容到文件<br>
C+x C+w  保存缓冲区内容到其它文件<br>
C+xk    关闭当前缓冲区<br>
C+x C+b 显示缓冲区列表，可以使用方向键来选择缓冲区<br>
C+x C+c  关闭所有缓冲区，并推出emacs<br>

##M+x命令：

##查找和替换：<br>
C+s 向前查找C+r 向后查找按下这两个快捷键后，<br>
M+p显示上一个搜索词，<br>
M+n显示下一个搜索词。输入查找内容后，按C+s跳到下一个结果，<br>
C+r跳到上一个结果。<br>
Enter结束查找光标在当前位置，C+g取消查找光标返回原处。<br>

2，查找单词

按C - s RET C - w 或 C - r RET C - w 来使用单词搜索。<br>

3，查找及替换<br>

按M - %启动查找替换，输入要被替换的词，回车，然后输入要替换的词，再回车。<br>

被替换的词会高亮起来，这时，输入y替换并跳到下一个，输入n忽略并跳到下一个，输入q结束，输入！替换剩下的全部。<br>

一些常用的选项：<br>

　　C - g 中断查找替换过程。<br>

　　^ 返回上一个替换点，按y继续下一个，如果不想替换上一个的话，用^返回到上一个，然后按 C - r 进入编辑，修改完后按C- M - c退出继续下一个。<br>

　　C - l 使当前匹配显示在文档中间。<br>

　　C - r 进入修改。<br>

4，列出匹配的模式<br>

有时候想列出匹配的全面模式，而不是在文档中浏览，这个可以使用occur这个函数。<br>

例子：M - x occur RET Create RET<br>

这时，emacs会新开一个窗口来列出匹配的行，用鼠标点击或把光标移到一行按回车就会跳转到那里。<br>

执行SHELL命令<br>
M-x shell<br>
打开shell命令<br>
M-!<br>
执行shell命令（shell-command）<br>
M-1 M-!<br>
执行Shell命令，命令输出插入光标位置，不打开新输入窗口<br>
M-|<br>
针对某一特定区域执行命令(shell-command-on-region),比如 C-x h M-juuencode<br>

##窗口操作
C-x 0<br>
关闭本窗口<br>
C-x 1
只留下一个窗口<br>
C-x 2
垂直均分窗口<br>
C-x 3
水平均分窗口<br>
C-x o
切换到别的窗口<br>
C-x s
保存所有窗口的缓冲<br>
C-x b
选择当前窗口的缓冲区<br>
C-x ^
纵向扩大窗口<br>
C-x }
横向扩大窗口<br>


##目录操作
C-x d
打开目录模式<br>
s
按日期/文件名排序显示<br>
v
阅读光标所在的文件<br>
q
退出阅读的文件<br>
d
标记为删除<br>
x
执行标记<br>
D
马上删除当前文件<br>
C
拷贝当前文件
R
重命名当前文件
+
新建文件
Z
压缩文件
！
对光标所在的文件执行SHELL命令
g
刷新显示
i
在当前缓冲区的末尾插入子目录的内容
[n]m
标记光标所在的文件，如果指定n,则从光标所在的文件后n个文件被标记
[n]u
取消当前光标标记的文件，n的含义同上
t
反向标记文件
%-m
正则标记
q
退出目录模式

##其他：
C+x u 撤销
C+x C+c 退出emacs


#Emacs Python开发环境配置
##1 Emacs安装
1. 安装Emacs
sudo apt-get install emacs24

接下来安装pip，很好用的Python包管理工具，用来安装Python模块。
sudo apt-get install python-pip #Python2 
sudo apt-get install python3-pip #Python3 

然后用pip安装elpy、rope、jedi模块
sudo pip install elpy rope jedi #Python2
sudo pip3 install elpy rope_py3k jedi #Python3

输入emacs &，即可打开IDE
注：编写init.el时，可以用emacs --debug-init命令打开调试模式，查看错误信息

##3 安装Python中的插件包

    IPython
    rope 重构工具
    jedi 补全工具
    flake8 代码检查工具
    importmagic 自动导入工具
    autopep8
    yapf 代码format

#python -m pip install ipython jedi flake8 importmagic autopep8 yapf
python -m pip install ipython jedi flake8 importmagic autopep8 yapf elpy rope_py3k
pip3 install ipython jedi flake8 importmagic autopep8 yapf elpy rope_py3k -i https://pypi.douban.com/simple/
注：需要先安装pip,setuptools,wheel (最好先修改pip使用国内源，或者在命令后用-i参数指定)
pip3 install wheel
pip3 install --upgrade setuptools
pip3 install setuptools

##4 配置Emacs
　　这里首先参考了Steve Purcell的配置方案，可以从这里（https://github.com/purcell/emacs.d）下载。主要配置文件在~/.emacs.d/init.el 中，下载文件：
git clone https://github.com/purcell/emacs.d.git ~/.emacs.d
　　如果报错说./emacs.d 文件已存在，则可以先删除此文件。下载完毕后，重启Emacs，重启后，所需的第三方插件会自动下载并安装。如果遇到错误，重启Emacs 或者在重启前运行M-x package-refresh-contents 即可。

##5 进阶配置—自动补齐和行号显示
在~/.emacs.d/init.el，写入以下内容，以初始化package.el并添加插件源：

(require 'package)  
(setq package-archives  
      '(("gnu" . "http://elpa.gnu.org/packages/")  
        ("marmalade" . "http://marmalade-repo.org/packages/")  
        ("melpa" . "http://melpa.milkbox.net/packages/")))  
(package-initialize) 

重启Emacs，使用M-x package-install [Enter] elpy [Enter]来安装（Enter即回车键）。也可以使用命令M-x list-packages获取插件列表，使用C-s找到elpy来安装。

Emacs插件源配置
输入 M-x package-refresh-contents，刷新package信息
使用M-x package-install 安装插件，如下安装 auto-complete
M-x package-install[ret]auto-complete [ret]
使用M-x package-list列出可以安装的插件扩展列表

接着，在在init.el文件中添加如下内容：
复制代码

;; Configuration of Python IDE  
;; https://github.com/jorgenschaefer/elpy  
(require 'elpy nil t)  
(elpy-enable) 

(setq elpy-rpc-python-command "python3")  ;; python3
(elpy-use-ipython)                        ;; ipython

复制代码
重启Emacs。至此Python IDE就算完成了。新建一个Python文件（C-x C-f，输入文件名），开始你的Python之旅吧，你会发现自动补全，语法错误检测，语法模板显示等功能都已经存在了。

如果你希望显示代码的行号，则将以下语句写入init.el文件。

(global-linum-mode t)  ;;显示行号

##emacs中的package包管理
该插件非常方便，首先添加以下代码到.emacs中，然后M-x package-list-packages
(require 'package)
(add-to-list 'package-archives '(“marmalade” . “http://marmalade-repo.org/packages/”) t)
(add-to-list 'package-archives '(“elpa” . “http://tromey.com/elpa/”) t)
(add-to-list 'package-archives '(“melpa” . “http://melpa.milkbox.net/packages/”) t)
(package-initialize)

常用快捷键,
i - 选择要安装的包
d - 选择要删除的包
U - 升级已安装的包
x - 执行操作
d - 选择要删除的包

##Emacs中设置字体，显示行号
1 设置字体
我暂时使用的是Windows Emacs自带的字体，在Options–Set Default Font 查询选择需要的字体，然后保存即可。
鉴于以上方法可能不会一直起效，可在.emacs文件添加：
(set-default-font “Consolas 14”)
其中，Consolas是字体名，14是字号，近几个Emacs版本才支持这种写法。
若此方法不可行，可在Options选择字体后，通过M-x describe-font查看字体信息，在.emacs添加：
(set-default-font “-outline-Courier New-normal-italic-normal-mono-16----c--iso8859-1″)
其中，“-outline-Courier New-normal-italic-normal-mono-16----c--iso8859-1”为字体信息，16 为字号

2 显示行号
可能所选择的主题没有设置行号，可在.emacs文件添加：
(global-linum-mode 1) ；1表示行号常显
(setq linum-format “%d “)；注意%d后有空格，即用空格将行号和代码隔开。
保存重启即可。

##安装新主题
设置好了package源，现在可以给Emacs安装新的扩展了。
M-x list-packages 进入package列表，如果你已经在这个界面，按 “r” 键来刷新，重写连接。
以安装Solarized主题为例，按C-s来搜索 “solarized”. 如下图所示，把光标放在“Solarized”那行，按“i”键，将其标记为“要安装的”，然后按“x”键执行标记为“i”的项目，这里仅仅标记这一个。
solarized_theme.jpg
安装过程中会提示你是否要执行未经安全确认的ELisp脚本之类的，选“yes”就行了。装完这个主题之后，使用M-x customize-themes进入主题切换界面，可以看到Solarized Dark和Solarized Light两种风格可供选择。这里假设选择了Solarized Dark主题，并且保存为长期使用。此时打开你的Emacs配置文件会看到如下内容：
(custom-set-variables
 '(custom-enabled-themes (quote (solarized-dark)))
 '(custom-safe-themes (quote ("8aebf25556399b58091e533e455dd50a6a9cba958cc4ebb0aab175863c25b9a4" default)))

可以看到，新安装的主题配置已经写入Emacs配置。如果你此时重启Emacs，进来后会发现主题没有保存下来。这是因为在执行这段主题配置脚本时，Solarized包还没有加载。因此要想让设置生效，需要在这段脚本上面初始化packages，在你的.emacs(或者init.el)文件最上方加入这句：
(package-initialize)
它会初始化packages，确保随后的配置生效。

##Emacs安装一个扩展包的方法
假定扩展包的名字叫作 xxx.el 通常情况下,安装方法如下.
    拷贝 xxx.el 到 ~/Emacs/download.elisp 下
    在 .emacs 中写入
(add-to-list 'load-path "~/Emacs/download.elisp")
    如果你的 .emacs 已经有了这句话， 就不用再写了。

    在 .emacs 中写入
(require 'xxx)
    这样基本就可以用了。然后注意 xxx.el 文件的开头 部分，一般 xxx.el 的作者会在那里纪录基本配置方 法和使用方法。有可能的话，可以从那里抄一些语句 到 .emacs 中了。
    重新启动 Emacs
    如果你不想重新启动 Emacs ， 也可以
 M-x load-file ~/.emacs 
    或者用 Emacs 打开 .emacs ，然后
 M-x eval-buffer

##6 进阶配置—IPython/Jupyter集成

接下来这个功能尤其强大：将Emacs与IPython REPL和Jupyter Notebooks集成。首先，你可以将Emacs中标准的Python REPL集成替换为IPython版本，之后如果按下C-c C-c再次运行Python代码，使用的将是IPython REPL。

M-x  elpy-use-ipython

尽管做到目前这样已经非常有用了，但是真正的神奇之处还在Emacs与Jupyter notebook之间的集成。为了在emacs 中使用jupyter notebook，我们要首先安装 ein（emacs ipython notebook）。首先，在~/.emacs.d/init.el，写入以下内容，

(defvar myPackages
  '(better-defaults
    ein ;; add the ein package (Emacs ipython notebook)
    py-autopep8))

然后安装重启emacs，安装ein：　

package-install [enter] ein [enter]

为了在emas中使用jupyter notebook，我们要首先在ubuntu的shell 中打开jupyter notebook 以等待连接，然后在emacs中输入
	
M-x ein:notebooklist-open
选择默认notebook的默认网络接口8888，打开或创建相应文件夹即可。emacs简直就是神器啊！！！　　

像Eclipse等IDE能有的功能，Emacs都可以实现。很多优秀的Emacs插件都可以直接通过M-x list-packages安装，一个简单的配置文件，就可以把Python IDE配置好！



#将emacs配置成好用的python IDE环境
##安装需要的安装包
首先配置虚拟环境：
    安装virtualenvwrapper 可以使用apt install virtualenvwrapper
    创建一个虚拟环境 mkvirtualenv -p /usr/bin/python3 python3
    然后就可以在python3的环境下操作，此时可能这个命令会报错，这就需要执行以下步骤：
    将以下字段添加到~/.bashrc 之中：

export WORKON_HOME=$HOME/.virtualenvs
source /usr/local/bin/virtualenvwrapper.sh

    使之生效，就在terminal中运行 source ~/.bashrc
    
    列出虚拟环境列表：workon 或者 lsvirtualenv
    再新建一个虚拟环境，可以使用：mkvirtualenv
    切换虚拟环境，可以使用：workon (虚拟环境名称)
    删除虚拟环境，可以使用：rmvirtualenv (虚拟环境名称)
    离开虚拟环境，可以使用：deactivate

对于python：
    需要确保安装了pip。
    需要安装 pylint，elpy，jedi 和 rope，使用pip install jedi elpy rope pylint
    pylint就不说了，看名字就知道。jedi是用于自动补全，rope是一个用于重构的库。

对于 emacs：
    打开emacs，然后是M-x package-list-packages 似乎没有看到需要安装的包，这就需要编辑一下配置文件

    打开 ~/.emacs.d/init.el ， 如果没有就新建一个，加上仓库源地址的字段：
    (setq package-archives '(
    ("gnu" . "http://elpa.gnu.org/packages/")
    ("melpa" . "http://melpa.milkbox.net/packages/")
    ))

    现在重复第二步，就可以看到emacs的插件列表，此时我们需要安装以下插件：
    elpy
    flycheck
    company-jedi
    virtualenvwrapper

    将自动补全设置成jedi：

;; enable elpy jedi backend
(setq elpy-rpc-backend "jedi")

    设置自动扩展，比方说，for之后按下如下所示的组合键，就自动展开为一个for语句
;; Fixing a key binding bug in elpy
(define-key yas-minor-mode-map (kbd "C-c k") 'yas-expand)

    用于重构，比方说，将光标放在某个单词上，按下如下所示的组合键，就选中了当前文件中所有的这个单词。
;; Fixing another key binding bug in iedit mode
(define-key global-map (kbd "C-c o") 'iedit-mode)

秀一下我当前使用的配置：
;;; package --- summary or add python emacs mode: elpy
;; add repository

(require 'package)
(setq package-archives '(
             ("gnu" . "http://elpa.gnu.org/packages/")
             ("melpa" . "http://melpa.milkbox.net/packages/")
             ))
(add-to-list 'package-archives
         '("marmalade" . "http://marmalade-repo.org/packages/"))
(package-initialize)

;; automatical complete: company
(require 'company)
(add-hook 'after-init-hook 'global-company-mode); global enable
(setq company-show-numbers t); display serial number
(setq company-idle-delay 0.2); menu delay
(setq company-minimum-prefix-length 1); start completelyness number

;; elpy-- main actor
(require 'elpy)
(elpy-enable)
;; enable elpy jedi backend
(setq elpy-rpc-backend "jedi")

;; Fixing a key binding bug in elpy
(define-key yas-minor-mode-map (kbd "C-c k") 'yas-expand)
;; Fixing another key binding bug in iedit mode
(define-key global-map (kbd "C-c o") 'iedit-mode)

;; grammal check: flycheck
(add-hook 'after-init-hook #'global-flycheck-mode);global enable
                    ; close flymake,  start flycheck
(when (require 'flycheck nil t)
  (setq elpy-modules(delq 'elpy-module-flymake elpy-modules))
  (add-hook 'elpy-mode-hook 'flycheck-mode))

;; virutal environment:  virtualenvwrapper
(require 'virtualenvwrapper)
(venv-initialize-interactive-shells)
(venv-initialize-eshell)
(setq venv-location "~/pyvirtualenv/"); setup virtual environment folder
;; if there multiple folder:
;; (setq venv-location '("~/myvenv-1/"
;;                       "~/myvenv-2/"))
;; M-x venv-workon open virtual environment

;;; Commentary:

;; 自动完成
(require 'company)
(global-company-mode t); 全局开启

(setq company-idle-delay 0.2;菜单延迟
      company-minimum-prefix-length 1; 开始补全字数
      company-require-match nil
      company-dabbrev-ignore-case nil
      company-dabbrev-downcase nil
      company-show-numbers t; 显示序号
      company-transformers '(company-sort-by-backend-importance)
      company-continue-commands '(not helm-dabbrev)
      )
                    ; 补全后端使用anaconda
(add-to-list 'company-backends '(company-anaconda :with company-yasnippet))
                    ; 补全快捷键
(global-set-key (kbd "<C-tab>") 'company-complete)
                    ; 补全菜单选项快捷键
(define-key company-active-map (kbd "C-n") 'company-select-next)
(define-key company-active-map (kbd "C-p") 'company-select-previous)

;; 在python模式中自动启用
(add-hook 'python-mode-hook 'anaconda-mode)

