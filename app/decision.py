

def dec(data):
    height = data['board']['height']
    width = data['board']['width']
    arena = layout(height,width,data)
    first = data['you']['body'][0]
    second = data['you']['body'][1]
    direction = 'up'
    if first['x'] == second['x']:
    	if first['y'] > second['y']:
    		# downward
    		if arena['snakes'][first['x']+1][first['y']+2] == 0:
    			direction = 'down'
    		elif arena['snakes'][first['x']][first['y']+1] == 0:
    			direction = 'left'
    		elif arena['snakes'][first['x']+2][first['y']+1] == 0:
    			direction = 'right'
    	else:
    		#upward
    		if arena['snakes'][first['x']+1][first['y']] == 0:
    			direction = 'up'
    		elif arena['snakes'][first['x']][first['y']+1] == 0:
    			direction = 'left'
    		elif arena['snakes'][first['x']+2][first['y']+1] == 0:
    			direction = 'right' 		
    elif first['y'] == second['y']:
    	if first['x'] > second['x']:
    		#rightward
    		if arena['snakes'][first['x']+2][first['y']+1] == 0:
    			direction = 'right'
    		elif arena['snakes'][first['x']+1][first['y']] == 0:
    			direction = 'up'
    		elif arena['snakes'][first['x']+1][first['y']+2] == 0:
    			direction = 'down'		
    	else:
    		#leftward
    		if arena['snakes'][first['x']][first['y']+1] == 0:
    			direction = 'left'
    		elif arena['snakes'][first['x']+1][first['y']] == 0:
    			direction = 'up'
    		elif arena['snakes'][first['x']+1][first['y']+2] == 0:
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
	print(snakes)
	food = []
	row = 0
	while(row < height+2):
		column = 0
		while(column < width+2):
			if(row == 0 or row == height+1 or column == 0 or column == width+1):
				snakes[row][column] = 1
				print(snakes)
				print(str(row)+','+str(column))
			column = column + 1
		row = row + 1


	for piece in data['board']['food']:
		food[piece['x']+1][piece['y']+1] = 1

	for component in data['you']['body']:
		snakes[component['x']+1][component['y']+1] = 1

	for players in data['board']['snakes']:
		print(players)
		for component in players['body']:
			snakes[component['x']+1][component['y']+1] = 1
	ret = {"snakes":snakes, "food":food}
	return ret








