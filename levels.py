import pygame

import constants
import platforms

class Level():
    """ This is a generic super-class used to define a level.  Each level is
        a specific child class"""


    # List of sprites used in all levels.  Add or remove lists as needed

    platform_list = None
    enemy_list = None
    feature_list = None

    #  Background image
    background = None

    # How far this world has been scrolled left/right
    world_shift = 0
    level_limit = -1000 #i may not need this... or modify it to define boundaries (referenced in platform_scroller too

    def __init__(self, player):
        """Constructor.  Pass in a handle to player.  Needed when moving platform
           Collides with the player."""
        self.platform_list = pygame.sprite.Group()
        self.enemy_list = pygame.sprite.Group()
        self.feature_list = pygame.sprite.Group()
        self.player = player

    # update everything in this level
    def update(self):

        self.platform_list.update()
        self.enemy_list.update()
        self.feature_list.update()

    def draw(self, screen):
        """ Draw everything on this level """

        #draw background
        #we don't shift the background as much as the sprites are shifted
        # to give a feeling of depth
        screen.fill(constants.BLUE)
        screen.blit(self.background,(self.world_shift // 3, 0))

        #draw all the sprite lists we have
        self.platform_list.draw(screen)
        self.enemy_list.draw(screen)
        self.feature_list.draw(screen)

    def shift_world(self, shift_x):
        """ When the user moves left/right and we need to scroll everything """

        # keep track of shift amount
        self.world_shift += shift_x

        #go through all the sprite lists and shift
        for platform in self.platform_list:
            platform.rect.x += shift_x

        for enemy in self.enemy_list:
            enemy.rect.x += shift_x

        for feature in self.feature_list:
            feature.rect.x += shift_x

# create platforms for the level
class Level_01(Level):
    """ definition for level 1 """

    def __init__(self, player):
        """ Create level 1. """

        # call the parent constructor
        Level.__init__(self, player)

        self.background = pygame.image.load("background_01.png").convert()
        self.background.set_colorkey(constants.WHITE)
        self.level_limit = -2500

        # Array with type of platform, and x, y location of the platform.
        level = [ [platforms.GRASS_LEFT, 500, 500],
                  [platforms.GRASS_MIDDLE, 570, 500],
                  [platforms.GRASS_RIGHT, 640, 500],
                  [platforms.GRASS_LEFT, 800, 400],
                  [platforms.GRASS_MIDDLE, 870, 400],
                  [platforms.GRASS_RIGHT, 940, 400],
                  [platforms.GRASS_LEFT, 1000, 500],
                  [platforms.GRASS_MIDDLE, 1070, 500],
                  [platforms.GRASS_RIGHT, 1140, 500],
                  [platforms.STONE_PLATFORM_LEFT, 1120, 280],
                  [platforms.STONE_PLATFORM_MIDDLE, 1190, 280],
                  [platforms.STONE_PLATFORM_RIGHT, 1260, 280],
                  ]


        # Go through the array above and add platforms
        for platform in level:
            block = platforms.Platform(platform[0])
            block.rect.x = platform[1]
            block.rect.y = platform[2]
            block.player = self.player
            self.platform_list.add(block)

        # add array of features that can't cause collisions
        level = [ [platforms.DOOR_BASE, 870, 330],
                  [platforms.DOOR_TOP, 870, 290],
                  ]
        
        for feature in level:
            block = platforms.Feature(feature[0])
            block.rect.x = feature[1]
            block.rect.y = feature[2]
            block.player = self.player
            self.feature_list.add(block)

        # Add a custom moving platform
        block = platforms.MovingPlatform(platforms.STONE_PLATFORM_MIDDLE)
        block.rect.x = 1350
        block.rect.y = 280
        block.boundary_left = 1350
        block.boundary_right = 1600
        block.change_x = 1
        block.player = self.player
        block.level = self
        self.platform_list.add(block)




# Create platforms for the level
class Level_02(Level):
    """ Definition for level 2 """

    def __init__(self, player):
        """ Create level 1. """

        # Call the parent constructor
        Level.__init__(self, player)

        self.background = pygame.image.load("background_02.png").convert()
        self.background.set_colorkey(constants.WHITE)
        self.level_limit = -2000

        # Array with types of platforms, x,y locations of the platform.
        level = [ [platforms.STONE_PLATFORM_LEFT, 500, 550],
                  [platforms.STONE_PLATFORM_MIDDLE, 570, 550],
                  [platforms.STONE_PLATFORM_RIGHT, 640, 550],
                  [platforms.GRASS_LEFT, 800, 400],
                  [platforms.GRASS_MIDDLE, 870, 400],
                  [platforms.GRASS_RIGHT, 940, 400],
                  [platforms.GRASS_LEFT, 1000, 500],
                  [platforms.GRASS_MIDDLE, 1070, 500],
                  [platforms.GRASS_RIGHT, 1140, 500],
                  [platforms.STONE_PLATFORM_LEFT, 1120, 280],
                  [platforms.STONE_PLATFORM_MIDDLE, 1190, 280],
                  [platforms.STONE_PLATFORM_RIGHT, 1260, 280],
                  ]


        # go through the array above and add platforms
        for platform in level:
            block = platforms.Platform(platform[0])
            block.rect.x = platform[1]
            block.rect.y = platform[2]
            block.player = self.player
            self.platform_list.add(block)

        # add a custom moving platform
        block = platforms.MovingPlatform(platforms.STONE_PLATFORM_MIDDLE)
        block.rect.x = 1500
        block.rect.y = 300
        block.boundary_top = 100
        block.boundary_bottom = 550
        block.change_y = -1
        block.player = self.player
        block.level = self
        self.platform_list.add(block)
        
