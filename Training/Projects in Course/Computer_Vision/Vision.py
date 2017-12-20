import cv2
import glob

ImgSource = cv2.imread("cosmos.jpg",0)          # 0 -Gray, 1 -Color, -1 -Color with Alpha
AllImages = glob.glob("*.jpg")
for n in AllImages:
    print(n)

print(ImgSource)
print(ImgSource.shape)
print(ImgSource.ndim)

# Resized = cv2.resize(ImgSource,(800,600))       # Resize image (Non aspect)
Resized = cv2.resize(ImgSource,(int(ImgSource.shape[1]/2),int(ImgSource.shape[0]/2)))

cv2.imshow("Cosmos",Resized)                    # Display Image
cv2.waitKey(5000)                               # For x milli seconds
cv2.destroyAllWindows()                         # Close window

cv2.imwrite("Cosmos_Resized.jpg", Resized)