# TestOpenCV
## Open CV
*First we read the image and put it in variable **img** then we reduce it's size by 60% in order to see the whole picture as in it's normal size we can't see the name and color of some shapes.*

*Then we assign the image again in variable **img** after resizing it.*

*We convert  BGR image to HSV and assign the result in **hsv** then we threshold the hsv image for the range of the colores that we want to trace then we but the resulted images in variable **mask\#**.*

*Each **mask** hold hsv image with specific range of color.*

*Then we put the mask's variables and the colores of shapes in two different lists.*

*Inside for loop that loop over the masks the contour start to countor each image of the masks and then another for loop start to loop over the contours and check inside it the coordinates of the contours of each single shape in order to print the name of the shape.*

*Also we print the color of each shape as the color list is looped with the mask list.*

*We finally print the image with the shapes and colores.*

  