import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style
style.use('ggplot')
web_stats={'Day':[1,2,3,4,5,6],
           'Visitors':[10,29,30,49,50,66],
           'Bounce_Rate':[67,12,33,45,56,31]}
df=pd.DataFrame(web_stats)
#print(df)
#print(df.head())
#print(df.head(3))
#print(df.tail())
#print(df.tail(2))
#print(df.set_index('Day'))
#print(df)
#df=df_setindex('Day')
#df2=df.set_index('Day')
#print(df2)
#df2.set_index('Visitors')
#print(df2)
#print(df['Bounce_Rate'])
#df.plot()
df['Bounce_Rate'].plot()
plt.show()
print(df[['Visitors','Bounce_Rate']])


