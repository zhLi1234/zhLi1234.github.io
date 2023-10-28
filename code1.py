import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif']=['SimHei'] #加上这一句就能在图表中显示中文
plt.rcParams['axes.unicode_minus']=False #用来正常显示负号
#正弦波连续信号
# 生成信号
t = np.arange(0, 1, 0.01)
x = np.sin(2*np.pi*5*t)
# 显示信号cd
plt.plot(t, x)
plt.xlabel('时间/秒')
plt.ylabel('振幅')
plt.title('正弦波连续信号')
plt.show()

#矩形波离散信号
# 生成信号
t = np.arange(0, 1, 0.01)
x = np.zeros_like(t)
x[t<=0.5] = 1
x[t>0.5] = -1
# 显示信号
plt.stem(t, x)
plt.xlabel('时间/秒')
plt.ylabel('振幅')
plt.title('矩形波离散信号')
plt.show()