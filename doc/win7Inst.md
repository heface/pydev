HP620������������:(F10)
�������ֻ���LOGO��ʱ���F9������ֿ�����ò˵���ʹ�����·����ѡ��CD/DVDѡ��س�ȷ�ϼ���

1 firefox��������ذ�װ http://www.firefox.com.cn/
	firefox���ز�� ->���� -> ������� �����Ұ�װ DownThemAll
2 notepad++�༭�����ذ�װ https://notepad-plus-plus.org/
3 anaconda���ذ�װ https://www.anaconda.com/  �廪����վ https://mirror.tuna.tsinghua.edu.cn/help/anaconda/
*4 emacs���ذ�װ 
*5 git���ذ�װ https://git-scm.com/downloads/
6 realplayer���������� https://hk.real.com/windows/  https://hk.real.com/windows/
7 foxmail���� https://www.foxmail.com/
8 virtualbox���� https://www.virtualbox.org/wiki/Downloads
9 python���� https://www.python.org/downloads/
10 manjaro Linux���� https://manjaro.org/download/    �廪����վ https://tuna.moe/    https://mirrors.tuna.tsinghua.edu.cn/
11 ���ް�ȫ https://www.huorong.cn
12 IDM���ع��� http://www.internetdownloadmanager.com/
13 sogo���뷨 https://pinyin.sogou.com/
14 С�Ǻ����뷨 https://rime.im/
15 �Կ����� https://www.geforce.com/drivers    https://www.geforce.cn/drivers  nvidia����
16 �Կ���⹤�� https://www.techpowerup.com/download/techpowerup-gpu-z/
17 ���pdf�Ķ���


 ��ʹ��jupyter���б��ʱ����ʼ��Ŀ¼���ܲ����Լ���Ҫ��Ŀ¼����ô���潲���޸ĳ��Լ���Ҫ��Ŀ¼��
1�� ��������������jupyter notebook --generate-config�������һ�������ļ�
�����ҵĻ���ʾWriting default config to: C:\Users\allen\.jupyter\jupyter_notebook_config.py��������ʾ�� 
2�� �ҵ���Ӧ���ļ�������c.NotebookApp.notebook_dir
������ǰ���#ע��ȥ�����ں��������Լ���Ҫ���õĳ�ʼ��Ŀ¼�����������ó�c.NotebookApp.notebook_dir = u'D:\chengxu\ML'
�����Ժ�ͻὫ'D:\chengxu\ML'���Ŀ¼��Ϊ��ʼ����Ŀ¼�� ��ʹ��jupyter���б��ʱ����ʼ��Ŀ¼���ܲ����Լ���Ҫ��Ŀ¼����ô���潲���޸ĳ��Լ���Ҫ��Ŀ¼��
1�� ��������������jupyter notebook --generate-config�������һ�������ļ�
�����ҵĻ���ʾWriting default config to: C:\Users\allen\.jupyter\jupyter_notebook_config.py��������ʾ�� 
2�� �ҵ���Ӧ���ļ�������c.NotebookApp.notebook_dir
������ǰ���#ע��ȥ�����ں��������Լ���Ҫ���õĳ�ʼ��Ŀ¼�����������ó�c.NotebookApp.notebook_dir = u'D:\chengxu\ML'
�����Ժ�ͻὫ'D:\chengxu\ML'���Ŀ¼��Ϊ��ʼ����Ŀ¼��


conda����Ϊ���ھ���Դ:
(base) C:\Users\HP>conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free
(base) C:\Users\HP>conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
(base) C:\Users\HP>conda config --set show_channel_urls yes

1��conda list �鿴��װ����Щ����
2��conda env list �� conda info -e �鿴��ǰ������Щ���⻷��

1 ����Python���⻷����
     ʹ�� conda create -n your_env_name python=X.X��2.7��3.6�ȣ� 
anaconda �����python�汾ΪX.X������Ϊyour_env_name�����⻷����
your_env_name�ļ�������Anaconda��װĿ¼envs�ļ����ҵ���

# ָ��python�汾Ϊ2.7��ע��������Ҫָ��python�汾����Ҫ��װ�İ�# ��һ������£��Զ���װ����python�汾
conda create -n env_name python=2.7
# ͬʱ��װ��Ҫ�İ�
conda create -n env_name numpy matplotlib python=2.7
conda create -n aistudy pandas keras python=3.6
2 ʹ�ü���(���л���ͬpython�汾)�����⻷����
    ������������python --version���Լ�鵱ǰpython�İ汾��
 ʹ����������� ����������⻷��(����python�İ汾�ı�)��
    Linux:  source activate your_env_name(���⻷������)
    Windows: activate your_env_name(���⻷������)
   ������ʹ��python --version���Լ�鵱ǰpython�汾�Ƿ�Ϊ��Ҫ�ġ�
