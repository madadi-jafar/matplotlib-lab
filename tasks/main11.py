import matplotlib.pyplot as plt
months = list(range(1,13))
temp = [2, 4, 8, 14, 19, 24, 27, 26, 21, 15, 9, 4]
rain = [50, 40, 45, 50, 60, 70, 80, 75, 65, 55, 45, 3]
fig,ax = plt.subplots(figsize = (9,2))
ax2 = ax.twinx()
ax.plot(months,temp,color = "yellow",lw= 2)
ax2.plot(months,rain,color = "red",lw = 2)
ax.set_xlabel("Months")
ax.set_ylabel("Ttemp")
ax2.set_ylabel("Rain")
plt.title("Dual_axis")
plt.savefig("c:/Users/Mahdi Siwa/Desktop/picture/Dual.png",dpi = 300,bbox_inches = "tight")
plt.show()