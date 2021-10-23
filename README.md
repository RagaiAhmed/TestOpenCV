# TestOpenCV
## opencv python

first approch was to loop through each contor found using gray thershold  

use gray scale to detect contours of each colored object then approxmate it to a polygon then counting the number of sides to detect its name.


adding its name in the center and detecting the contour center using contour moment.


second we added ratio comparison for quad to detect square or rectangle


third we wanted to detect colors so instead of using gray scale we used hsv mask for each of the four colors to find contours of this colors and adding them to list of this color 


then we added each list to a one big list with four colors in order approxmated and detected the shape then added colors name respectivly 