3 �����⻷���а�װ����İ���
    ʹ������conda install -n your_env_name [package]���ɰ�װpackage��your_env_name��
4 �ر����⻷��(���ӵ�ǰ�����˳�����ʹ��PATH�����е�Ĭ��python�汾)��
   ʹ����������ɡ�
deactivate env_name��Ҳ����ʹ��`activate root`�л�root����
Linux��ʹ�� source deactivate 
5 ɾ�����⻷����
�Ƴ�����
   ʹ������conda remove -n your_env_name(���⻷������) --all�� ����ɾ����
ɾ�������е�ĳ������
   ʹ������conda remove --name $your_env_name  $package_name ���ɡ�

pipʹ�ù��ھ���Դ��
ʹ��pipʱ������������ -i������ָ��pipԴ
��: pip install scrapy -i https://pypi.douban.com/simple/
pip����Դ��
	���http://mirrors.aliyun.com/pypi/simple/
	�пƴ�https://pypi.mirrors.ustc.edu.cn/simple/
	�廪��https://pypi.tuna.tsinghua.edu.cn/simple/



����װanaconda����ΰ�װjupyter
�������л��� {PythonHome}\ScriptsĿ¼��
���룺 pip install jupyter 
���룺 jupyter notebook
jupyter notebook --generate-config 
�򿪡�.jupyter���ļ��У����Կ��������и������ļ���
�޸�jupyter_notebook_config.py�����ļ�
����������ļ����ҵ���c.NotebookApp.notebook_dir=����������·���ĳ��Լ��Ĺ���Ŀ¼��
## The directory to use for notebooks and kernels.
c.NotebookApp.notebook_dir = 'D:\PythonDev\jupyterCode'

ǰ�ᣬ��Ҫ����Python�Ļ���������
���£��ҵ�ϵͳ���� path���༭�������� 2 ��·�����÷ֺŸ�����
D:\Python36
D:\Python36\Scripts

��װpython36ʱ����������ж�ʧapi-ms-win-crt-runtime-|1-1-0.dll
���������
(1) ��װVC redit.exe
��΢�����������������
    https://www.microsoft.com/zh-cn/download/details.aspx?id=48145
�����װʧ�ܣ����������Ĳ��͵ķ�����
    http://blog.csdn.net/huqiao1206/article/details/50768481
(2) ��װKB2999226��������
���������������ɹ���װ֮����Ȼû�н�����⣬�����ٴΰ�װ���������������
    Windows6.1-KB2999226-x64.msu   https://www.microsoft.com/zh-cn/download/details.aspx?id=49093
������64λ�ģ�32λ�����ص�ַ���£�
    Windows6.1-KB2999226-x86.msu   https://www.microsoft.com/zh-cn/download/details.aspx?id=49077
��װ���������֮��ͽ�������ˡ�
3 ����Ҳ���
������õ�win10����win8��Ҫ������Ӧ�Ĳ������Ҳ����ķ������£��ȵ�΢�������
    https://www.microsoft.com/zh-cn/download/details.aspx?id=49077
Ȼ��������������������ţ������Լ���ϵͳ�ҵ���Ӧ�Ĳ������򼴿ɣ����Ҫ��64λ�ģ������� KB2999226 x64



��δӹ�������redhat enterprise iso����
1����½������www.redhat.com ��������Ϸ��� LOGIN  ��
��Ȼ��վ����£���֮�ҵ���½�������û���˺ţ��͵����register��ע��һ����ע�⣬��ע��Ϊ����˾�˻�����
��дע����Ϣ��
ע����ɺ��½���ҵ�PRODUCTS����Ʒ��ѡ��Server����������������롣
ѡ������������أ�
�����汾����������ʮ��ļ���֧�֡������Download a free Red Hat Enterprise Linux 30-day evalution�� ������
ȷ�����������������Ѿ�����һ�Σ�������ʾexisting���Ѵ��ڡ��������Back to Downloads��������
����������ҵlinux��
Ȼ��Ϳ��Կ��������汾����Ϣ���ҵ��Լ���Ҫ�İ汾��������룬���а���32λ��64λ�����������������ء�


