import sys
import os
sys.path.append('../joker-project/robots')

import manager as mg


if __name__ == "__main__":
    print('\n === Hey there, lets start data hacking shall we =] ===\n')
    print('Select the robot you want to use: \n')
    print('1- listener\n')
    print('2- preprocessor\n')
    print('3- analyser\n')
    print('4- posprocessor\n')
    print('9- exit\n')

    option = int(input())

    if option == 1:
        try:
            mg.start_to_listen()
        except KeyboardInterrupt:
            print(' Byebye!')


    elif option == 2:
        mg.start_to_preprocess()

    elif option == 3:
        mg.start_to_analyse()

    elif option == 4:
        mg.start_to_posprocess()

    elif option == 9:
        os._exit



