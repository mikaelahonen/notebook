from sklearn.preprocessing import StandardScaler, Normalizer

data = [[2, 6], [0, 0], [1, 1], [1, 1]]
print(data)

#Standardize variables to obey standard deviation
print("Scaler")
scaler = StandardScaler()
scaler.fit(data)
print(scaler.mean_)
print(scaler.var_)
print(scaler.transform(data))

#Normalize. The sum of squared variable values should become 1 for each row. 
print("Normalizer")
norm = Normalizer()
norm.fit(data)
print(norm.transform(data))
