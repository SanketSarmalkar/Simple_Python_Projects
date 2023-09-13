import cv2

# Configurable Parameters
source = "image.jpeg"
destination = "resizedImage.jpeg"
# percentage by which the image is resized
scale_percent_width = 10
scale_percent_height = 10

image = cv2.imread(source, cv2.IMREAD_UNCHANGED)
# cv2.imshow("title", image)
#
# cv2.waitKey(0)


# new height and width of the image
new_width = int(image.shape[1] * scale_percent_width/100)
new_height = int(image.shape[0] * scale_percent_height/100)

# resize the image
output = cv2.resize(image, (new_width,new_height)) # second attribute is a tuple

# saving it in this folder (can be converted to any type i.e. png or jpg or jpeg)
# cv2.inwrite('resizedImage.jpg', output)
cv2.imwrite(destination, output)