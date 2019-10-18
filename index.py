import sys
sys.path.append('../joker-project/robots')

import manager as mg

##to start the listener, use this
# try:
#     mg.start_to_listen()
# except KeyboardInterrupt:
#     print(' Byebye!')


# to start preprocessing, use this
try:
    mg.start_to_preprocess()
except:
    pass



# mg.start_to_search()


