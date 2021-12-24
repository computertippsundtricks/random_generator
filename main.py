#Importieren der Bibliotheken
import time
import random
random.seed()

def english():
    #Header
    print()
    print("=================")
    print("Random generator")
    print("=================")
    print("--Version: 1.1")
    print("--Coded by redhead--")
    print("--All rights by redhead--")
    print("--Contact: read-head@t-online.de--")
    print()
    print()

    #def Zahl
    def zahl_en():
        print("Please enter in which area you would like to generate a number!")
        print("From:")
        try:
            von = int(input())
        except:
            print("No number, please enter a number! Please try again!")
            print("If you want to abort this program please press: 'a', if you want to try it again press enter")
            nextstep = str(input())
            if nextstep == "a":
                main_en()
            else:
                zahl_en()

        print("To:")
        try:
            bis = int(input())
        except:
            print("No number, please enter a number! Please try again!")
            print("If you want to abort this program please press: 'a', if you want to try it again press enter")
            nextstep = str(input())
            if nextstep == "a":
                main_en()
            else:
                zahl_en()

        try:
            result = random.randint(von, bis)
            print()
            print("-----------------------------------------------")
            print("The randomly generated number is:", result)
            print("-----------------------------------------------")
            print()
        except:
            print("Unfortunately this did not work! Please try again!")
            print("If you want to abort this program please press: 'a', if you want to try it again press enter")
            nextstep = str(input())
            if nextstep == "a":
                main_en()
            else:
                zahl_en()

    # def Buchstabe
    def buchstabe_en():
        anzahl = -1
        bu = ""
        wieviel = -1
        resultb = ""

        # Eingabe Menge an buchstaben
        print("Please enter the number of letters from which letters should be generated")
        print("If you want to use the complete alphabet (with umlauts: ä, ö, ü), just type in an 'a'.")
        nextstep10 = input()
        if nextstep10 == "a":
            print("The complete alphabet is used as a basis ...")
            anzahl = "Complete alphabet"
            anzahlprogramm = 0
        elif not nextstep10 == "a":
            try:
                anzahl = int(nextstep10)
                anzahlprogramm = 1
            except:
                print("Input incorrect, please enter a number ...")
                buchstabe_en()

        # Eingabe zu generierende Menge an Buchstaben
        print("How many letters would you like to have randomly generated?")
        input2 = str(input())
        input1 = input2

        if anzahl == "Complete alphabet":
            wieviel = input1
        else:
            try:
                input1 = int(input2)
                if input1 > anzahl:
                    print("The number entered is larger than the number of letters entered, please try again")
                    print()
                    buchstabe_en()
                elif input1 < 1:
                    print("The number entered is less than 1, please try again ...")
                    print()
                    buchstabe_en()
                else:
                    wieviel = input1
            except:
                print("Wrong entry ...")
                buchstabe_en()

        print()
        print("You have made the following entries:  | Amount of letters:", anzahl, " | Amount of letters to be generated:", wieviel, "|")
        print()

        time.sleep(0.5)

        if anzahl == "Complete alphabet":
            wieviel = int(input2)

        if not anzahlprogramm == 0:
            for buchstaben in range(1, anzahl + 1):
                print("Please enter a desired letter:")
                b = str(input())
                bu = bu + b
                print("Entry successful")


        elif anzahlprogramm == 0:
            bu = "abcdefghijklmnopqrstuvwxyzäöü"

        for howmach in range(1, wieviel + 1):
            print("1 letter is determined from the following letters:", bu)
            resultbu = random.choice(bu)
            resultb = resultb + resultbu

        print()
        print("Letters are generated ...")
        time.sleep(1)
        print("Letters have been generated!")
        print()
        print("-----------------------------------------------")
        print("The randomly generated letters are:", resultb)
        print("-----------------------------------------------")
        print()
        main_en()

    #Main Programm
    def main_en():
        print("Please enter what you want to generate randomly, or whether you want to exit the program:")
        print("Number (b), letters (l), exit program (e)")
        nextstep = str(input())
        
        if nextstep == "b":
            zahl_en()
            print("Restart the program (r) or cancel (e)?")
            nextstep1 = str(input())
            if nextstep1 == "r":
                main_en()
            elif nextstep1 == "e":
                print("The program is ending ...")
                time.sleep(0.5)
                print("Program has ended!")
                exit()
            else:
                print("The program was terminated automatically due to incorrect entry!")
                exit()

        elif nextstep == "l":
            buchstabe_en()

        elif nextstep == "e":
            print("The program is ending ...")
            time.sleep(1)
            print("Program has ended!")
            exit()

        else:
            print("Wrong entry please try again!")
            main_en()

        

    #Main Programm Aufruf      
    main_en()

