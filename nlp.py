from nltk.corpus import stopwords
from nltk.stem import *
from stemming.porter2 import stem
from DiseaseFinder import getPotentialDiseasesFromIds
import re
from nearestDoctor import getNearestDoctor
from locationBasedAnalysis import getLocations
import json

"""
Performs NLP on the body receieved to figure out the key symptoms in the user message
Lemmitization + Tokenization + Stemming -> Intersect data and map symptoms to ids

"""

def getDiseaseFromSymptom(message, number):

    user_input = message
    letters_only = re.sub("[^a-zA-Z]", " ", user_input)
    lower_case = letters_only.lower()
    words = lower_case.split()
    words = [w for w in words if not w in stopwords.words("english")]
    stemmed_words = [stem(word) for word in words]

    val = getDiseaseFromLocalValues(stemmed_words, number)
    if val != "":
        return val

    symptoms_having_ids = ['dizzi', 'weight', 'tired', 'feel', 'heartburn', 'back', 'menstruat', 'paralysi', 'skin', 'stomach', 'cold', 'miss', 'sleepless', 'eye', 'droop', 'earach', 'memori', 'nervous', 'hot', 'chest', 'lip', 'nausea', 'earli', 'headach', 'fever', 'reduc', 'itch', 'swollen', 'burn', 'weak', 'stuffi', 'sneez', 'sore', 'hiccup', 'vomit', 'wheez', 'fast,', 'increas', 'tremor', 'cough', 'runni', 'chill', 'palpit', 'short', 'neck', 'sputum', 'tear', 'abdomin', 'cheek', 'dri', 'anxieti', 'sweat', 'night', 'unconsciousness,']

    symptom_to_id = {'dizzi': 207, 'weight': 23, 'tired': 16, 'feel': 76, 'heartburn': 45, 'back': 104, 'menstruat': 112, 'paralysi': 140, 'skin': 124, 'stomach': 179, 'sweat': 139, 'sleep': 52, 'eye': 33, 'droop': 244, 'earach': 87, 'memori': 235, 'nervous': 114, 'chest': 17, 'lip': 35, 'nausea': 44, 'earli': 92, 'headach': 9, 'fever': 11, 'appetit': 54, 'itch': 96, 'swollen': 169, 'burn': 46, 'weak': 56, 'stuffi': 28, 'sneez': 95, 'sore': 13, 'hiccup': 122, 'vomit': 181, 'wheez': 30, 'thirst': 40, 'tremor': 115, 'cough': 15, 'runni': 14, 'chill': 175, 'palpit': 37, 'neck': 136, 'sputum': 64, 'tear': 211, 'abdomin': 10, 'cheek': 170, 'dri': 273, 'anxieti': 238, 'sweat': 138, 'night': 133, 'unconsciousness,': 144}

    the_real_symptoms_with_ids = list(set(symptoms_having_ids).intersection(stemmed_words))
    print(the_real_symptoms_with_ids)
    ids = []
    for i in the_real_symptoms_with_ids:
        ids.append(str(symptom_to_id[i]))
    return getPotentialDiseasesFromIds(ids, number)



