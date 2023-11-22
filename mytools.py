import pandas as pd
from pyreadstat import pyreadstat
import matplotlib.pyplot as plt
plt.rcParams["font.sans-serif"]=["SimHei"]#设置字体


def 生成有序类别变量描述统计表(表名,变量名):
                      
                      result = 表名[变量名].value_counts(sort=False)
                      描述统计表 = pd.DataFrame(result)
                      描述统计表['比例'] = 描述统计表['count']/ 描述统计表['count'].sum()
                      描述统计表['累计求和'] = df_result['count'].cumsum()
                      df_result['比例'] = 描述统计表['比例'].cumsum()
                      return 描述统计表

def 绘制直方图(表名,y):
        x = 表名.index
        y = 表名[y].values
        fig,ax2 = plt.subplots()
        ax2.bar(x,y)
        plt.show()                 