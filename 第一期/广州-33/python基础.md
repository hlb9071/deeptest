## 目录<br> ##
[String](#1)<br>
[元组tuple](#2)<br>
[列表](#3)<br>
[字典](#4)<br>
[函数](#5)<br>
[迭代器和生成器](#6)<br>
[INI文件读写](#7)<br>
[目录与文件操作](#8)<br>
[JSON解析](#9)<br>
[遗留问题](#20)<br>

<h3 id='1'>String</h3>
1.String（字符串）中判断字符串类型的方法，isdigit和isnumric都是判断字符串是否都是数字，是则返回true，否则返回false，那么它们有什么不同之处呢？

<h3 id='2'>元组tuple</h3>
1.元组可以通过下标索引的方式来读取元素，注意索引下标从0开始<br>
2.元组可以通过负数下标索引的方式反向读取元素<br>
3.元组可以通过  起始:终止  方式截取一段元素，其中终止是不包含的开括号<br>
4.元组的元素不可修改，但可删除<br>

<h3 id='3'>列表</h3>
1.元组与列表可互相转换<br>
2.列表拷贝的意思是，将A列表的值拷贝到B列表中去<br>
3.列表清空，不影响<br>
4.python具有切片机制，可运用在序列中<br>
5.元组不能修改元素,可删除;列表可修改元素可删除<br>

<h3 id='4'>字典</h3>
1.用get获取指定key的value，如果参数不是key，则获取不到，在获取不到的情况下，回传一个默认值<br>
2.字典不能修改key，只能修改value，找不到key时，就使用新的value插入到字典中去<br>
3.字典不能删除value，因为是通过key去找的<br>

<h3 id='5'>函数</h3>
1. 在python中一切皆为对象，在python中不能说是值传递或引用传递，而是分为可变对象和不可变对象。<br>
可变对象举例：list、dict、set<br>
不可变对象举例：strings、tuples、numbers<br>
2. 模块是比包更大的范围，模块是包的集合<br>
3. 模块和包体现的是一种组织思想，有好的组织才能有好的架构设计

<h3 id='6'>迭代器和生成器</h3>
1. 生成器是功能更强大的迭代器，返回的是一个迭代器的函数。

<h3 id='7'>INI文件读写</h3>
1.option也就是key

<h3 id='8'>目录与文件操作</h3>
1.os模块的删除目录方法，目标删除目录必须存在且无子目录、子文件<br>
2.path模块获取文件大小单位为字节<br>
3.os模块所提供的目录遍历方法walk，返回值为一个迭代器对象，它的每个部分包含一个元组，即(目录X, [目录X下的目录列表], [目录X下的文件列表])

<h3 id='9'>JSON解析</h3>
1.json是JavaScript object notation的简写，是一种轻量级的数据交换格式，易于阅读和编写，是目前前后端最常用的数据交互格式之一。

<h3 id='20'>遗留问题</h3>
1.利用生成器函数去读大文件，例如10G的文件，你可以利用生成器函数，每次只读100M进行处理，处理完后再读取下一个100M，如此迭代下去<br>
2.提问：os_walk.py为什么最后两个for是平级的？不平级的效果为什么遍历不到部分文件最深层？<br>
3.用类封装一个通用的ini文件操作类<br>
4.提问：格式化日期时间函数strftime为什么后面要加上time.loacltime()<br>