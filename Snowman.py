import arcade

window = arcade.Window(800, 600, "Drawing a Rectangle")
arcade.start_render()

arcade.draw_rectangle_filled(400, 0, 800, 400, arcade.color.BLUEBERRY)
arcade.draw_rectangle_filled(400, 400, 800, 400, arcade.color.BLUEBONNET)

arcade.draw_circle_filled(400, 225, 75, arcade.color.PAPAYA_WHIP)
arcade.draw_circle_filled(400, 345, 60, arcade.color.PAPAYA_WHIP)
arcade.draw_circle_filled(400, 440, 45, arcade.color.PAPAYA_WHIP)

arcade.draw_circle_filled(415, 450, 5, arcade.color.BLACK_BEAN)
arcade.draw_circle_filled(385, 450, 5, arcade.color.BLACK_BEAN)

arcade.draw_circle_filled(400, 385, 5, arcade.color.BLACK_BEAN)
arcade.draw_circle_filled(400, 350, 5, arcade.color.BLACK_BEAN)
arcade.draw_circle_filled(400, 315, 5, arcade.color.BLACK_BEAN)

arcade.finish_render()
arcade.run()