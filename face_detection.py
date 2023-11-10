import cv2
import glob
eye_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + 'haarcascade_eye.xml')
face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

images = glob.glob('faces/*.png')
#i = 0
for image in images:
    print("newimage\n")
    print(image)
    img = cv2.imread(image)
    gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    print("gray here:\n\n")
    print(gray)
    faces = face_cascade.detectMultiScale(gray, 1.085, 2)
    print("gray here:\n")
    print(gray)
    # I think 1.09 for scale and 2 for minNeighbors works best
    # I think 1.085 and 2 work the best

    # i = 0.1
    # while i < 10:
    #     faces = face_cascade.detectMultiScale(gray, i, 4)
    #     if()
    #     i=i+0.1

    # scoring function
    # declare intermediate variables for the parameter
    # second parameter be 1 to 9
    # area of one circle, bigger is better

    # draw ellipse
    i = 0
    greatest_width = 0
    greatest_height = 0
    good_x = 0
    good_y = 0

    for(x, y, w, h) in faces:
        # new code for 3 lines below that draws a circle around the face
        print("gray inside loop:\n")
        print(gray)

        if(w > greatest_width):
            greatest_width = w
            greatest_height = h
            good_x = x
            good_y = y
        # denote the major and minor axes lengths of ellipse
        print(w)
        print(h)
        print("width is \n")
        print(faces[i][2])
        print("gray inside loop:222\n")
        print(gray)
        print(faces)

        # print(faces[2])
        # axes_length = (w, h//2)
        # center_coordinates = x + w // 2, y + h // 2
        # angle = 90  # ellipse rotation angle
        # start = 0  # ellipse start drawing at this angle
        # end = 359  # ellipse end drawing at this angle
        # color = (0, 0, 100)
        # thickness = 3
        # cv2.ellipse(img, center_coordinates, axes_length,
        #             angle, start, end, color, thickness)

        #gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

        # print("img:\n")
        # print("x is")
        # print(x)
        # print("y is")
        # print(y)
        # print("h is")
        # print(h)
        # print("w is")
        # print(w)
        # print("gray:\n")
        # print(gray)
        # print(img)
        gray_face = gray[y:y+h, x:x+w]  # this section includes only the face
        # x and y are the top left coordinate of the face
        color_face = img[y:y+h, x:x+w]

        # detects eyes of within the detected face area (roi)
        print("gray face:\n")
        print(gray_face)
        print("eye_cascade")
        print(eye_cascade)
        print("face_cascade")
        print(face_cascade)
        print("end debug here")


# pick one photo and check where the eye location is
# manually calculate the coordinates of the eyes
        scalefactor = 1.01
        correct_scale = scalefactor
        neighbors = 1
        correct_neighbors = neighbors

        # see what are the element of biggest
        biggest = eye_cascade.detectMultiScale(gray_face, 1.01, 1)
        while scalefactor < 1.5:
            while neighbors < 7:
                eyes = eye_cascade.detectMultiScale(
                    gray_face, scalefactor, neighbors)
                length1 = len(eyes)
                length2 = len(eyes[0])
                if(eyes[length1//2][length2//2] < biggest[length1//2][length2//2]):
                    biggest = eyes
                    correct_scale = scalefactor
                    correct_neighbors = neighbors
                neighbors = neighbors + 1
            scalefactor = scalefactor + 0.01

        eyes = eye_cascade.detectMultiScale(
            gray_face, correct_scale, correct_neighbors)  # before was 1.05 and 4
        print("eyes\n")
        print(eyes)
        # draw a rectangle around eyes
        color = (0, 255, 255)
        thickness = 2

        # scoring function base on smaller difference between the area of the rectangle and the area of the eye
        # another scoring function base on differences between model prediction and actual locations: x and y and width and height
        # second one is beter
        # print out the values of x y width and height to see if it is pixel
        # Root mean square
        # feed in photo without glass
        # k-means algorithm:lookp at the wikipedia   k = 3, mouth and 2 eye
        # scoring function is base on distance between center of cluster
        for (eye_x, eye_y, eye_width, eye_height) in eyes:
            topleftcoordinate = (eye_x, eye_y)
            width_height = (eye_x+eye_width, eye_y+eye_height)
            cv2.rectangle(color_face, topleftcoordinate,
                          width_height, color, thickness)

        # look up a cv2.ellipse function
        # radius = w // 2  # or can be h / 2 or can be anything based on your requirements
        #cv2.circle(img, center_coordinates, radius, (0, 0, 100), 3)
        i = i + 1
        # the line below draws a rectangle around the face
        #cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)

    # this is a tuple containing the major and minor axes in that order for ellipse
    minor = (greatest_height*2)//4
    major = (greatest_height*1)//3  # greatest_width//3
    axes_length = (major, minor)
    # dividing the height by 2 will give a horizontal ellipse
    # dividing the width by 2 will give a vertical ellipse
    center_coordinates = good_x + greatest_width // 2, good_y + greatest_height // 2
    angle = 0  # ellipse rotation angle
    start = 0  # ellipse start drawing at this angle
    end = 359  # ellipse end drawing at this angle
    color = (0, 0, 100)
    thickness = 3
    cv2.ellipse(img, center_coordinates, axes_length,
                angle, start, end, color, thickness)
    cv2.imshow('image', img)
    cv2.waitKey(1000)
cv2.destroyAllWindows()


# ellipse too large
# print out circle with one color and ellipse with different color and see if circle is touch the ellipse
# take a photo of nothing/no face or wall
# feed the image and nothing to draw
# if empty exception then
