win = GraphWin("Graphics!!!!!!", 500, 500)   # create new GraphWin object, 500x500 pixels in size
win.setBackground("blue")                    # set the background color to blue

cp = Point(50,50)          # creates a new Point object at 50,50
circ = Circle(cp, 20)      # creates new Circle object centered at point cp with a radius of 20 pixels
circ.setFill("red")        # invoke the setFill method of the Circle object referred to by circ
circ.draw(win)             # draw the circ object to the GraphWin win
win.getMouse()             # wait for user to click mouse
win.close()                # close window
