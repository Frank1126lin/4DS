#! /usr/bin/env python3
# *_* coding: utf-8 *_*
# @File  : re_practice.py
# @Author: Frank1126lin
# @Date  : 2019/8/29

'''正则速记'''
"""
正则表达式
作用：指定一个规则，根据队则对字符串进行筛选
A. 原子：组成正则的基本单位就是原子
    1. 所有可见字符都是原子:abc123#$%^&
    2. 所有不可见字符也都是原子: \n \t \r
    3. 表示所有数字的原子：\d [表示0-9任意一个字符]
    4. 表示所有非数字的原子： \D 【表示除了0-9任意一个字符】
    5. 表示能够当作变量使用的原子： \w 【表示0-9a-zA-Z任意一个字符】
    6. 表示不能够当作变量使用的原子： \W 【表示除了0-9a-zA-Z任意一个字符】
    7. 表示不可见字符都是原子： \s 【表示任意一个不可见字符】
    8. 表示可见字符都是原子： \S 【表示任意一个可见字符】
    
B. 原则：正则表达式至少包含一个原子
C. 元字符： 用于修饰原子的符号
    1. [] :原子列表：自定义原子范围 【表示列表中任意一个字符】 [0123456789]=\d
    2. [^] :排除列表：自定义原子范围 【表示列表外任意一个字符】 [^0123456789]
    3. + :1个或以上的指定原子
    4. * :0个或以上的指定原子
    5. ? :0个或1个指定原子
    6. {m,n} :指定原子数量最少m个，最多n个
    7. {m,}或{,n} :指定原子数量最少m个或最多n个
    8. {m} :指定原子数量必须m个
    9. ^ :限制内容必须在整个字符串的开头位置
    10. $ :限制内容必须在整个字符串的结束位置
    11. . :表示任意一个字符 除了\n
    12. | :唯一一个逻辑运算符或（万能钥匙）
    13. \b 词边界：能够当作英文单词的分隔符号,即除了数字和字母
    14. \B 非词边界：不能够当作英文单词的分隔符号
    
    
"""

import re
str = "www.google.com"
pattern = re.compile(r'\bgoogle\b')
result = re.findall(pattern=pattern,string=str)
print(result)