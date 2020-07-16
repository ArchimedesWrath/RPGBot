from random import random

action = [0, 1]
creatures = ['The Wise old Man', 'A fairy', 'A witch', 'A druid', 'An ent']
placesItems = ['a fork in the road', 'an enchanted medow', 'an unmarked grave', 'a rundown shack']
placesExp = ['a fairy ring', 'a sacred ritual site', 'a burial ground', 'a magical field', 'an ominous relic']
item = ['an apple', 'a potion', 'a key', 'a bone']

eventStat = { 'type':'stat', 'message':None, 'action':None, 'ammount':None, 'stat':None }

eventItem = { 'type':'item', 'message':None, 'item':None }

randomEvent = {
        'easy': {
            'item': {
                'item1' : 'You happen upon a <<place>> and find <<gift>>!\n<<gift>> has been added to your inventory!',
                'item2' : 'A <<creature>> appears and gives you <<gift>>!\n<<gift>> has been added to your inventory!'
            },
            'stat': {
                'stat1' : 'You happen upon a <<place>> and <<action>> <<ammount>> <<stat>>!\nYour <<stat>> is now <<ammount>>.',
                'stat2' : 'A <<creature>> appears and <<actionCreature>> your <<stat>>!\nYour <<stat>> is now <<ammount>>.'
            }
        }, 
        # 'medium': {
        #     'pure': {
        #         'pure1' : 'You spot a relic in the road, what will you do?',
        #         'pure2' : 'You happen upon a mystical pond, what will you do?'
        #     },
        #     'skill': {
        #         'skill1' : 'You come across a locked chest, what will you do?',
        #         'skill2' : 'You meet a weary traveler, what will you do?'
        #     }
        # }, 
        # 'hard': {
        #     'monster': {
        #         'monster1' : 'A slime has appeared!',
        #         'monster2' : 'A rat has appeared!'
        #     },
        #     'human': {
        #         'human1' : 'A robber has appeared!',
        #         'human2' : 'A knight has appeared!'
        #     }
        # }
    }

def randomRoll(min: int, max: int):
    return round(min + (random() * (max - min)))

def getRandomDictKey(dict):
    return list(dict.keys())[randomRoll(0, len(dict.keys()) - 1)]

def getRandomEvent():
    randomType = randomEvent[getRandomDictKey(randomEvent)]
    randomSubType = randomType[getRandomDictKey(randomType)]
    return {'subtype' : getRandomDictKey(randomType), 'message' :  randomSubType[getRandomDictKey(randomSubType)]}

def generateEventData(event):
    if event['subtype'] == item:
        eventData = eventItem
        eventData['item'] = item[randomRoll(0, len(item) - 1)]
        eventData['message'] = event['message']
        
        return {  }
    else:



# -------------------- EASY EVENTS ----------------------------------------------------------

# Item random events, give you an item
"""
<< You happen upon a <<place / relic>> and recieve <<gift>> ! >>
<< A <<creature / person>> appears and gives you <<gift>> ! >>
<< <<gift>> X <<ammount>> has been added to your inventory! >>

EXAMPLE:
You happen upon a merchant and recieve an apple!
An apple has been added to your inventory!

A fairy appears and gives you an apple!
An apple has been added to your inventory!
"""

# Heal random event, gives you health / experience / stats
"""
<< You happen upon a <<place / relic>> and <<recieve / lose>> <<ammount>> <<gift>> ! >>
<< A <<creature / person>> appears and <<grants / removes>> your <<gift>> ! >>
<< You have <<been given / lost>> <<ammount>> <<gift>> ! >>

EXAMPLE:
You happen upon a shrine and recieve 5 health!
You have been given 5 health!

You happen upon a robber and lose 4 health!
You have lost 4 health!

You happen upon a witch doctor and lose 1 strength!
You have lost 1 strength!
"""

#-------------------MEDIUM EVENTS-----------------------------------------------------------

# Pure random events. Don't require any skills
"""
You come across a pool
What will you do?
1. Drink from pool
2. Wade into pool
3. Leave
"""

# Skill based random events. Require a specific skill for completion.
"""
<< You come across a <<place / relic>> >>
What will you do?
[options...]
<<You decide to <<option>>, you are <<reward / penalty>> <<gift>> <<gift type>> ! >>

EXAMPLE:
You come across a locked chest
What will you do?
1. Pick the lock (speed)
2. Break the lock (strength)
3. Use key (item)
4. Leave

You decide to break the lock, you fail and lose 3 health!
"""


#---------------------HARDEST EVENTS-------------------------------------------------------------

"""
A Monster has appeared
What will you do?
1. Attack
2. Run
3. Use item (optional)
    a. Heal
    b. Use a special item
"""