import arcade

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

def draw_person(x_position, y_position):

    #Snowballs

    arcade.draw_circle_filled(x_position, y_position, 60, arcade.color.WHITE)
    y_middle = y_position + 80
    arcade.draw_circle_filled(x_position, y_middle, 50, arcade.color.WHITE)
    y_top = y_position + 140
    arcade.draw_circle_filled(x_position, y_top, 40, arcade.color.WHITE)

    # Eyes
    arcade.draw_circle_filled(x_position-15, y_top+10, 5, arcade.color.BLACK)
    arcade.draw_circle_filled(x_position+15, y_top+10, 5, arcade.color.BLACK)



def main():
    arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, "Many Snowmen")
    arcade.set_background_color(arcade.color.DARK_BLUE)
    arcade.start_render()

    # Draw the ground
    arcade.draw_lrtb_rectangle_filled(0, SCREEN_WIDTH, SCREEN_HEIGHT / 3, 0, arcade.color.AIR_SUPERIORITY_BLUE)

    # Draw a snow person
    draw_person(300, 200)
    draw_person(500, 200)

    #  Finish and run
    arcade.finish_render()
    arcade.run()


if __name__ == "__main__":
    main()
