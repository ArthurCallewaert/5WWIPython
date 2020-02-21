tweet = input('tweet: ')
woord = ''

for i in range(0, len(tweet)):
    woord = ''
    if tweet[i] == '#':
        while tweet[i] == ' ':
            woord = woord + tweet[i]

            print(woord)

