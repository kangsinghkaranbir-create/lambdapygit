class Tamagotchi:
    def __init__(self, nome):
        self.nome = nome
        self.fame = 50
        self.felicita = 50
        self.stanchezza = 50

    def nutri(self):
        self.fame = max(0, self.fame - 10)
        self.stanchezza = min(100, self.stanchezza + 5)

    def gioca(self):
        self.felicita = min(100, self.felicita + 10)
        self.stanchezza = min(100, self.stanchezza + 10)

    def dormi(self):
        self.stanchezza = max(0, self.stanchezza - 20)
        self.felicita = max(0, self.felicita - 5)
        self.fame = min(100, self.fame + 10)

    def mostra_stato(self):
        print("\n--- STATO DEL TAMAGOTCHI ---")
        print("Nome:", self.nome)
        print("Fame:", self.fame)
        print("Felicità:", self.felicita)
        print("Stanchezza:", self.stanchezza)


def menu(tama):
    while True:
        tama.mostra_stato()

        print("\nScegli un'azione:")
        print("1 - Nutri")
        print("2 - Gioca")
        print("3 - Dormi")
        print("0 - Esci")

        scelta = input("Scelta: ")

        if scelta == "1":
            tama.nutri()
        elif scelta == "2":
            tama.gioca()
        elif scelta == "3":
            tama.dormi()
        elif scelta == "0":
            print("Gioco terminato")
            break
        else:
            print("Scelta non valida")


nome = input("Inserisci il nome del Tamagotchi: ")
t = Tamagotchi(nome)
menu(t)
