import time
import random
from characters import Wizard, SmallAnimal, Dragon, Creature


def print_header():
    # Yes, I added this after I recorded the video
    # but I thought you'd get a kick out if it. ;)
    print()
    print('-----------------------------------------------------------------------')
    print('''
   (  )   /\   _                 (
    \ |  (  \ ( \.(               )                      _____
  \  \ \  `  `   ) \             (  ___                 / _   \\
 (_`    \+   . x  ( .\            \/   \____-----------/ (o)   \_
- .-               \+  ;          (  O                           \____
     WIZARD BATTLE        )        \_____________  `              \  /
(__       APP      +- .( -'.- <. - _  VVVVVVV VV V\                 \/
(_____            ._._: <_ - <- _  (--  _AAAAAAA__A_/                  |
  .    /./.+-  . .- /  +--  - .     \______________//_              \_______
  (__ ' /x  / x _/ (                                  \___'          \     /
 , x / ( '  . / .  /                                      |           \   /
    /  /  _/ /    +                                      /              \/
   '  (__/                                             /                  \\
    ''')
    print()
    print('-----------------------------------------------------------------------')
    print()

def game_loop():
    creatures = [
        SmallAnimal('Toad', 1),
        Creature('Tiger', 12),
        SmallAnimal('Bat', 3),
        Dragon('Dragon', 50, 10, False),
        Wizard('Evil Wizard', 100)
    ]

    #print(creatures)

    hero = Wizard('Gandolf', 75)

    while True:

        active_creature = random.choice(creatures)
        print('A {} of Level {} has appeared from a dark and foggy forest...'
              .format(active_creature.name, active_creature.level))
        print ()
        cmd = input('Do you [a] attack, [r] runaway, or [l] look around?')
        if cmd == 'a':
            if hero.attack(active_creature):
                creatures.remove(active_creature)
            else:
                print('The Wizard runs and hides taking time to recover ...')
                time.sleep(5)
                print('The Wizard regenerates! ')
        elif cmd == 'r':
            print('The wizard {} has become unsure of his power and flees!!!'.format(hero.name))
        elif cmd == 'l':
            print('The wizard {} takes in the surrounding and sees:'.
                  format(hero.name))
            for c in creatures:
                print(' * A {} of level {}'.format(c.name, c.level))
        else:
            print("Ok, exiting game .. bye !")
            break

        if not creatures:
            print("You've defeated all the creatures, well done !")
            break

        print()


def main():
    print_header()
    game_loop()


if __name__ == '__main__':
    main()