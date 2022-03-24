import random
import streamlit as s
import requests
from operator import itemgetter
from datetime import date
import calendar

fil = open("vaskeliste.txt", "r")


tekst1 = fil.readline()
tekst2 = fil.readline()
tekst3 = fil.readline()

s.title("Vaskeliste")

s.header(tekst1)
s.header(tekst2)
s.header(tekst3)
s.header(calendar.day_name[date.today().weekday()])
    

