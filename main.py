import arcade

window = arcade.Window(800, 600, "Drawing a Circle")
arcade.start_render()

arcade.draw_circle_filled(400, 300, 50, arcade.color.BLUE)

arcade.finish_render()
arcade.run()
