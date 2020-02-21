def yiq(rgb):
    r, g, b = rgb
    y = round((0.299*r + 0.587*g + 0.114*b), 4)
    i = round((0.596*r - 0.274*g - 0.322*b), 4)
    q = round((0.211*r - 0.523*g + 0.312*b), 4)

    rgb = (y, i, q)
    return rgb
