import json
from nlp import getDiseaseFromSymptom
from firebase import firebase

def getMessage(from_number, body, img_url):

    fb = firebase.FirebaseApplication("https://medicai-4e398.firebaseio.com/", None)
    data = fb.get('/Users', None)
    message = ""
    if from_number in data:
        if data[from_number]["current"] == "location":
            data[from_number]["current"] = "age"
            data[from_number]["location"] = body
            message = "The next thing we need to know is how old you are. Please enter your age."

        elif data[from_number]["current"] == "age":
            try:
                val = int(body)
                data[from_number]["age"] = body
                data[from_number]["current"] = "gender"
                message = "We need one last thing. Please enter your gender (M/F)."
            except:
                message = "Please enter an actual number. (Ex: 12, 73)"

        elif data[from_number]["current"] == "gender":
            message = "Thanks for registering on MedicAI! How can we help you today?"
            if body == "M" or "m":
                data[from_number]["current"] = "completed"
                data[from_number]["gender"] = "male"
            elif body == "F" or "f":
                data[from_number]["current"] = "completed"
                data[from_number]["gender"] = "female"
            else:
                message = "Please enter your gender as M (male) or F (female)"
        else:
            finalDisease = getDiseaseFromSymptom(body, from_number)

            if finalDisease == "":
                message = "We were unable to find a disease with those conditions. Try being more specific or upload a picture!"
            else:
                message = finalDisease

    else:
        print("asdasd")
        data[from_number] = {"current": "location"}
        message = "Hi there! Welcome to MedicAI. Before we can help you out, we're going to need a couple of things to achieve better results. Please enter your address."
    print(data)
    result = fb.put('', '/Users', data)
    return message

print(getMessage("5163123123", "Hello my name is", "asd"))