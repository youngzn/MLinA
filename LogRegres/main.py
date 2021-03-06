# coding=UTF-8
#程序名：逻辑回归分类（西格玛函数实现的监督分类）
#程序内容：1.利用训练数据使用上升梯度算法计算权重，2.利用权重和测试数据预测结果，3.多级运行程序求平均错误率
#程序说明：
#0.梯度上升求最大值，下降求最小值（程序中的 + 不能更改成 - ）
#1.每一个数据的x0输入全部设置为常数1，其实其实可以设置成任何常数，因为其权重w0会自动调节x0的输入大小。
#2.步长：的设置在合理的前提下越大越好越快逼近最佳参数，越小越不会出现异常但迭代效果越慢。通常取0.0001这一类的小数
#3.初始权重：设置也是任意的，通常设置为1，多次迭代后都会趋于最有权重参数（前提是有唯一最优解/最大似然函数有唯一极值解）。
#4.迭代的次数：这个多试几次，看图大概就能知道设置为多少，理论上来说迭代次数越大最好，但实际后面的迭代没有太大效果
#5.第三个例子中的X0是直接在文档中就给出的，不需要在程序中添加其值。训练样本和测试样本都是22列（21列属性值 + 1列 标签值01 ）
#5.#程序内容：

#疑问：1.为什么每个数据都要添加一个常数属性呢？
#其他：程序提供的例子有两个属性（不含常数x0=1）,则绘制出的是切分二位空间的直线x1+x2=0，如果是三个属性，则绘制出的是切分三维空间的平面x1+x2+x3=0。
#同理可知，四个属性绘制出的是切分思维空间的立方体（思维图形是想象不出来的，但是其投影是可以想象出来的三维，所以可推测x1+x2+x3+x4=0是思维空间表达式下的三维空间方程）。
#一维是直线，二位是平面，三维是显示空间，平面可能存在交集，但蚂蚁不能从一个平面到另一个平面，甚至不能抬头看见另一个平面。同理现实空间与现实空间也会存在交集，但是去不了，甚至不能抬头看见另一个空间。
#时间：2018年6月8日（星期五） 下午开始，6月12日（星期二）上午完成备注分析

import logRegres
from numpy import *


#从文件夹中提取数据
dataArr, labelMat = logRegres.loadDataSet() #加载数据，存放在列表中
print "\n数据列表是：\n", dataArr   #打印数据，测试读取是否异常
print "\n类列表是:\n", labelMat


#用数据和标签 利用梯度上升算法计算 权重
weights = logRegres.gradAscent(dataArr,labelMat)  #梯度上升算法计算最佳参数值
stocWeights = logRegres.stocGradAscent1(array(dataArr),labelMat,500)  #随机梯度上升算法计算最佳参数值
print "\n权重w0,w1,w2的值是：\n", weights


#######################################       第一个图：梯度上升算法的例子          #################################
#利用权重绘制直线 利用数据绘制点
print "\n第一个图：梯度上升算法的例子"
#梯度上升算法：批量处理方法（一次性处理所有数）
logRegres.plotBestFit(weights.getA())    # .getA()将矩阵转换成数组 因为数组可以很方便的任意读取其中的元素，矩阵不行


#######################################       第二个图：随机梯度上升算法的例子          #################################
#随机梯度上升：在线学习方法（新样本来到时，对分类器进行增量式更新）
print "第二个图：随机梯度上升算法的例子" #
logRegres.plotBestFit(stocWeights)


########################################       第三个例子：预测病马的死亡率          #################################
#病马死亡率预测
print "\n第三个例子：预测病马的死亡率"
logRegres.multiTest()


