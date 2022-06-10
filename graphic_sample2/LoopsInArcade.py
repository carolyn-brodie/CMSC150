"""
Example "Arcade" library code.

Showing how to do nested loops.

If Python and Arcade are installed, this example can be run from the command line with:
python -m arcade.examples.nested_loops_bottom_left_triangle
"""

# Library imports
import arcade

COLUMN_SPACING = 20
ROW_SPACING = 20
LEFT_MARGIN = 110
BOTTOM_MARGIN = 110
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 400

# Open the window and set the background
arcade.open_window(400, 400, "Complex Loops - Bottom Left Triangle")

arcade.set_background_color(arcade.color.WHITE)

# Start the render process. This must be done before any drawing commands.
arcade.start_render()

xPos = 20
yPos = SCREEN_HEIGHT // 2


# Draw a shape on the screen
# arcade.draw_circle_filled(xPos, yPos, 7, arcade.color.GREEN)
# xPos += COLUMN_SPACING
# arcade.draw_circle_filled(xPos, yPos, 7, arcade.color.GREEN)
# xPos += COLUMN_SPACING
# arcade.draw_circle_filled(xPos, yPos, 7, arcade.color.GREEN)

# Write a loop to display green circles accross the screen
# The loop should range from 20 to the SCREEN_WIDTH - 20 with a Step size of COLUMN_SPACING

# Think about how you could use a second loop to


# Try using shapes to make something

# Make a row of you items using a loop

# Finish the render.
arcade.finish_render()

# Keep the window up until someone closes it.
arcade.run()