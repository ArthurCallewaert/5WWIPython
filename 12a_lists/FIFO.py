invoer = ''
lijst = []
lijst2 = []

while invoer != 'STOP':
    invoer = input('invoer: ')
    if invoer == '?' and len(lijst) >= 1:
        lijst2.append(lijst[0])
        lijst = lijst[1:]
    elif invoer != '?':
        lijst.append(invoer)
    else:
        pass


for i in range(0, len(lijst2)):
    print(lijst2[i])


