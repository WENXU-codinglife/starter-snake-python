

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
    if first['x'] == second['x']:
        if first['y'] > second['y']:
            # downward
            if arena['snakes'][first['y']+2][first['x']+1] == 0:
                direction = 'down'
            elif arena['snakes'][first['y']+1][first['x']] == 0:
                direction = 'left'
            elif arena['snakes'][first['y']+1][first['x']+2] == 0:
                direction = 'right'
        else:
            #upward
            if arena['snakes'][first['y']][first['x']+1] == 0:
                direction = 'up'
            elif arena['snakes'][first['y']+1][first['x']] == 0:
                direction = 'left'
            elif arena['snakes'][first['y']+1][first['x']+2] == 0:
                direction = 'right' 		
    elif first['y'] == second['y']:
        if first['x'] > second['x']:
            #rightward
            if arena['snakes'][first['y']+1][first['x']+2] == 0:
                direction = 'right'
            elif arena['snakes'][first['y']][first['x']+1] == 0:
                direction = 'up'
            elif arena['snakes'][first['y']+2][first['x']+1] == 0:
                direction = 'down'		
        else:
            #leftward
            if arena['snakes'][first['y']+1][first['x']] == 0:
                direction = 'left'
            elif arena['snakes'][first['y']][first['x']+1] == 0:
                direction = 'up'
            elif arena['snakes'][first['y']+2][first['x']+1] == 0:
                direction = 'down'	
    return direction



def  layout(height,width,data):
    row = 0
    column = 0
    snakes = []
    while(row < height+2):
        snakes.append([])
        column = 0
        while(column < width+2):
            snakes[row].append(0)
            column+=1
        row+=1
    food = []
    row = 0
    while(row < height+2):
        column = 0
        while(column < width+2):
            if(row == 0 or row == height+1 or column == 0 or column == width+1):
                snakes[column][row] = 1
            column = column + 1
        row = row + 1


    #for piece in data['board']['food']:
        #food[piece['x']+1][piece['y']+1] = 1

    for component in data['you']['body']:
        snakes[component['y']+1][component['x']+1] = 1

    for players in data['board']['snakes']:
        print(players)
        snakes[players['body'][0]['y']+1][players['body'][0]['x']] = 1
        snakes[players['body'][0]['y']][players['body'][0]['x']+1] = 1
        snakes[players['body'][0]['y']+1][players['body'][0]['x']+2] = 1
        snakes[players['body'][0]['y']+2][players['body'][0]['x']+1] = 1
        for component in players['body']:
            snakes[component['y']+1][component['x']+1] = 1
    ret = {"snakes":snakes, "food":food}
    return ret








