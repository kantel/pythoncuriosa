import matplotlib.pyplot as plt

months = ["12/21", "01/22", "02/22", "03/22", "04/22", "05/22", "06/22", "07/22", "08/22", "09/22", "10/22", "11/22"]
pageviews = [10769, 13147, 11459, 12163, 10341, 11108, 9307, 8782, 9836, 12992, 12743, 12087]
visitors  = [5848, 6422, 5413, 5842, 5149, 5386, 4676, 4145, 4378, 5604, 5457, 5499]

plt.figure(figsize = (10, 4))
plt.plot(months, visitors, "^--", label = "Visitors")
plt.plot(pageviews, "o:", label = "Pageviews")
plt.grid(True)
plt.ylim(0, 20000)
plt.legend()

plt.show()