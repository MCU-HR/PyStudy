# MARVEL
# MCU-HR
# 2024/4/25 20:25

print('Hello, MCU!')


#字典
#python中内置的数据结构之一，与列表一样是一个可变序列（可以执行增删改查的操作）
#以键值对的方式存储数据，字典是一个无序的序列

#字典的创建方式
#利用{}去创建字典
scores = {'张三':100,'李四':200,'王五':300}
print(scores,type(scores))


#列表（相当于其他语言的数组）

"""lst = [10,23,2,3,56,4,89,7,1,16,12,10]
#列表生成式（生成列公式）
lst1 = [i for i in range(1,10)]
print(lst1)
lst1 = [i*i for i in range(1,10)]
print(lst1)
lst1 = [2*i for i in range(1,10)]
print(lst1)
"""

#列表的排序
"""print('排序前的列表',lst,id(lst))
lst.sort()#默认升序 默认reserve=False
print('排序后的列表',lst,id(lst))
lst.sort(reverse=True)#降序
print(lst)
lst.sort(reverse=False)#升序
print(lst)"""

#使用内置函数sorted()函数，将会产生一个新的列表对象
"""print('原列表',lst)
new_lst = sorted(lst)#产生新的对象
#默认reserve = False
print('排序后',new_lst)
#降序
new_lst = sorted(lst,reverse=True)
print(new_lst)
#升序
new_lst = sorted(lst,reverse=False)
print(new_lst)"""


#列表的增删改操作
#改
#一次修改一个值
"""lst[2] = 100#指定修改
print(lst)
#用切片去修改
lst[2:6] = [300,400,600,400]
print(lst)
"""
#删
#remove()函数：一次删除一个元素，重复元素只删除第一个，元素不存在抛出ValueError
"""lst.remove(99)
print(lst)"""

#pop()函数：删除一个指定索引位置上的元素，指出索引不存在时抛出IndexError，不指定索引时删除列表中最后一个元素
"""lst.pop()
print(lst)"""

#切片：一次至少删除一个元素
#切片操作：删除至少一个元素，将产生一个新的列表对象
"""New_List = lst[4:6]
print('原列表',lst)
print('切片后的列表',New_List)
"""
#如何不产生新的对象，而是去删除原列表的内容
"""lst[4:6]=[] # 用空列表去替代
print(lst)"""

#clear()函数：清空列表
"""lst.clear()
print(lst)"""

#del：删除列表对象
"""del lst
print(lst)#这个时候已经报警告了
# NameError: name 'lst' is not defined报错"""




#增
#append()函数，在列表末尾添加一个元素
"""print('添加元素之前',lst,id(lst))
lst.append(100)
print('添加元素之后',lst,id(lst))"""

#extend()函数，在列表的末尾至少添加一个元素
"""lst2 = ['MCU','HR']
#先用append()函数
lst.append(lst2)# append()函数是将lst2中的所有元素当成一个元素放到lst的末尾
print(lst)
#再用extend()函数
lst.extend(lst2)# extend()函数是将lst2中的所有元素放到lst末尾
print(lst)
"""

#insert()函数，在列表的任意位置添加一个元素
"""print(lst)
lst.insert(1,30)# 在索引为1的位置添加30这个元素
print(lst)"""

#切片，在列表的任意位置至少添加一个元素

"""lst2 = ['MCU', 'HR']
lst[1::] = lst2  # 切片,默认从一开始,到末尾结束,步长为1,切出来,然后用lst2去替换
print(lst)"""



#判断指定的元素在列表中是否存在
# in 和 not in
"""list1 = [10,23,2,3,'MCU','HR',56,4,89,7,1,16,12]
print('mcu' in list1)
print('MCU' in list1[1:3:1])
print('MCU' in list1[1:5:2])
print(10 not in list1[1:4:1])
print(2 not in list1)"""

"""#通过索引查看元素是否存在
list1 = [12,23,34,45,56,67,78,89,99,100]
#获取索引为2的元素
print(list1[1])
#获取列表中的多个元素_切片操作
print(list1[1:4:1]) #print(list1[start:stop:step])
print(list1[2:5:2]) #print(list1[start:stop:step])

#步长为负数的情况
print('原列表：  ',list1)
print('步长为负数',list1[::-1])#倒着输出
print('步长为负数',list1[::-2])
print('步长为负数',list1[-7::-1])
print('步长为负数',list1[9::-1])"""


