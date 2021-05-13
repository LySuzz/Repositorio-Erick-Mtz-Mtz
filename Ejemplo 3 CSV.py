import pandas as pd
name = ["ABC", "TUV", "XYZ", "PQR"] 
degree = ["BBA", "MBA", "BSC", "MSC"] 
score = [98, 90, 88, 95] 	
dict = {'name': name, 'degree': degree, 'score': score} 
df = pd.DataFrame(dict) 
df.to_csv('test.csv')