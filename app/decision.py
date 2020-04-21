

def dec(data):
    height = data['board']['height']
    width = data['board']['width']
    num = len(data['board']['snakes'])-1
    while(num>=0):
        if data['board']['snakes'][num]["name"] == "drasnakegon":
            del data['board']['snakes'][num]
            break
        num-=1
    arena = layout(height,width,data)
    first = data['you']['body'][0]
    second = data['you']['body'][1]
    direction = 'up'
    #vertical
    if first['x'] == second['x']:
        if first['y'] > second['y']:
            # downward
            """
            if the surrounding entris are '0', follow the previous direction
            priority: low
            """
            if arena['snakes'][first['y']+2][first['x']+1] == 0:
                direction = 'down'
            elif arena['snakes'][first['y']+1][first['x']] == 0:
                direction = 'left'
            elif arena['snakes'][first['y']+1][first['x']+2] == 0:
                direction = 'right'
                
            """
            if other snake's head (whose body is shorter them mine) is adjacent to my head, go after it and try to crash
            priority: medium
            """
            """
            if arena['snakes'][first['y']+2][first['x']+1] > 1 and arena['snakes'][first['y']+2][first['x']+1] < len(data['you']['body']):
                direction = 'down'
            elif arena['snakes'][first['y']+1][first['x']] > 1 and arena['snakes'][first['y']+1][first['x']] < len(data['you']['body']):
                direction = 'left'
            elif arena['snakes'][first['y']+1][first['x']+2] > 1 and arena['snakes'][first['y']+1][first['x']+2] < len(data['you']['body']):
                direction = 'right'
            """
            """
            if a food exists in the adjacent entris, go to eat it
            priority: high
            """
            if arena['food'][first['y']+2][first['x']+1] == -1:
                direction = 'down'
            elif arena['food'][first['y']+1][first['x']] == -1:
                direction = 'left'
            elif arena['food'][first['y']+1][first['x']+2] == -1:
                direction = 'right'
        else:
            #upward
            if arena['snakes'][first['y']][first['x']+1] == 0:
                direction = 'up'
            elif arena['snakes'][first['y']+1][first['x']] == 0:
                direction = 'left'
            elif arena['snakes'][first['y']+1][first['x']+2] == 0:
                direction = 'right'


            if arena['food'][first['y']][first['x']+1] == -1:
                direction = 'down'
            elif arena['food'][first['y']+1][first['x']] == -1:
                direction = 'left'
            elif arena['food'][first['y']+1][first['x']+2] == -1:
                direction = 'right'
    #horizontal             		
    elif first['y'] == second['y']:
        if first['x'] > second['x']:
            #rightward
            if arena['snakes'][first['y']+1][first['x']+2] == 0:
                direction = 'right'
            elif arena['snakes'][first['y']][first['x']+1] == 0:
                direction = 'up'
            elif arena['snakes'][first['y']+2][first['x']+1] == 0:
                direction = 'down'	

            if arena['food'][first['y']+1][first['x']+2] == -1:
                direction = 'right'
            elif arena['food'][first['y']][first['x']+1] == -1:
                direction = 'up'
            elif arena['food'][first['y']+2][first['x']+1] == -1:
                direction = 'down'	
        else:
            #leftward
            if arena['snakes'][first['y']+1][first['x']] == 0:
                direction = 'left'
            elif arena['snakes'][first['y']][first['x']+1] == 0:
                direction = 'up'
            elif arena['snakes'][first['y']+2][first['x']+1] == 0:
                direction = 'down'	

            if arena['food'][first['y']+1][first['x']] == -1:
                direction = 'left'
            elif arena['food'][first['y']][first['x']+1] == -1:
                direction = 'up'
            elif arena['food'][first['y']+2][first['x']+1] == -1:
                direction = 'down'	
    return direction



def  layout(height,width,data):
    row = 0
    column = 0
    snakes = []
    food = []
    """
    create a 2D list that stores the information on the snakes' position and food's position
    Now initialize the list: the outermost entries are '1' indicating walls, otherwise '0'
    """
    while(row < height+2):
        snakes.append([])
        food.append([])
        column = 0
        while(column < width+2):
            snakes[row].append(0)
            food[row].append(0)
            column+=1
        row+=1
    
    row = 0
    while(row < height+2):
        column = 0
        while(column < width+2):
            if(row == 0 or row == height+1 or column == 0 or column == width+1):
                snakes[column][row] = 1
                food[column][row] = 1
            column = column + 1
        row = row + 1
#"""
#locate the foods with '-1'
#"""
    for piece in data['board']['food']:
        food[piece['y']+1][piece['x']+1] = -1

#"""
#locate my snake's body
#"""
    for component in data['you']['body']:
        snakes[component['y']+1][component['x']+1] = 1
#"""
#locate other snakes' bodies
#the head entris reflect the lengths and other body entries hold '1'
#and the adjacent entries of heads hold -1*lengths
#"""
    for players in data['board']['snakes']:
        #print(players)
        if snakes[players['body'][0]['y']+1][players['body'][0]['x']] == 0:
            snakes[players['body'][0]['y']+1][players['body'][0]['x']] = -1 * len(players['body'])
        if snakes[players['body'][0]['y']][players['body'][0]['x']+1] == 0:
            snakes[players['body'][0]['y']][players['body'][0]['x']+1] = -1 * len(players['body'])
        if snakes[players['body'][0]['y']+1][players['body'][0]['x']+2] == 0:
            snakes[players['body'][0]['y']+1][players['body'][0]['x']+2] = -1 * len(players['body'])
        if snakes[players['body'][0]['y']+2][players['body'][0]['x']+1] == 0:
            snakes[players['body'][0]['y']+2][players['body'][0]['x']+1] = -1 * len(players['body'])
        snakes[players['body'][0]['y']+1][players['body'][0]['x']+1] = len(players['body'])
        i = 1
        while(i<len(players['body'])):
            snakes[players['body'][i]['y']+1][players['body'][i]['x']+1] = 1
            i+=1

    ret = {"snakes":snakes, "food":food}
    return ret








