import blenderbot
import facts
import face_capture as fc
import object
import similarity
import story_bot
import tweetr
import google_search as gs
import warnings
import os 
import threading
import movie_recommendation as mr

import logging
logging.getLogger("Python").setLevel(logging.CRITICAL)
logging.getLogger("Coding").setLevel(logging.CRITICAL)

os.system('cls')
warnings.filterwarnings('ignore')

def mytimer():
    pass 


if __name__ == '__main__':
    query = ''
    response = ''
    positive = [3, 4, 6]
    negative = [0, 1, 2, 5]
    a = 1
    while query != 'quit':
        query = input('query: ')
        if query == 'quit':
            print('chitti: good bye, have a great day')
            break
        mood = fc.bot()
        if mood in positive:
            a = 1
        if mood in negative:
            a = 0
        obj = object.bot(query)
        c = similarity.classify(query)
        if c == 0:
            response = facts.bot(query)
        elif c == 1:
            response = tweetr.bot(query)
        elif c == 2:
            response = story_bot.bot()
        elif c == 3:
            pass
        elif c == 4:
            response = mr.bot(mood)
        elif c == 5:
            response = gs.bot(query)
        else:
            response = blenderbot.bot(query)

        print('Chitti: ', response)
        print()

