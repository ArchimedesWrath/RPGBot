stats = { 
    'ID': 1, 
    'level' : 1, 
    'exp': 0, 
    'expNext': 10, 
    'health': 10, 
    'maxHealth': 10, 
    'attack': 1, 
    'defense': 1, 
    'wisdom': 1, 
    'speed': 1,
    'inventory': {
        'apple': 2,
        'key': 1,
    } 
    }

def levelUp(stats):
    newStats = stats
    newStats['level'] += 1
    newStats['expNext'] = round(newStats['expNext'] * 1.2 + 10)
    return newStats

def addLevel(stats, ctx):
    newStats = stats
    increase = newStats['expNext'] - newStats['exp']
    newStats = addExp(newStats, increase)
    return newStats

def addExp(stats, increase):
    newStats = stats
    totalExp = newStats['exp'] + increase
    if totalExp >= newStats['expNext']:
        increase = totalExp - newStats['expNext']
        newStats['exp'] = newStats['expNext']
        # Call level up
        newStats = levelUp(newStats)
        return addExp(newStats, increase)
    else:
        newStats['exp'] += increase
        return newStats

def addHealth(stats, increase):
    newStats = stats
    newStats['health'] += increase
    return newStats

def damage(stats, decrease):
    newStats = stats
    newStats['health'] -= decrease
    return newStats

def addAttack(stats, increase):
    newStats = stats
    newStats['attack'] += increase
    return newStats

def addDefense(stats, increase):
    newStats = stats
    newStats['defense'] += increase
    return newStats

def addWisdom(stats, increase):
    newStats = stats
    newStats['wisdom'] += increase
    return newStats

def addSpeed(stats, increase):
    newStats = stats
    newStats['speed'] += increase
    return newStats