def german():
    #Header
    print()
    print("=================")
    print("Zufallsgenerator")
    print("=================")
    print("--Version: 1.1")
    print("--Coded by redhead--")
    print("--All rights by redhead--")
    print("--Contact: read-head@t-online.de--")
    print()
    print()

    #def Zahl
    def zahl():
        print("Bitte geben sie ein in welchem Bereich sie eine Zahl generieren Möchten!")
        print("Von:")
        try:
            von = int(input())
        except:
            print("Keine Zahl, bitte gebe eine Zahl ein! Bitte Probiere es erneut!")
            print("Wenn sie dieses Programm abrechen wollen drücken sie bitte: 'a', wollen sie es nocheinmal Probieren drücken sie Enter")
            nextstep = str(input())
            if nextstep == "a":
                main()
            else:
                zahl()

        print("bis:")
        try:
            bis = int(input())
        except:
            print("Keine Zahl, bitte gebe eine Zahl ein! Bitte Probiere es erneut!")
            print("Wenn sie dieses Programm abrechen wollen drücken sie bitte: 'a', wollen sie es nocheinmal Probieren drücken sie Enter")
            nextstep = str(input())
            if nextstep == "a":
                main()
            else:
                zahl()

        try:
            result = random.randint(von, bis)
            print()
            print("-----------------------------------------------")
            print("Die Zufällig generierte Zahl ist:", result)
            print("-----------------------------------------------")
            print()
        except:
            print("Das hat leider nicht funktioniert! Bitte Probiere es erneut!")
            print("Wenn sie dieses Programm abrechen wollen drücken sie bitte: 'a', wollen sie es nocheinmal Probieren drücken sie Enter")
            nextstep = str(input())
            if nextstep == "a":
                main()
            else:
                zahl()



    #def Buchstabe
    def buchstabe():
        anzahl = -1
        bu = ""
        wieviel = -1
        resultb = ""

        #Eingabe Menge an buchstaben
        print("Bitte geben sie die Menge der Buchstaben an, aus denen Buchstaben generiert werden sollen")
        print("Sollten sie das Komplette Alphabet nehmen wollen (mit Umlauten: ä, ö, ü), tippen sie einfach ein 'a' ein.")
        nextstep10 = input()
        if nextstep10 == "a":
            print("Das Komplette Alphabet wird als Grundlage genutzt...")
            anzahl = "Komplettes Alphabet"
            anzahlprogramm = 0
        elif not nextstep10 == "a":
            try:
                anzahl = int(nextstep10)
                anzahlprogramm = 1
            except:
                print("Eingabe Fehlerhaft, bitte geben sie eine Zahl ein...")
                buchstabe()

        #Eingabe zu generierende Menge an Buchstaben
        print("Wie viele Buchstaben möchten sie zufällig generiert haben?")
        input2 = str(input())
        input1 = input2

        if anzahl == "Komplettes Alphabet":
            wieviel = input1
        else:
            try:
                input1 = int(input2)
                if input1 > anzahl:
                    print("Die eingegeben Zahl ist größer als die Menge der Eingegeben Buchstaben, bitte Probieren sie es erneut")
                    print()
                    buchstabe()
                elif input1 < 1:
                    print("Die eingegeben Zahl ist kleiner als 1, bitte Probieren sie es erneut...")
                    print()
                    buchstabe()
                else:
                    wieviel = input1
            except:
                print("Falsche eingabe...")
                buchstabe()

        print()
        print("Sie haben folgende eingaben gemacht:  | Menge an Buchstaben:", anzahl, " | Menge an zu generieden Buchstaben:", wieviel, "|")
        print()

        time.sleep(0.5)

        if anzahl == "Komplettes Alphabet":
            wieviel = int(input2)


        if not anzahlprogramm == 0:
            for buchstaben in range(1,anzahl+1):
                print("Bitte geben sie einen Gewünschten Buchstaben ein:")
                b = str(input())
                bu = bu + b
                print("Eingabe erfolgreich")


        elif anzahlprogramm == 0:
            bu = "abcdefghijklmnopqrstuvwxyzäöü"


        for howmach in range(1, wieviel+1):
            print("Aus folgenden Buchstaben wird 1 Buchstabe ermittelt:", bu)
            resultbu = random.choice(bu)
            resultb = resultb + resultbu

        print()
        print("Buchstaben werden generiert...")
        time.sleep(1)
        print("Buchstaben wurden generiert!")
        print()
        print("-----------------------------------------------")
        print("Die Zufällig generierten Buchstaben sind:", resultb)
        print("-----------------------------------------------")
        print()
        main()


    #Main Programm
    def main():
        print("Bitte gebe ein was du zufällig generieren willst, oder ob du dass Programm beenden willst:")
        print("Zahl (z), Buchstaben (b), Programm Beenden (e)")
        nextstep = str(input())
        
        if nextstep == "z":
            zahl()
            print("Programm neu starten (n) oder abbrechen (a)?")
            nextstep1 = str(input())
            if nextstep1 == "n":
                main()
            elif nextstep1 == "a":
                print("Das Programm wird beendet...")
                time.sleep(0.5)
                exit()
            else:
                print("Das Programm wurde automatisch beendet, da falsche eingabe!")
                exit()

        elif nextstep == "b":
            buchstabe()

        elif nextstep == "e":
            print("Programm wird beendet...")
            time.sleep(1)
            print("Programm wurde beendet!")
            exit()

        else:
            print("Falsche eingabe bitte probieren sie es erneut!")
            main()

        

    #Main Programm Aufruf      
    main()

#Sprache Auswählen (Start des Programms)s
print()
print("Info: Please contact me if the program crashes or you discover another error (read-head@t-online.de)")
print()
print("Please choose your Language:")
print("[1] -- German")
print("[2] -- English")
print("┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅")
print("[3] -- Exit Programm")
print("┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅")
print("Insert here:")

try:
    language = int(input())
except:
    language = 2
    print("Wrong entry, the language was automatically set to English")

if language == 1:
    german()
elif language == 2:
    english()
elif language == 3:
    print("The programm is ending...")
    time.sleep(1)
    print("The Program has ended!")
else:
    print("Wrong entry, the language was automatically set to English")
    english()