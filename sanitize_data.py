import json
import logging, sys

logger = logging.getLogger("{}.{}".format(
    __name__,
    sys._getframe().f_code.co_name)
)

TOP_LEVEL_DROPS = [
    'auth', 'achievements', 'backer', 'contributor', 'purchased', 'flags', 'items', 'invitations', #'tutorial','emailNotifications',
    'party', 'preferences', 'profile', 'stats', 'inbox', 'guilds', 'loginIncentives', 'invitesSent',
    'pinnedItemsOrder', '_id', 'apiToken', 'lastCron', 'newMessages', 'notifications',
    '_v', 'balance', 'challenges', 'tags', 'extra', 'pushDevices', 'webhooks', 'pinnedItems', 'unpinnedItems',
    '_ABTests', 'migration', 'id','tasksOrder'
    # 'history', 'tasks'
]

def get_cleaned_json(filepath):
    with open(filepath) as json_file:
        data = json.load(json_file)

    for key in TOP_LEVEL_DROPS:
        # try:
            del data[key]
            # print(".", end="")
        # except KeyError:
            # print("'", end="")
    # print("")
    del data['tasks']['rewards']
    
    # del data['history']
    for task_type in ['habits', 'dailys', 'todos']:
        for task_n, task_json in enumerate(data['tasks'][task_type]):
            logger.debug(f'del {task_type} {task_n} userId') 
            del data['tasks'][task_type][task_n]['userId']    
    
    return data