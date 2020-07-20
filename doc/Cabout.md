# 编译C程序，使用stdio.h之前，需要安装build-essential
sudo apt-get update
sudo apt-get install build-essential
 

# gcc编译
一步到位编译：gcc hello.c -o hello
预处理 -E (.i) 编译 -S (.s) 汇编-c (.o) 连接-o
预处理
gcc -E hello.c -o hello.i -E:仅执行编译预处理
-o:将结果输出并指定输出文件的文件名
编译为汇编代码
gcc -S hello.c(.i) -o hello.s -S：将C代码转换为汇编代码
汇编：
gcc -c hello.c -o hello.o -c：仅执行编译操作，不进行连接操作
连接：
gcc hello.o -o hello
-o:将结果输出并指定输出文件的文件名
-O0、-O1、-O2、-O3:编译优化选项的四个级别，-O0 表示没有优化, -O1 为默认值，-O3 优化级别最高
-g：只是编译器，在编译的时候，产生调试信息

# gcc详解
GCC仅仅是一个编译器，不是IDE，没有界面，只能在命令行下使用。GCC是可以直接完成源文件的编译。经常使用的命令就是直接生成一个可执行文件。

gcc 源文件 -o 可执行文件
这样的方式，可以把源文件直接编译为可执行文件，并且为可执行文件指定名称。更加简单的编译命令如下

gcc 源文件
这样生成的可执行文件，默认名字是a.out。例如：

可以看到，默认生成的可执行文件名字就是a.out。这个.out后缀对于Linux是没有意义的，Linux的文件类型就是那么几类。它不依文件后缀来区分文件类型。下面按照指定可执行文件的名称来编译一次。

 GCC是可以分步编译源文件的。其过程正如学习C语言的时候讲述的一致，如下图所示。
          打开helloworld.i文件可以看到，头文件会被包含进来。形成一个很大的文件。接下来，将预处理过的文件进行编译。

    预处理使用选项“-E”。预处理阶段展开宏，文件包含，条件编译。在正常情形下，GCC不会保留预处理阶段的文件，但是使用-E选项可以保留。例如
    编译是对上面的.i文件进行的，编译完成以后生成汇编文件。
    gcc -S helloworld.i -o helloworld.s

    打开 helloworld.s文件，可以看到汇编语言。
    汇编，将上面生成的汇编语言编译为目标机器的二进制文件。只汇编，不链接。

    　gcc -c helloworld.s -o helloworld.o

    链接，链接器把多个二进制的目标文件（.o文件）链接成一个单独的可执行文件。在链接过程中，它必须把符号（变量名、函数名等一些列标识符）用对应的数据的内存地址（变量地址、函数地址等）替代，以完成程序中多个模块的外部引用。最终生成可执行文件。

    gcc helloworld.o -o helloworld

    上面的代码很简单，不需要链接什么，直接生成可执行文件。

当头文件和源文件非常多的时候，使用GCC基本命令编译是非常麻烦的。每次调试都需要重新编译。这时候你可能会想到使用IDE吧！不使用GCC了。不能一键编译，好蠢，好麻烦。幸运的是，虽然GCC没有自动项目管理工具，但是它提供了Makefile文件来帮助我们提高写程序的效率。

GCC可以使用-O0，-O1，-O2，-O3可以优化程序。O0表示不优化，O3表示优化等级最高。

GCC使用-Wall来打印警告信息，这样有助于调试程序。

GCC使用-w来忽略所有的警告。

GCC使用-g包含调试信息，这在使用gdb调试的时候是必要的。

GCC使用-static来阻止使用共享库。

C99规定新的for循环语法，借鉴于C++ : for(int i=1; i <= n; i++){......}
此时i只在for循环中有效，注意用gcc编译时需加上选项 -std=c99

