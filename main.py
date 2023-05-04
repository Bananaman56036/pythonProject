import arcade

window1 = arcade.Window(800, 600, "Drawing a Circle")
arcade.start_render()

arcade.draw_rectangle_filled(100, 200, 25, 100, arcade.color.WOOD_BROWN)
arcade.draw_circle_filled(100, 250, 50, arcade.color.BANGLADESH_GREEN)

arcade.draw_rectangle_filled(250, 200, 25, 100, arcade.color.WOOD_BROWN)
arcade.draw_ellipse_filled(250, 250, 75, 100, arcade.color.BANGLADESH_GREEN)

arcade.draw_rectangle_filled(250, 200, 25, 100, arcade.color.WOOD_BROWN)
points = ((400, 250),
          (425, 300),
          (450, 250))

arcade.draw_polygon_filled(points, arcade.color.ORANGE)

arcade.finish_render()
arcade.run()
