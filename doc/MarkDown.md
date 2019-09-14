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


pandoc
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

