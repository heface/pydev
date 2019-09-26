#如何在Linux下使用Markdown进行文档工作
在Linux系统中，编辑markdown可以用retext工具：
sudo apt-get install retext
retext Release-Notes.md

要将markdown文件转换成html文件，可以用discount
sudo apt-get install discount

转换工作很简单：
markdown -o Release-Notes.html Release-Notes.md

我们也可以在文档目录下放置这样一个Makefile来自动这个过程
MD = markdown
MDFLAGS = -T
H2PFLAGS = --html
SOURCES := $(wildcard *.md)
OBJECTS := $(patsubst %.md, %.html, $(wildcard *.md))
build: html
html: $(OBJECTS)
$(OBJECTS): %.html: %.md
    $(MD) $(MDFLAGS) -o $@ $

#markdown 简单语法
代码包裹```
标题==== ---- # ###
斜体** 粗体 **** 粗斜体 ******
连接 <>   []()
列表  无序 *-+ 有序 1. 2. 嵌套 缩进
引用 >
图片地址 ![图片](地址)
换行 结尾加俩个空格
另起一段 空出一行
分隔符  新起一行  --- 前后都有段落，都要空一行
转义   \

#markdown查看器：Typora
一、windows下使用

    官网下载安装即可
    https://www.typora.io/#windows

二、linux下使用，可以用命令行的方式进行安装

# or run:
# sudo apt-key adv --keyserver keyserver.ubuntu.com --recv-keys BA300B7755AFCFAE
wget -qO - https://typora.io/linux/public-key.asc | sudo apt-key add -

# add Typora's repository
sudo add-apt-repository 'deb https://typora.io/linux ./'
sudo apt-get update

# install typora
sudo apt-get install typora

#linux下查看markdown

将markdown转换成html查看。

要将markdown文件转换成html文件，可以用discount或python-markdown软件包提供的markdown
# Debian/Ubuntu
sudo apt-get install discount

或：
# Debian/Ubuntu
sudo apt-get install python-markdown

转换工作很简单：
# 用discount提供的markdown工具
markdown -o Release-Notes.html Release-Notes.md
# 用python-markdown提供的markdown_py工具
markdown_py -o html4 Release-Notest.md > Release-Notes.html

如果要生成PDF，也很简单，可以用python-pisa提供的xhtml2pdf：
# Debian/Ubuntu
sudo apt-get install python-pisa

# 将html转换成PDF
xhtml2pdf --html Release-Notes.html Release-Notes.pdf

所以，你可以在文档目录下放置这样一个Makefile来自动这个过程：
复制代码
# Makefile
MD = markdown
MDFLAGS = -T
H2P = xhtml2pdf
H2PFLAGS = --html
SOURCES := $(wildcard *.md)
OBJECTS := $(patsubst %.md, %.html, $(wildcard *.md))
OBJECTS_PDF := $(patsubst %.md, %.pdf, $(wildcard *.md))

all: build
build: html pdf
pdf: $(OBJECTS_PDF)
html: $(OBJECTS)

$(OBJECTS_PDF): %.pdf: %.html
    $(H2P) $(H2PFLAGS) $< > $@ 

$(OBJECTS): %.html: %.md
    $(MD) $(MDFLAGS) -o $@ $<
clean:
    rm -f $(OBJECTS)

复制代码

这样你就可以通过简单的一个命令生成当前目录下所有md文件的pdf或html输出了：

# html 输出
make html

# pdf输出
make pdf

这里有个问题是如果markdown的内容是中文，那么转换出来的html在浏览器中打开就无法自动识别编码，pdf更惨，直接是一堆乱码。这时我们可以借助markdown对html标记的支持来在markdown文件中加入编码信息。例如我们要将markdown转换为html4文件，可以在文件的开头加上meta标记，指明编码格式：

sed -i '1i\<meta http-equiv="content-type" content="text/html; charset=UTF-8">' *.md

这样就可以了。另外，最近使用图灵社区的编辑系统时，markdown会时不时将下划线（_）当作斜体的标记，结果函数名就成了这样的：
# 实际上是ssl_use_cabundle
sslusecabundle

我建议斜体字标记采用单个星号（*），加粗字体采用两个星号（**），这样使用起来就方便多了。当然，这个问题本身在于markdown说用星号或下划线都可以。但实际上，两个都支持反倒会造成一些问题。比如有的地方用下划线（__粗体__ -> 粗体），有的地方用星号（**粗体** -> 粗体），看起来反倒混乱不堪（选星号*的另一个理由是下划线在内容中出现的概率比星号高很多）。


#基本语法
一、标题

在想要设置为标题的文字前面加#来表示
一个#是一级标题，二个#是二级标题，以此类推。支持六级标题。

注：标准语法一般在#后跟个空格再写文字，貌似简书不加空格也行。

示例：

# 这是一级标题
## 这是二级标题
### 这是三级标题
#### 这是四级标题
##### 这是五级标题
###### 这是六级标题

效果如下：
这是一级标题
这是二级标题
这是三级标题
这是四级标题
这是五级标题
这是六级标题
二、字体

    加粗

要加粗的文字左右分别用两个*号包起来

    斜体

要倾斜的文字左右分别用一个*号包起来

    斜体加粗

要倾斜和加粗的文字左右分别用三个*号包起来

    删除线

要加删除线的文字左右分别用两个~~号包起来

示例：

**这是加粗的文字**
*这是倾斜的文字*`
***这是斜体加粗的文字***
~~这是加删除线的文字~~

效果如下：

这是加粗的文字
这是倾斜的文字
这是斜体加粗的文字
这是加删除线的文字
三、引用