# 参考书
《The C Programming Language》（作者Kernighan和Ritchie，中译名《C程序设计语言》）堪称经典中的经典，不过旧版的内容已过时，看最新的版本。
《C语言参考手册》就是《C Reference Manual》，是C语言标准的详细描述，最好的标准C语言的工具书。最新的《C程序设计语言》是根据C89标准修订的，而《C语言参考手册》描述的是C99标准，二者可能会有些出入。
《C和指针》，写得也是相当地不错，英文名是《Pointers on C》，特别地强调指针的重要性，算是本书的一个特点吧。
《C Traps and Pitfalls》（中译名《C陷井与缺陷》），这本书是二十多年前写成的，里面提到的很多C语言的缺陷都已被改进，不过能够了解一些历史也不是什么坏事。
《Expert C Programming》（中译名《C专家编程》），书如其名，这本书颇具难度，一旦仔细读完并能透彻理解，可以放心大胆地在简历上写“精通C语言”。

1.emacs hehe.c创建并打开hehe.c文件，录入程序
2.保存所编写的程序，命令是C-x,C-s，(先按ctrl+x,再按ctrl+s) 
3.编译程序。
通过命令M-x (alt+x)shell或M-x eshell进行shell模式，然后使用gcc -Wall -o hehe hehe.c进行编译，如果没有安装gcc，请先安装gcc
4.切换回编辑区: c-x b ’buffername‘可以切换到某个buffer，如要切换回刚才那个hehe.c编辑区,输入c-x b "buffername"(例如先按ctrl+x 再输入b 再输入hehe.c)。有木有发现，emacs比vi好用多了。
 
# emacs缩进-差点崩溃，直接复制到init.el中去了，确实管用
emacs很强大，但是强大是以复杂的配置为前提的！没有配置好的时候，可能它比notepad还要难用。
前一段时间我就被缩进弄得晕头转向，tab经常是缩进5个空格，源码会乱，等等，我都几乎要放弃emacs了。
今天偶然看了看emacs自带的manual中的cc-mode一节，哇，发现新大陆了！不光讲得很细，还有个例子，拷过来就可以用了，那缩进，怎一个酷字了得！
后来又参考了王垠、ann77的主页，将tab和缩进基本搞定，下面是配置内容：

(setq indent-tabs-mode nil)
(setq default-tab-width 4)
(setq tab-width 4)
(setq tab-stop-list ())
(loop for x downfrom 40 to 1 do
      (setq tab-stop-list (cons (* x 4) tab-stop-list)))

(defconst my-c-style
  '((c-tab-always-indent        . t)
    (c-comment-only-line-offset . 4)
    (c-hanging-braces-alist     . ((substatement-open after)
                                   (brace-list-open)))
    (c-hanging-colons-alist     . ((member-init-intro before)
                                   (inher-intro)
                                   (case-label after)
                                   (label after)
                                   (access-label after)))
    (c-cleanup-list             . (scope-operator
                                   empty-defun-braces
                                   defun-close-semi))
    (c-offsets-alist            . ((arglist-close . c-lineup-arglist)
                                   (substatement-open . 0)
                                   (case-label        . 4)
                                   (block-open        . 0)
                                   (knr-argdecl-intro . -)))
    (c-echo-syntactic-information-p . t)
    )
  "My C Programming Style")

;; offset customizations not in my-c-style
(setq c-offsets-alist '((member-init-intro . ++)))

;; Customizations for all modes in CC Mode.
(defun my-c-mode-common-hook ()
  ;; add my personal style and set it for the current buffer
  (c-add-style "PERSONAL" my-c-style t)
  ;; other customizations
  (setq tab-width 4
        ;; this will make sure spaces are used instead of tabs
        indent-tabs-mode nil)
  ;; we like auto-newline and hungry-delete
  (c-toggle-auto-hungry-state 1)
  ;; key bindings for all supported languages.  We can put these in
  ;; c-mode-base-map because c-mode-map, c++-mode-map, objc-mode-map,
  ;; java-mode-map, idl-mode-map, and pike-mode-map inherit from it.
  (define-key c-mode-base-map "/C-m" 'c-context-line-break)
  )

(add-hook 'c-mode-common-hook 'my-c-mode-common-hook) 
