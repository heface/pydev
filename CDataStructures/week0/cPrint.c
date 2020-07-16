/* 本题要求你写个程序把给定的符号打印成沙漏的形状。例如给定17个“*”，要求按下列格式打印
# *****
#  ***
#   *
#  ***
# *****
所谓“沙漏形状”，是指每行输出奇数个符号；各行符号中心对齐；相邻两行符号数差2；符号数先从大到小顺序递减到1，再从小到大顺序递增；首尾符号数相等。

给定任意N个符号，不一定能正好组成一个沙漏。要求打印出的沙漏能用掉尽可能多的符号。
输入格式:

输入在一行给出1个正整数N（≤1000）和一个符号，中间以空格分隔。
输出格式:

首先打印出由给定符号组成的最大的沙漏形状，最后在一行中输出剩下没用掉的符号数。
you输入样例:

19 *

输出样例:

*****
 ***
  *
 ***
*****
2
解决方案: 
假定从中间到底端有n行，则每行数据为2n+1(n从0开始)，到顶端是一样的
则总量为(2n+2)*n-1,由此计算总行数
# ------------------------------------------------*/

#include <stdio.h>


int printStr(int len,int maxLen,char printChar){
  for(int i=0;i<(maxLen-len)/2;i++){
    putchar(' ');
  }
  for(int i=0;i<len;i++){
    putchar(printChar);
  }
  for(int i=0;i<(maxLen-len)/2;i++){
    putchar(' ');
  }
  putchar('\n');
  return 0;
}

int main(void){
    int num, lineNum=-1;
    char data;

    scanf("%d %c",&num,&data);
    printf("input:%d,%c\n",num,data);
    int flg = 0;
    for(int i=0;i<num;i++){
      flg = (i*2+2)*(i+1)-1;
      if(flg==num){
	lineNum = i;
	break;
      }else if(flg>num){
	lineNum = i-1;
	break;
      }else{
	continue;
      }
    }
    //printf("lineNum:%d\n",lineNum);
    int maxNum = lineNum*2+1;
    //printf("max num:%d\n",maxNum);
    //printf("flg:%d\n",flg);
    int count = (lineNum*2+2)*(lineNum+1)-1;
    //printf("count:%d\n",count);
    for(int i=lineNum;i>0;i--){
      printStr(i*2+1,maxNum,data);
    }
    for(int i=0;i<=lineNum;i++){
      printStr(i*2+1,maxNum,data);
    }
    printf("%d\n",num-count);
    return 0;
}

