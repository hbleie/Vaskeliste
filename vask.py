import random
import streamlit as s
import requests
from operator import itemgetter
from datetime import date, datetime
import calendar

fil = open("vaskeliste.txt", "r")

today = date.today()

dato = fil.readline()
tekst1 = fil.readline()
tekst2 = fil.readline()
tekst3 = fil.readline()

s.title("Vaskeliste")

s.header(tekst1)
s.header(tekst2)
s.header(tekst3)

knapp = s.button("Trekk vaskeliste")

if knapp:
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

    fil.write(today + "\n" + tekst1 + "\n" + tekst2 + "\n" + tekst3)
    

