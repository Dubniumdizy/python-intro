"""
Minitester och Quiz i Objektorienterad Programmering (OOP) och Mängder.

Detta skript innehåller 10 självständiga minitester utformade för att testa och 
säkerställa att en student har förstått grundläggande koncept inom OOP, 
inkapsling, metoder, referenser och mängder (sets) i Python.
"""

# =============================================================================
# KLASSER OCH HJÄLPKOD FÖR TESTERNA
# =============================================================================

class Bil:
    """
    En klass som representerar en bil.
    Används i testerna för att demonstrera attribut, metoder och inkapsling.
    """
    # Klassattribut: Delas av alla instanser av klassen Bil
    tävling = "Formula 1"

    def __init__(self, ålder: int, vikt: float):
        """
        Konstruktor för Bil.
        
        Args:
            ålder (int): Bilens ålder i år.
            vikt (float): Bilens vikt i kg.
        """
        # Privata instansattribut (inleds med understreck enligt konvention)
        self._ålder = ålder
        self._vikt = vikt

    def beräkna_värde(self) -> float:
        """Beräknar bilens värde baserat på dess ålder och vikt."""
        return self._ålder * 1000 + self._vikt * 500

    def __str__(self) -> str:
        """Returnerar en läsbar strängrepresentatons av objektet."""
        return f"Bil (Ålder: {self._ålder}, Vikt: {self._vikt})"


# =============================================================================
# 10 ST MINITESTER (KÖRBARA FUNKTIONER)
# =============================================================================

def test_1_klass_vs_objekt():
    """
    MINITEST 1: Skillnad mellan Klass och Objekt (Instans).
    -----------------------------------------------------
    Teori: 
    En klass är en 'mall' eller 'ritning'. Ett objekt är en 'instans' 
    (ett konkret exempel) som skapats utifrån klassen.
    
    Fråga: 
    Skapas minnesutrymme för specifika instansvariabler när klassen definieras 
    eller när objektet instansieras?
    
    Svar/Förklaring:
    Minnesutrymmet för instansattribut skapas först när objektet initieras 
    via konstruktorn (`Bil(...)`).
    """
    # Vi skapar två separata objekt från samma klass
    bil_a = Bil(ålder=2, vikt=1200)
    bil_b = Bil(ålder=6, vikt=1600)

    # Verifiera att de är två olika objekt i minnet (olika id)
    assert bil_a is not bil_b, "bil_a och bil_b ska vara två olika objekt!"
    assert bil_a._ålder != bil_b._ålder, "Objekten ska ha egna instansvärden!"
    print("[Passerat] Test 1: Klass vs Objekt")


def test_2_konstruktor_och_init():
    """
    MINITEST 2: Konstruktorn __init__().
    -----------------------------------
    Teori: 
    Metoden __init__() anropas automatiskt när ett nytt objekt skapas. 
    Den sätter upp objektets initiala tillstånd genom att tilldela instansattribut.
    
    Fråga: 
    Vad händer om vi försöker skapa ett Bil-objekt utan att skicka med argumenten 
    som __init__ förväntar sig?
    
    Svar/Förklaring:
    Python kastar ett TypeError eftersom parametrarna `ålder` och `vikt` saknar standardvärden.
    """
    try:
        # Försök skapa en bil utan argument (skall misslyckas)
        ogiltig_bil = Bil()  # type: ignore
        assert False, "Koden borde ha kastat ett TypeError!"
    except TypeError:
        # Förväntat beteende
        pass

    # Korrekt anrop
    korrekt_bil = Bil(3, 1000)
    assert korrekt_bil._ålder == 3, "Åldern initierades inte korrekt!"
    print("[Passerat] Test 2: Konstruktor och __init__()")


def test_3_klassattribut_vs_instansattribut():
    """
    MINITEST 3: Klassattribut vs Instansattribut.
    ----------------------------------------------
    Teori: 
    Klassattribut delas av ALLA objekt som skapas från klassen. 
    Instansattribut hör enbart till det specifika objektet där de skapades.
    
    Fråga: 
    Om vi ändrar klassattributet `tävling` på själva klassen `Bil`, vad händer 
    med värdet för de befintliga bil-objekten?
    
    Svar/Förklaring:
    Alla objekt som inte har skrivit över attributet lokalt ser den nya uppdateringen.
    """
    b1 = Bil(1, 1000)
    b2 = Bil(2, 1100)

    # Båda bilarna delar ursprungsvärdet för klassattributet
    assert b1.tävling == "Formula 1" and b2.tävling == "Formula 1"

    # Vi ändrar klassattributet på klassnivå
    Bil.tävling = "NASCAR"

    # Ändringen reflekteras hos båda objekten
    assert b1.tävling == "NASCAR", "b1 borde ha fått det nya klassattributet!"
    assert b2.tävling == "NASCAR", "b2 borde ha fått det nya klassattributet!"

    # Återställ för framtida tester
    Bil.tävling = "Formula 1"
    print("[Passerat] Test 3: Klassattribut vs Instansattribut")