def getDiseaseFromLocalValues(stemmed_words, number):

    no_duplicate_stemmed_symptoms = ['neck','dot','spot','sore', 'throat', 'hyperventil', 'code', 'help', 'edema', 'scratch', 'move', 'amusia', 'fecal', 'urinari', 'diarrhea', 'sleep', 'miscarriag', 'discharg', 'sleepi', 'convuls', 'onset', 'dyspnea', 'tire', 'gastrointestin', 'show', 'chorea', 'rash', 'sensat', 'vaginismus', 'hyperthermia', 'labour', 'black', 'under', 'stranguri', 'persecut', 'bradykinesia', 'dysphagia', 'ejacul', 'shoot', 'apnea', 'around', 'tinnitus', 'mydriasi', 'hiss', 'stop', 'dermatom', 'hypoventil', 'prosopagnosia', 'odynophagia', 'mania', 'vomit', 'walk', 'dyspepsia', 'bruis', 'loss', 'hematuria', 'like', 'rectal', 'edit', 'tachypnea', 'syncop', 'integumentari', 'list', 'cataplexi', 'malodor', 'pregnanc', 'lose', 'miosi', 'tic', 'alexia', 'side', 'vision', 'hallucin', 'vagin', 'flatul', 'anomia', 'weight', 'hemiballismus', 'back', 'infertil', 'sign', 'dysuria', 'see', 'paralysi', 'cachexia', 'ballismus', 'pass', 'proper', 'sciatica', 'arm', 'agoraphobia', 'depress', 'vertigo', 'paresthesia', 'constip', 'obstetr', 'stool', 'intercours', 'icd', 'earli', 'blur', 'claustrophobia', 'condit', 'gynaecolog', 'overdos', 'arrhythmia', 'sweati', 'ocular', 'acalculia', 'leg', 'late', 'asthenia', 'weak', 'akinesia', 'abras', 'tremor', 'impot', 'cough', 'bleed', 'anorexia', 'dysarthria', 'akathisia', 'abdomin', 'nausea', 'ach', 'paranoia', 'drug', 'malais', 'dri', 'thing', 'frequenc', 'sweat', 'confus', 'action', 'swallow', 'loud', 'blind', 'dalrympl', 'acrophobia', 'harm', 'hypothermia', 'claudic', 'feel', 'tweak', 'pulmonari', 'cramp', 'one', 'chronic', 'phobia', 'fatigu', 'urolog', 'ataxia', 'ring', 'urticaria', 'speak', 'urin', 'avail', 'use', 'earach', 'doubl', 'sputum', 'suicid', 'euphoria', 'breath', 'shiver', 'electr', 'nauseat', 'lacer', 'tachycardia', 'hemoptysi', 'headach', 'head', 'alopecia', 'bowel', 'muscl', 'deliber', 'fugax', 'sx', 'hear', 'gain', 'rememb', 'palpit', 'ear', 'spin', 'symptom', 'chill', 'sound', 'room', 'anosognosia', 'bloat', 'bradypnea', 'flu', 'proctalgia', 'anxieti', 'haematemesi', 'jaundic', 'neurolog', 'anasarca', 'hirsut', 'psycholog', 'retent', 'exophthalmo', 'retrograd', 'hematochezia', 'dizzi', 'cardiovascular', 'pelvic', 'general', 'dysgraphia', 'incomplet', 'anhedonia', 'amaurosi', 'thirsti', 'somnol', 'pyrosi', 'apraxia', 'pleurit', 'self', 'medic', 'deform', 'nystagmus', 'write', 'chest', 'preced', 'sick', 'belch', 'polyuria', 'appetit', 'lhermitt', 'smell', 'tingl', 'product', 'fever', 'pain', 'itch', 'normal', 'insomnia', 'swell', 'steatorrhea', 'wateri', 'dysdiadochokinesia', 'mouth', 'blood', 'numb', 'toothach', 'blister', 'expand', 'incontin', 'short', 'light', 'pyrexia', 'arachnophobia', 'bloodi', 'homicid', 'epistaxi', 'abnorm', 'dystonia', 'melena', 'bradycardia', 'tast', 'ideat', 'agnosia']

    disease_symptoms = {"Chicken Pox":[('blister', 1), ('scab',1), ('ulcer',1), ('dot', 3), ('spot', 3), ('fatigu', 1), ('fever',1), ('appetit',1), ('headach',1), ('itch',1), ('swell',1)], "Goitre": [('lump', 3), ('swell', 1), ('coughing',1), ('breath',1), ('throat', 3), ('neck', 3)]}

    actual_symptoms = set(stemmed_words).intersection(no_duplicate_stemmed_symptoms)

    maxNum = 0
    final_disease = ""

    for disease in disease_symptoms:
        values = [d for d in disease_symptoms[disease]]
        real_symptoms = []
        vals = []
        for i in values:
            real_symptoms.append(i[0])
            vals.append(i[1])
        list_of_symptoms = list(set(real_symptoms).intersection(actual_symptoms))
        value = sum([vals[real_symptoms.index(w)] for w in list_of_symptoms])
        if maxNum >= value:
            pass
        else:
            final_disease = disease
            maxNum = value

    if maxNum >= 4:
        finalData = ""
        finalData += "Name of disease: " + final_disease + "\n\n"
        calc = 80 + 2*(int(maxNum)-5)
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
    return ""