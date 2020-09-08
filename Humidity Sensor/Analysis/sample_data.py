import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

df = pd.read_csv("DATALOG.TXT")
df = df.iloc[::60]

# print(df)

# df.to_csv("datalog_sample.csv")

# df.reset_index().plot(kind='scatter',x='index',y='humidity',color='red')

# plot humidity
# df.plot(x="time", y="humidity")
# plt.show()

# print(df['humidity'].dtypes)

# for col in df.columns: 
#     print(col) 

df['time'] = pd.to_datetime(df.time, unit="s")
# df['hour'] = df.time.dt.hour

# print df.head()

fig, ax = plt.subplots(figsize=(15,7))

# df.plot(x="time", y=["humidity", "temperature"], ax=ax)
df.plot(x="time", y=["temperature"], ax=ax)

ax.xaxis.set_major_locator(mdates.HourLocator())
ax.xaxis.set_major_formatter(mdates.DateFormatter('%H'))
plt.show()

# print df