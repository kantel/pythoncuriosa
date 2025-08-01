from proceso import Sketch

WIDTH, HEIGHT = 640, 360   # Aspect Ratio: 16:9

sun_diam = 80

earth_diam = 30
earth_orbit_radius = 130
earth_angle = 0

moon_diam = 10
moon_orbit_radius = 42
moon_angle = 0

nem_diam = 12
nem_orbit_radius = 32
nem_angle = 0

p5 = Sketch()

def setup():
    p5.create_canvas(WIDTH, HEIGHT)

def draw():
    global earth_angle, moon_angle, nem_angle
    p5.background(0, 0, 0)

    # Sonne im Zentrum
    p5.translate(p5.width//2, p5.height//2)
    p5.fill(255, 200, 64)
    p5.circle(0, 0, sun_diam)

    # Erde dreht sich um die Sonne
    p5.rotate(earth_angle)
    p5.translate(earth_orbit_radius, 0)
    p5.fill(64, 64, 255)
    # p5.circle(0, 0, earth_diam)
    p5.rect(-earth_diam//2, -earth_diam//2, earth_diam, earth_diam)

    # Mond dreht sich um die Erde
    p5.push()
    p5.rotate(moon_angle)
    p5.translate(moon_orbit_radius, 0)
    p5.fill(192, 192, 80)
    p5.rect(-moon_diam//2, -moon_diam//2, moon_diam, moon_diam)
    p5.pop()

    # Nemesis dreht sich um die Erde
    p5.push()
    p5.rotate(nem_angle)
    p5.translate(nem_orbit_radius, 0)
    p5.fill(220, 75, 75)
    p5.rect(-nem_diam//2, -nem_diam//2, nem_diam, nem_diam)
    p5.pop()
    
    earth_angle += 0.01
    moon_angle += 0.01
    nem_angle += 0.015

p5.run_sketch(setup=setup, draw=draw)