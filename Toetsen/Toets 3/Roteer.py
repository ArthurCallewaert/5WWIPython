def roteer(woord, n):
    if n > len(woord):
        n -= (n // len(woord)) * len(woord)
    woord = woord[n:] + woord[:n]
    return woord


