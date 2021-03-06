"""
 Pygame base template for opening a window

 Sample Python/Pygame Programs
 Simpson College Computer Science
 http://programarcadegames.com/
 http://simpson.edu/computer-science/

 Explanation video: http://youtu.be/vRB_983kUMc
"""

import pygame
import random
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREY = (129, 129, 129)
colors = [BLACK, GREEN, BLUE, RED]

def random_color():
    return random.choice(colors)



class Building():
    """
    This class will be used to create the building objects.

    It takes:
      x_point - an integer that represents where along the x-axis the building will be drawn
      y_point - an integer that represents where along the y-axis the building will be drawn
      Together the x_point and y_point represent the top, left corner of the building

      width - an integer that represents how wide the building will be in pixels.
            A positive integer draws the building right to left(->).
            A negative integer draws the building left to right (<-).
      height - an integer that represents how tall the building will be in pixels
            A positive integer draws the building up 
            A negative integer draws the building down 
      color - a tuple of three elements which represents the color of the building
            Each element being a number from 0 - 255 that represents how much red, green and blue the color should have.

    It depends on:
        pygame being initialized in the environment.
        It depends on a "screen" global variable that represents the surface where the buildings will be drawn

    """
    def __init__(self, screen, x_point, y_point, width, height, color):
        self.x_point = x_point
        self.screen = screen 
        self.y_point = y_point
        self.width   = width
        self.height  = height
        self.color   = color

    def draw(self):
        """
        uses pygame and the global screen variable to draw the building on the screen
        """
        pygame.draw.rect(self.screen, self.color, (self.x_point, self.y_point, self.width, self.height))

    def move(self, speed):
        """
        Takes in an integer that represents the speed at which the building is moving
            A positive integer moves the building to the right ->
            A negative integer moves the building to the left  <-
        Moves the building horizontally across the screen by changing the position of the
        x_point by the speed
        """
        self.x_point = self.x_point - speed
        # self.x_point -= speed



class Scroller(object):
    """
    Scroller object will create the group of buildings to fill the screen and scroll

    It takes:
        width - an integer that represents in pixels the width of the scroller
            This should only be a positive integer because a negative integer will draw buildings outside of the screen
        height - an integer that represents in pixels the height scroller
            A negative integer here will draw the buildings upside down.
        base - an integer that represents where along the y-axis to start drawing buildings for this
            A negative integer will draw the buildings off the screen
            A smaller number means the buildings will be drawn higher up on the screen
            A larger number means the buildings will be drawn further down the screen
            To start drawing the buildings on the bottom of the screen this should be the height of the screen
        color - a tuple of three elements which represents the color of the building
              Each element being a number from 0 - 255 that represents how much red, green and blue the color should have.
        speed - An integer that represents how fast the buildings will scroll

    It depends on:
        A Building class being available to create the building obecjts.
        The building objects should have "draw" and "move" methods.

    Other info:
        It has an instance variable "buildings" which is a list of buildings for the scroller
    """

    def __init__(self, screen, width, height, base, color, speed):
        self.width  = width
        self.height = height
        self.base = base
        self.color = color
        self.speed = speed
        self.screen = screen 


        self.buildings = []
        self.add_buildings() # Add builings each time a new instance is created

    def add_buildings(self):
        """
        Will call add_building until there the buildings fill up the width of the
        scroller.
        """
        bwidth = 0;
        while bwidth < self.width:
            self.add_building(bwidth)
            bwidth += self.buildings[-1].width

    def add_building(self, x_location):
        """
        takes in an x_location, an integer, that represents where along the x-axis to
        put a buildng.
        Adds a building to list of buildings.
        """
        # x_point, y_point, width, height, color
        max_height = self.base - self.height
        height = random.randint(max_height//4, max_height)
        width = random.randint(50, 100)
        y_coordinate = self.base - height
        my_new_building = Building(self.screen, x_location, y_coordinate, width, height, self.color)
        self.buildings.append(my_new_building)

    def draw_buildings(self):
        """
        This calls the draw method on each building.
        """
        for building in self.buildings:
            building.draw()

    def move_buildings(self):
        """
        This calls the move method on each building passing in the speed variable
        As the buildings move off the screen a new one is added.
        """

        visible_buildings = []

        for building in self.buildings:
            building.move(self.speed)

            #If the combined X coordinate plus the width is less than zero, 
            #We know it is off of the screen!
            if building.x_point + building.width > 0:
                visible_buildings.append(building)
        
        self.buildings = visible_buildings
        


        last_building = self.buildings[-1]
        building_x = last_building.x_point
        building_width = last_building.width
        
        final_new_x = building_x + building_width
        #If the X coordinate minus the width of the screen is less than 10,
        #aka if there are only 10 pixels of a building outside of the screen,
        #add another building
        if final_new_x - self.width < 10:
            self.add_building(final_new_x)