在引用的文字前加>即可。引用也可以嵌套，如加两个>>三个>>>
n个...
貌似可以一直加下去，但没神马卵用

示例：

>这是引用的内容
>>这是引用的内容
>>>>>>>>>>这是引用的内容

效果如下：

    这是引用的内容

        这是引用的内容

                                        这是引用的内容

四、分割线

三个或者三个以上的 - 或者 * 都可以。

示例：

---
----
***
*****

效果如下：
可以看到，显示效果是一样的。
五、图片

语法：

![图片alt](图片地址 ''图片title'')

图片alt就是显示在图片下面的文字，相当于对图片内容的解释。
图片title是图片的标题，当鼠标移到图片上时显示的内容。title可加可不加

示例：

![blockchain](https://ss0.bdstatic.com/70cFvHSh_Q1YnxGkpoWK1HF6hhy/it/
u=702257389,1274025419&fm=27&gp=0.jpg "区块链")

效果如下：

blockchain

上传本地图片直接点击导航栏的图片标志，选择图片即可
六、超链接

语法：

[超链接名](超链接地址 "超链接title")
title可加可不加

示例：

[简书](http://jianshu.com)
[百度](http://baidu.com)

效果如下：

简书
百度

注：Markdown本身语法不支持链接在新页面中打开，貌似简书做了处理，是可以的。别的平台可能就不行了，如果想要在新页面中打开的话可以用html语言的a标签代替。

<a href="超链接地址" target="_blank">超链接名</a>

示例
<a href="https://www.jianshu.com/u/1f5ac0cf6a8b" target="_blank">简书</a>

七、列表

    无序列表

语法：
无序列表用 - + * 任何一种都可以

- 列表内容
+ 列表内容
* 列表内容

注意：- + * 跟内容之间都要有一个空格

效果如下：

    列表内容

    列表内容

    列表内容

    有序列表

语法：
数字加点

1.列表内容
2.列表内容
3.列表内容

注意：序号跟内容之间要有空格

效果如下：

1.列表内容
2.列表内容
3.列表内容

    列表嵌套

上一级和下一级之间敲三个空格即可

    一级无序列表内容
        二级无序列表内容
        二级无序列表内容
        二级无序列表内容

    一级无序列表内容
        二级有序列表内容
        二级有序列表内容
        二级有序列表内容

    一级有序列表内容
        二级无序列表内容
        二级无序列表内容
        二级无序列表内容

    一级有序列表内容
        二级有序列表内容
        二级有序列表内容
        二级有序列表内容

八、表格

语法：

表头|表头|表头
---|:--:|---:
内容|内容|内容
内容|内容|内容

第二行分割表头和内容。
- 有一个就行，为了对齐，多加了几个
文字默认居左
-两边加：表示文字居中
-右边加：表示文字居右
注：原生的语法两边都要用 | 包起来。此处省略

示例：

姓名|技能|排行
--|:--:|--:
刘备|哭|大哥
关羽|打|二哥
张飞|骂|三弟

效果如下：
姓名 	技能 	排行
刘备 	哭 	大哥
关羽 	打 	二哥
张飞 	骂 	三弟
九、代码

语法：
单行代码：代码之间分别用一个反引号包起来

    `代码内容`

代码块：代码之间分别用三个反引号包起来，且两边的反引号单独占一行

(```)
  代码...
  代码...
  代码...
(```)

    注：为了防止转译，前后三个反引号处加了小括号，实际是没有的。这里只是用来演示，实际中去掉两边小括号即可。

示例：

单行代码

`create database hero;`

代码块

(```)
    function fun(){
         echo "这是一句非常牛逼的代码";
    }
    fun();
(```)

效果如下：

单行代码

create database hero;

代码块

function fun(){
  echo "这是一句非常牛逼的代码";
}
fun();




#pandoc
If you need to convert files from one markup format into another, pandoc is your swiss-army knife. Pandoc can convert between the following formats:

(← = conversion from; → = conversion to; ↔︎ = conversion from and to)

Lightweight markup formats

    ↔︎ Markdown (including CommonMark and GitHub-flavored Markdown)
    ↔︎ reStructuredText
    → AsciiDoc
    ↔︎ Emacs Org-Mode
    ↔︎ Emacs Muse
    → Textile
    ← txt2tags
HTML formats

    ↔︎ (X)HTML 4
    ↔︎ HTML5
Ebooks

    ↔︎ EPUB version 2 or 3
    ↔︎ FictionBook2
Documentation formats

    → GNU TexInfo
    ↔︎ Haddock markup
Roff formats

    ↔︎ roff man
    → roff ms
TeX formats

    ↔︎ LaTeX
    → ConTeXt
XML formats

    ↔︎ DocBook version 4 or 5
    ↔︎ JATS
    → TEI Simple
Outline formats

    ↔︎ OPML

Word processor formats

    ↔︎ Microsoft Word docx
    ↔︎ OpenOffice/LibreOffice ODT
    → OpenDocument XML
    → Microsoft PowerPoint
Interactive notebook formats

    ↔︎ Jupyter notebook (ipynb)
Page layout formats

    → InDesign ICML
Wiki markup formats

    ↔︎ MediaWiki markup
    ↔︎ DokuWiki markup
    ← TikiWiki markup
    ← TWiki markup
    → Vimwiki markup
    → XWiki markup
    → ZimWiki markup
    → Jira wiki markup
Slide show formats

    → LaTeX Beamer
    → Slidy
    → reveal.js
    → Slideous
    → S5
    → DZSlides
Custom formats

    → custom writers can be written in lua.
PDF

    → via pdflatex, xelatex, lualatex, pdfroff, wkhtml2pdf, prince, or weasyprint.

