import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import matplotlib
matplotlib.style.use('bmh')

df = pd.read_csv(r'C:\Users\Lukas\Documents\!UNI\Biophysik\Mol. Bph\Fachkurs\ESR Tag 1\txt_Tag_1\SP01.TXT'
                 ,delimiter="\s+", header = None) # importiert die Datei

df = df.drop(df.index[:4]) #Entfernt die Reihen 0,1,2,3 (Hier nur Text)

df = df.drop(df.columns[[0,3,4,5]], axis = 1) #Entfernt die Entsprechenden Spalten (Unnötige Infos)

df.columns = ["B-Field", "Intensity"] #Benennt die Spalten um
df["B-Field"] = df["B-Field"].astype(np.float64) #Ändert den Typ von der Spalte von einem Objekt zu einer Zahl. Wichtig fürs plotten
df["Intensity"] = df["Intensity"].astype(np.float64)


###plotting###

fig = plt.figure(figsize = (25,10))
ax = plt.axes()

x = df["B-Field"]
y = df["Intensity"]

ax.plot(x ,y, label = "ESR Spektrum", lw = 4, c = 'black')

ax.set_ylabel("Intensity", fontsize = 20)#
ax.set_xlabel("B-Field", fontsize = 20)
ax.legend()


plt.show()
