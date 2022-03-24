import random
import streamlit as s
import requests
from operator import itemgetter
from datetime import date
import calendar

navn = ['Gard', 'Vemund', 'Håkon']
rom = ['Kjøkken, gang', 'Bad', 'Stue']
søppel = ['Glass', 'Papp', 'Pant']

random.shuffle(navn)
random.shuffle(rom)
random.shuffle(søppel)

vask = list(zip(navn, rom, søppel))

tekst1 = vask[0][0] + ': ' + vask[0][1] + ' og ' + vask[0][2]
tekst2 = vask[1][0] + ': ' + vask[1][1] + ' og ' + vask[1][2]
tekst3 = vask[2][0] + ': ' + vask[2][1] + ' og ' + vask[2][2]

s.title("Vaskeliste")

knapp = s.button('Trekk vaskeliste')



if knapp:
    s.header(tekst1)
    s.header(tekst2)
    s.header(tekst3)
    s.header(calendar.day_name[date.today().weekday()])
    

