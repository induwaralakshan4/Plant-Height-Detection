import cv2
import numpy as np

list=('#plants/D5.png','#plants/D6.png','#plants/D7.png','#plants/D8.png','#plants/D9.png','#plants/D10.png','#plants/D11.png','#plants/D12.png','#plants/D13.png','#plants/D14.png')

for i in range(len(list)):
    
    imgs=cv2.imread(list[i])
    height,width=imgs.shape[0:2]
    img=cv2.resize(imgs,(int(width/2),int(height/2)))
    hsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    
    lower_color=np.array((23,32,111))
    upper_color=np.array((80,255,255))
    
    msk=cv2.inRange(hsv,lower_color,upper_color)
    res=cv2.bitwise_and(img,img,mask=msk)
    contours,hierarchy=cv2.findContours(msk,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    def px_to_cm(pixels: float, dpi: float = 96) -> float:
        return pixels * 2.54 / dpi
    for cnt in contours:
        area=cv2.contourArea(cnt)
        #print(area)
        if area>250:
            #cv2.drawContours(img,[cnt],-1,(0,255,255),1)
            if area>2000:
                x,y,w,h=cv2.boundingRect(cnt)
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
                cv2.circle(img,(int(x+w/2),y),10,(0,255,0),-1)
                cv2.circle(img,(int(x+w/2),y+h),10,(0,255,0),-1)
                cm = px_to_cm(h)
                c=round(cm, 2)
                cv2.putText(img,"Height: "+str(c)+"cm",(x+w,y+h),cv2.FONT_HERSHEY_SIMPLEX,0.75,(255,255,255),2)
            if area>200 and i<5:
                x,y,w,h=cv2.boundingRect(cnt)
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
                cv2.circle(img,(int(x+w/2),y),10,(0,255,0),-1)
                cv2.circle(img,(int(x+w/2),y+h),10,(0,255,0),-1)
                cm = px_to_cm(h)
                c=round(cm, 2)
                cv2.putText(img,"Height: "+str(c)+"cm",(x+w,y+h),cv2.FONT_HERSHEY_SIMPLEX,0.75,(255,255,255),2)
        
        
    cv2.imshow("live",img)
    cv2.waitKey(700)
cv2.destroyAllWindows()
