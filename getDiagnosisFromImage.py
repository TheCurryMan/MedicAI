import pickle
from sklearn import svm
from PIL import Image
import numpy as np
import urllib2
from locationBasedAnalysis import getLocations
from nearestDoctor import getNearestDoctor
import json
import warnings
import io

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

def loadImage(image):
	"""
	Given a filename, opens and loads the image
	"""
	img = image
	img = img.resize(STANDARD_SIZE)
	img = list(img.getdata())
	img = np.array(img)
	return flatten_image(img)

def getImage(imageURL, number):

    warnings.filterwarnings("ignore")

    f = io.BytesIO(urllib2.urlopen(imageURL).read())
    im = Image.open(f)
    model = svm.SVC()
    with open('chickenpox.pkl', 'rb') as f:
        model = pickle.load(f)
    print(model.predict(loadImage(im)))[0]
    if(model.predict(loadImage(im)))[0] == 1:
        final_disease = "Chicken Pox"
        finalData = ""
        finalData += "Name of disease: " + final_disease + "\n\n"
        calc = 90
        if calc > 100:
            calc = 100
        finalData += "Likelihood: " + str(calc) + "%\n\n"
        if getLocations(final_disease, number) > 4:
            finalData += "Warning! We've detected a high number of " + str(
                final_disease) + " cases in your locality (" + str(
                getLocations(final_disease,
                             number)) + ") making the likelihood of this disease much higher." + "\n\n"
        with open('details.json') as data_file:
            data = json.load(data_file)
            finalData += data[final_disease]["TreatmentDescription"] + "\n"
        finalData += "\n" + getNearestDoctor(number)

        return finalData