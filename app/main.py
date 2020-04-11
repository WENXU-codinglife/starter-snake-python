import json
import os
import random
import bottle

from api import ping_response, start_response, move_response, end_response


@bottle.route('/')
def index():
    return '''
    Battlesnake documentation can be found at
       <a href="https://docs.battlesnake.com">https://docs.battlesnake.com</a>.
    '''


@bottle.route('/static/<path:path>')
def static(path):
    """
    Given a path, return the static file located relative
    to the static folder.

    This can be used to return the snake head URL in an API response.
    """
    return bottle.static_file(path, root='static/')


@bottle.post('/ping')
def ping():
    """
    A keep-alive endpoint used to prevent cloud application platforms,
    such as Heroku, from sleeping the application instance.
    """
    return ping_response()


@bottle.post('/start')
def start():
    data = bottle.request.json

    """
    TODO: If you intend to have a stateful snake AI,
            initialize your snake state here using the
            request's data if necessary.
    """
    print(json.dumps(data))

    color = "#00fcef",
    headType = "smile",
    tailType = "freckled"

    return {'color':color,'headType':headType,'tailType':tailType}


@bottle.post('/move')
def move():
    data = bottle.request.json

    """
    TODO: Using the data from the endpoint request object, your
            snake AI must choose a direction to move in.
    """
    print(json.dumps(data))
    height = data['board']['height']
    width = data['board']['width']
    print(height)
    print(width)
    #directions = ['up', 'down', 'left', 'right']
    #direction = random.choice(directions)
    direction = 'up'
    first = data['you']['body'][0]
    second = data['you']['body'][1]
    print(first)
    print(second)
    if first['x'] == second['x']:
    	if first['y'] > second['y']:
    		# downward
    		direction = 'down'
    		if first['y'] == height - 1:
    			direction = 'right'
    			if first['x'] == width - 1:
    				direction = 'left'
    	else:
    		#upward
    		direction = 'up'
    		if first['y'] == 0:
    			direction = 'left'
    			if first['x'] == 0:
    				direction = 'right'    		
    elif first['y'] == second['y']:
    	if first['x'] > second['x']:
    		#rightward
    		direction = 'right'
    		if first['x'] == width - 1:
    			direction = 'up'
    			if first['y'] == 0:
    				direction = 'down'    		
    	else:
    		#leftward
    		direction = 'left'
    		if first['x'] == 0:
    			direction = 'down'
    			if first['y'] == height - 1:
    				direction = 'up'  
    return move_response(direction)


@bottle.post('/end')
def end():
    data = bottle.request.json

    """
    TODO: If your snake AI was stateful,
        clean up any stateful objects here.
    """
    print(json.dumps(data))

    return end_response()


# Expose WSGI app (so gunicorn can find it)
application = bottle.default_app()

if __name__ == '__main__':
    bottle.run(
        application,
        host=os.getenv('IP', '0.0.0.0'),
        port=os.getenv('PORT', '8080'),
        debug=os.getenv('DEBUG', True)
    )
