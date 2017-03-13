import json
from nlp import getDiseaseFromSymptom
from firebase import firebase
from translation import bing

"""
Overall message function that decides what to return back to the user
Either gets data from user, returns symptom analysis, or restarts the user
"""


def getMessage(from_number, body, img_url):

    language_data = {'portuguese': 'pt', 'irish': 'ga', 'chinese': 'zh-CHS', 'danish': 'da', 'czech': 'cs',
                     'japanese': 'ja', 'spanish': 'es', 'urdu': 'ur', 'polish': 'pl', 'arabic': 'ar', 'swahili': 'sw',
                     'vietnamese': 'vi', 'german': 'de', 'hindi': 'hi', 'dutch': 'nl', 'korean': 'ko', 'swedish': 'sv',
                     'bulgarian': 'bg', 'latin': 'la', 'ukrainian': 'uk', 'lithuanian': 'lt', 'french': 'fr',
                     'russian': 'ru', 'thai': 'th', 'finnish': 'fi', 'filipino': 'tl', 'turkish': 'tr', 'greek': 'el',
                     'latvian': 'lv', 'english': 'en', 'italian': 'it'}

    # Initialize Firebase Application and get user data
    fb = firebase.FirebaseApplication("https://medicai-4e398.firebaseio.com/", None)
    data = fb.get('/Users', None)

    message = ""

    # Check to see if the user has used our app before
    if from_number in data:

        # Resets User Data
        if body == "R":
            data[from_number]["current"] = "location"
            result = fb.put('', '/Users', data)
            message = "Hi there! Welcome to MedicAI. Before we can help you out, we're going to need a couple of things to achieve better results. Please enter your address."
            return message

        if body.split(" ")[0].lower() == "language":
            data[from_number]["language"] = language_data[body.split(" ")[2].lower()]
            print(data[from_number]["language"])
            message = "Changed your language to " + body.split(" ")[2].lower() + "."
            result = fb.put('', '/Users', data)
            message = bing(message, dst=data[from_number]["language"])
            return message

        # Takes data as location, goes to age
        if data[from_number]["current"] == "location":
            data[from_number]["current"] = "age"
            data[from_number]["location"] = body
            message = "The next thing we need to know is how old you are. Please enter your age."

        # Takes data as age, goes to gender
        elif data[from_number]["current"] == "age":
            try:
                val = int(body)
                data[from_number]["age"] = body
                data[from_number]["current"] = "gender"
                message = "We need one last thing. Please enter your gender (M/F)."
            except:
                message = "Please enter an actual number. (Ex: 12, 73)"

        # Takes data as gender, now user can use application
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

        # Start getting symptom analysis from text
        else:
            finalDisease = getDiseaseFromSymptom(body, from_number)

            if finalDisease == "":
                message = "We were unable to find a disease with those conditions. Try being more specific or upload a picture!"
            else:
                message = finalDisease

    # If the user has never used our app, then we walk him through our intialization process
    else:
        data[from_number] = {"current": "location", "language": "es"}
        print(data)
        message = "Hi there! Welcome to MedicAI. Before we can help you out, we're going to need a couple of things to achieve better results. Please enter your address."

    # Save the new data back to firebase
    result = fb.put('', '/Users', data)
    print(message)
    message = bing(message, dst=data[from_number]["language"])
    return message