from re import template
import cv2 
list_names=[]

#reading the data in the txt file
def clean():
    with open("data.txt") as f:
        for line in f:
            list_names.append(line.strip())

def certificate():
    for name in list_names:
        template = cv2.imread("template.png")
        cv2.putText(template,name,(236,372),cv2.FONT_HERSHEY_SIMPLEX,0.5,(0,0,255),1,cv2.LINE_AA)
        cv2.putText(template,"ANKSHALA",(246,447),cv2.FONT_HERSHEY_SIMPLEX,0.5,(0,0,255),1,cv2.LINE_AA)
        cv2.putText(template,"19",(336,484),cv2.FONT_HERSHEY_SIMPLEX,0.5,(0,0,255),1,cv2.LINE_AA)
        cv2.putText(template,"09",(398,484),cv2.FONT_HERSHEY_SIMPLEX,0.5,(0,0,255),1,cv2.LINE_AA)
        cv2.putText(template,"2022",(460,484),cv2.FONT_HERSHEY_SIMPLEX,0.5,(0,0,255),1,cv2.LINE_AA)
        cv2.imwrite(f'generated_certificate/{name}.png',template)

clean()
certificate()