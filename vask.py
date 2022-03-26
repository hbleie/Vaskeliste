import random
import streamlit as s
import requests
from operator import itemgetter
from datetime import date, timedelta
import calendar

fil = open("vaskeliste.txt", "r")

today = str(date.today()).split('-')
dato = fil.readline()
tekst1 = fil.readline()
tekst1 = tekst1.split(": ")

tekst1[1] = tekst1[1].replace("\n", "")
tekst2 = fil.readline()
tekst2 = tekst2.split(": ")
tekst2[1] = tekst2[1].replace("\n", "")

tekst3 = fil.readline()
tekst3 = tekst3.split(": ")
tekst3[1] = tekst3[1].replace("\n", "")

dato = dato.split(" ")
dato[2] = dato[2].replace("\n", "")

s.title("Vaskeliste")
s.markdown("____")

col1, col2, col3 = s.columns(3)

with col1:
    s.header(tekst1[0]) 
    s.write(tekst1[1])
with col2:
    s.write(tekst2[0])
    s.metric("", tekst2[1])
with col3:
    s.write(tekst3[0])
    s.metric("", tekst3[1])

s.sidebar.image('_dsc8499.jpg')

def sistoppdatering(idag, siste):
    today_date = date(int(idag[0]), int(idag[1]), int(idag[2]))
    siste_date = date(int(siste[0]), int(siste[1]), int(siste[2]))
    delta = today_date-siste_date
    return delta.days

def finnSøndag():
    idag = date.today()
    navnDag = calendar.day_name[idag.weekday()]
    if navnDag == "Monday":
        return date.today() - timedelta(days=1)
    elif navnDag == "Tuesday":
        return date.today() - timedelta(days=2)
    elif navnDag == "Wednesday":
        return date.today() - timedelta(days=3)
    elif navnDag == "Thursday":
        return date.today() - timedelta(days=4)
    elif navnDag == "Friday":
        return date.today() - timedelta(days=5)
    elif navnDag == "Saturday":
        return date.today() - timedelta(days=6)
    else:
        return date.today()


if sistoppdatering(today, dato) > 7:
    navn = ['Gard', 'Vemund', 'Håkon']
    rom = ['Kjøkken, gang', 'Bad', 'Stue']
    søppel = ['Glass', 'Papp', 'Pant']

    random.shuffle(navn)
    random.shuffle(rom)
    random.shuffle(søppel)

    vask = list(zip(navn, rom, søppel))

    fil = open("vaskeliste.txt", "w")

    søndag = str(finnSøndag()).split("-")
    tekst1 = vask[0][0] + ' ' + vask[0][1] + ' og ' + vask[0][2]
    tekst2 = vask[1][0] + ' ' + vask[1][1] + ' og ' + vask[1][2]
    tekst3 = vask[2][0] + ' ' + vask[2][1] + ' og ' + vask[2][2]

    fil.write(søndag[0] + ' '  + søndag[1] + ' ' + søndag[2] + "\n" + tekst1 + "\n" + tekst2 + "\n" + tekst3)
    
    

