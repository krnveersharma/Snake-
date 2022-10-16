from turtle import Turtle

# NOTE: writing CONSTANTS as variables is good, because then you do not have to dig through the code to change them
STARTING_POSITIONS = [(0,0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
class Snake(Turtle):
    """contains everything snake related: its appearance and behaviour"""

    def __init__(self):
        """initializes a new Snake object"""
        super().__init__()
        self.all_segments = []
        self.create_snake()

    def create_snake(self):
        """creates a new snake"""
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        """returns position to where the segment should be added"""
        new_segment = Turtle(shape="square")
        new_segment.penup()
        new_segment.goto(position)
        new_segment.color("white")
        self.all_segments.append(new_segment)

    def reset(self):
        """initiates a new snake once game is over"""
        for segment in self.all_segments:
            segment.goto(1000, 1000)  # send current segments to a place off the screen.
            # if you don't do this, you will keep seeing the segments of the previous snake on the screen.
        self.all_segments.clear()  # removes all items from list
        self.create_snake()

    def extend(self):
        """adds a new segment to the end of the snake"""
        self.add_segment(self.all_segments[-1].position())  # get hold of the last segment in the list of segments

    def move(self):
        """moves all segments of the snake forward: first the third segment goes were the second segment was, secondly the
          2nd segment goes where the 1st segment was, lastly the first segment moves forward"""
        for segment_number in range(len(self.all_segments) - 1, 0, -1):  # range(start=len(all_segments)-1, stop=0,
            # step=-1)
            # going from segment#3 to segment#0
            new_x = self.all_segments[segment_number - 1].xcor()
            new_y = self.all_segments[segment_number - 1].ycor()
            self.all_segments[segment_number].goto(new_x, new_y)
        self.all_segments[0].forward(MOVE_DISTANCE)

    def up(self):
        """turns the first segment facing upwards"""
        if self.all_segments[0].heading() != DOWN:  # snake is not allowed to turn around
            self.all_segments[0].setheading(UP)

    def down(self):
        """turns the first segment facing downwards"""
        if self.all_segments[0].heading() != UP:  # snake is not allowed to turn around
            self.all_segments[0].setheading(DOWN)

    def left(self):
        """turns the first segment facing left"""
        if self.all_segments[0].heading() != RIGHT:  # snake is not allowed to turn around
            self.all_segments[0].setheading(LEFT)

    def right(self):
        """turns the first segment facing right"""
        if self.all_segments[0].heading() != LEFT:  # snake is not allowed to turn around
            self.all_segments[0].setheading(RIGHT)
