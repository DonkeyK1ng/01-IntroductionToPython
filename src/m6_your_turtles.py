"""
Your chance to explore Loops and Turtles!

Authors: David Mutchler, Dave Fisher, Vibha Alangar, Amanda Stouder,
         their colleagues and Yuanning Zuo.
"""
###############################################################################
# Done: 1.
#   On Line 5 above, replace  PUT_YOUR_NAME_HERE  with your own name.
###############################################################################

###############################################################################
# TODO: 2.
#   You should have RUN the  m5e_loopy_turtles  module and READ its code.
#   (Do so now if you have not already done so.)
#
#   Below this comment, add ANY CODE THAT YOU WANT, as long as:
#     1. You construct at least 2 rg.SimpleTurtle objects.
#     2. Each rg.SimpleTurtle object draws something
#          (by moving, using its rg.Pen).  ANYTHING is fine!
#     3. Each rg.SimpleTurtle moves inside a LOOP.
#
#   Be creative!  Strive for way-cool pictures!  Abstract pictures rule!
#
#   If you make syntax (notational) errors, no worries -- get help
#   fixing them at either this session OR at the NEXT session.
#
#   Don't forget to COMMIT-and-PUSH when you are done with this module.
###############################################################################
import rosegraphics as rg


window = rg.TurtleWindow()

monkey_king = rg.SimpleTurtle('turtle')
monkey_king.pen = rg.Pen('green', 2.5)
monkey_king.speed = 15

size = 200

for king in range (51):
    monkey_king.draw_circle(150)
    monkey_king.pen_up()
    monkey_king.left(1)
    monkey_king.backward(10)
    monkey_king.right(10)
    monkey_king.pen_down()
    size = size - 5


window1 = rg.TurtleWindow()

donkey_king = rg.SimpleTurtle('arrow')
donkey_king.pen = rg.Pen('red', 5)
donkey_king.speed = 10
donkey_king.forward(150)
size1 = 100

for donkey in range (20):

    donkey_king.draw_square(size1)
    donkey_king.pen_up()
    donkey_king.right(10)
    donkey_king.left(15)
    donkey_king.pen_down()
    size1 = size1 - 15

window.close_on_mouse_click()
