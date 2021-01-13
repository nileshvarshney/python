""" task is to write methods that return the highest score from the list, 
the last added score and the three highest scores."""
import logging

logging.getLogger().setLevel(logging.INFO)
def high_score(list_item):
    list_item.sort(reverse=True)
    logging.info('***** {} *******'.format(list_item[0]))
    return list_item[0]

def last_score(list_item):
    logging.info('***** {} *******'.format(list_item[-1]))
    return list_item[-1]

def top_three_scores(list_item):
    list_item.sort(reverse=True)
    logging.info('top_three_scores : ***** {} *******'.format(list_item[0:3]))
    return list_item[0:3]