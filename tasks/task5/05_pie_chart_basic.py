# Difficulty: Easy
# Task: Plot pie chart for ["Red", "Blue", "Green"] with sizes [40, 35, 25].
import matplotlib.pyplot as plt
labels = ["Red", "Blue", "Green"]
sizes = [40, 35, 25]
# TODO: Create pie chart with percentage labels

# Draw
plt.pie(sizes, labels=labels, autopct='%1.1f%%')


# Show
plt.show()

