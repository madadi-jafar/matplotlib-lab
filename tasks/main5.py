import matplotlib.pyplot as plt
labels = ["Red", "Blue", "Green"]
sizes = [40, 35, 25]
color = ["red","blue","green"]
plt.pie(sizes,labels = labels,
         autopct = "%1.1f%%",
         explode=[0,0,0.1],
         shadow=True,
         startangle=180,
         colors =color )
plt.show()