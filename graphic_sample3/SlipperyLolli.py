import arcade
import random

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600


GAME_RUNNING = 1
GAME_INTRO = 2
GAME_OVER = 3


class Lolli (arcade.Sprite):
    def update(self):

        ## bounce off sides
        if self.left <= 0 or self.right >= SCREEN_WIDTH:
            self.change_x *= -1

        elif self.bottom <=0 or self.top >= SCREEN_HEIGHT:
            self.change_y *= -1

        self.center_x += self.change_x
        super(Lolli,self).update()


class Game(arcade.Window):
    """ Main application class """

    def __init__(self, width, height):
        super().__init__(width, height)
        # Background image will be stored in this variable
        self.background = None
        self.lolli = None
        self.cake = None
        self.all_sprites_list = []
        self.lolli_list = []
        self.score = 0
        self.score_text = None
        self.state = None


        # Do show the mouse cursor
        self.set_mouse_visible(True)

        # Set the background color
        arcade.set_background_color(arcade.color.BLACK)

    def setup(self):

        self.background = arcade.load_texture("images/wall.jpg")
        self.all_sprites_list = arcade.SpriteList()
        self.lolli_list = arcade.SpriteList()

        self.current_state = GAME_INTRO

        self.lolli = Lolli("images/lollipopRed.png", 1)

        self.lolli.center_x = SCREEN_WIDTH // 2
        self.lolli.center_y = SCREEN_HEIGHT // 2
        self.lolli.angle = 0
        self.lolli.change_x = 1
        self.lolli.change_y  = 1
        self.all_sprites_list.append(self.lolli)
        self.lolli_list.append(self.lolli)

        self.cake = arcade.Sprite("images/cake.png", .75)
        self.all_sprites_list.append(self.cake)

        self.score = 0





    def on_draw(self):
        """Render the screen. """

        arcade.start_render()
        # Draw the background texture
        arcade.draw_texture_rectangle(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2,
                                      SCREEN_WIDTH, SCREEN_HEIGHT, self.background)

        if self.current_state == GAME_INTRO:
            self.current_state = GAME_RUNNING
        elif self.current_state == GAME_RUNNING:
            self.draw_game()

        else:
            ##End game
            self.draw_game_over()




    def draw_game(self):



        self.lolli.draw()
        self.cake.draw()

        # Put the text on the screen.
        output = f"Score: {self.score}"
        arcade.draw_text(output, 10, 550, arcade.color.BLACK, 14)





    def update(self, delta_time):
        """All the logic to move, and the game logic goes here. """
        self.lolli.update()

        # Generate a list of all sprites that collided with the player.
        hit_list = arcade.check_for_collision_with_list(self.cake, self.lolli_list)

        # Loop through each colliding sprite, remove it, and add to the score.
        for lolli in hit_list:
            self.lolli.center_x = random.randrange(SCREEN_WIDTH)
            self.lolli.center_y = random.randrange(SCREEN_HEIGHT)



    def on_mouse_motion(self, x, y, delta_x, delta_y):
        """ Called whenever the mouse moves. """
        self.cake.center_x = x
        self.cake.center_y = y

    def on_key_release(self, key, modifiers):

        if key == arcade.key.ESCAPE:
            self.close()

    def draw_game_over(self):
        print("Done")







def main():
    """ Main method """
    window = Game(SCREEN_WIDTH, SCREEN_HEIGHT)
    window.setup()
    arcade.run()



main()