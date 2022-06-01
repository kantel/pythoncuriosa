import matplotlib.pyplot as plt

months = ["06/21", "07/21", "08/21", "09/21", "10/21", "11/21", "12/21", "01/22", "02/22", "03/22", "04/22", "05/22"]
pageviews = [9898, 8823, 9979, 9071, 10742, 11312, 10769, 13147, 11459, 12163, 10341, 11108]
visitors  = [5518, 4725, 5073, 4690, 5468, 5911, 5848, 6422, 5413, 5842, 5149, 5386]

plt.figure(figsize = (10, 4))
plt.plot(months, visitors, "^--", label = "Visitors")
plt.plot(pageviews, "o:", label = "Pageviews")
plt.grid(True)
plt.ylim(0, 20000)
plt.legend()

plt.show()