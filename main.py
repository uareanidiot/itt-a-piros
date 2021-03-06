
from random import shuffle


def shuffle_list(my_list):
    '''
    Random miatt nem lehetséges a szabályban leírt meghatározás...
    '''
    shuffle(my_list)
    return my_list


def player_guess():
    '''
    Itt a felhasználó által megadott poharat el kell menteni egy változóként, amint lefut egyből véget ér a megadott
    utasítás.
    '''
    while True:

        try:
            guess = int(input("Hanyas pohár alatt lehet a piros? (0, 1 vagy 2) :-\n"))
            if guess > 2:
                print("Rossz számot adtál meg. 0, 1, 2-amik közül választhatsz...")
            else:
                return guess
        except:
            print("Kérlek add meg a számot")


def final_result(my_list, guess):
    '''
    Itt kezdődik az eljárás
    '''
    if my_list[guess] == 'O':
        print("Eltaláltad!\nDe nagy pali vagy")
        print(my_list)

    else:
        print("Ez most nem jött össze\nMásik alatt volt a piros.")
        print(f"A piros a(z) {my_list} -alatt volt")


if __name__ == "__main__":

    print("Kezdődik a játék")

    # Used while True to continue the cycle
    while True:
        play = input("Ha szeretnél játszani, nyomd meg az 's' betűt, viszont ha nem szeretnél, nyomd meg a 'q' betűt:-\n")
        if play == 's':
            cup_n_ball_list = [' ', 'O', ' ']

            shuff_result = shuffle_list(cup_n_ball_list)

            guess_result = player_guess()

            final_result(shuff_result, guess_result)

        # Ha itt "q" gombot nyomsz, és leütöd az entert, kilép az egész. Ezt amiatt írtam ele, mert a tanárunknak ez a mániája
        elif play == 'q':
            print("A program bezáródik...")
            break

        else:
            print("Kérlek, írj az utasításnak megfelelően")