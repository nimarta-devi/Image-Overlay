import cv2

# Load the t-shirt image and the logo image
tshirt = cv2.imread('mug.jpg')
logo = cv2.imread('cat.jpg')
print("logo shape", logo.shape)
# Create a copy of the t-shirt image for displaying the selection
tshirt_copy = tshirt.copy()

# Allow the user to select a ROI on the t-shirt image
r = cv2.selectROI(tshirt_copy)

# Crop the t-shirt image to the selected ROI
roi = tshirt[int(r[1]):int(r[1]+r[3]), int(r[0]):int(r[0]+r[2])]
print("roi shape", roi.shape)


logo = cv2.resize(logo, (roi.shape[1], roi.shape[0]))

# Create a mask of the logo and create its inverse mask also
img2gray = cv2.cvtColor(logo, cv2.COLOR_BGR2GRAY)
ret, mask = cv2.threshold(img2gray, 10, 255, cv2.THRESH_BINARY)
mask_inv = cv2.bitwise_not(mask)

# Now black-out the area of logo in ROI
img1_bg = cv2.bitwise_and(roi, roi, mask=mask_inv)

# Take only region of logo from logo image.
img2_fg = cv2.bitwise_and(logo, logo, mask = mask)

# Put logo in ROI and modify the t-shirt image
dst = cv2.add(img1_bg, img2_fg)
tshirt[int(r[1]):int(r[1]+r[3]), int(r[0]):int(r[0]+r[2])] = dst

# Show the final t-shirt image with the logo overlay
cv2.imshow('tshirt', tshirt)
cv2.waitKey(0)
cv2.destroyAllWindows()
