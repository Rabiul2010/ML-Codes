from sklearn import linear_model

#import matplotlib.pyplot as plt

import numpy as np

log = np.genfromtxt("trainingdata.txt", delimiter=',')

#print log

charge_time1 = []
charge_time2 = []

life_time1 = []
life_time2 = []

for i in log:
   
    tmp = []
    if float(i[0])<=4.0:
    	tmp.append(i[0])
	charge_time1.append(tmp)
	life_time1.append(i[1])
    else:
	tmp.append(i[0])
	charge_time2.append(tmp)
	life_time2.append(i[1])
    
#plt.scatter(charge_time, life_time,  color='black')

#plt.show()

lin1 = linear_model.LinearRegression()
lin2 = linear_model.LinearRegression()

lin1.fit(charge_time1, life_time1)
lin2.fit(charge_time2, life_time2)

#print lin.get_params()
val=float(input())

if val <= 4.0:
	print round(lin1.predict(val), 2)
else:
	print round(lin2.predict(val), 2)
