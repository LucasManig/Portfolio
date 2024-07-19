import random
from art import logo
import os


def cls():
    os.system('cls' if os.name=='nt' else 'clear')

def karte_ziehen():
    karten = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    karte = random.choice(karten)
    return karte


def punktzahl_berechnen(karten):
    if sum(karten) == 21 and len(karten) == 2:
        return 0

    if 11 in karten and sum(karten) > 21:
        karten.remove(11)
        karten.append(1)
    return sum(karten)


def vergleiche(spieler_punkte, computer_punkte):
    if spieler_punkte > 21 and computer_punkte > 21:
        return "Du bist über 21. Du verlierst 😤"

    if spieler_punkte == computer_punkte:
        return "Unentschieden 🙃"
    elif computer_punkte == 0:
        return "Du verlierst, der Gegner hat Blackjack 😱"
    elif spieler_punkte == 0:
        return "Du gewinnst mit einem Blackjack 😎"
    elif spieler_punkte > 21:
        return "Du bist über 21. Du verlierst 😭"
    elif computer_punkte > 21:
        return "Der Gegner ist über 21. Du gewinnst 😁"
    elif spieler_punkte > computer_punkte:
        return "Du gewinnst 😃"
    else:
        return "Du verlierst 😤"


def spiel_starten():
    print(logo)

    spieler_karten = []
    computer_karten = []
    spiel_vorbei = False

    for _ in range(2):
        spieler_karten.append(karte_ziehen())
        computer_karten.append(karte_ziehen())

    while not spiel_vorbei:
        spieler_punkte = punktzahl_berechnen(spieler_karten)
        computer_punkte = punktzahl_berechnen(computer_karten)
        print(f"   Deine Karten: {spieler_karten}, aktuelle Punktzahl: {spieler_punkte}")
        print(f"   Erste Karte des Computers: {computer_karten[0]}")

        if spieler_punkte == 0 or computer_punkte == 0 or spieler_punkte > 21:
            spiel_vorbei = True
        else:
            weitere_karte = input("Gib 'j' ein, um eine weitere Karte zu ziehen, oder 'n', um zu passen: ")
            if weitere_karte == "j":
                spieler_karten.append(karte_ziehen())
            else:
                spiel_vorbei = True

    while computer_punkte != 0 and computer_punkte < 17:
        computer_karten.append(karte_ziehen())
        computer_punkte = punktzahl_berechnen(computer_karten)

    print(f"   Deine endgültigen Karten: {spieler_karten}, endgültige Punktzahl: {spieler_punkte}")
    print(f"   Endgültige Karten des Computers: {computer_karten}, endgültige Punktzahl: {computer_punkte}")
    print(vergleiche(spieler_punkte, computer_punkte))


while input("Möchtest du eine Runde Blackjack spielen? Gib 'j' oder 'n' ein: ") == "j":
    cls()
    spiel_starten()