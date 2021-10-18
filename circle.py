# # 원찾기
# img_src = cv2.imread('balls.jpg',cv2.IMREAD_COLOR)
# img_dst = img_src.copy()
# img_gray = cv2.cvtColor(img_src, cv2.COLOR_BGR2GRAY)
#
# circles = cv2.HoughCircles(img_gray, cv2.HOUGH_GRADIENT, 1,
#                           minDist=100, param1=250, param2=10,
#                           minRadius=80, maxRadius=120)
#
# for i, circle in enumerate(circles[0]):
#    # 값이 실수로 들어오므로 정수로 변환하여야 표시가 됨
#    cv2.circle(img_dst,
#              (int(circle[0]),int(circle[1])), int(circle[2]),
#              (255,255,255), 3)
# cv2.imshow('dst',img_dst)
# cv2.waitKey(0)