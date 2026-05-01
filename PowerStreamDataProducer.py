import pandas as pd
import numpy as np
import time

power_streaming_data=pd.read_csv("power_streaming_data.csv")

for _ in range(20):
    samp=power_streaming_data.loc[np.random.randint(power_streaming_data.shape[0],size=5)]
    samp["timestamp"]=[time.strftime("%H:%M:%S",time.localtime())]*5
    samp.to_csv("Other_Files/PowerStream"+str(_)+".csv",index=False)
    time.sleep(20)