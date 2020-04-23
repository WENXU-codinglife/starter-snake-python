from decision import dec, layout
data = {"game": {"id": "0041d2f3-c77b-4600-9e02-40af88e8229e"}, "turn": 98, "board": {"height": 11, "width": 11, "snakes": [{"body": [{"x": 3, "y": 7}, {"x": 4, "y": 7}, {"x": 5, "y": 7}, {"x": 6, "y": 7}, {"x": 7, "y": 7}, {"x": 7, "y": 6}], "id": "gs_G3h9rbg8gJcVRKtPjywQxCtS", "health": 83, "shout": "", "name": "TSnek"}, {"body": [{"x": 0, "y": 0}, {"x": 0, "y": 1}, {"x": 0, "y": 2}, {"x": 1, "y": 2}, {"x": 2, "y": 2}, {"x": 3, "y": 2}, {"x": 4, "y": 2}, {"x": 5, "y": 2}], "id": "gs_dDHkJx3DFSVvbCJSKcGxqTXC", "health": 92, "shout": "", "name": "drasnakegon"}], "food": [{"x": 2, "y": 5}, {"x": 8, "y": 4}, {"x": 3, "y": 8}, {"x": 1, "y": 10}, {"x": 9, "y": 7}, {"x": 3, "y": 4}]}, "you": {"body": [{"x": 0, "y": 0}, {"x": 0, "y": 1}, {"x": 0, "y": 2}, {"x": 1, "y": 2}, {"x": 2, "y": 2}, {"x": 3, "y": 2}, {"x": 4, "y": 2}, {"x": 5, "y": 2}], "id": "gs_dDHkJx3DFSVvbCJSKcGxqTXC", "health": 92, "shout": "", "name": "drasnakegon"}}
"""
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
"""
print(dec(data))

print(layout(11,11,data))
