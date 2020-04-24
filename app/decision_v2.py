

def dec_v2(data):
    height = data['board']['height']
    width = data['board']['width']
    num = len(data['board']['snakes'])-1
    while(num>=0):
        if data['board']['snakes'][num]["name"] == "drasnakegon" or data['board']['snakes'][num]["name"] == "Demon Hunter":
            del data['board']['snakes'][num]
            break
        num-=1
    arena = layout(height,width,data)
    first = data['you']['body'][0]
    second = data['you']['body'][1]
    direction = []
    #vertical
    if first['x'] == second['x']:
        if first['y'] > second['y']:
            # downward
            """
            if the surrounding entris are '0', follow the previous direction
            priority: low
            """
            if arena['snakes'][first['y']+2][first['x']+1] <= 0:
                direction.append('down')
            if arena['snakes'][first['y']+1][first['x']] <= 0:
                direction.append('left')
            if arena['snakes'][first['y']+1][first['x']+2] <= 0:
                direction.append('right')
                
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
            if arena['food'][first['y']+1][first['x']+2] == -1 and arena['snakes'][first['y']+1][first['x']+2] != 1 and arena['snakes'][first['y']+1][first['x']+2]*(-1)<len(data['you']['body']):
                direction.append('right')
            if arena['food'][first['y']+2][first['x']+1] == -1 and arena['snakes'][first['y']+2][first['x']+1] != 1 and arena['snakes'][first['y']+2][first['x']+1]*(-1)<len(data['you']['body']):
                direction.append('down')
            if arena['food'][first['y']+1][first['x']] == -1 and arena['snakes'][first['y']+1][first['x']] != 1 and arena['snakes'][first['y']+1][first['x']]*(-1)<len(data['you']['body']):
                direction.append('left')
            
        else:
            #upward
            if arena['snakes'][first['y']][first['x']+1] <= 0:
                direction.append('up')
            if arena['snakes'][first['y']+1][first['x']] <= 0:
                direction.append('left')
            if arena['snakes'][first['y']+1][first['x']+2] <= 0:
                direction.append('right')


            if arena['food'][first['y']][first['x']+1] == -1 and arena['snakes'][first['y']][first['x']+1] != 1 and arena['snakes'][first['y']][first['x']+1]*(-1)<len(data['you']['body']):
                direction.append('up')
            if arena['food'][first['y']+1][first['x']] == -1 and arena['snakes'][first['y']+1][first['x']] != 1 and arena['snakes'][first['y']+1][first['x']]*(-1)<len(data['you']['body']):
                direction.append('left')
            if arena['food'][first['y']+1][first['x']+2] == -1 and arena['snakes'][first['y']+1][first['x']+2] != 1 and arena['snakes'][first['y']+1][first['x']+2]*(-1)<len(data['you']['body']):
                direction.append('right')
    #horizontal             		
    elif first['y'] == second['y']:
        if first['x'] > second['x']:
            #rightward
            if arena['snakes'][first['y']+1][first['x']+2] <= 0:
                direction.append('right')
            if arena['snakes'][first['y']][first['x']+1] <= 0:
                direction.append('up')
            if arena['snakes'][first['y']+2][first['x']+1] <= 0:
                direction.append('down')	

            if arena['food'][first['y']+1][first['x']+2] == -1 and arena['snakes'][first['y']+1][first['x']+2] != 1 and arena['snakes'][first['y']+1][first['x']+2]*(-1)<len(data['you']['body']):
                direction.append('right')
            if arena['food'][first['y']][first['x']+1] == -1 and arena['snakes'][first['y']][first['x']+1] != 1 and arena['snakes'][first['y']][first['x']+1]*(-1)<len(data['you']['body']):
                direction.append('up')
            if arena['food'][first['y']+2][first['x']+1] == -1 and arena['snakes'][first['y']+2][first['x']+1] != 1 and arena['snakes'][first['y']+2][first['x']+1]*(-1)<len(data['you']['body']):
                direction.append('down')	
        else:
            #leftward
            if arena['snakes'][first['y']+1][first['x']] <= 0:
                direction.append('left')
            if arena['snakes'][first['y']+2][first['x']+1] <= 0:
                direction.append('down')
            if arena['snakes'][first['y']][first['x']+1] <= 0:
                direction.append('up')

            if arena['food'][first['y']+1][first['x']] == -1 and arena['snakes'][first['y']+1][first['x']] != 1 and arena['snakes'][first['y']+1][first['x']]*(-1)<len(data['you']['body']):
                direction.append('left')
            if arena['food'][first['y']][first['x']+1] == -1 and arena['snakes'][first['y']][first['x']+1] != 1 and arena['snakes'][first['y']][first['x']+1]*(-1)<len(data['you']['body']):
                direction.append('up')
            if arena['food'][first['y']+2][first['x']+1] == -1 and arena['snakes'][first['y']+2][first['x']+1] != 1 and arena['snakes'][first['y']+2][first['x']+1]*(-1)<len(data['you']['body']):
                direction.append('down')	
    print(direction)
    dic_dir = {'up':0,'down':0,'left':0,'right':0}
    zero_area_dir = {'up':0,'down':0,'left':0,'right':0}
    ret = 'up'
    for way in direction:
        dic_dir[way] += 1
        if dic_dir[way] == 2:
            ret = way
    if dic_dir['up'] > 0:
        zero_area_dir['up'] = zero_area(first['x'],first['y']-1,arena['snakes'])
    if dic_dir['down'] > 0:
        zero_area_dir['down'] = zero_area(first['x'],first['y']+1,arena['snakes'])
    if dic_dir['left'] > 0:
        zero_area_dir['left'] = zero_area(first['x']-1,first['y'],arena['snakes'])
    if dic_dir['right'] > 0:
        zero_area_dir['right'] = zero_area(first['x']+1,first['y'],arena['snakes'])
    if(zero_area_dir[ret] < zero_area_dir['up']):
        ret = 'up'
    if(zero_area_dir[ret] < zero_area_dir['down']):
        ret = 'down'
    if(zero_area_dir[ret] < zero_area_dir['left']):
        ret = 'left'
    if(zero_area_dir[ret] < zero_area_dir['right']):
        ret = 'right'
    print(dic_dir)
    print(zero_area_dir)
    print(ret)
    return ret



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
        if snakes[players['body'][0]['y']+1][players['body'][0]['x']] == 0 or snakes[players['body'][0]['y']+1][players['body'][0]['x']] > -1 * len(players['body']):
            snakes[players['body'][0]['y']+1][players['body'][0]['x']] = -1 * len(players['body'])
        if snakes[players['body'][0]['y']][players['body'][0]['x']+1] == 0 or snakes[players['body'][0]['y']][players['body'][0]['x']+1] > -1 * len(players['body']):
            snakes[players['body'][0]['y']][players['body'][0]['x']+1] = -1 * len(players['body'])
        if snakes[players['body'][0]['y']+1][players['body'][0]['x']+2] == 0 or snakes[players['body'][0]['y']+1][players['body'][0]['x']+2] > -1 * len(players['body']):
            snakes[players['body'][0]['y']+1][players['body'][0]['x']+2] = -1 * len(players['body'])
        if snakes[players['body'][0]['y']+2][players['body'][0]['x']+1] == 0 or snakes[players['body'][0]['y']+2][players['body'][0]['x']+1] > -1 * len(players['body']):
            snakes[players['body'][0]['y']+2][players['body'][0]['x']+1] = -1 * len(players['body'])
        snakes[players['body'][0]['y']+1][players['body'][0]['x']+1] = len(players['body'])
        if len(players['body']) >= len(data['you']['body']):
            delta_x = players['body'][0]['x'] - players['body'][1]['x']
            delta_y = players['body'][0]['y'] - players['body'][1]['y']
            snakes[players['body'][0]['y']+1+delta_y][players['body'][0]['x']+1+delta_x] = 1
        i = 1
        while(i<len(players['body'])):
            snakes[players['body'][i]['y']+1][players['body'][i]['x']+1] = 1
            i+=1

    ret = {"snakes":snakes, "food":food}
    return ret


