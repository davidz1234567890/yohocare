import cv2
import glob


def draw(color_face, list_of_coordinates):
    print("the width of good eye:")
    print(list_of_coordinates[0][2])
    print("\n")
    print("the height of good eye:")
    print(list_of_coordinates[0][3])
    topleftcoordinate = (list_of_coordinates[0][0], list_of_coordinates[0][1])
    width_height = (list_of_coordinates[0][0]+list_of_coordinates[0][2],
                    list_of_coordinates[0][1]+list_of_coordinates[0][3])
    color = (0, 255, 255)
    thickness = 2
    cv2.rectangle(color_face, topleftcoordinate,
                  width_height, color, thickness)


eye_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + 'haarcascade_eye.xml')
face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# substitute this with the appropriate folder name
images = glob.glob('straight/*.png')

for image in images[:]:
    print(image)
    good_left_eyes = []
    good_right_eyes = []
    img = cv2.imread(image)
    gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

    faces = face_cascade.detectMultiScale(gray, 1.085, 5)
    print("here is faces on line 35")
    print(faces)

    i = 0
    greatest_width = 0
    greatest_height = 0
    good_x = 0
    good_y = 0

    for(x, y, w, h) in faces:

        if(w > greatest_width):
            print("enters here, this if statement")
            greatest_width = w
            greatest_height = h
            good_x = x
            good_y = y

        # for each face find the eyes and see if the eyes are in the rectangle

        # # this is a tuple containing the major and minor axes in that order for ellipse
        minor = (h*2)//4
        major = (h*1)//3  # greatest_width//3
        axes_length = (major, minor)
        # dividing the height by 2 will give a horizontal ellipse
        # dividing the width by 2 will give a vertical ellipse
        center_coordinates = x + w // 2, y + h // 2
        angle = 0  # ellipse rotation angle
        start = 0  # ellipse start drawing at this angle
        end = 359  # ellipse end drawing at this angle
        color = (0, 0, 100)
        thickness = 3

        cv2.ellipse(img, center_coordinates, axes_length,
                    angle, start, end, color, thickness)
    print("here is goodx")
    print(good_x)
    print("\n")
    print("here is goody")
    print(good_y)
    print("\n")
    print("here is greatest_width")
    print(greatest_width)
    print("\n")
    print("here is greatest height")
    print(greatest_height)
    print("\n")
    # this is a tuple containing the major and minor axes in that order for ellipse
    minor = (greatest_height*2)//4
    major = (greatest_height*1)//3
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

    # this section includes only the face
    gray_face = gray[good_y:good_y+greatest_height,
                     good_x:good_x+greatest_width]
    # x and y are the top left coordinate of the face
    color_face = img[good_y:good_y+greatest_height,
                     good_x:good_x+greatest_width]

    eyes = eye_cascade.detectMultiScale(
        gray_face, 1.1, 5)  # before was 1.05 and 4
    print("here is eyes line 143")
    print(eyes)

    for eye in eyes:
        print("entering here\n")

        x = eye[0]

        x = x + good_x
        # print("x is")
        # print(x)
        # print("\n")
        y = eye[1]

        y = y + good_y
        # print("y is")
        # print(y)
        # print("\n")

        width = eye[2]

        # print("width is")
        # print(width)
        # print("\n")
        height = eye[3]

        # print("height is")
        # print(height)
        # print("\n")
        # make this or in the middle
        if((y+height <= good_y+greatest_height//2 + 25) and (y >= good_y)) and ((x >= good_x) and (x+width <= good_x+greatest_width//2 + 25)):
            # if((x >= good_x - 50) and (x+width <= good_x+greatest_width//2 + 50)):
            good_right_eyes.append(eye)

    for eye in eyes:

        x = eye[0]
        x = x+good_x
        y = eye[1]
        y = y+good_y
        width = eye[2]
        height = eye[3]

        if(((y+height <= good_y+greatest_height//2 + 25) and (y >= good_y)) and ((x >= good_x+greatest_width//2 - 25) and (x+width <= good_x + greatest_width + 25))):
            # if(((x >= good_x+greatest_width//2 - 50) and (x+width <= good_x + greatest_width + 50))):
            good_left_eyes.append(eye)

    print("good left\n")
    print(good_left_eyes)
    print("good right\n")
    print(good_right_eyes)

    # draw a rectangle around eyes
    color = (0, 255, 255)
    thickness = 2

    print("reaching here in the code\n")
    print("here is eyes")
    print(eyes)

    # for (eye_x, eye_y, eye_width, eye_height) in eyes:
    #     print("on line 168")
    #     topleftcoordinate = (eye_x, eye_y)
    #     width_height = (eye_x+eye_width, eye_y+eye_height)
    #     cv2.rectangle(color_face, topleftcoordinate,
    #                   width_height, color, thickness)
    # before was 1.05 and 4

    # separation here

    # left eye refers to the person's left eye, which is on the viewer's right
    left_eye = good_left_eyes[0]
    best_left_eye = []
    best_left_eye.append(left_eye)
    largest_width = 0
    for eye in good_right_eyes:
        print(eye[2])
        if(largest_width < eye[2] and eye[0] != left_eye[0]):
            print("enters line 198")
            largest_width = eye[2]
            right_eye = eye
    #right_eye = good_right_eyes[0]
    print(right_eye)
    best_right_eye = []
    best_right_eye.append(right_eye)
    for (eye_x, eye_y, eye_width, eye_height) in best_left_eye:
        topleftcoordinate = (eye_x, eye_y)
        width_height = (eye_x+eye_width, eye_y+eye_height)
        cv2.rectangle(color_face, topleftcoordinate,
                      width_height, color, thickness)
        break

    for (eye_x, eye_y, eye_width, eye_height) in best_right_eye[:]:
        topleftcoordinate = (eye_x, eye_y)
        width_height = (eye_x+eye_width, eye_y+eye_height)
        cv2.rectangle(color_face, topleftcoordinate,
                      width_height, color, thickness)
        break

    cv2.imshow('image', img)

    #right_eye = good_right_eyes[0]
    face_midline = good_x + greatest_width//2
    print("here is face midline")
    print(face_midline)
    print("\n")
    left_eye_outside = left_eye[0] + good_x + left_eye[2]
    print("here is left eye midline")
    print(left_eye_outside)
    print("\n")
    right_eye_outside = right_eye[0] + good_x
    print("here is right eye midline")
    print(right_eye_outside)
    print("\n")

    left_diff = (left_eye_outside - (face_midline))
    right_diff = (right_eye_outside - (face_midline))
    if(abs(left_diff) - abs(right_diff) < -5):
        print("user is looking to his/her right")
    elif(abs(left_diff) - abs(right_diff) > 5):
        print("user is looking to his/her left")
    else:
        print("user is looking straight ahead")
    cv2.waitKey(4000)
    # break


cv2.destroyAllWindows()


# back up this code
# define a draw function
# define a function test whether user is looking towards left whether user is looking towards right


# document what did I learn throughout the internships and what can I apply to the upcoming five months and five years
