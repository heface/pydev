#GIT设置SSH KEY
一 、设置git：
设置git的user name和email：
$ git config --global user.name "xxx"
$ git config --global user.email "xxx@gmail.com"
查看git配置：
$git config --lis
二、生成SSH密钥过程：
1.查看是否已经有了ssh密钥：cd ~/.ssh
如果没有密钥则不会有此文件夹，有则备份删除
2.生存密钥：
$ ssh-keygen -t rsa -C "gudujianjsk@gmail.com"
按3个回车，密码为空这里一般不使用密钥。
最后得到了两个文件：id_rsa和id_rsa.pub
3.添加 私密钥 到ssh：ssh-add id_rsa
需要之前输入密码（如果有）。 
4.在github上添加ssh密钥，这要添加的是“id_rsa.pub”里面的公钥。
打开 http://github.com,登陆xushichao，然后添加ssh。
注意在这里由于直接复制粘帖公钥，可能会导致增加一些字符或者减少些字符，最好用系统工具xclip来做这些事情。
xclip -selection c  id_rsa.pub
注意：密匙生成就不要改了，如果已经生成到~/.ssh文件夹下去找。
id_rsa.pub文件内容全部弄到github上。
首先用如下命令（如未特别说明，所有命令均默认在Git Bash工具下执行）检查一下用户名和邮箱是否配置（github支持我们用用户名或邮箱登录）：
git config --global  --list
如未配置，则执行以下命令进行配置：
git config --global  user.name "这里换上你的用户名"
git config --global user.email "这里换上你的邮箱"

然后执行以下命令生成秘钥：
ssh-keygen -t rsa -C "这里换上你的邮箱"

执行命令后需要进行3次或4次确认：
    确认秘钥的保存路径（如果不需要改路径则直接回车）；
    如果上一步置顶的保存路径下已经有秘钥文件，则需要确认是否覆盖（如果之前的秘钥不再需要则直接回车覆盖，如需要则手动拷贝到其他目录后再覆盖）；
    创建密码（如果不需要密码则直接回车）；
    确认密码；

再次尝试用git方式下载，可以看到已经可以正常下载： 
git clone git@github.com:heface/pydev

#use git
1 初始化git
git init

2 添加py文件到本地仓库
git add ***.py(添加到暂存区)
git commit ***.py -m '注释'（添加到版本库）

3 查看git记录
git log -2（最近两次）

4 撤销版本回退
git reflog(查看需要的版本号)
git reset --hard bad9adt(版本号)

想要远程提交代码只需在步骤2的commit命令后面加一步：git push

5 删除远程仓库中的文件或目录
git rm -r --cached page/__init__.py
git commit -m '删除文件'
git pus

6 分支管理
- 创建
  a. 创建一个本地分支
    [ethan@ubuntu:minifs]$ git branch test
  b. 将本地分支同步到GitHub上面: 这个时候你就可以在github看到一个新的分支
    [ethan@ubuntu:minifs]$ git push origin test
  c. 切换到新建立的分支： 
    [ethan@ubuntu:minifs]$ git checkout test
  d. 推送新的修改的新的分支
    [ethan@ubuntu:minifs]$ git push -u origin test 

- 删除
  a. 从本地删除一个分支
    [ethan@ubuntu:minifs]$ git branch -D test 
  b.  同步到GitHub上面删除这个分支
    [ethan@ubuntu:minifs]$ git push origin :test

7 代码对比git diff
执行 git diff 来查看执行 git status 的结果的详细信息。
git diff 命令显示已写入缓存与已修改但尚未写入缓存的改动的区别。git diff 有三个主要的应用场景。
git diff            #未缓存与已经缓存的对比
git diff --cached   #已缓存与仓库的对比
git diff HEAD       #未缓存以及已经缓存与仓库的对比
​
后面跟上两个提交号，可以比较两次修改内容

8 Git的使用注意事项

1. 代码提交流程
代码的提交流程需要严格遵守，不仅能提高效率还能避免出错。

git branch检查当前分支是否在master，若不在master ，使用git checkout master 切换至master；
git pull origin master, 拉取最新的master代码；
根据目的（feature/bugfix/release等）创建本地分支，如：feature/xx; bugfix/xx; release/1.0;
修改本地代码，如果修改代码时间较长，至少每天push一次代码到服务器
修改完成后，push 到对应分支，提交merge request
若果Merge request有 comments，需要修改后，再次提交到对应分支
Comments修改完毕，切无新增，该分支会被merge到master
修改的分支merge到master后，删除本地分支 
禁止：在merge后的分支上修改代码或新建其他分支； 
禁止：修改他人的code； 

2.提交冲突的解决办法
当你修改代码完成，准备提交时，git提示服务器代码已经修改，你需要如下步骤操作.

git pull 对应分支的代码，如果代码与本地有冲突，会有conflict提示，切会提示哪些文件有冲突
手动逐个文件修改冲突，保留有效有改部分
修改完成后，git add 和git commit
最后git push 
禁止：有冲突使用新开分支提交

注:ssh公私钥生成
ssh-keygen -t rsa -C "youremail@youremail.com"
测试ssh连接
ssh -T git@coding.net
ssh -T git@github.com

#常用代码托管平台
1、GitHub
关于GItHub相信大家都有耳闻，我就不详细介绍了。GitHub地址：https://github.com/

2 gitlab
提到GitHub就会自然的想到Gitlab,Gitlab支持无限的公有项目和私有项目。Gitlab地址：https://about.gitlab.com/，

3 Bitbucket
bitbucket免费支持5个开发成员的团队创建无限私有代码托管库。bitbucket地址：https://bitbucket.org/

4 (推荐)开源中国代码托管
前面说的都是国外的，下面来说几个国内的。开源中国一个账号最多可以创建1000个项目，包含公有和私有，开源中国代码托管地址：http://git.oschina.net/

开源中国在几个月前又发布了团队协作开发平台，和代码托管平台一起，打造了一个十分好的团队开发平台，开源中国团队协作平台地址：http://team.oschina.net/，团队协作平台支持任务的创建、讨论、便签等

5 (推荐)coding.net
谈到coding.net,首先必须提的是速度快，功能与开源中国相似，同样一个账号最多可以创建1000个项目，也支持任务的创建等。coding.net地址：https://coding.net/home.html

6 CSDN代码托管
CSDN代码托管地址：https://code.csdn.net/

7 京东代码托管平台
京东代码托管平台地址：https://code.jd.com/


