

def des(data):
    height = data['board']['height']
    width = data['board']['width']
    layout = layout(height,width,data)
    first = data['you']['body'][0]
    second = data['you']['body'][1]
    direction = 'up'
    if first['x'] == second['x']:
    	if first['y'] > second['y']:
    		# downward
    		if layout['snake'][first['x']+1][first['y']+2] == 0:
    			direction = 'down'
    		elif layout['snake'][first['x']][first['y']+1] == 0:
    			direction = 'left'
    		elif layout['snake'][first['x'+2]][first['y']+1] == 0:
    			direction = 'right'
    	else:
    		#upward
    		if layout['snake'][first['x']+1][first['y']] == 0:
    			direction = 'up'
    		elif layout['snake'][first['x']][first['y']+1] == 0:
    			direction = 'left'
    		elif layout['snake'][first['x'+2]][first['y']+1] == 0:
    			direction = 'right' 		
    elif first['y'] == second['y']:
    	if first['x'] > second['x']:
    		#rightward
    		if layout['snake'][first['x']+2][first['y']+1] == 0:
    			direction = 'right'
    		elif layout['snake'][first['x']+1][first['y']] == 0:
    			direction = 'up'
    		elif layout['snake'][first['x'+1]][first['y']+2] == 0:
    			direction = 'down'		
    	else:
    		#leftward
    		if layout['snake'][first['x']][first['y']+1] == 0:
    			direction = 'left'
    		elif layout['snake'][first['x']+1][first['y']] == 0:
    			direction = 'up'
    		elif layout['snake'][first['x'+1]][first['y']+2] == 0:
    			direction = 'down'	
    return direction



def  layout(height,width,data):
	b = [0]*(width+2)
	snake = [b] * (height+2)
	food = [b] * (height+2)
	row = 0
	column = 0
	while(row < height+2):
		while(column < width+2):
			if(row == 0 or row == height+1 or column == 0 or column == width+1):
				snake[row][column] = 1
			column = column + 1
		row = row + 1


	for piece in data['board']['food']:
		food[piece['x']+1][piece['y']+1] = 1

	for component in data['you']['body']:
		snake[component['x']+1][component['y']+1] = 1

	for players in data['board']['snake']:
		for player in players:
			for component in player['body']:
				snake[component['x']+1][component['y']+1] = 1
	ret = {"snake":snake, "food":food}
	return ret








