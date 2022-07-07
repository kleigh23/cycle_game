import constants
from game.casting.actor import Actor
from game.shared.point import Point


class Snake(Actor):
    """
    A long limbless reptile.
    
    The responsibility of Snake is to move itself.

    Attributes:
        _points (int): The number of points the food is worth.
    """
    def __init__(self):
        super().__init__()
        self._segments_green = []
        self._segments_red = []
        self._prepare_body_red()
        self._prepare_body_green()
        

    def get_segments(self):
        return self._segments_green

    def get_segments_red(self):
        return self._segments_red 
        

    def move_next(self):
        # move all segments
        for segment in self._segments_green:
            segment.move_next()

        # update velocities
        for i in range(len(self._segments_green) - 1, 0, -1):
            trailing = self._segments_green[i]
            previous = self._segments_green[i - 1]
            velocity = previous.get_velocity()
            trailing.set_velocity(velocity)


    def move_next_red(self):
        for segment in self._segments_red:
            segment.move_next_red() 

        for i in range(len(self._segments_red) - 1, 0, -1):
            trailing = self._segments_red[i]
            previous = self._segments_red[i - 1]
            velocity = previous.get_velocity()
            trailing.set_velocity(velocity)       

    def get_head(self):
        return self._segments_green[0] 
    
    def get_head_red(self):
        return self._segments_red[0]

    def grow_tail(self, number_of_segments):
        for i in range(number_of_segments):
            tail = self._segments_green[-1]
            velocity = tail.get_velocity()
            offset = velocity.reverse()
            position = tail.get_position().add(offset)
            
            segment = Actor()
            segment.set_position(position)
            segment.set_velocity(velocity)
            segment.set_text("#")
            segment.set_color(constants.GREEN)
            self._segments_green.append(segment)

    def grow_tail_red(self, number_of_segments):
        for i in range(number_of_segments):
            tail = self._segments_red[-1]
            velocity = tail.get_velocity()
            offset = velocity.reverse()
            position = tail.get_position().add(offset)
            
            segment = Actor()
            segment.set_position(position)
            segment.set_velocity(velocity)
            segment.set_text("#")
            segment.set_color(constants.RED)
            self._segments_red.append(segment)

    def turn_head(self, velocity):
        self._segments_green[0].set_velocity(velocity)
        

    def turn_head_red(self, velocity):
        self._segments_red[0].set_velocity(velocity)
    
    def _prepare_body_green(self):
        x = int(constants.MAX_X / 2)
        y = int(constants.MAX_Y - 300)

        for i in range(constants.SNAKE_LENGTH):
            position = Point(x - i * constants.CELL_SIZE, y)
            velocity = Point(1 * constants.CELL_SIZE, 0)
            text = "@" if i == 0 else "#"
            color = constants.GREEN
            
            segment = Actor()
            segment.set_position(position)
            segment.set_velocity(velocity)
            segment.set_text(text)
            segment.set_color(color)
            self._segments_green.append(segment)

    def _prepare_body_red(self):
        x = int(constants.MAX_X / 2)
        y = int(constants.MAX_Y + 300)

        for i in range(constants.SNAKE_LENGTH):
            position = Point(y - i * constants.CELL_SIZE, x)
            velocity = Point(1 * constants.CELL_SIZE, 0)
            text = "@" if i == 0 else "#"
            color = constants.RED
            
            segment = Actor()
            segment.set_position(position)
            segment.set_velocity(velocity)
            segment.set_text(text)
            segment.set_color(color)
            self._segments_red.append(segment)