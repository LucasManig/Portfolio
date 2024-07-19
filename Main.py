MENUE = {
    "espresso": {
        "zutaten": {
            "wasser": 50,
            "kaffee": 18,
        },
        "kosten": 1.5,
    },
    "latte": {
        "zutaten": {
            "wasser": 200,
            "milch": 150,
            "kaffee": 24,
        },
        "kosten": 2.5,
    },
    "cappuccino": {
        "zutaten": {
            "wasser": 250,
            "milch": 100,
            "kaffee": 24,
        },
        "kosten": 3.0,
    }
}

gewinn = 0
ressourcen = {
    "wasser": 300,
    "milch": 200,
    "kaffee": 100,
}

print('espresso 1.5$ latte 2.5$ cappuccino 3.0$ - tippe "bericht" um die Menge an Zutaten zu sehen')

def sind_ressourcen_ausreichend(bestellte_zutaten):
    for item in bestellte_zutaten:
        if bestellte_zutaten[item] > ressourcen[item]:
            print(f"Entschuldigung, es gibt nicht genug {item}.")
            return False
    return True

def münzen_verarbeiten():
    print("Bitte Münzen einwerfen.")
    gesamt = int(input("Wie viele Vierteldollar?: ")) * 0.25
    gesamt += int(input("Wie viele Zehnteldollar?: ")) * 0.1
    gesamt += int(input("Wie viele Fünfcentstücke?: ")) * 0.05
    gesamt += int(input("Wie viele Centstücke?: ")) * 0.01
    return gesamt

def ist_transaktion_erfolgreich(bezahlt, kosten_getränk):
    if bezahlt >= kosten_getränk:
        wechselgeld = round(bezahlt - kosten_getränk, 2)
        print(f"Hier ist ${wechselgeld} an Wechselgeld.")
        global gewinn
        gewinn += kosten_getränk
        return True
    else:
        print("Entschuldigung, das ist nicht genug Geld. Geld zurückerstattet.")
        return False

def kaffee_zubereiten(getränk_name, bestellte_zutaten):
    for item in bestellte_zutaten:
        ressourcen[item] -= bestellte_zutaten[item]
    print(f"Hier ist dein {getränk_name} ☕️. Genieße ihn!")

ist_an = True

while ist_an:
    wahl = input("Was möchtest du? (espresso/latte/cappuccino): ")
    if wahl == "aus":
        ist_an = False
    elif wahl == "bericht":
        print(f"Wasser: {ressourcen['wasser']}ml")
        print(f"Milch: {ressourcen['milch']}ml")
        print(f"Kaffee: {ressourcen['kaffee']}g")
        print(f"Geld: ${gewinn}")
    else:
        getränk = MENUE.get(wahl)
        if getränk:
            if sind_ressourcen_ausreichend(getränk["zutaten"]):
                bezahlung = münzen_verarbeiten()
                if ist_transaktion_erfolgreich(bezahlung, getränk["kosten"]):
                    kaffee_zubereiten(wahl, getränk["zutaten"])
        else:
            print("Ungültige Auswahl. Bitte wählen Sie espresso, latte oder cappuccino.")