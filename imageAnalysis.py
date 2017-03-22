#IMPORT MODULES
import sys
import os
import pickle
if ".".join([str(x) for x in sys.version_info[:2]]) != "3.4":
	print("This script requires Python version 3.4. Relaunching now...")	 
	os.system('python3.4 main.py')

from sklearn import svm
from PIL import Image
import numpy as np
import warnings
import random

STANDARD_SIZE = (300, 172)

def flatten_image(img):
	"""
	takes in an (m, n) numpy array and flattens it
	into an array of shape (1, m * n)
	"""
	if len(img.shape) != 2 or img.shape[1] != 3:
		return "L"
	s = img.shape[0] * img.shape[1]
	img_wide = img.reshape(1, s)
	return img_wide[0]

def loadImage(filename):
	"""
	Given a filename, opens and loads the image
	"""
	img = Image.open(filename)
	img = img.resize(STANDARD_SIZE)
	img = list(img.getdata())
	img = np.array(img)
	return flatten_image(img)


#IGNORE WARNINGS
warnings.filterwarnings("ignore")

inputs = []
outputs = []

for fname in os.listdir('/Users/Avinash/Documents/chickenpox/')[:-4]:
	try:
		temp = loadImage("/Users/Avinash/Documents/chickenpox/" + fname)
		if temp != "L":
			inputs.append(temp)
			outputs.append(1)
	except:
		pass

print(len(outputs))
for fname in os.listdir('/Users/Avinash/Documents/nonchickenpox/')[:-4]:
	try:
		temp = loadImage("/Users/Avinash/Documents/nonchickenpox/" + fname)
		if temp != "L":
			inputs.append(temp)
			outputs.append(0)
	except:
		pass

print(len(inputs))
print(len(outputs))

X = np.array(inputs)
Y = np.array(outputs)
model = svm.SVC()
model.fit(X,Y)

with open('chickenpox.pkl', 'wb') as f:
	pickle.dump(model,f)


