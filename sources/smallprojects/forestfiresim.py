# Forest Fire Simulation

import random, sys, time, bext

# Konstanten-Deklaration
WIDTH = 79
HEIGHT = 22
TREE  = "A"
FIRE  = "W"
EMPTY = " "

# Parameter, mit denen experimentiert werden kann
INITIALER_BAUM_BESTAND = 0.2
WACHSTUMSRATE = 0.01           # Rate, wie oft auf einer leeren Zelle ein Baum wächst
BRANDGEFAHR   = 0.05           # Rate, wie oft ein Brand ausbricht
PAUSE         = 0.5

def main():
    forest = create_new_forest()
    bext.clear()
    
    while True:               # Hauptschleife der Simulation
        display_forest(forest)
        
        # Simulations-Schritte
        next_forest = {"width": forest["width"], "height": forest["height"]}
        for x in range(forest["width"]):
            for y in range(forest["height"]):
                if (x, y) in next_forest:
                    # Wenn der Wert schon in einer vorherigen Iteration
                    # gesetzt wurde, tue nichts
                    continue
                
                if ((forest[(x, y)] == EMPTY) and (random.random() <= WACHSTUMSRATE)):
                    # Neuer Baum
                    next_forest[(x, y)] = TREE
                elif ((forest[(x, y)] == TREE) and (random.random() <= BRANDGEFAHR)):      
                    # Zünde Baum an
                    next_forest[(x, y)] = FIRE
                elif forest[(x, y)] == FIRE:
                    # Wenn der Baum brennt, untersuche die Nachbarfelder …
                    for ix in range(-1, 2):
                        for iy in range(-1, 2):
                            # Wenn Baum, dann anzünden
                            if forest.get((x + ix, y + iy)) == TREE:
                                next_forest[(x + ix, y + iy)] = FIRE
                    # und lösche den brennenden Baum
                    next_forest[(x, y)] = EMPTY
                else:
                    # Kopiere das Feld in die nächste Iteratrion
                    next_forest[(x, y)] = forest[(x, y)]
        
        forest = next_forest
        time.sleep(PAUSE)
        
def create_new_forest():
    forest = {"width": WIDTH, "height": HEIGHT}
    for x in range(WIDTH):
        for y in range(HEIGHT):
            if (random.random()*100) <= INITIALER_BAUM_BESTAND:
                # Pflanze einen Baum
                forest[(x, y)] = TREE
            else:
                forest[(x, y)] = EMPTY
    return(forest)

def display_forest(forest):
    bext.goto(0, 0)
    for y in range(forest["height"]):
        for x in range(forest["width"]):
            if forest[(x, y)] == TREE:
                bext.fg("green")
                print(TREE, end="")
            elif forest[(x, y)] == FIRE:
                bext.fg("red")
                print(FIRE, end="")
            elif forest[(x, y)] == EMPTY:
                print(EMPTY, end="")
        print()
    bext.fg("reset")     # Auf Terminal-Standard-Einstellung zurücksetzen
    print("Wachstumsrate: {}%  ".format(WACHSTUMSRATE*100), end="")
    print("Brandgefahr: {}%  ".format(BRANDGEFAHR*100), end="")
    print("Mit CTRL-C beenden.")
    
if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        sys.exit()
                    
                      