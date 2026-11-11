"""
Arbeidskrav 2, frist 13.11.26 kl.21.00

Linda Tangen (linda@tjacobsen.no)

20261027

"""
#%% Oppgave 1 Hvor gammel blir du i år
alder = int(input('Hvilket år er du født? ') ) # [input fødselsår]
alder_i_år = 2024-alder #[hvor mange år fyller du i år]

print("I år fyller du=", alder_i_år, "år, gratulerer!") #utskrift

#%% Oppgave 2 Hvor mange pizzaer trenger vi

import math as math  # [#importer math for avrundingsfunksjon] 
antall_elever = int(input("Skriv inn antall elver som skal spise:")) # [input antall elever]
antall_pizzaer = math.ceil(antall_elever/4) #[funksjon for å beregne ogavrunde antall]

print("Det må handles inn", antall_pizzaer, "pizzaer til klassefesten.") #utskrift

 #%% Oppgave 3 Fra grader til radianer

import numpy as np

v_grad = float(input("Skriv inn gradtallet:")) #input grader
v_rad = v_grad*np.pi/180 #omregning fra grad til radian

print("Dette gir Radiantallet=", v_rad) #utskrift

#%% Oppgave 4 Dictionary

#a
data = {
        "Norge": ["Oslo", 0.634],
        "England": ["London", 8.982],
        "Frankrike": ["Paris", 2.161],
        "Italia": ["Roma", 2.873]
        }

#%%b Be om et land for oppslag
land = input("Skriv inn et land: ")  #her ber vi bruker om å sette inn et land, nøkkelen

hovedstad = data[land][0]            # ber programmet hente verdien, første i lista
innbyggere = data[land][1]           # ber programmet hente verdien, andre i lista

print(f"{hovedstad} er hovedstad i {land} og det er {innbyggere} millioner innbyggere i {hovedstad}")

#%%c be om at bruker legger til data i listen
nytt_land = input("Skriv inn et nytt land: ")            #ber bruker om et nytt land til listen
ny_hovedstad = input("Hva er hovedstaden i landet:") #ber bruker legge til hovedstad
ant_innbyggere = float(input("skriv inn antall innbyggere i milioner: ")) #floatfordi det tall. Ber bruker legge til innbyggertall

data[nytt_land] = [ny_hovedstad,ant_innbyggere] # vil legge til oppgitt innput i listen

print (data) #skriver ut oppdatert liste


#%% Oppgave 5 Funksjon

import math

def beregn(a, b):
    radius = a / 2
    
    areal_trekant = a* b / 2  # areal trekant
    areal_halvsirkel = math.pi * radius**2 / 2 # areal sirkel/2, ** gir opphøyd i
    areal = areal_trekant + areal_halvsirkel  #sum areal
    
    skraa_side =math.sqrt(a**2 + b**2) # ytre omkrets trekant
    bue_halvsirkel = math.pi * radius #ytre omkrets halvsirkel
    
    omkrets = b + skraa_side + bue_halvsirkel #summerer omkrets
    
    return areal, omkrets 

areal, omkrets = beregn(2, 4) # beskjed om hvilke tallsom skal representere a og b

print("Arealet er: ", areal) #utskrift
print("Ytre omkrets er;", omkrets) #utskrift

#%% oppgave 6  Plotting
import numpy as np  #gir mulighet til å lage og beregne med mange tall samtidig
import matplotlib.pyplot as plt #for å lage selve grafen

x = np.linspace(-10, 10, 200)  # lager 200 verdier/punkter fra -10 til 10
y = -x**2 - 5 #regner ut funskjonen f(x)=x opphøyd i 2 - 5

plt.plot(x, y)  # plotter funksjonen

plt.xlabel("x")  #gir navn til x aksen
plt.ylabel("f(x)")  #gir navn til y aksen

plt.title("f(x) = -x² - 5")  #tittel på grafen

plt.grid() #viser grafen
plt.show() # viser grafen



