#列表的创建
#第一种方式
"""list1 = ['123',132,456]
print(list1)
#第二种方式
#使用内置函数list()
list2 = list(['13',123,456])
print(list2)
#python中的索引
#   -4    -3   -2  -1
#['123','123',123,456]
#   0     1    2   3
print(list2[0],list2[-3])
#获取列表的索引
#通过列表中的index方法
print(list2.index('13'))
print(list2.index(123,0,3)) #index(value,start,stop)"""

#列表可以存储多个类型
"""list = ['hello',123,'h']
print(id(list),'\n',type(list),'\n',list)"""


#循环
#九九乘法表
"""for i in range(1,10):
    for j in range(1,i+1):
        print(j,'*',i,'=',i*j,end='\t')#end = '\t'是在末尾添加水平制表符
    print()#换行，也可以print('\n')"""

#和else搭配
"""for i in range(3):
    pwd = input('请输入密码：')
    if pwd == '8888':
        print('right')
        break
    else:
        print('error')
else:
    print('已结束')"""
#水仙花数
"""for i in range(100,1000):
    a = i // 100 # 153 // 100 = 1
    b = i // 10 % 10 # 153 // 10 = 15 % 10 = 5
    c = i % 10
    if a**3 + b**3 + c**3 == i:
        print(i)"""



#for in循环
"""for item in 'python':
    print(item)"""
# in 是在什么里面，这里是在‘python’这个字符串里面
# 然后用item变量去逐个取python中的字母
"""for item in range(10):
    print(item)#0-9"""
# 如果不想用变量接收，用'_'去替代变量，代表执行in后面的循环次数
"""for _ in range(10):
    print('250')"""
#求100内的累加和
"""sum = 0
for i in range(1,101):
    sum = sum + i
print(sum)
"""

#用for循环去求100以内的质数
"""for i in range(2,101):
    flag = True
    for j in range(2,i):
        if i % j == 0:
            flag = False
            break
    if flag:
        print(i)
"""
#用for循环求阶乘
"""sum = 0
a = 1
n = int(input())
for i in range(1,n+1):
    a = a * i
    sum = sum + a
print(sum)"""

#python中while循环求100内质数
"""i = 2
while i <= 100:
    j = 2
    while j < i:
        if i % j == 0:
            break
        j = j + 1
    if i == j:
        print(i)
    i = i + 1"""

#python求阶乘
"""a = int(input())
sum = 0
i = 1
b = 1
while i <= a:
    b = b * i
    sum = sum + b
    i = i + 1
print(sum)"""


#内置函数range(start,stop,step)
"""s = range(20) #默认从0开始，步长为1，到19结束，不包括20
print(list(s))
s = range(1,20) #从一开始，默认步长为1，到19结束
print(list(s))
s = range(1,20,2) #从一开始，步长为2，到19结束
print(list(s))"""


