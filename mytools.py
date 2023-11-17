import pandas as pd
from pyreadstat import pyreadstat
import matplotlib.pyplot as plt
plt.rcParams["font.sans-serif"]=["SimHei"]#设置字体


def 生成有序类别变量描述统计表(数据表路径及文件名，变量):
                  数据表,metadata = pyreadstat.read_sav(
                      R'data\identity.sav',apply_value_formats=True,formats_as_ordered_category=True)
                      df_result = pd.DataFrame(数据表[变量].value_counts(sort=False))
                      df_result['累计求和'] = df_result['count'].cumsum()
                      df_result['比例'] = 数据表[变量].value_counts(normalize=True)
                      df_result['累计比例'] = df_result['比例'].cumsum()