def test_4_self_och_metoder():
    """
    MINITEST 4: Parametern 'self' och metodanrop.
    --------------------------------------------
    Teori: 
    'self' representerar den aktuella instansen av klassen. När en metod anropas 
    med punktnotation (`objekt.metod()`), skickar Python automatiskt med `objekt` 
    som det första argumentet (`self`).
    
    Fråga: 
    Är `min_bil.beräkna_värde()` ekvivalent med `Bil.beräkna_värde(min_bil)`?
    
    Svar/Förklaring:
    Ja! Punktnotationen är bara syntaktiskt för att skicka instansen som `self`. 
    Först har vi objekt.metod() sen har vi klass.metod(instans) vilket är samma sak.
    """
    min_bil = Bil(ålder=4, vikt=1000)

    # Metodanrop via punktnotation
    värde1 = min_bil.beräkna_värde()

    # Explicit metodanrop via klassen där vi skickar med instansen manuellt
    värde2 = Bil.beräkna_värde(min_bil)

    assert värde1 == värde2 == 504000, "Båda sätten att anropa metoden måste ge samma resultat!"
    print("[Passerat] Test 4: Self och metoder")


def test_5_inkapsling_och_privata_attribut():
    """
    MINITEST 5: Inkapsling (Privata attribut med understreck).
    ---------------------------------------------------------
    Teori: 
    Ett understreck i början av ett attributnamn (`_ålder`) markerar att attributet 
    är 'privat' och endast bör ändras internt i klassen för att skydda dess tillstånd.
    
    Fråga: 
    Kan man tekniskt sett ändra `_ålder` utifrån i Python, även om det bryter mot god sed?
    
    Svar/Förklaring:
    Ja, Python tillämpar inte strikt privat tillgång på språk-nivå, utan litar på 
    konventioner ("vi är alla vuxna här"). Men att göra det bryter mot inkapslingsprincipen.
    """
    min_bil = Bil(5, 1200)

    # Ändra via rekommenderat vis (metoder) eller förstå konsekvensen av direktändring:
    min_bil._ålder = 10  # Bryter mot konventionen, men Python tillåter det

    assert min_bil._ålder == 10, "Attributet ändrades i minnet trots att det är 'privat'."
    print("[Passerat] Test 5: Inkapsling och privata attribut")


def test_6_str_metoden():
    """
    MINITEST 6: Den magiska metoden __str__().
    -------------------------------------------
    Teori: 
    __str__() är en speciell metod som definierar hur objektet ska representeras 
    som en sträng när man t.ex. anropar `str(objekt)` eller `print(objekt)`.
    
    Fråga: 
    Vad returneras om vi konverterar ett `Bil`-objekt till en sträng?

    Svar:
    Det returneras en sträng i formatet: "Bil (Ålder: <ålder>, Vikt: <vikt>)".
    """
    min_bil = Bil(ålder=3, vikt=1100)
    sträng_representaion = str(min_bil)

    assert sträng_representaion == "Bil (Ålder: 3, Vikt: 1100)", "__str__ returnerade fel format!"
    print("[Passerat] Test 6: Magiska metoden __str__()")


def test_7_dynamiska_attribut():
    """
    MINITEST 7: Dynamisk tilldelning av nya attribut.
    --------------------------------------------------
    Teori: 
    I Python kan man lägga till ett nytt attribut på ett enskilt objekt NÄR SOM HELST 
    efter att det har skapats, utan att ändra klassdefinitionen.
    
    Fråga: 
    Om vi lägger till `objekt1.färg = 'Röd'`, får då `objekt2` också attributet `färg`?
    
    Svar/Förklaring:
    Nej, det nya attributet knyts enbart till det specifika objektet (`objekt1`).
    """
    bil1 = Bil(2, 1000)
    bil2 = Bil(4, 1200)

    # Dynamiskt lägga till ett nytt attribut på bil1
    bil1.färg = "Röd"  # type: ignore

    assert hasattr(bil1, "färg"), "bil1 borde nu ha attributet 'färg'."
    assert not hasattr(bil2, "färg"), "bil2 ska INTE ha fått attributet 'färg'!"
    print("[Passerat] Test 7: Dynamiska attribut")


