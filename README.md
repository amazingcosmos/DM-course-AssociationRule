# UCI”急性炎症”数据集关联规则挖掘报告

姓名：李懿

学号：2120151008

# 一、数据预处理&格式转换

原始数据如图1所示

![图1 原始数据](./image/original_data)

由8列特征组成，分别代表体温、恶心、腰疼、连续排尿、排尿疼痛、尿道肿胀、膀胱炎症和肾炎。除了体温为数值属性，其他属性都是二值的标称属性，所以考虑将体温转换为同为标称属性的发烧属性。在实验中选取38摄氏度为基准，低于38度为正常，高于38度为发烧。

原始数据为
对数据集进行处理，转换成适合关联规则挖掘的形式；
找出频繁项集；
导出关联规则，计算其支持度和置信度；
去除冗余的规则；
对规则进行评价，可使用Lift，也可以使用教材中所提及的其它指标；
使用可视化技术，如散点图、平行坐标、泡泡图等，对规则进行展示。

# 

# Reference

1. http://www.cnblogs.com/dolphin0520/archive/2012/10/29/2733356.html
2. http://www.jb51.net/article/57209.htm
3. http://www.cnblogs.com/Dzhouqi/p/3464995.html
4. http://blog.csdn.net/gjwang1983/article/details/45015203
5. http://www.cnblogs.com/lzllovesyl/p/5434401.html
