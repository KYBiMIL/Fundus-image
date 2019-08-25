import os
import sys
import pandas as pd
import shutil

file = pd.read_excel("H:/labeling/label.xlsx")

p1 = "H:/labeling/kjh/sample/"
p2 = "H:/labeling/녹내장-진선영/녹내장(2013년)-진선영/"
p3 = "H:/labeling/녹내장-진선영/녹내장(2014년)-진선영/"

d = "H:/labeling/결과물/일반_Normal/"

for i in range(len(file)):

    name = file["name"][i]

    if name.startswith("C"):
        shutil.copy2(p1 + name + ".jpg", d + name + ".jpg")
    elif name.startswith("0"):
        shutil.copy2(p2 + name + ".jpg", d + name + ".jpg")
    elif name.startswith("V"):
        shutil.copy2(p3 + name + ".jpg", d + name + ".jpg")

