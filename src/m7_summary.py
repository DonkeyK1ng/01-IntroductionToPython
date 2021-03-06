"""
An exercise that summarizes what you have learned in this Session.

Authors: David Mutchler, Dave Fisher, Vibha Alangar, Amanda Stouder,
         their colleagues and Yuanning Zuo.
"""
########################################################################
# Done: 1.
#   On Line 5 above, replace  PUT_YOUR_NAME_HERE  with your own name.
########################################################################

########################################################################
# TODO: 2.
#   Write code that accomplishes the following:
#     - Constructs a SimpleTurtle with a  blue  Pen.
#     - Makes the SimpleTurtle go straight UP 200 pixels.
#     - Tells the SimpleTurtle to make its pen go UP
#          (so that the next movements do NOT leave a "trail")
#          HINT: Use the "dot trick" to figure out how to do this.
#     - Tells the SimpleTurtle to go to (100, -40).
#     - Tells the SimpleTurtle to make its pen go DOWN
#          (so that the next movements will return to leaving a "trail")
#     - Makes the SimpleTurtle's pen have color "green" and thickness 10.
#     - Tells the SimpleTurtle to go 150 pixels straight DOWN.
#
# Don't forget to:
#     - import rosegraphics and construct a TurtleWindow
#          at the BEGINNING of your code, and to
#     - ask your TurtleWindow to   close_on_mouse_click
#          as the LAST line of your code.
#   See the beginning and end of m4e_loopy_turtles for an example.
#
#      ** Nothing fancy is required. **
#      ** The NEXT exercise will let you show your creativity. **
#
#   As always, test by running the module.
#
#   As always, COMMIT-and-PUSH when you are done with this module.
#
###############################################################################

import rosegraphics as rg

window = rg.TurtleWindow()


blue = rg.SimpleTurtle('turtle')
blue.pen = rg.Pen('blue' , 20)
blue.pen_down()
blue.right(90)
blue.backward(200)
blue.speed = 10
blue.pen_up()

# now will leave a rail
blue.go_to(rg.Point(100, -40))
blue.pen.color = 'green'
blue.pen.thickness = 10
blue.pen_down()
blue.speed = 5
# blue.right(0)
blue.forward(150)
blue.pen_up()


window.close_on_mouse_click()