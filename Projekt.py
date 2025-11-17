import random
import tkinter as tk
from tkinter import messagebox


def Buch_fun(gegeb_wort, ent_wort):
    gegeb_wort = gegeb_wort.upper()
    ent_wort = ent_wort.upper()
    Buchstaben_list = []
    zaehlung_dict = {}
    for i in ent_wort:
        zaehlung_dict[i] = zaehlung_dict.get(i,0) + 1
    #print(zaehlung_dict)
    for i in range(len(gegeb_wort)):
        Buchstaben_dict = {}
        Buchstaben_dict["Position"] = i
        Buchstaben_dict["Buchstabe"] = gegeb_wort[i]
        #print(Buchstaben_dict)
        if gegeb_wort[i] == ent_wort[i]:
            Buchstaben_dict["Farbe"] = "green"
            #print(zaehlung_dict[gegeb_wort[i]])
            zaehlung_dict[gegeb_wort[i]] -= 1
        else:
            Buchstaben_dict["Farbe"] = "white"
        Buchstaben_list.append(Buchstaben_dict)
    for x in range(len(ent_wort)):
        buchst = gegeb_wort[x]
        #print(x,"      " ,buchst,"      ", Buchstaben_list[x])
        if buchst in ent_wort:
            if zaehlung_dict[buchst] > 0 and Buchstaben_list[x]["Farbe"] != "Green":
                Buchstaben_list[x]["Farbe"] = "yellow"
                zaehlung_dict[buchst] -= 1
    return Buchstaben_list

list3 = ["arm", "Ion", "man", "tag", "weg", "see", "gut", "rot", "neu", "CPU" ]
list4 = ["baum", "geld", "netz", "herz", "kopf", "ecke", "mond", "raum", "zeit","kern", "volt","atom","Code","Nano"]
list5 = ["stahl", "stern", "robot", "monat", "nacht", "modul", "kraft", "wolke", "licht", "stoff"]
list6 = ["fehler", "sensor", "stimme","plasma", "wasser", "proton", "berlin", "system", "magnet", "moment", "aktion","statik"]
list7 = ["technik", "elektron", "verkehr", "energie","nominal", "analyse", "einheit", "bahnhof", "betrieb", "Kinetik"]
list8 = ["haustier", "hochzeit", "freiheit", "tierpark", "reaktion","netzwerk","Material","Funktion","steigung","Fachwerk",]
lists ={
    3:list3,
    4:list4,
    5:list5,
    6:list6,
    7:list7,
    8:list8,
}

