import quandl
import pandas as pd
import pickle
import matplotlib.pyplot as plt
from matplotlib import style
style.use('fivethirtyeight')



def state_list():
    fiddy_states = pd.read_html('https://simple.wikipedia.org/wiki/List_of_U.S._states')
    return fiddy_states[0][0][1:]
    

def grab_initial_state_data():
    states = state_list()

    main_df = pd.DataFrame()

    for abbv in states:
        query = "FMAC/HPI_"+str(abbv)
        df = quandl.get(query, authtoken='WU9saayUghcsH6AGwNvS')
        df.rename(columns={'Value':abbv},inplace=True)
        #print(query)
        df[abbv] = (df[abbv]-df[abbv][0]) / df[abbv][0] * 100.0
        print(df.head())
        if main_df.empty:
            main_df = df
        else:
            main_df = main_df.join(df)
            
    pickle_out = open('fiddy_states3.pickle','wb')
    pickle.dump(main_df, pickle_out)
    pickle_out.close()

def HPI_Benchmark():
    df = quandl.get("FMAC/HPI_USA", authtoken='WU9saayUghcsH6AGwNvS')
    df["Value"] = (df["Value"]-df["Value"][0]) / df["Value"][0] * 100.0
    return df
fig = plt.figure()
ax1 = plt.subplot2grid((1,1), (0,0))
HPI_data = pd.read_pickle('fiddy_states3.pickle')
HPI_data['TX1yr']=HPI_data['TX'].resample('A').mean()
#HPI_data.dropna(inplace=True,how='all')
#HPI_data.fillna(method='ffill',inplace=True)
HPI_data.fillna(method='bfill',inplace=True)
#HPI_data.fillna(value=-99999,inplace=True)
HPI_data.dropna(inplace=True)
print(HPI_data[['TX','TX1yr']])
HPI_data['TX'].plot(ax=ax1)
HPI_data['TX1yr'].plot(ax=ax1,color='k')
plt.legend().remove()
plt.show()
