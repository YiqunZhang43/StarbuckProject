import pandas as pd
import numpy as np
import json
import math
import json
from json.decoder import JSONDecodeError
json.loads
import os
import ast
import sys
import warnings
warnings.simplefilter('ignore')
os.chdir("/Users/yiqunzhang/Downloads/Starbucks/")
"""
with open('/Users/yiqunzhang/Downloads/Starbucks/transcript.json') as f:
   data = f.readlines()
transcript = pd.DataFrame(columns = ["person", "event", "value", "time"], index = range(0, len(data)))
for i in range(0, len(data)):
    try:
        test = json.loads(data[i])
        transcript.iloc[i] = pd.Series(
            {"person": test["person"], "event": test["event"], "value": test["value"], "time": test["time"]})
    except JSONDecodeError:
        continue

transcript.to_csv("transcript.csv")
"""

portfolio = pd.read_json("/Users/yiqunzhang/Downloads/Starbucks/portfolio.json", orient='records', lines=True)
profile = pd.read_json('/Users/yiqunzhang/Downloads/Starbucks/profile.json', orient='records', lines=True)
transcript = pd.read_csv("/Users/yiqunzhang/Downloads/Starbucks/transcript3.csv")
#test = pd.concat([transcript.drop(['value'], axis=1), transcript['value'].apply(pd.DataFrame)], axis=1)
transcript['value2'] =np.nan
transcript["offer id"] = np.nan
transcript["amount"] = np.nan
transcript["reward"] =np.nan
#print(len(transcript)
#transcript2= transcript[transcript["event"]=="offer completed"]
"""
print(transcript["value"][0])
test= ast.literal_eval(transcript["value"][0])
print(type(test))
transcript["offer id"][0] = test["offer_id"]
print(transcript.iloc[0])
"""

for i in range(0, len(transcript)):
    print(i)
    try:
        test = ast.literal_eval(transcript['value'][i])
        transcript["offer id"][i] = test["offer_id"]
        transcript["reward"][i] =test["reward"]
    except KeyError:
        continue


transcript.to_csv("transcript3.csv")


