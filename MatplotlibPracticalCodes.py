#Visualization Part
import matplotlib.pyplot as plt
import numpy as np

x = np.array([1, 2, 3, 4])
y = np.array([4, 3, 2, 1])

plt.figure()
plt.plot(x, y, color="red", alpha = 0.3, label = "line")
plt.scatter(x, y, color="blue", alpha = 0.4, label = "scatter")
plt.title("Matplotlib")
plt.xlabel("x")
plt.ylabel("y")
plt.grid(True)
plt.xticks([0, 1, 2, 3, 4, 5])
plt.yticks([0, 1, 1.5, 3.5, 4, 10])
plt.legend()
plt.show()

fig, axes = plt.subplots(2, 1, figsize = (9, 7))
fig.subplots_adjust(hspace = 0.5)

x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
y = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

axes[0].scatter(x, y)
axes[0].set_title("sub_1")
axes[0].set_ylabel("sub_1 y")
axes[0].set_xlabel("sub-1 x")

axes[1].scatter(y, x)
axes[1].set_title("sub_2")
axes[1].set_ylabel("sub_2 y")
axes[1].set_xlabel("sub_2 x")

#Random image
plt.figure()
img = np.random.random((50, 50))
plt.imshow(img)#0-Black, 1-White, 0.5-Gray
#plt.axis("off")
plt.show()

print(img[12, 0])