"""#print函数 输出数字
print(321)
print(98.5)

#print函数 输出字符串
print("hello")
print('hello')
print("h")
print('h')

#print函数 输出计算式子
print(9+1)
print(3.33+1)
print(1/3)
print(-1/3)

#print输出文件内容
fp = open('F:/PyCharm/MCU/ONE/test.txt','a+')#a+是指追加，没有就自动新建
print('hello',file = fp)
fp.close()

#prinf函数 输出在同一行
print('hello','python')

#转义字符
print('hello\nhello')#\n n->newline
print('hello\thello')#\t t->tab键四个空格(水平制表符)
print('helloooo\thello')
print('hello\bhello')#\b b->back退一个格子
print('hello\rhello')#\r r->return回车,将后面的内容覆盖
print('https:\\www.baidu.com')
print('我说：\'我是MCU-HR\'')

#原字符：不希望字符串中的转义字符起作用，就是用原字符，就是在字符串之前加上r或R
print(r'hello\n')
print(R'hello\n')

#最后一个字符不可以是反斜线‘\’，但是两个没事
#print('hello\')#会报错
print('hello\\')
#print(r'hello\')
print(r'hello\\')


print(chr(0b100111001011000))#chr()转换为字符集Unicode
print(ord('乘'))#ord()转换为编码
print(chr(20056))


#变量
name = 'MCU'
print(name)
#变量有三个属性
print('标识',id(name))#内存地址
print('类型',type(name))
print('值',name)

#float精度问题
n1 = 1.1
n2 = 2.2
print(n1+n2)
#避免
from decimal import Decimal
print(Decimal('1.1')+Decimal('2.2'))

#python中的bool类型可以看成数字
print(True+1)
print(False+1)

#引号使用
#使用三对引号作用是可以换行继续写
str1 = "我是MCU-HR"
str2 = '我是MCU-HR'

str4 = '''我是
MCU-HR'''

print(str1,type(str1))
print(str2,type(str2))
print(str3,type(str3))
print(str4,type(str4))


#类型转换
name = 'MCU-HR'
age = 19

#print('我叫'+name+',今年'+age+'岁')#类型不一样的拼接会报错
print('我叫'+name+',今年'+str(age)+'岁')


#多行注释
'''hello


我是MCU-HR
'''

#input函数：屏幕提示，现输现出（用变量接收）
#present = input('你是谁？')
#print(present,type(present))

#python中的整除
print(11//2) # 5 // 整除
print(11/2) # 5.5 / 除法运算
print(11%2) # 1 % 取余运算


#幂运算
print(2**2) # 4 ** 幂次
print(4**5) # 1024

#整除中出现一个负数时向下取整
print(-9//4)
print(9//-4)
#出现两个负数就是相当于两个正数整除
print(9//4)
print(-9//-4)
#取余出现负数要遵循公式：余数=被除数-除数*商
print(9%-4) # 9-(-4*(-3))=-3
print(-9%4) # -9-(4*(-3))=3
print(-9%-4) # -9-(-4*2)=-1
print(9%4)

#python中解包赋值
a,b,c = 10,20,30;
print(a,b,c)

#交换值
a,b = 1,2
print('交换前\n',a,b)
print('交换后')
a,b = b,a
print(a,b)

#python中比较对象的标识用 is
a=10
b=10
print(a==b)
print(a is b)
#以下还没有学到
list1=[1,2,3,4]
list2=[1,2,3,4]
print(list1==list2,id(list1),id(list2))
print(list2 is list1)
print(list1 is not list2)
print(a is not b)



#python中的并且是and，或者是or
#非：not 对布尔类型取反
f1 = False
f2 = True
print(not f1)
print(not f2)
#in 和 not in
str = '123456'
print('1' in str)
print('65' in str)
print('1' not in str)
print('65' not in str)

#python中一切皆对象
#每个对象都有一个布尔值，用内置函数bool()获取

#以下对象的bool值均为false
'''
False
数值0
None
空字符串
空列表
空元组
空字典
空集合
'''

#test
print(bool(False))
print(bool(0))
print(bool(0.0))
print(bool(None))
print(bool(''))
print(bool(""))
print(bool([])) #空列表
print(bool(list())) #空列表
print(bool(())) #空元组
print(bool(tuple())) #空元组
print(bool({})) #空字典
print(bool(dict())) #空字典
print(bool(set())) #空集合
#除了以上的，其他对象都是True

#python单分支结构
money = 1020
s = int(input('请输入取款金额'))
if money >= s:
    money = money - s
    print('取款成功,余额为',money)


#双分支
s = int(input('请输入一个数'))
if s % 2 == 0:
    print('这个数是偶数')
else:
    print('这个数是奇数')


#多分支
score = int(input('请输入你的成绩'))
if score >= 90 and score <= 100:
    print(score,'等级为A')
elif score >= 80 and score < 90:
    print(score, '等级为B')
elif score >= 70 and score < 80:
    print(score, '等级为C')
elif score >= 60 and score < 70:
    print(score, '等级为D')
elif score >= 0 and score < 60:
    print(score, '等级为E')
else:
    print(score,'成绩不符合规定')

#牛逼的写法
score = int(input('请输入你的成绩'))
if 90<= score <= 100:
    print(score,'等级为A')
elif 80<= score < 90:
    print(score, '等级为B')
elif 70<= score < 80:
    print(score, '等级为C')
elif 60<= score < 70:
    print(score, '等级为D')
elif 0<= score < 60:
    print(score, '等级为E')
else:
    print(score,'成绩不符合规定')


#条件表达式（相当于C/C++中的三目运算符）
a = int(input())
b = int(input())
print (str(a)+'大于等于'+str(b) if a >= b else str(a)+'小于'+str(b))

#pass语句
#只是一个占位符
if True:
    pass
else:
    pass
#不报错只是一个占位符
"""