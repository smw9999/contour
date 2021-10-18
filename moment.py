# # 모멘트 구해서 표시하기 - 무게중심
# img_src = cv2.imread('shape.png', cv2.IMREAD_COLOR)
#
# #1 - 이미지를 Gray로 변환
# img_gray = cv2.cvtColor(img_src, cv2.COLOR_BGR2GRAY)
# #2 이진화를 진행
# #  이미지의 특성을 파악 : 검출할려고 하는것(도형)이 흰색으로 나와야함
# #  배경이 흰색 : 검출해야하는 물체보다 배경이 밝은 상태
#
# # 방법 2-1 : 그레이 이미지를 반전하고 Threshold 를 적용
# # img_gray = cv2.bitwise_not(img_gray)
# # ret, img_binary = cv2.threshold(img_gray, 100, 255, cv2.THRESH_BINARY)
#
# # 방법 2-2 : cv2.threshold()함수의 옵션사용
# ret, img_binary = cv2.threshold(img_gray, 150, 255, cv2.THRESH_BINARY_INV)
#
# # 검출하려고 하는 도형의 외곽선 검출 : findContours()함수 사용
# contours, hierarchy = cv2.findContours(img_binary, cv2.RETR_LIST,
#                                       cv2.CHAIN_APPROX_NONE)
#
# my_color = (0,255,0) # (B,G,R)
# text_color = (255,0,0) # (B,G,R)
# thickness = 2
#
# for i, contour in enumerate(contours):
#    area = cv2.contourArea(contour)
#    # contourArea()함수로 객체의 면적을 구하고 면적기준으로 임계값보다
#    # 큰 객체만 외곽선을 그리고 면적정보를 표시한다.
#    if area > 10000:
#        cv2.drawContours(img_src, contours, i, my_color, thickness)
#        #모멘트 그리기(무게중심)
#        mu = cv2.moments(contour)
#        cx = int(mu['m10'] / (mu['m00']+1e-5))
#        cy = int(mu['m01'] / (mu['m00']+1e-5))
#        cv2.circle(img_src, (cx,cy), 5, (0,255,255),-1)
#        cv2.putText(img_src, f'{i}: {int(area)}', (cx-50,cy-20),
#                    cv2.FONT_HERSHEY_COMPLEX, 0.8, text_color, 1)
#        cv2.imshow('dst',img_src)
#        cv2.waitKey(0)
#
# cv2.destroyAllWindows()