VirtualBox��װ64λ��ϵͳ��Ҫ��������������
1. 64λ��cpu
2. cpu����Ӳ�����⻯
��������һ��������64λ��CPU���������ڵıʼǱ�һ�㶼��64λ���ˣ����Բ��õ��ģ������Ǻü���֮��ĵ��ԡ�����㲻��������Դ������У�����systeminfo�����������Ϣ���ҵ�CPU��һ�У������X86_64�ģ�����64λCPU�����ߣ�Ҳ�������ظ�CPU-Z����鿴��PS���������ܺ��ã�����һ��������ϡ�
Ȼ���ǵڶ������Ƿ���CPUӲ�����⻯1�����������̵����������ͬ���еĵ���Ĭ�Ͽ����ˣ����磬�ҵ�HP�����е�û�У�������Ҫ���п�������������������ʱ��ĳ��������BIOS���ý���2��
Ȼ��setup==>security==>cpu virtualization����cpu virtualization��һ����Disable����ΪEnable�����棬Ȼ���������ԣ�Ӳ�����⻯�Ϳ����ɹ��ˡ�
Ȼ�󣬰���˵����������������VirtualBox��Ӧ�û����64bit��ѡ���ˣ�Ȼ��������ֻ��32λ��ѡ��������⻹�治�ǳ������
���棬��ȥ�����ϣ����ڷ���������֮���ڣ�ԭ������ΪWindows8.1�Դ���Hyper-V�������ͬѧʹ�õ���Win8.1ϵͳ��ϵͳ�Դ�Hyper-V������΢���Լҵ�������������ô��˵�ɣ�VirtualBox��workstation��Hyper-v�ǿ��Թ���ģ����ǣ������������棬Hyper-v�Ƕ�ռӲ�����⻯�ģ�Windows 8.1�°�װ��Hyper-v��VirtualBox��VMware workstation�ǲ��ܰ�װ64λ�Ĳ���ϵͳ�ġ������ֻ����Windows8.1/8�ϳ��֣�Win7�ǲ�������������ģ���ΪWin7���Դ�Hyper-V����_��
��ô�����Ǿ�ֻҪ����Hyper-V�����ˡ����õĲ��裺
Ctrl+Shift+Esc��������������� 
�ҵ�Hyper-V��ͷ��8�����񣬽�Hyper-V�������������Ϊ�ֶ�������ͬʱ�رո÷���
�ر�Hyper-V֮�󣬴󹦸�ɣ�
����˵��
1. ʲô��Ӳ�����⻯��
Ӳ�����⻯��ʵ����CPU�����⻯������intel�Ľ�VT-x��amd�Ľ�AMD-V��֧�����⼼����CPU�����ر��Ż�����ָ�������������̣�ͨ����Щָ���VMM(Virtual Machine Monitor�������������)�������������ܣ�������������ʵ�ַ�ʽ��ܴ�̶���������ܡ��� �⻯�������ṩ����оƬ�Ĺ��ܣ���������VMM����ܹ��Ľ����������������������⻯Ӳ�����ṩȫ�µļܹ���֧�ֲ���ϵͳֱ�����������У��Ӷ�������� ������ת������������ص����ܿ������������VMM��ƣ�����ʹVMM�ܹ���ͨ�ñ�׼���б�д�����ܸ���ǿ��
2. ����ж��Ƿ�֧��Ӳ�����⻯�أ�
Windows��
����һ��С���� securable.exe ���������ǲ���Ӳ�������⻯������֧�̶ֳȡ����ǳ������н���п��Կ��������֧�� 64 λ���㣬֧��Ӳ�� DEP��֧�����⻯�����������Ľ���������ǿ��Է��Ĳ��� XP MODE������� Hardware Virtualization ����ʾ�Ľ���ǡ� Locked OFF ��������� CPU ֧�����⻯������������� BIOS ȴ��ֹ�˶����⻯��֧�֣�����������Ǿ���Ҫ���� BIOS �趨������ BIOS�����������������һ����ʾ�ˡ�NO�����Ǿͱ�������Ӳ���������� XP MODE �Ĳ����������Ͳ��ü��������ˡ�
Linux��
��Linux�£�ʹ�����grep -E ��(vmx|svm)�� /proc/cpuinfo�������vmx��svm�����������˵��CPU֧�����⻯������
3. ��װ���ǳ���Ϊʲô�أ�
�½��������ʱ��Ҫ��װ64λ��Ubuntu����û�ж�Ӧѡ��64λ���������ü��ɡ����ﻹҪע��һ�㣺Ҫ��VirtualBox��vt-x/amd-v���ã������ʵ���Զ��򿪡����°�װ���󹦸���ˣ�
����һ�㣬���������в�����������֮���������һ�Σ������ٴγ���


git��ȡԴ��:
git clone git@github.com:heface/pydev

jupyter�޸Ķ˿ں�IP��ַ
jupyter notebook --no-browser --port 6000 --ip=192.168.1.103