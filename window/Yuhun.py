from window.Core import *

exppath = basePath + "exp"
ex = "D://exp.png"
img = cv2.imread(ex, 0 )
cv2.imshow("a", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
