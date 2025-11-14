#Wordlegame 

                #messagebox.showinfo("titel", "richtig")                        
                #label.grid(row=0, column=0)
import random
import tkinter as tk
from tkinter import messagebox


def Buch_fun(gegeb_wort, ent_wort):
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
            Buchstaben_dict["Farbe"] = "Gruen"
            #print(zaehlung_dict[gegeb_wort[i]])
            zaehlung_dict[gegeb_wort[i]] -= 1
        else:
            Buchstaben_dict["Farbe"] = "Weiss"
        Buchstaben_list.append(Buchstaben_dict)
    
    for x in range(len(ent_wort)):
        buchst = gegeb_wort[x]
        #print(x,"      " ,buchst,"      ", Buchstaben_list[x])
        if buchst in ent_wort:
            if zaehlung_dict[buchst] > 0 and Buchstaben_list[x]["Farbe"] != "Gruen":
                Buchstaben_list[x]["Farbe"] = "Gelb"
                zaehlung_dict[buchst] -= 1
    return Buchstaben_list


n = 3
list3 = ["das"]
list4 = ["Stah"]
list5 = ["Stahl"]
list6 = ["fehler"]
list7 = ["fehlern"]
list8 = ["ergebnis"]
lists ={
    3:list3,
    4:list4,
    5:list5,
    6:list6,
    7:list7,
    8:list8,
}

while(n<9):
    gew_wort = random.choices(lists[n], k = 1)[0]
    print (gew_wort)
    while(n==3):
        root = tk.Tk()
        root.title("WORDLE")
        root.geometry("400x400")
        for versuch in range(1, 7):
            gewinn3 = 0
            ben_wort = str(input("Geben Sie ein 3 Buchstabige Wort an:"))
            tk.Entry(root)
            Buch_list = Buch_fun(ben_wort, gew_wort)
            print(Buch_list)
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
            if(ben_wort == gew_wort):
                print("Das Wort ist richtig")
                label = tk.Label(root, text = "Das Wort ist richtig")
                label.pack()
                gewinn3 += 1
                n += 1
                break
            if (versuch == 6):
                print(f"du hast alle deine Chancen benutzt.\n das richtige Wort ist {gew_wort}")
                n += 1        
    gew_wort = random.choices(lists[n],k=1)[0]
    print (gew_wort)    
    while(n==4):
        root = tk.Tk()
        root.title("WORDLE")
        root.geometry("400x400")
        for versuch in range(1, 7):
            gewinn4 = 0
            ben_wort = str(input("Geben Sie ein 4 Buchstabige Wort an:"))
            Buch_list = Buch_fun(ben_wort, gew_wort)
            if(ben_wort == gew_wort):
                print("Das Wort ist richtig")
                label = tk.Label(root, text = "Das Wort ist richtig")
                label.pack()
                gewinn4 += 1
                n += 1
                break
            if (versuch == 6):
                print(f"du hast alle deine Chancen benutzt.\n das richtige Wort ist {gew_wort}")
                n += 1
    gew_wort = random.choices(lists[n],k=1)[0]
    print (gew_wort) 
    while(n==5):
        for versuch in range(1, 7):
            gewinn5 = 0
            ben_wort = str(input("Geben Sie ein 5 Buchstabige Wort an:"))
            Buch_list = Buch_fun(ben_wort, gew_wort)
            if(ben_wort == gew_wort):
                print("Das Wort ist richtig")
                gewinn5 += 1
                n += 1
                break
            if (versuch == 6):
                print(f"du hast alle deine Chancen benutzt.\n das richtige Wort ist {gew_wort}")
                n += 1
    gew_wort = random.choices(lists[n],k=1)[0]
    print (gew_wort)    
    while(n==6):
        for versuch in range(1, 7):
            gewinn6 = 0
            ben_wort = str(input("Geben Sie ein 6 Buchstabige Wort an:"))
            Buch_list = Buch_fun(ben_wort, gew_wort)
            if(ben_wort == gew_wort):
                print("Das Wort ist richtig")
                gewinn6 += 1
                n += 1
                break
            if (versuch == 6):
                print(f"du hast alle deine Chancen benutzt.\n das richtige Wort ist {gew_wort}")
                n += 1
    gew_wort = random.choices(lists[n],k=1)[0]       
    print (gew_wort)
    while(n==7):
        for versuch in range(1, 7):
            gewinn7 = 0
            ben_wort = str(input("Geben Sie ein 7 Buchstabige Wort an:"))
            Buch_list = Buch_fun(ben_wort, gew_wort)
            if(ben_wort == gew_wort):
                print("Das Wort ist richtig")
                gewinn7 += 1
                n += 1
                break
            if (versuch == 6):
                print(f"du hast alle deine Chancen benutzt.\n das richtige Wort ist {gew_wort}")
                n += 1    
    gew_wort = random.choices(lists[n],k=1)[0]       
    print (gew_wort)
    while(n==8):
        for versuch in range(1, 7):
            gewinn8 = 0
            ben_wort = str(input("Geben Sie ein 8 Buchstabige Wort an:"))
            Buch_list = Buch_fun(ben_wort, gew_wort)
            if(ben_wort == gew_wort):
                print("Das Wort ist richtig")
                gewinn8 += 1
                n += 1
                break
            if (versuch == 6):
                print(f"du hast alle deine Chancen benutzt.\n das richtige Wort ist {gew_wort}")
                n += 1    
    