#程序运行结果：
'''
数据列表是： [[1.0, -0.017612, 14.053064], [1.0, -1.395634, 4.662541], [1.0, -0.752157, 6.53862], [1.0, -1.322371, 7.152853], [1.0, 0.423363, 11.054677], [1.0, 0.406704, 7.067335], [1.0, 0.667394, 12.741452], [1.0, -2.46015, 6.866805], [1.0, 0.569411, 9.548755], [1.0, -0.026632, 10.427743], [1.0, 0.850433, 6.920334], [1.0, 1.347183, 13.1755], [1.0, 1.176813, 3.16702], [1.0, -1.781871, 9.097953], [1.0, -0.566606, 5.749003], [1.0, 0.931635, 1.589505], [1.0, -0.024205, 6.151823], [1.0, -0.036453, 2.690988], [1.0, -0.196949, 0.444165], [1.0, 1.014459, 5.754399], [1.0, 1.985298, 3.230619], [1.0, -1.693453, -0.55754], [1.0, -0.576525, 11.778922], [1.0, -0.346811, -1.67873], [1.0, -2.124484, 2.672471], [1.0, 1.217916, 9.597015], [1.0, -0.733928, 9.098687], [1.0, -3.642001, -1.618087], [1.0, 0.315985, 3.523953], [1.0, 1.416614, 9.619232], [1.0, -0.386323, 3.989286], [1.0, 0.556921, 8.294984], [1.0, 1.224863, 11.58736], [1.0, -1.347803, -2.406051], [1.0, 1.196604, 4.951851], [1.0, 0.275221, 9.543647], [1.0, 0.470575, 9.332488], [1.0, -1.889567, 9.542662], [1.0, -1.527893, 12.150579], [1.0, -1.185247, 11.309318], [1.0, -0.445678, 3.297303], [1.0, 1.042222, 6.105155], [1.0, -0.618787, 10.320986], [1.0, 1.152083, 0.548467], [1.0, 0.828534, 2.676045], [1.0, -1.237728, 10.549033], [1.0, -0.683565, -2.166125], [1.0, 0.229456, 5.921938], [1.0, -0.959885, 11.555336], [1.0, 0.492911, 10.993324], [1.0, 0.184992, 8.721488], [1.0, -0.355715, 10.325976], [1.0, -0.397822, 8.058397], [1.0, 0.824839, 13.730343], [1.0, 1.507278, 5.027866], [1.0, 0.099671, 6.835839], [1.0, -0.344008, 10.717485], [1.0, 1.785928, 7.718645], [1.0, -0.918801, 11.560217], [1.0, -0.364009, 4.7473], [1.0, -0.841722, 4.119083], [1.0, 0.490426, 1.960539], [1.0, -0.007194, 9.075792], [1.0, 0.356107, 12.447863], [1.0, 0.342578, 12.281162], [1.0, -0.810823, -1.466018], [1.0, 2.530777, 6.476801], [1.0, 1.296683, 11.607559], [1.0, 0.475487, 12.040035], [1.0, -0.783277, 11.009725], [1.0, 0.074798, 11.02365], [1.0, -1.337472, 0.468339], [1.0, -0.102781, 13.763651], [1.0, -0.147324, 2.874846], [1.0, 0.518389, 9.887035], [1.0, 1.015399, 7.571882], [1.0, -1.658086, -0.027255], [1.0, 1.319944, 2.171228], [1.0, 2.056216, 5.019981], [1.0, -0.851633, 4.375691], [1.0, -1.510047, 6.061992], [1.0, -1.076637, -3.181888], [1.0, 1.821096, 10.28399], [1.0, 3.01015, 8.401766], [1.0, -1.099458, 1.688274], [1.0, -0.834872, -1.733869], [1.0, -0.846637, 3.849075], [1.0, 1.400102, 12.628781], [1.0, 1.752842, 5.468166], [1.0, 0.078557, 0.059736], [1.0, 0.089392, -0.7153], [1.0, 1.825662, 12.693808], [1.0, 0.197445, 9.744638], [1.0, 0.126117, 0.922311], [1.0, -0.679797, 1.22053], [1.0, 0.677983, 2.556666], [1.0, 0.761349, 10.693862], [1.0, -2.168791, 0.143632], [1.0, 1.38861, 9.341997], [1.0, 0.317029, 14.739025]]
类列表是： [0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 1, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 0, 0, 1, 1, 1, 0, 1, 0, 0]

权重w0,w1,w2的值是：
[[ 9.3509465 ]
 [ 0.87394863]
 [-1.28879659]]
 
第一个图：梯度上升算法的例子
第二个图：随机梯度上升算法的例子

第三个例子：预测病马的死亡率
the error rate of this test is: 0.298507
the error rate of this test is: 0.388060
 ......
the error rate of this test is: 0.402985
the error rate of this test is: 0.313433

after 10 iterations the average error rate is: 0.347761

'''
