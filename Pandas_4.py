import quandl
import pandas as pd

df=quandl.get("FMAC/HPI_TX")
#print(df.head())
fiddy_states=pd.read_html('https://simple.wikipedia.org/wiki/List_of_U.S._states')
#print(fiddy_states)
#First Table
#print(fiddy_states[0])
#First table first column
#print(fiddy_states[0][0])
#Only abbreviations
for abbv in fiddy_states[0][0][1:]:
    #print(abbv)
     print("FMAC/HPI_"+str(abbv))
