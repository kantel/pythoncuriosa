import matplotlib.pyplot as plt

months = ["10/20", "11/20", "12/20", "01/21", "02/21", "03/21", "04/21", "05/21", "06/21", "07/21", "08/21", "09/21"]
pageviews = [12224, 13520, 13849, 15031, 13487, 13964, 12554, 13582, 9898, 8823, 9979, 9071]
visitors  = [6242, 7121, 6987, 7159, 6243, 6951, 6439, 6300, 5518, 4725, 5073, 4690]

plt.figure(figsize = (8, 4))
plt.plot(months, visitors, "^--", label = "Visitors")
plt.plot(pageviews, "o:", label = "Pageviews")
plt.grid(True)
plt.ylim(0, 20000)
plt.legend()

plt.show()