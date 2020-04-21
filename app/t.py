from decision import dec, layout

data = {
    "turn": 5, 
    "game": {"id": "34e3647b-5798-4df4-a376-a53f78306e44"}, 
    "board": {
        "width": 11, 
        "snakes": [
            {"id": "gs_pM7yYCK8KKbrPjVVkSdbkXqC", 
            "name": "johnwilkes-0.7", 
            "body": [
                {"x": 1, "y": 0}, 
                {"x": 1, "y": 1}, 
                {"x": 1, "y": 2}
                ], 
            "shout": "", 
            "health": 95
            }, 
            {"id": "gs_TFx4JR3wcPXDTjKpDGQH9YGS", 
            "name": "drasnakegon", 
            "body": [
                {"x": 5, "y": 4}, 
                {"x": 5, "y": 5}, 
                {"x": 5, "y": 6}
                ], 
            "shout": "", 
            "health": 95
            }
        ], 
        "height": 11, 
        "food": [{"x": 8, "y": 10}, {"x": 7, "y": 8}, {"x": 2, "y": 3}]
    }, 
    "you": {
        "id": "gs_TFx4JR3wcPXDTjKpDGQH9YGS", 
        "name": "drasnakegon", 
        "body": [
            {"x": 5, "y": 4}, 
            {"x": 5, "y": 5}, 
            {"x": 5, "y": 6}], 
        "shout": "", 
        "health": 95
        }
    }


print(dec(data))

print(layout(11,11,data))


