import glob
import cv2
#cv_img = []
#img_dir = "rj/" # Enter Directory of all images 
#data_path = os.path.join(img_dir,'*g')
#files = glob.glob(data_path)
i = 0 
for img in glob.glob("kanna/*.jpg"):
    n= cv2.imread(img)
    m = cv2.resize(n,(640,480))
    name = str(i)
    cv2.imwrite("kannan/"+name+".jpg",m)
    i=i+1
    #cv_img.append(n)`