"""
create a function with parameter (start, arena_snakes) and return the number of entries whose value is also 0 connective* to 'start'.
connectivity of a pair of entris means that there must be at least a path between this pair where all values on it are 0's
"""

def zero_area(start_x,start_y, arena_snakes):
    if(arena_snakes[start_y][start_x] > 0):
        return 0
    size = len(arena_snakes)
    arena_snakes[start_y][start_x] = 1
    ret = 1
    if((start_x > 0 and start_x < size-1 and start_y>0 and start_y<size-1) and arena_snakes[start_y+1][start_x] <= 0):
        ret = ret + arena_snakes[start_y+1][start_x]
    if((start_x > 0 and start_x < size-1 and start_y>0 and start_y<size-1) and arena_snakes[start_y-1][start_x] <= 0):
        ret = ret + arena_snakes[start_y-1][start_x]
    if((start_x > 0 and start_x < size-1 and start_y>0 and start_y<size-1) and arena_snakes[start_y][start_x+1] <= 0):
        ret = ret + arena_snakes[start_y][start_x+1]
    if((start_x > 0 and start_x < size-1 and start_y>0 and start_y<size-1) and arena_snakes[start_y][start_x-1] <= 0):
        ret = ret + arena_snakes[start_y][start_x-1]    

    return ret