def test_8_objektreferenser_i_minnet():
    """
    MINITEST 8: Objektreferenser och variabler.
    -------------------------------------------
    Teori: 
    I Python är en variabel en referens (pekare) till ett objekt i minnet. 
    Om du tilldelar `b2 = b1` pekar båda variablerna på EXAKT samma objekt.
    
    Fråga: 
    Vad händer med `b1._ålder` om vi ändrar `b2._ålder` när `b2 = b1`?
    
    Svar/Förklaring:
    `b1._ålder` ändras också, eftersom både `b1` och `b2` pekar på samma Bil-instans.
    """
    b1 = Bil(ålder=1, vikt=900)
    b2 = b1  # b2 pekar nu på samma objekt som b1

    b2._ålder = 5  # Ändring via b2

    assert b1._ålder == 5, "b1._ålder borde också ha ändrats eftersom b1 och b2 är samma objekt!"
    assert b1 is b2, "b1 och b2 ska peka på exakt samma identitet i minnet!"
    print("[Passerat] Test 8: Objektreferenser i minnet")


def test_9_mengder_mängdlära():
    """
    MINITEST 9: Sets (Mängder) - Unika element och operander.
    --------------------------------------------------------
    Teori: 
    Ett `set` i Python kan endast innehålla unika element. 
    Det stödjer matematiska operationer som Union (`|`), Snitt (`&`), 
    Differens (`-`) och Symmetrisk differens (`^`).
    
    Fråga: 
    Vad blir resultatet av `a - b` och `a & b` om `a = {1, 2, 3}` och `b = {3, 4, 5}`?

    Svar:
    'a - b' ger {1, 2} (element i a som inte finns i b) och
    'a & b' ger {3} (element som finns i både a och b).
    """
    a = {1, 2, 3, 4, 5}
    b = {4, 5, 6, 7, 8}

    # Union: Alla element från båda sets utan dubbletter
    union_set = a | b
    assert union_set == {1, 2, 3, 4, 5, 6, 7, 8}

    # Snitt (Intersection): Element som finns i BÅDA
    snitt_set = a & b
    assert snitt_set == {4, 5}

    # Differens: Element i 'a' som INTE finns i 'b'
    diff_set = a - b
    assert diff_set == {1, 2, 3}

    print("[Passerat] Test 9: Sets (Mängder) och operatorer")


def test_10_symmetrisk_differens():
    """
    MINITEST 10: Symmetrisk differens på Sets.
    -----------------------------------------
    Teori: 
    Symmetrisk differens (`a ^ b`) returnerar alla element som finns i antingen 
    `a` eller `b`, men INTE i båda två samtidigt. 
    Det är samma sak som `(a - b) | (b - a)`.
    
    Fråga: 
    Vad blir resultatet av `{1, 2, 3} ^ {2, 3, 4}`?

    Svar:
    Resultatet blir {1, 4}, eftersom 1 finns bara i det första setet och 4 bara i det andra.
    """
    set1 = {1, 2, 3}
    set2 = {2, 3, 4}

    sym_diff = set1 ^ set2
    förväntat = {1, 4}

    assert sym_diff == förväntat, "Symmetrisk differens beräknades felaktigt!"
    assert sym_diff == (set1 - set2) | (set2 - set1), "Formeln (a-b)|(b-a) stämmer inte!"
    print("[Passerat] Test 10: Symmetrisk differens")


# =============================================================================
# HUVUDPROGRAM FÖR AT KÖRA ALLA TESTER
# =============================================================================

if __name__ == "__main__":
    print("--- STARTAR MINITESTER I PYTHON OOP OCH MÄNGDER ---\n")
    
    test_1_klass_vs_objekt()
    test_2_konstruktor_och_init()
    test_3_klassattribut_vs_instansattribut()
    test_4_self_och_metoder()
    test_5_inkapsling_och_privata_attribut()
    test_6_str_metoden()
    test_7_dynamiska_attribut()
    test_8_objektreferenser_i_minnet()
    test_9_mengder_mängdlära()
    test_10_symmetrisk_differens()
    
    print("\n--- ALLA 10 MINITESTER GICK IGENOM UTAN FEL! ---")