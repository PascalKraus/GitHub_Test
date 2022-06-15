def TemperaturZuRgb(temperatur):
    if temperatur <= 15:
        rgb = (0,0,255)
    elif temperatur == 20:
        rgb = (0,255,0)
    elif temperatur > 15 and temperatur < 20: #von blau zu grün
        temperatur = temperatur - 15
        rgb = (0,0,255)
        y = list(rgb)
        y[2] = 255 - 51 * temperatur
        y[1] = 51 * temperatur
        rgb = tuple(y)
        print(rgb)
    elif temperatur > 20 and temperatur < 22.5: #von grün zu gelb
        temperatur = temperatur - 20
        rgb = (0,255,0)
        y = list(rgb)
        y[0] = 102 * temperatur
        rgb = tuple(y)
        print(rgb)
    elif temperatur >= 22.5  and temperatur < 25: #von gelb zu rot
        temperatur = temperatur - 22.5
        rgb = (255,255,0)
        y = list(rgb)
        y[1] = 255 - 102 * temperatur
        rgb = tuple(y)
        print(rgb)
    else:
        rgb = (255,0,0)
    return rgb

temperatur = float(input("Geben Sie bitte die Temperatur ein: \n"))
rgb = TemperaturZuRgb(temperatur)
print(rgb)
