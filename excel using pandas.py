# TO FIND MEAN,MEDIAN MODE .STANDARD DEVIATION USING PANDAS

import pandas as pd
inputs=pd.read_excel("C:/Users/ELCOT/Desktop/assign 3 pandas.xlsx")

print("to find the particulars of city A -TRICHY:\n")
print(inputs.trichy.mean())
print(inputs.trichy.median())
print(inputs.trichy.mode())
print(inputs.trichy.std())
print(inputs.trichy.var())

print("\nTo find particulars of city G - OOTY:\n")

print(inputs.ooty.mean())
print(inputs.ooty.median())
print(inputs.ooty.mode())
print(inputs.ooty.std())
print(inputs.ooty.var())