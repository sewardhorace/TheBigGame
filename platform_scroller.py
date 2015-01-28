"""
main module for scroller example























"""
import pygame

import constants
import levels

from player import Player

def main():
    # main program
    pygame.init()

    # height and width of screen
    size = [constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT]
    screen = pygame.display.set_mode(size)

    pygame.display.set_caption("Hey it works i guess")

    # create player
    player = Player()

    # create all the levels
    level_list = []
    level_list.append(levels.Level_01(player))
    level_list.append(levels.Level_02(player))

    # set current level
    current_level_no = 0
    current_level = level_list[current_level_no]

    active_sprite_list = pygame.sprite.Group()
    player.level = current_level

    player.rect.x = 340
    player.rect.y = constants.SCREEN_HEIGHT - player.rect.height
    active_sprite_list.add(player)

    # loop until user clicks close button
    done = False

    # used to manage how fast screen updates
    clock = pygame.time.Clock()

    # main program loop
    while not done:
        for event in pygame.event.get(): #user did something
            if event.type == pygame.QUIT: # if user clicked close
                done = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    player.go_left()
                if event.key == pygame.K_RIGHT:
                    player.go_right()
                if event.key == pygame.K_UP:
                    player.jump()

                #if player is touching a door, warp levels.
                if event.key == pygame.K_DOWN and player.door():
                    current_level_no = 1
                    current_level = level_list[current_level_no]
                    player.level = current_level

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT and player.change_x < 0:
                    player.stop()
                if event.key == pygame.K_RIGHT and player.change_x > 0:
                    player.stop()

        # update the player
        active_sprite_list.update()

        # update items in the level
        current_level.update()

        # if the player gets near the right side, shift the world left (-x)
        if player.rect.right >= 500:
            diff = player.rect.right - 500
            player.rect.right = 500
            current_level.shift_world(-diff)

        # if player gets near left...
        if player.rect.left <= 120:
            diff = 120 - player.rect.left
            player.rect.left = 120
            current_level.shift_world(diff)

        # if player gets to end of level, go to next level
        current_position = player.rect.x + current_level.world_shift
        if current_position < current_level.level_limit:
            player.rect.x = 120
            if current_level_no < len(level_list)-1:
                current_level_no += 1
                current_level = level_list[current_level_no]
                player.level = current_level

        # all code to draw should go below here
        current_level.draw(screen)
        active_sprite_list.draw(screen)

        # all code to draw should go above here

        # limit 60 fps
        clock.tick(60)

        # go ahead and update the screen with what we've drawn
        pygame.display.flip()

    # program will "hang" without this line:

    pygame.quit()

if __name__ == "__main__":
    main()
