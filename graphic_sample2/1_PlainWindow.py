import arcade


SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

 #Set Background color
arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, "Drawing Primitives Example")
arcade.set_background_color(arcade.color.BLACK)

# Start the render process. This must be done before any drawing commands.
arcade.start_render()
arcade.finish_render()
arcade.run()