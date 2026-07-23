'''
Karolina's defenitions

OOP = print(str) (can take in variables with dif syntax). Function, specific datatypes it takes in. write(filename)
Klass, objekt, instans = Klass (def) creates objects (references/copy). instances is a specific object are refering to. mom, siblings, sibling

Klass = rules ex print, write - rules with empty data
Objekt = copy of klass / ex of class - rules with data (copy + data)
instans = one specfic objekt
Attribut = variables
Method = function
'''


    # Syntax for classes
    class Bilar: # Bör namnges med stor bokstav i början, va ett substantiv tex Bilar

        competition = "Formula 1" # Klassattribut, delad av alla objekt i klassen

        def __init__(self, age, arg2): # Instansatribut, unik för varje objekt genom att data läggs till
            self.age = age # Här skapas attribut/variabler tex ålder, vikt
            self.weight = arg2
        
        def värde(self, age, weight): # funktion/metod som beräknar bilens värde
            pengar = self.age * 1000 + self.weight * 500 # Obs även enkla funktioner som len() behövs läggas till så de funkar på din klass
            return pengar

        # Lägg till enkla funktioner vi vill ha
        def __str__(self): # __str__() är en speciell metod som definierar hur objektet ska representeras som en sträng
            return f"Bil med ålder: {self.age}, vikt: {self.weight}, tävling: {KlassNamn.competition}"
        
        def __len__(self):
            pass
        
        def hoarse_happines(self, age):
            return hapiness = self.age ** 2
    
    # Syntax för att skapa ett objekt (instans) av klassen
    objekt = KlassNamn(ålder1, vikt2) # objekt kan nu manipulera hela datan från Bilar med hjälp av enkel punktnotation
    objekt.attribut3 = värde3 # Här kan man lägga till fler attribut, obs kan skrivas över
    objekt.metod() # Här kan man anropa metoder som redan finns i klassen
    objekt2 = KlassNamn(ålder2, vikt3) # Här skapas ett nytt objekt med annan data som en kopia
    print(objekt2.attribut2) # För att använda funktioner som redan finns på objektet, kalla på dess info/attribut

    VolvoW80 = Bilar(2, 800, "blue")
    volvo_pengar = volow80.värde()
    Hoarses = Bilar(7, 900, "brown")


    # Privata och publika attribut/metoder
    class Bil:
        def __init__(self, ålder, vikt):
            self._ålder = ålder  # Privata attribut (bör inte ändras utanför klassen)
            self._vikt = vikt    # Privata attribut (bör inte ändras utanför klassen)

        def beräkna_värde(self):
            return self._ålder * 1000 + self._vikt * 500  # Publik metod som använder privata attribut

    min_bil = Bil(5, 1500) # man kan manipulera med beräkna_värde() men inte ändra _ålder eller _vikt direkt om man inte skriver...
    min_bil._ålder = 10  # ...så här, men det är inte rekommenderat eftersom det bryter mot principen om inkapsling.


class verify_data(self, data)
    __init__
    0 < data < 5000
    data == int

class verify_functions

class algoritm_preperation

class algoritm_v1

class algoritm_v2

def call function(data, algoritm, v2)

