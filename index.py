import sys
sys.path.append('../joker-project/robots')

import manager as mg

print('\n === Hey there, be welcome! ===\n')
print('Choose the function please\n')
print('1- listen\n')
print('2- preprocessar\n')
print('9- exit\n')

option = input()
if option == '1':
    try:
        mg.start_to_listen()
    except KeyboardInterrupt:
        print(' Byebye!')
elif option == '2':
    pass




# mg.start_to_search()


