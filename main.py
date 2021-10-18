import cv2
import numpy as np

# # CONTOUR 찾기
# img_src = cv2.imread('shape.png', cv2.IMREAD_COLOR)
#
# #1 이미지를 Gray로 변환
# img_gray = cv2.cvtColor(img_src, cv2.COLOR_BGR2GRAY)
#
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
# cv2.imshow('dst',img_binary)
# cv2.waitKey(0)
# cv2.destroyAllWindows()


# # 컨투어 추출 및 그리기
# img_src = cv2.imread('shape.png', cv2.IMREAD_COLOR)
# #1 이미지를 Gray로 변환
# img_gray = cv2.cvtColor(img_src, cv2.COLOR_BGR2GRAY)
# #2 이진화를 진행
# # 방법 2-2 : cv2.threshold()함수의 옵션사용
# ret, img_binary = cv2.threshold(img_gray, 150, 255, cv2.THRESH_BINARY_INV)
#
# # 검출하려고 하는 도형의 외곽선 검출 : findContours()함수 사용
# contours, hierarchy = cv2.findContours(img_binary, cv2.RETR_CCOMP,
#                                       cv2.CHAIN_APPROX_NONE)
# my_color = (255,0,0)
# thickness = 2
#
# for i, contour in enumerate(contours):
#    cv2.drawContours(img_src, [contour], 0, my_color, thickness)
#    cv2.putText(img_src, str(i), tuple(contour[0][0]),
#                cv2.FONT_HERSHEY_COMPLEX, 0.8, my_color, 1)
#    cv2.imshow('dst',img_src)
#    cv2.waitKey(0)
#
# cv2.destroyAllWindows()


# # drawContour사용법
# contours, hierarchy = cv2.findContours(img_binary, cv2.RETR_CCOMP,
#                                       cv2.CHAIN_APPROX_NONE)
# my_color = (255,0,0)
# thickness = 2
#
# # for문을 사용할 때 contour를 사용하는 방법
# for i, contour in enumerate(contours):
#    cv2.drawContours(img_src, [contour], 0, my_color, thickness)
#    cv2.imshow('dst',img_src)
#    cv2.waitKey(0)
#
# # for문에서 drawContours함수의 인덱스를 사용하는 방법
# for i, contour in enumerate(contours):
#    cv2.drawContours(img_src, contours, i, my_color, thickness)
#    cv2.imshow('dst',img_src)
#    cv2.waitKey(0)


# # 컨투어를 한꺼번에 다 그릴 경우 : for문을 사용하지 않으므로 조건적용이 힘들다
# contours, hierarchy = cv2.findContours(img_binary, cv2.RETR_CCOMP,
#                                       cv2.CHAIN_APPROX_NONE)
# my_color = (255,0,0)
# thickness = 2
#
# #외곽선만 표시할 경우, 한꺼번에 외곽선을 다 그림
# cv2.drawContours(img_src, contours, -1, my_color, thickness)
# cv2.imshow('dst',img_src)
# cv2.waitKey(0)


# # contourArea()를 사용하여 객체의 면적구하기
# img_src = cv2.imread('shape.png', cv2.IMREAD_COLOR)
# #1 - 이미지를 Gray로 변환
# img_gray = cv2.cvtColor(img_src, cv2.COLOR_BGR2GRAY)
#
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
# # 검출하려고 하는 도형의 외곽선 검출 : findContours()함수 사용
#
# contours, hierarchy = cv2.findContours(img_binary, cv2.RETR_LIST,
#                                       cv2.CHAIN_APPROX_NONE)
# my_color = (0,255,0) # (B,G,R)
# thickness = 2
# for i, contour in enumerate(contours):
#    area = cv2.contourArea(contour)
#    # contourArea()함수로 객체의 면적을 구하고 면적기준으로 임계값보다
#    # 큰 객체만 외곽선을 그리고 면적정보를 표시한다.
#    if area > 10000:    # 10000보다 큰 contour만 표시
#        cv2.drawContours(img_src, contours, i, my_color, thickness)
#        cv2.putText(img_src, f'{i}: {int(area)}', tuple(contour[0][0]),
#                cv2.FONT_HERSHEY_COMPLEX, 0.8, my_color, 1)
#        cv2.imshow('dst',img_src)
#        cv2.waitKey(0)
#
# cv2.destroyAllWindows()