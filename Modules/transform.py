# Class handles the storage of x and y coordinates.
class Vector2:
    def __init__(self, x: float = 0, y: float = 0):
        self.x: float = x
        self.y: float = y 

# Class handles the storage of positional, rotational and local scale values.
class Transform:
    def __init__(self, position: Vector2 = Vector2(), rotation: Vector2 = Vector2(), localScale: Vector2 = Vector2(1, 1)):
        self.position = position
        self.rotation = rotation

        # If localScale argument is 50. localScale will equal to (50, 50)
        if type(localScale) == float or type(localScale) == int:
            self.localScale = Vector2(localScale, localScale)
        else:
            self.localScale = localScale