gewinn3 = 0 
n = 3
while(n<9):
    #Richtige Wort wurde Random gewählt 
    gew_wort = random.choices(lists[n], k = 1)[0].upper()
    #print (gew_wort)
    while(n==3):
        root = tk.Tk()
        root.title("WORDLE")
        root.geometry("400x600")
        versuch = 1 
        while(versuch<=6): 
            #wir wndeln alle Buchstaben in Großen Buchstaben (für einfachen Vergleichen)
            ben_wort = str(input(f"Geben Sie ein {n} Buchstabige Wort an:")).upper()
            if(len(ben_wort) == n): 
                tk.Entry(root)  
                #print(Buch_list) 
                # create a frame to hold the boxes 
                row_frame = tk.Frame(root) 
                row_frame.pack(pady=20) 
                # create 5 empty letter boxes 
                boxes = []   # to save the labels so we can change them later 
                Buch_list = Buch_fun(ben_wort, gew_wort) #funktion wurde benutzt
                for i in range(0, len(ben_wort)): 
                    label = tk.Label( 
                    row_frame, 
                    text=str(ben_wort[i]), 
                    width=2, 
                    height=1, 
                    borderwidth=2, 
                    relief="solid", 
                    font=("Arial", 24)) 
                    label.grid(row=0, column=i, padx=3) 
                    boxes.append(label) 
                    #Farbe von Boxs ändern
                    Farbe = Buch_list[i]["Farbe"]
                    label.config(bg=Farbe)
                if(ben_wort == gew_wort): 
                    print("Das Wort ist richtig") 
                    label = tk.Label(root, text = "Das Wort ist richtig") 
                    label.pack() 
                    gewinn3 += 1 
                    n += 1 
                    break 
                if (versuch == 6): 
                    print(f"Sie haben alle Ihre Chancen benutzt.\n das richtige Wort ist {gew_wort}") 
                    label = tk.Label(root, text = f"Sie haben alle Ihre Chancen benutzt.\n das richtige Wort ist {gew_wort}") 
                    label.pack() 
                    n += 1  
                versuch += 1 
            else: 
                print(f"Das ist mehr/weniger als {n} Buchstabe. Versuchen Sie noch einmal")
    
    gew_wort = random.choices(lists[n],k=1)[0].upper()
    #print (gew_wort)    
    while(n==4):
        root = tk.Tk()
        root.title("WORDLE")
        root.geometry("400x600")
        versuch = 1 
        while(versuch<=6): 
            #wir wndeln alle Buchstaben in Großen Buchstaben (für einfachen Vergleichen)
            ben_wort = str(input(f"Geben Sie ein {n} Buchstabige Wort an:")).upper()
            if(len(ben_wort) == n): 
                tk.Entry(root)  
                #print(Buch_list) 
                # create a frame to hold the boxes 
                row_frame = tk.Frame(root) 
                row_frame.pack(pady=20) 
                # create 5 empty letter boxes 
                boxes = []   # to save the labels so we can change them later 
                Buch_list = Buch_fun(ben_wort, gew_wort) #funktion wurde benutzt
                for i in range(0, len(ben_wort)): 
                    label = tk.Label( 
                    row_frame, 
                    text=str(ben_wort[i]), 
                    width=2, 
                    height=1, 
                    borderwidth=2, 
                    relief="solid", 
                    font=("Arial", 24)) 
                    label.grid(row=0, column=i, padx=3) 
                    boxes.append(label) 
                    #Farbe von Boxs ändern
                    Farbe = Buch_list[i]["Farbe"]
                    label.config(bg=Farbe)
                if(ben_wort == gew_wort): 
                    print("Das Wort ist richtig") 
                    label = tk.Label(root, text = "Das Wort ist richtig") 
                    label.pack() 
                    gewinn3 += 1 
                    n += 1 
                    break 
                if (versuch == 6): 
                    print(f"Sie haben alle Ihre Chancen benutzt.\n das richtige Wort ist {gew_wort}") 
                    label = tk.Label(root, text = f"Sie haben alle Ihre Chancen benutzt.\n das richtige Wort ist {gew_wort}") 
                    label.pack() 
                    n += 1  
                versuch += 1 
            else: 
                print(f"Das ist mehr/weniger als {n} Buchstabe. Versuchen Sie noch einmal")


    gew_wort = random.choices(lists[n],k=1)[0].upper()
    #print (gew_wort) 
    while(n==5):
        root = tk.Tk()
        root.title("WORDLE")
        root.geometry("400x600")
        versuch = 1 
        while(versuch<=6): 
            #wir wndeln alle Buchstaben in Großen Buchstaben (für einfachen Vergleichen)
            ben_wort = str(input(f"Geben Sie ein {n} Buchstabige Wort an:")).upper()
            if(len(ben_wort) == n): 
                tk.Entry(root)  
                #print(Buch_list) 
                # create a frame to hold the boxes 
                row_frame = tk.Frame(root) 
                row_frame.pack(pady=20) 
                # create 5 empty letter boxes 
                boxes = []   # to save the labels so we can change them later 
                Buch_list = Buch_fun(ben_wort, gew_wort) #funktion wurde benutzt
                for i in range(0, len(ben_wort)): 
                    label = tk.Label( 
                    row_frame, 
                    text=str(ben_wort[i]), 
                    width=2, 
                    height=1, 
                    borderwidth=2, 
                    relief="solid", 
                    font=("Arial", 24)) 
                    label.grid(row=0, column=i, padx=3) 
                    boxes.append(label) 
                    #Farbe von Boxs ändern
                    Farbe = Buch_list[i]["Farbe"]
                    label.config(bg=Farbe)
                if(ben_wort == gew_wort): 
                    print("Das Wort ist richtig") 
                    label = tk.Label(root, text = "Das Wort ist richtig") 
                    label.pack() 
                    gewinn3 += 1 
                    n += 1 
                    break 
                if (versuch == 6): 
                    print(f"Sie haben alle Ihre Chancen benutzt.\n das richtige Wort ist {gew_wort}") 
                    label = tk.Label(root, text = f"Sie haben alle Ihre Chancen benutzt.\n das richtige Wort ist {gew_wort}") 
                    label.pack() 
                    n += 1  
                versuch += 1 
            else: 
                print(f"Das ist mehr/weniger als {n} Buchstabe. Versuchen Sie noch einmal")


    gew_wort = random.choices(lists[n],k=1)[0].upper()
    #print (gew_wort)    
    while(n==6):
        root = tk.Tk()
        root.title("WORDLE")
        root.geometry("400x600")
        versuch = 1 
        while(versuch<=6): 
            #wir wndeln alle Buchstaben in Großen Buchstaben (für einfachen Vergleichen)
            ben_wort = str(input(f"Geben Sie ein {n} Buchstabige Wort an:")).upper()
            if(len(ben_wort) == n): 
                tk.Entry(root)  
                #print(Buch_list) 
                # create a frame to hold the boxes 
                row_frame = tk.Frame(root) 
                row_frame.pack(pady=20) 
                # create 5 empty letter boxes 
                boxes = []   # to save the labels so we can change them later 
                Buch_list = Buch_fun(ben_wort, gew_wort) #funktion wurde benutzt
                for i in range(0, len(ben_wort)): 
                    label = tk.Label( 
                    row_frame, 
                    text=str(ben_wort[i]), 
                    width=2, 
                    height=1, 
                    borderwidth=2, 
                    relief="solid", 
                    font=("Arial", 24)) 
                    label.grid(row=0, column=i, padx=3) 
                    boxes.append(label) 
                    #Farbe von Boxs ändern
                    Farbe = Buch_list[i]["Farbe"]
                    label.config(bg=Farbe)
                if(ben_wort == gew_wort): 
                    print("Das Wort ist richtig") 
                    label = tk.Label(root, text = "Das Wort ist richtig") 
                    label.pack() 
                    gewinn3 += 1 
                    n += 1 
                    break 
                if (versuch == 6): 
                    print(f"Sie haben alle Ihre Chancen benutzt.\n das richtige Wort ist {gew_wort}") 
                    label = tk.Label(root, text = f"Sie haben alle Ihre Chancen benutzt.\n das richtige Wort ist {gew_wort}") 
                    label.pack() 
                    n += 1  
                versuch += 1 
            else: 
                print(f"Das ist mehr/weniger als {n} Buchstabe. Versuchen Sie noch einmal")


    gew_wort = random.choices(lists[n],k=1)[0].upper()
    #print (gew_wort)
    while(n==7):
        root = tk.Tk()
        root.title("WORDLE")
        root.geometry("400x600")
        versuch = 1 
        while(versuch<=6): 
            #wir wndeln alle Buchstaben in Großen Buchstaben (für einfachen Vergleichen)
            ben_wort = str(input(f"Geben Sie ein {n} Buchstabige Wort an:")).upper()
            if(len(ben_wort) == n): 
                tk.Entry(root)  
                #print(Buch_list) 
                # create a frame to hold the boxes 
                row_frame = tk.Frame(root) 
                row_frame.pack(pady=20) 
                # create 5 empty letter boxes 
                boxes = []   # to save the labels so we can change them later 
                Buch_list = Buch_fun(ben_wort, gew_wort) #funktion wurde benutzt
                for i in range(0, len(ben_wort)): 
                    label = tk.Label( 
                    row_frame, 
                    text=str(ben_wort[i]), 
                    width=2, 
                    height=1, 
                    borderwidth=2, 
                    relief="solid", 
                    font=("Arial", 24)) 
                    label.grid(row=0, column=i, padx=3) 
                    boxes.append(label) 
                    #Farbe von Boxs ändern
                    Farbe = Buch_list[i]["Farbe"]
                    label.config(bg=Farbe)
                if(ben_wort == gew_wort): 
                    print("Das Wort ist richtig") 
                    label = tk.Label(root, text = "Das Wort ist richtig") 
                    label.pack() 
                    gewinn3 += 1 
                    n += 1 
                    break 
                if (versuch == 6): 
                    print(f"Sie haben alle Ihre Chancen benutzt.\n das richtige Wort ist {gew_wort}") 
                    label = tk.Label(root, text = f"Sie haben alle Ihre Chancen benutzt.\n das richtige Wort ist {gew_wort}") 
                    label.pack() 
                    n += 1  
                versuch += 1 
            else: 
                print(f"Das ist mehr/weniger als {n} Buchstabe. Versuchen Sie noch einmal")

    gew_wort = random.choices(lists[n],k=1)[0].upper()       
    #print (gew_wort)
    while(n==8):
        root = tk.Tk()
        root.title("WORDLE")
        root.geometry("400x600")
        versuch = 1 
        while(versuch<=6): 
            ben_wort = str(input(f"Geben Sie ein {n} Buchstabige Wort an:")).upper()
            if(len(ben_wort) == n): 
                tk.Entry(root) 
                Buch_list = Buch_fun(ben_wort, gew_wort) 
                #print(Buch_list) 
                # create a frame to hold the boxes 
                row_frame = tk.Frame(root) 
                row_frame.pack(pady=20) 
                # create 5 empty letter boxes 
                boxes = []   # to save the labels so we can change them later 
                for i in range(0, len(ben_wort)): 
                    label = tk.Label( 
                    row_frame, 
                    text=str(ben_wort[i]), 
                    width=2, 
                    height=1, 
                    borderwidth=2, 
                    relief="solid", 
                    font=("Arial", 24)) 
                    label.grid(row=0, column=i, padx=3) 
                    boxes.append(label) 
                    #Farbe von Boxs ändern
                    Farbe = Buch_list[i]["Farbe"]
                    label.config(bg=Farbe)
                if(ben_wort == gew_wort): 
                    print("Das Wort ist richtig") 
                    label = tk.Label(root, text = "Das Wort ist richtig") 
                    label.pack() 
                    gewinn3 += 1 
                    n += 1 
                    break 
                if (versuch == 6): 
                    print(f"Sie haben alle Ihre Chancen benutzt.\n das richtige Wort ist {gew_wort}") 
                    label = tk.Label(root, text = f"Sie haben alle Ihre Chancen benutzt.\n das richtige Wort ist {gew_wort}") 
                    label.pack()
                    n += 1  
                versuch += 1 
            else: 
                print(f"Das ist mehr/weniger als {n} Buchstabe. Versuchen Sie noch einmal")

#Ergebnisse abgeben:   
print (f"Sie gaben {gewinn3} mal gewonnen")
