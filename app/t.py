from decision import dec, layout
data = {"you": {"name": "drasnakegon", "body": [{"y": 9, "x": 10}, {"y": 9, "x": 9}, {"y": 9, "x": 8}, {"y": 9, "x": 7}, {"y": 9, "x": 6}, {"y": 9, "x": 5}, {"y": 9, "x": 4}, {"y": 9, "x": 3}, {"y": 9, "x": 2}], "health": 85, "id": "gs_HmKJCBYC9ywFDmb3bR9SYvKT", "shout": ""}, "board": {"food": [{"y": 0, "x": 0}, {"y": 1, "x": 0}], "snakes": [{"name": "drasnakegon", "body": [{"y": 9, "x": 10}, {"y": 9, "x": 9}, {"y": 9, "x": 8}, {"y": 9, "x": 7}, {"y": 9, "x": 6}, {"y": 9, "x": 5}, {"y": 9, "x": 4}, {"y": 9, "x": 3}, {"y": 9, "x": 2}], "health": 85, "id": "gs_HmKJCBYC9ywFDmb3bR9SYvKT", "shout": ""}, {"name": "BattleSnek", "body": [{"y": 1, "x": 4}, {"y": 1, "x": 5}, {"y": 1, "x": 6}, {"y": 2, "x": 6}, {"y": 3, "x": 6}, {"y": 4, "x": 6}, {"y": 5, "x": 6}, {"y": 6, "x": 6}, {"y": 7, "x": 6}, {"y": 8, "x": 6}, {"y": 8, "x": 5}, {"y": 8, "x": 4}, {"y": 8, "x": 3}, {"y": 8, "x": 2}, {"y": 8, "x": 1}, {"y": 9, "x": 1}, {"y": 10, "x": 1}, {"y": 10, "x": 0}, {"y": 9, "x": 0}], "health": 91, "id": "gs_jqS8rvVhF6hJ4Grx3hPQDkg3", "shout": ""}], "width": 11, "height": 11}, "turn": 111, "game": {"id": "105892fb-836c-4ef0-8512-3b06da6376f8"}}
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

