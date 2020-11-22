第三周 第7课 泛型递归、树的递归  
一、递归的实现、特性以及思维要点  
1、树的面试题解法一般都是递归：节点的定义、重复性（自相似性）  
2、递归就是循环，通过函数体来进行递归   
树的递归：二叉搜索树的的中序遍历是升序

类比盗梦空间：  
向下进入到不同梦境；向上又回到原来一层  
通过声音同步回到上一层  
每一层的环境和周围的人都是一份拷贝、主角等几个人穿越不同层级的梦境（发生和携带变化）  
python代码模版：  
def recursion(level, param1, param2,...): 
    #recursion terminator 
    if level>max_level:  
        process_result  
        return  
    #process logic in current level  
    process(level, data...)  
    #drill down  
    self.recursion(level+1, p1,...)  
    #reverse the current level status if needed  
不要进行人肉递归；找到最近最简方法，将其拆解成可重复解决的问题（重复子问题）  
数学归纳法解决问题
二、实战题目：爬楼梯、括号生成等问题  

第3周 第8课 分治、回溯  
1、分治、回溯的实现和特性   
分治和回溯是一种特殊的递归，找重复性来解决问题  
熟记 分治代码模板：  
recursion terminator\prepare data\conquer subproblems\process and generate the final result\revert the current level states  
回溯法采用试错的思想，通常用最简单的递归方法来实现，会出现两种情况：  
找到一个可能存在的正确的答案；尝试所有可能的分步方法后宣告该问题没有正确答案。  回溯一般使用深度遍历，采用递归的思想。
2、实战题目pow(x, n)、子集   
快速幂+递归、快速幂+迭代 
3、实战题目解析：众数、电话号码的字母组合、N皇后
