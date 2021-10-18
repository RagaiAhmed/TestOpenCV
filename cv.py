import cv2

def get_contours(img):
    # Those are the counts of the shapes
    count_tri, count_squ, count_react, count_circle = 0, 0, 0, 0
    # Now, we generate the contours from the Canny image
    contours, hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    for cnt in contours:
        # using drawContours() function
        cv2.drawContours(imgContour, cnt, -1, (0, 0, 0), 2)
        # cv2.approxPloyDP() function to approximate the shape
        peri = cv2.arcLength(cnt, True)
        approx = cv2.approxPolyDP(cnt, 0.02 * peri, True)
        objCor = len(approx)
        # Getting the coordinates and the corners of the shape to be used later
        x, y, w, h = cv2.boundingRect(approx)
        # incrementing shape count each contour
        # If it was 3 then the shape will be triangle.
        if objCor == 3:
            count_tri += 1
        # If it was 4 then the shape will be a small rectangle or a square
        # depending on the aspect ratio between the length and height.
        elif objCor == 4:
            if w < 300 and h < 300:
                aspRatio = w / float(h)
                if 0.94 < aspRatio < 1.3:
                    count_squ += 1
                else:
                    count_react += 1
        else:
            if w < 300 and h < 300:
                count_circle += 1
    print("Number of triangles =", count_tri
          , "\nNumber of Squares =", count_squ
          , "\nNumber of Rectangles =", count_react
          , "\nNumber of circles =", count_circle)


# First we read the image
img = cv2.imread('test2.png')
# we make a copy to draw the contours on it.
imgContour = img.copy()
# We convert it to greyScale to apply the GaussianBlur on it.
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray, (7, 7), 1)
# This function is called canny edge detection used to detect the edges of the shapes in the image
imgCanny = cv2.Canny(imgBlur, 50, 50)
# Now we pass the imgCanny to the above function to get the contours.
get_contours(imgCanny)

imgContour = cv2.resize(imgContour, (600, 400))
cv2.imshow('imgContour', imgContour)
cv2.waitKey(0)
