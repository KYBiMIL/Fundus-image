import os
import sys
import numpy as np
import cv2
import glob
from PIL import Image
import PIL

p = "./g_glaucoma/"

# images = [cv2.imread(file) for file in glob.glob(p+"*.jpg")]
list = [os.path.join(dirpath, f) for dirpath, dirnames, files in os.walk(p) for f in files if all(s in f for s in ['.jpg'])]
list.sort()


side = []
f_side = []
for i, l in enumerate(list): # l = list[i]
	img = cv2.imread(l)
	g = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
	res = cv2.resize(g,(250,250))

	h = g.shape[0]
	w = g.shape[1]
	_, max_val, _, max_loc = cv2.minMaxLoc(g)	
	#cv2.circle(res,max_loc, 5,(255,0,0),-1)
		
	if max_loc[0]<1600:
		side.append('l')
		f_side.append(l + "                l")
	else:
		side.append('r')	
		f_side.append(l + "                r")

f = open("./g_glaucoma_fside.txt",'w')
s = open("./g_glaucoma_side.txt","w")	
for lr in f_side:
	f.write(lr+'\n')
for flr in side:
	s.write(flr+'\n')
f.close()
s.close()

	
	#print(l)
	#print(w/2,h/2, max_loc)
	#cv2.imshow("MAX",res)
	#cv2.waitKey(0)
	#cv2.destroyAllWindows()

