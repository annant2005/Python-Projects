import cv2
import mediapipe as mp
import pyautogui
hand_detector = mp.solutions.hands.Hands()
cap = cv2.VideoCapture(1)
drwaing_utils = mp.solutions.drawing_utils
screen_width ,screen_height = pyautogui.size()
index_y = 0
scrool_y = 0
while True:
   _, frame = cap.read()

   frame_height, frame_width, _ = frame.shape
   rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
   frame = cv2.flip(frame ,1)
   output = hand_detector.process(rgb_frame)
   hands = output.multi_hand_landmarks
   if hands:
        for hand in hands:
            drwaing_utils.draw_landmarks(frame, hand)
            landmarks = hand.landmark
            for id, landmark in enumerate(landmarks):
                x = int(landmark.x*frame_width)
                y = int(landmark.y*frame_height)
                print(x,y)
                if id == 8:
                    cv2.circle(img =frame, center=(x,y), radius=10, color=(0,255,255))
                    index_x = screen_width/frame_width*x
                    index_y = screen_height/frame_height*y
                    pyautogui.moveTo(index_x, index_y)
                if id == 4:
                    cv2.circle(img =frame, center=(x,y), radius=10, color=(0,255,255))
                    thumb_x = screen_width/frame_width*x
                    thumb_y = screen_height/frame_height*y
                    if abs(index_y - thumb_y) < 15:
                        print('click')
                        print(abs(index_y - thumb_y))
                        pyautogui.click()
                        pyautogui.sleep(1)
                if id == 12:
                    cv2.circle(img =frame, center=(x,y), radius=10, color=(2,255,255))
                    scrool_x = screen_width/frame_width*x
                    scrool_y = screen_height/frame_height*y
                    if abs(index_y - scrool_y) < 15:
                        print('Scrool')
                        print(abs(index_y - scrool_y))
                        pyautogui.click(button='middle')
                if id == 16:
                    cv2.circle(img =frame, center=(x,y), radius=10, color=(2,255,255))
                    ri_x = screen_width/frame_width*x
                    ri_y = screen_height/frame_height*y
                    if abs(index_y - scrool_y) < 15:
                        print('right')
                        print(abs(scrool_y - ri_y))
                        pyautogui.click(button='right')

   cv2.imshow('Virtual Mouse', frame)
   cv2.waitKey(1)