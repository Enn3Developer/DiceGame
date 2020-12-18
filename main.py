from math import floor
from random import randint

class Player:
    def __init__(self, name: str, is_player: bool):
        self.name = name
        self.is_player = is_player
        self.winning = 0.0
    
    def add_win(self, amount: float):
        self.winning += amount
    
    def sub_win(self, amount: float):
        self.add_win(-amount)

def get_amount() -> float:
    while True:
        try:
            return float(input("Inserisci la tua posta: €"))
        except ValueError:
            pass

def get_amount_cpu(cpu: Player) -> float:
    if cpu.winning > 0:
        return randint(1, floor(cpu.winning/2))
    elif cpu.winning == 0:
        return 10
    else:
        return randint(1, abs(floor(cpu.winning/2)))

def get_name() -> str:
    return input("Inserisci il tuo nome: ")

def get_dice() -> (int, int):
    return randint(1, 6), randint(1, 6)

def get_num() -> int:
    while True:
        try:
            num = int(input("Inserisci un numero fra 1 e 12: "))
            if num == max(1, min(num, 12)):
                return num
        except ValueError:
            pass

def end_play(players: [Player]):
    print(f"{'Nomi':15} {'Vincite totali':20}")
    for i in range(len(players)):
        print(f"{players[i].name:15} {f'€{players[i].winning:.2f}':20}")

def play(players: [Player]):
    for _ in range(5):
        for i in range(len(players)):
            amount = 0.0
            num = 0
            dice = get_dice()

            if players[i].is_player:
                amount = get_amount()
                num = get_num()
            else:
                amount = get_amount_cpu(players[i])
                num = randint(2, 12)

            if num == (dice[0] + dice[1]):
                players[i].add_win(amount*2)
                if players[i].is_player:
                    print(f"Hai vinto: €{amount*2}")
            else:
                players[i].sub_win(amount)
                if players[i].is_player:
                    print(f"Hai perso: €{amount}")
    
    end_play(players)

def players():
    players = []
    for _ in range(3):
        players.append(Player(get_name(), True))
    play(players)

def computer():
    players = []
    players.append(Player(get_name(), True))
    players.append(Player("Computer", False))
    play(players)

def main():
    isValid = False
    u_c = ""
    while not isValid:
        u_c = input("Scrivi 'u' se vuoi giocare con altre due persone o 'c' se vuoi giocare contro il computer: ")
        isValid = True if u_c == 'u' or u_c == 'c' else False
    if u_c == 'u':
        players()
    else:
        computer()


if __name__ == "__main__":
    print("Puoi giocare da solo contro il computer o contro altri due giocatori")
    print("Si gioca in 5 lanci, alla fine dei 5 lanci verranno mostrati le vincite di tutti")
    print("Buona fortuna!\n")
    main()