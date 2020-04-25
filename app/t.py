from decision import dec, layout
from decision_v2 import zero_area
data = {"game": {"id": "3a82b971-aea2-4378-a6af-23941a89199a"}, "turn": 46, "board": {"height": 11, "width": 11, "snakes": [{"shout": "get in my belly!", "id": "gs_hDvXjmjXqp4wJw3mhrV9j8yd", "health": 90, "name": "dokuhebi_rida", "body": [{"x": 2, "y": 8}, {"x": 2, "y": 7}, {"x": 2, "y": 6}, {"x": 3, "y": 6}, {"x": 4, "y": 6}, {"x": 5, "y": 6}, {"x": 5, "y": 7}, {"x": 5, "y": 8}, {"x": 5, "y": 9}]}, {"shout": "", "id": "gs_BxyfjPcjSBM49YhXW8bxvRJ4", "health": 95, "name": "drasnakegon", "body": [{"x": 1, "y": 5}, {"x": 2, "y": 5}, {"x": 2, "y": 4}, {"x": 2, "y": 3}, {"x": 2, "y": 2}, {"x": 2, "y": 1}]}], "food": [{"x": 9, "y": 0}, {"x": 2, "y": 10}]}, "you": {"shout": "", "id": "gs_BxyfjPcjSBM49YhXW8bxvRJ4", "health": 95, "name": "drasnakegon", "body": [{"x": 1, "y": 5}, {"x": 2, "y": 5}, {"x": 2, "y": 4}, {"x": 2, "y": 3}, {"x": 2, "y": 2}, {"x": 2, "y": 1}]}}
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

arena = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 
    [1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1], 
    [1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1], 
    [1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1], 
    [1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1], 
    [1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1], 
    [1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1], 
    [1, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1], 
    [1, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1], 
    [1, 0, -9, 9, -9, 0, 1, 0, 0, 0, 0, 0, 1], 
    [1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1], 
    [1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1], 
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    ]
print(zero_area(11,1,arena))