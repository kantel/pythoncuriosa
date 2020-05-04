import matplotlib.pyplot as plt

movies = ["Annie Hall", "Ben Hur", "Casablanca", "Gandhi", "West Side Story"]
num_oscars = [5, 11, 3, 8, 10]

# Balken haben per Default die Breite 0.8, daher fügen wir zur linken
# Koordinate 0.1 hinzu, so daß die Balken zentriert sind
xs = [i + 0.1 for i, _ in enumerate(movies)]

# Plotte die Balken mit den Koordinaten der linken Seite [xs] und der
# Höhe [num_oscars]
plt.bar(xs, num_oscars)
plt.title("Berühmte Filme")
plt.ylabel("Anzahl der Oscars")
# Beschrifte die x-Achse mit dem Namen der Filme in der Mitte der Balken
plt.xticks([i + 0.1 for i, _ in enumerate(movies)], movies)

plt.show()