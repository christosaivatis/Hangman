# HANGMAN-SPIEL (GANGELMÄNNCHEN)
# made by Chris

logo = """
<>        <>          <>          <>        <>      <><><><><>     <>                <>          <>          <>        <>
<>        <>         <><>         <><>      <>    <>          <>   <><>            <><>         <><>         <><>      <>
<>        <>        <>  <>        <> <>     <>   <>                <> <>          <> <>        <>  <>        <> <>     <>
<>        <>       <>    <>       <>  <>    <>  <>                 <>  <>        <>  <>       <>    <>       <>  <>    <>
<><><><><><>      <><><><><>      <>   <>   <>  <>       <><><><>  <>   <>      <>   <>      <><><><><>      <>   <>   <>
<>        <>     <>        <>     <>    <>  <>  <>             <>  <>    <>    <>    <>     <>        <>     <>    <>  <>
<>        <>    <>          <>    <>     <> <>   <>            <>  <>     <>  <>     <>    <>          <>    <>     <> <>
<>        <>   <>            <>   <>      <><>    <>           <>  <>      <><>      <>   <>            <>   <>      <><>
<>        <>  <>              <>  <>        <>      <><><><><> <>  <>       <>       <>  <>              <>  <>        <>
"""

fehler_meldung = '''
!?!?!?!?!?!?!?!?!?!?!?!?!?!?!?!?!?!?!?!?!?!?!?!?!?!?!?!?!?!?!?!?!?
?                                                                !
!               Das war keine gültige Eingabe...                 ?
?   Bitte nächstes Mal die Anweisungen sorgfältig durchlesen!!!  !
!               Sonst explodiert Dein Rechner :-O                ?
?                                                                !
!?!?!?!?!?!?!?!?!?!?!?!?!?!?!?!?!?!?!?!?!?!?!?!?!?!?!?!?!?!?!?!?!?
'''

sieg = """HERZLICHEN GLÜCKWUNSCH !!!
               \\------------\\
                \\  Hurra!!!  \\
                 \\------------\\
            \\ O /
             \\|/
              |
             / \\         
            /   \\
          =========
       ___||     ||___
      ||             ||
=====================================
"""

fehler_1 = """Leider nicht :(








      =============
      ||         ||___
      ||             ||
=====================================
"""

fehler_2 = """Leider nicht :(


          ||
          ||
          ||
          ||
          ||
          ||
      =============
      ||         ||___
      ||             ||
=====================================
"""

fehler_3 = """Leider nicht :(
           _________
          |/
          ||
          ||
          ||
          ||
          ||
          ||
      =============
      ||         ||___
      ||             ||
=====================================
"""

fehler_4 = """Leider nicht :(
           _________
          |/       |
          ||       |
          ||
          ||
          ||
          ||
          ||
      =============
      ||         ||___
      ||             ||
=====================================
"""

fehler_5 = """Leider nicht :(    Vorsicht, keine Fehler mehr möglich!!!
           _________
          |/       |
          ||       |
          ||      ( )
          ||
          ||
          ||
          ||
      =============
      ||         ||___
      ||             ||
=====================================
"""

niederlage = """Unser Beileid ...
           _________
          |/       |
          ||       |
          ||      (O)
          ||      /|\\
          ||       |
          ||      / \\
          ||
      =============
      ||         ||___
      ||             ||
=====================================
"""

# Das eigentliche Suchwort (String)
suchwort = ""

# Das bislang entdeckte Suchwort (String)
teilwort_entdeckt_str = ""
# Die bislang entdeckte Stellen des Suchwortes (List)
teilwort_entdeckt_liste = []

# Die bislang falsch geratene Buchstaben (List)
falsche_buchstaben = []

# Die maximal erlaubte Anzahl an Fehlversuchen (Integer)
fehlversuche_max = 5
# Die bislang gemachte Anzahl an Fehlversuchen (Integer)
fehlversuche_bislang = 0
# Die noch übrige Anzahl an erlaubten Fehlversuchen (Integer)
fehlversuche_uebrig = 5

# Der geratene Buchstabe (String)
buchstabe = ""

# Hilfsvariable (String)
x = ""
# Hilfsvariable (Integer)
i = 0

# Hilfsvariable (String)
spiel_start = 'j'


# TODO: Diese ziemlich große Funktion in mehreren kleineren Funktionen auslagern ("Clean Code"-Grundsätze)
def start_new_game():
    suchwort = input("Gib jetzt bitte das Suchwort ein." + "\n" +
                     "Vorsicht! Keine Leerzeichen und nur alphabetische Buchstaben erlaubt: ")

    if (suchwort.isalpha() == False):
        print(fehler_meldung)
        return

    # Alle Buchstaben des Suchwortes werden in Großbuchstaben umgewandelt
    suchwort = suchwort.upper()

    teilwort_entdeckt_liste = []
    for x in suchwort:
        teilwort_entdeckt_liste.append("_")

    falsche_buchstaben = []
    fehlversuche_bislang = 0

    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n" + "Fertig? Los geht's!!!" + "\n")

    while (('_' in teilwort_entdeckt_liste) and (fehlversuche_bislang <= fehlversuche_max)):
        teilwort_entdeckt_str = ""
        for x in teilwort_entdeckt_liste:
            teilwort_entdeckt_str = teilwort_entdeckt_str + x + " "

        print("Bislang Teilwort entdeckt:", teilwort_entdeckt_str)
        print("Bislang falsche Buchstaben:", falsche_buchstaben)

        fehlversuche_uebrig = fehlversuche_max - fehlversuche_bislang
        print("Fehlversuche noch übrig:", fehlversuche_uebrig)

        print("...")

        # Eingabe eines Buchstabes und Kontrolle auf evtl. Fehleingabe
        buchstabe = ""
        while ( (buchstabe.isalpha() == False) or (len(buchstabe) > 1) ):
            buchstabe = input(">> Rate einen Buchstaben: ")

        # Der Buchstabe wird in einen Großbuchstaben umgewandelt
        buchstabe = buchstabe.upper()

        if (buchstabe in suchwort):
            print("Korrekt! :D")
            i = 0
            for x in suchwort:
                if (x == buchstabe):
                    teilwort_entdeckt_liste[i] = x
                i += 1
        # TODO: Wenn der Benutzer mehrmals denselben falschen Buchstaben rät,
        #  wäre es vielleicht besser, wenn das nur beim ersten Mal als Fehler zählt..!?
        else:
            fehlversuche_bislang += 1
            match fehlversuche_bislang:
                case 1:
                    print(fehler_1)
                case 2:
                    print(fehler_2)
                case 3:
                    print(fehler_3)
                case 4:
                    print(fehler_4)
                case 5:
                    print(fehler_5)

            falsche_buchstaben.append(buchstabe)

    if (fehlversuche_bislang <= fehlversuche_max):
        print("Vollständig entdeckt")
        print("---------->", suchwort, "<----------")
        print(sieg)
    else:
        print("Das gesuchte Wort war")
        print("---------->", suchwort, "<----------")
        print(niederlage)


def run():
    print(logo)

    spiel_start = 'j'
    while (spiel_start == 'j'):

        start_new_game()

        while True:
            spiel_start = input("Möchtest Du es nochmal versuchen? (j/n): ")
            if (spiel_start == 'j'):
                break
            elif (spiel_start == 'n'):
                break

if __name__ == '__main__':
    run()
