import random

navn = ['Gard', 'Vemund', 'Håkon']
rom = ['Kjøkken, gang', 'Bad', 'Stue']
søppel = ['Glass', 'Papp', 'Pant']

random.shuffle(navn)
random.shuffle(rom)
random.shuffle(søppel)

vask = list(zip(navn, rom, søppel))

fil = open("vaskeliste.txt", "w")

tekst1 = vask[0][0] + ': ' + vask[0][1] + ' og ' + vask[0][2]
tekst2 = vask[1][0] + ': ' + vask[1][1] + ' og ' + vask[1][2]
tekst3 = vask[2][0] + ': ' + vask[2][1] + ' og ' + vask[2][2]

fil.write(tekst1 + "\n" + tekst2 + "\n" + tekst3)
