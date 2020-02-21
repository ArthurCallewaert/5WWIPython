def is_palindroom(woord):
    omgekeerd_woord = ''
    for i in woord:
        omgekeerd_woord = i + omgekeerd_woord
    if omgekeerd_woord == woord:
        antw = True
    else:
        antw = False
    return antw
