# Difficulty: Intermediate
# Task: Plot temperature (left axis) and rainfall (right axis) over 12 months.
import matplotlib.pyplot as plt
months = list(range(1,13))
temp = [2, 4, 8, 14, 19, 24, 27, 26, 21, 15, 9, 4]
rain = [50, 40, 45, 50, 60, 70, 80, 75, 65, 55, 45, 35]
# TODO: Create dual y-axis plot

# create two objects for y axis

sheet,x1 = plt.subplots()
x1.plot(months,temp,color = '#fc3424',marker ='o')
x1.set_xlabel('Month')
plt.ylabel('temperature C')

x2 =x1.twinx()  
x2.plot(months,rain,color = "#2453fc",ls ='--',marker = 'h')
plt.ylabel('Rain fall')
x2.set_xlabel('Month')
plt.title('Weather analysis')
plt.legend()

plt.show()