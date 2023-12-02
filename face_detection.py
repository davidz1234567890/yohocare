import cv2
import glob
eye_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + 'haarcascade_eye.xml')
face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

images = glob.glob('faces/*.png')

for image in images[1:]:
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

        eyes = eye_cascade.detectMultiScale(
            gray_face, 1.085, 2)  # before was 1.05 and 4
        print("here is eyes line 143")
        print(eyes)
        best_left_eye = (0, 0, 0, 0)
        good_left_eyes = []
        for eye in eyes:
            # distance_difference = (
            #     eye[0] - correct_left_x) + (eye[1] - correct_left_y)
            # area_difference = (eye[2] * eye[3] - area_of_left_rectangle)
            # if(distance_difference < smallest_difference_in_distance and area_difference < smallest_difference_in_area):
            #     smallest_difference_in_distance = distance_difference
            #     smallest_difference_in_area = area_difference
            #     best_left_eye = eye
            x = eye[0]
            x = x + good_x
            y = eye[1]
            y = y + good_y
            width = eye[2]
            height = eye[3]
            if((y+height < good_y+greatest_height//2) and (y > good_y) and (x > good_x) and (x+width < good_x+greatest_width//2)):
                good_left_eyes.append(eye)

        smallest_difference_in_distance = 1000000
        smallest_difference_in_area = 1000000

        best_right_eye = (0, 0, 0, 0)
        good_right_eyes = []
        for eye in eyes:
            # distance_difference = (
            #     eye[0] - correct_right_x) + (eye[1] - correct_right_y)
            # area_difference = (eye[2] * eye[3] - area_of_right_rectangle)
            # if(distance_difference < smallest_difference_in_distance and area_difference < smallest_difference_in_area):
            #     smallest_difference_in_distance = distance_difference
            #     smallest_difference_in_area = area_difference
            #     best_right_eye = eye
            x = eye[0]
            x = x+good_x
            y = eye[1]
            y = y+good_y
            width = eye[2]
            height = eye[3]

            print("here is goodx\n")
            print(good_x)
            print("here is goody")
            print(good_y)
            print("here is greatest width\n")
            print(greatest_width)
            print("here is greatest height\n")
            print(greatest_height)
            print("here is greatest width\n")
            print(greatest_width)

            print("here is x")
            print(x)
            print("here is y")
            print(y)
            print("here is width")
            print(width)
            print("here is height")
            print(height)
            if((y+height < good_y+greatest_height//2) and (y > good_y) and (x > good_x+greatest_width//2) and (x+width < good_x + greatest_width)):
                good_right_eyes.append(eye)

        print("good left\n")
        print(good_left_eyes)
        print("good right\n")
        print(good_right_eyes)

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

        # for (eye_x, eye_y, eye_width, eye_height) in eyes:
        #     topleftcoordinate = (eye_x, eye_y)
        #     width_height = (eye_x+eye_width, eye_y+eye_height)
        #     cv2.rectangle(color_face, topleftcoordinate,
        #                   width_height, color, thickness)

        # left eye
        topleftcoordinate = (good_left_eyes[0][0], good_left_eyes[0][1])
        width_height = (good_left_eyes[0][0]+good_left_eyes[0][2],
                        good_left_eyes[0][1]+good_left_eyes[0][3])
        cv2.rectangle(color_face, topleftcoordinate,
                      width_height, color, thickness)

        toprightcoordinate = (good_right_eyes[0][0], good_right_eyes[0][1])
        width_height = (good_right_eyes[0][0]+good_right_eyes[0][2],
                        good_right_eyes[0][1]+good_right_eyes[0][3])
        cv2.rectangle(color_face, toprightcoordinate,
                      width_height, color, thickness)

        # topleftcoordinate = (good_right_eyes[0][0], good_right_eyes[0][1])
        # width_height = (
        #     good_right_eyes[0][0]+good_right_eyes[0][2], good_right_eyes[0][1]+good_right_eyes[0][3])
        # cv2.rectangle(color_face, topleftcoordinate,
        #               width_height, color, thickness)
        #         length1 = len(eyes)
        #         length2 = len(eyes[0])
        #         if(eyes[length1//2][length2//2] < biggest[length1//2][length2//2]):
        #             biggest = eyes
        #             correct_scale = scalefactor
        #             correct_neighbors = neighbors

        #         neighbors = neighbors + 1
        #     scalefactor = scalefactor + 0.01

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
    cv2.waitKey(5000)
    break


cv2.destroyAllWindows()


# ellipse too large
# print out circle with one color and ellipse with different color and see if circle is touch the ellipse
# take a photo of nothing/no face or wall
# feed the image and nothing to draw
# if empty exception then


# back up this code
# define a draw function
# define a function test whether user is looking towards left whether user is looking towards right
