import cv2
import mediapipe as mp
import time

class HandDetector:
    def __init__(self,mode=False,maxHands=2,detectionCon=0.5,trackCon=0.5):
        self.hands=mp.solutions.hands.Hands(
            static_image_mode=mode,
            max_num_hands=maxHands,
            min_detection_confidence=detectionCon,
            min_tracking_confidence=trackCon
        )
        self.mpDraw=mp.solutions.drawing_utils

    def findHands(self,img,draw=True):
        results=self.hands.process(cv2.cvtColor(img,cv2.COLOR_BGR2RGB))
        if draw and results.multi_hand_landmarks:
            for handLms in results.multi_hand_landmarks:
                self.mpDraw.draw_landmarks(img,handLms,mp.solutions.hands.HAND_CONNECTIONS)
        return img,results
    
    def findPosition(self,img,results,draw=True):
        lmList=[]
        if results.multi_hand_landmarks:
            h,w,_=img.shape
            for lm in results.multi_hand_landmarks[0].landmark:
                cx,cy=int(lm.x*w),int(lm.y*h)
                lmList.append([cx,cy])
                if draw:
                    cv2.circle(img,(cx,cy),5,(255,0,255),cv2.FILLED)
        return lmList

def main():
    pTime=0
    cap=cv2.VideoCapture(0)
    detector=HandDetector()
    while True:
        success,img=cap.read()
        if not success:
            break
        img,results=detector.findHands(img)
        lmList=detector.findPosition(img,results)
        if lmList:
            print(lmList[4])

        fps=1/(time.time()-pTime)
        pTime=time.time()
        cv2.putText(img,f'FPS: {int(fps)}',(10,70),cv2.FONT_HERSHEY_PLAIN,3,(255,0,255),3)
        cv2.imshow("Image",img)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
