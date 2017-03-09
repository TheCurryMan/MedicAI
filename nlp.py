from nltk.corpus import stopwords
from nltk.stem import *
from stemming.porter2 import stem
from DiseaseFinder import getPotentialDiseasesFromIds
import re

"""
Performs NLP on the body receieved to figure out the key symptoms in the user message
Lemmitization + Tokenization + Stemming -> Intersect data and map symptoms to ids

"""

def getDiseaseFromSymptom(message, number):

    user_input = message

    letters_only = re.sub("[^a-zA-Z]", " ", user_input)

    lower_case = letters_only.lower()x

    words = lower_case.split()

    words = [w for w in words if not w in stopwords.words("english")]

    stemmed_words = [stem(word) for word in words]

    symptoms = ['abdominal', 'pain', 'back', 'pain', 'chest', 'pain', 'earache', 'headache', 'chronic', 'pelvic', 'pain', 'toothache', 'ache', 'vaginal', 'pain', 'rectal', 'pain', 'dermatomal', 'pain', 'feel', 'chills', 'fever', 'paresthesia', 'numbness', 'tingling', 'electric', 'tweaks', 'light', 'headed', 'dizzy', 'dizzy', 'black', 'dizzy', 'room', 'spinning', 'around', 'mouth', 'dry', 'nauseated', 'sick', 'like', 'flu', 'like', 'vomit', 'short', 'breath', 'sleepy', 'sweaty', 'thirsty', 'tired', 'weak', 'breathe', 'normally', 'hear', 'normally', 'losing', 'hearing', 'sounds', 'loud', 'ringing', 'hissing', 'ears', 'move', 'one', 'side', 'arm', 'leg', 'pass', 'bowel', 'action', 'normally', 'pass', 'urine', 'normally', 'remember', 'normally', 'see', 'properly', 'blindness', 'blurred', 'vision', 'double', 'vision', 'sleep', 'normally', 'smell', 'things', 'normally', 'speak', 'normally', 'stop', 'passing', 'watery', 'bowel', 'actions', 'stop', 'scratching', 'stop', 'sweating', 'swallow', 'normally', 'taste', 'properly', 'walk', 'normally', 'write', 'normally', 'medical', 'symptoms', 'edit', 'list', 'incomplete', 'help', 'expanding', 'available', 'icd', 'codes', 'listed', 'codes', 'available', 'sign', 'symptom', 'code', 'underlying', 'condition', 'code', 'sign', 'used', 'general', 'cachexia', 'loss', 'appetite', 'weight', 'loss', 'weight', 'gain', 'dry', 'mouth', 'fatigue', 'malaise', 'asthenia', 'muscle', 'weakness', 'pyrexia', 'jaundice', 'pain', 'abdominal', 'pain', 'chest', 'pain', 'bruising', 'sx', 'epistaxis', 'tremor', 'convulsions', 'muscle', 'cramps', 'tinnitus', 'dizziness', 'vertigo', 'syncope', 'hypothermia', 'hyperthermia', 'discharge', 'bleeding', 'swelling', 'deformity', 'sweats', 'chills', 'shivering', 'neurological', 'psychological', 'acalculia', 'acrophobia', 'agnosia', 'agoraphobia', 'akathisia', 'akinesia', 'alexia', 'amusia', 'anhedonia', 'anomia', 'anosognosia', 'anxiety', 'apraxia', 'arachnophobia', 'ataxia', 'bradykinesia', 'cataplexy', 'chorea', 'claustrophobia', 'confusion', 'deliberate', 'self', 'harm', 'drug', 'overdose', 'depression', 'dysarthria', 'dysdiadochokinesia', 'dysgraphia', 'dystonia', 'euphoria', 'hallucination', 'headache', 'hemiballismus', 'ballismus', 'homicidal', 'ideation', 'insomnia', 'lhermitte', 'sign', 'electrical', 'sensation', 'shoots', 'back', 'arms', 'mania', 'paralysis', 'paranoia', 'persecution', 'paresthesia', 'phobia', 'see', 'list', 'phobias', 'prosopagnosia', 'sciatica', 'somnolence', 'suicidal', 'ideation', 'tic', 'tremor', 'ocular', 'amaurosis', 'fugax', 'amaurosis', 'blurred', 'vision', 'dalrymple', 'sign', 'double', 'vision', 'exophthalmos', 'mydriasis', 'miosis', 'nystagmus', 'gastrointestinal', 'anorexia', 'bloating', 'belching', 'blood', 'stool', 'melena', 'hematochezia', 'constipation', 'diarrhea', 'dysphagia', 'dyspepsia', 'flatulence', 'fecal', 'incontinence', 'haematemesis', 'nausea', 'odynophagia', 'proctalgia', 'fugax', 'pyrosis', 'rectal', 'malodor', 'steatorrhea', 'vomiting', 'cardiovascular', 'chest', 'pain', 'claudication', 'palpitation', 'tachycardia', 'bradycardia', 'arrhythmia', 'urologic', 'dysuria', 'hematuria', 'impotence', 'polyuria', 'retrograde', 'ejaculation', 'strangury', 'urinary', 'frequency', 'urinary', 'incontinence', 'urinary', 'retention', 'pulmonary', 'hypoventilation', 'hyperventilation', 'bradypnea', 'apnea', 'cough', 'dyspnea', 'hemoptysis', 'pleuritic', 'chest', 'pain', 'sputum', 'production', 'tachypnea', 'integumentary', 'abrasion', 'alopecia', 'anasarca', 'blister', 'edema', 'hirsutism', 'itching', 'laceration', 'paresthesia', 'rash', 'urticaria', 'obstetric', 'gynaecological', 'abnormal', 'vaginal', 'bleeding', 'bloody', 'show', 'preceding', 'onset', 'labour', 'painful', 'intercourse', 'pelvic', 'pain', 'infertility', 'labour', 'pains', 'vaginal', 'bleeding', 'early', 'pregnancy', 'miscarriage', 'vaginal', 'bleeding', 'late', 'pregnancy', 'vaginal', 'discharge', 'vaginismus']

    stemmed_sympyoms = ['abdomin', 'pain', 'back', 'pain', 'chest', 'pain', 'earach', 'headach', 'chronic', 'pelvic', 'pain', 'toothach', 'ach', 'vagin', 'pain', 'rectal', 'pain', 'dermatom', 'pain', 'feel', 'chill', 'fever', 'paresthesia', 'numb', 'tingl', 'electr', 'tweak', 'light', 'head', 'dizzi', 'dizzi', 'black', 'dizzi', 'room', 'spin', 'around', 'mouth', 'dri', 'nauseat', 'sick', 'like', 'flu', 'like', 'vomit', 'short', 'breath', 'sleepi', 'sweati', 'thirsti', 'tire', 'weak', 'breath', 'normal', 'hear', 'normal', 'lose', 'hear', 'sound', 'loud', 'ring', 'hiss', 'ear', 'move', 'one', 'side', 'arm', 'leg', 'pass', 'bowel', 'action', 'normal', 'pass', 'urin', 'normal', 'rememb', 'normal', 'see', 'proper', 'blind', 'blur', 'vision', 'doubl', 'vision', 'sleep', 'normal', 'smell', 'thing', 'normal', 'speak', 'normal', 'stop', 'pass', 'wateri', 'bowel', 'action', 'stop', 'scratch', 'stop', 'sweat', 'swallow', 'normal', 'tast', 'proper', 'walk', 'normal', 'write', 'normal', 'medic', 'symptom', 'edit', 'list', 'incomplet', 'help', 'expand', 'avail', 'icd', 'code', 'list', 'code', 'avail', 'sign', 'symptom', 'code', 'under', 'condit', 'code', 'sign', 'use', 'general', 'cachexia', 'loss', 'appetit', 'weight', 'loss', 'weight', 'gain', 'dri', 'mouth', 'fatigu', 'malais', 'asthenia', 'muscl', 'weak', 'pyrexia', 'jaundic', 'pain', 'abdomin', 'pain', 'chest', 'pain', 'bruis', 'sx', 'epistaxi', 'tremor', 'convuls', 'muscl', 'cramp', 'tinnitus', 'dizzi', 'vertigo', 'syncop', 'hypothermia', 'hyperthermia', 'discharg', 'bleed', 'swell', 'deform', 'sweat', 'chill', 'shiver', 'neurolog', 'psycholog', 'acalculia', 'acrophobia', 'agnosia', 'agoraphobia', 'akathisia', 'akinesia', 'alexia', 'amusia', 'anhedonia', 'anomia', 'anosognosia', 'anxieti', 'apraxia', 'arachnophobia', 'ataxia', 'bradykinesia', 'cataplexi', 'chorea', 'claustrophobia', 'confus', 'deliber', 'self', 'harm', 'drug', 'overdos', 'depress', 'dysarthria', 'dysdiadochokinesia', 'dysgraphia', 'dystonia', 'euphoria', 'hallucin', 'headach', 'hemiballismus', 'ballismus', 'homicid', 'ideat', 'insomnia', 'lhermitt', 'sign', 'electr', 'sensat', 'shoot', 'back', 'arm', 'mania', 'paralysi', 'paranoia', 'persecut', 'paresthesia', 'phobia', 'see', 'list', 'phobia', 'prosopagnosia', 'sciatica', 'somnol', 'suicid', 'ideat', 'tic', 'tremor', 'ocular', 'amaurosi', 'fugax', 'amaurosi', 'blur', 'vision', 'dalrympl', 'sign', 'doubl', 'vision', 'exophthalmo', 'mydriasi', 'miosi', 'nystagmus', 'gastrointestin', 'anorexia', 'bloat', 'belch', 'blood', 'stool', 'melena', 'hematochezia', 'constip', 'diarrhea', 'dysphagia', 'dyspepsia', 'flatul', 'fecal', 'incontin', 'haematemesi', 'nausea', 'odynophagia', 'proctalgia', 'fugax', 'pyrosi', 'rectal', 'malodor', 'steatorrhea', 'vomit', 'cardiovascular', 'chest', 'pain', 'claudic', 'palpit', 'tachycardia', 'bradycardia', 'arrhythmia', 'urolog', 'dysuria', 'hematuria', 'impot', 'polyuria', 'retrograd', 'ejacul', 'stranguri', 'urinari', 'frequenc', 'urinari', 'incontin', 'urinari', 'retent', 'pulmonari', 'hypoventil', 'hyperventil', 'bradypnea', 'apnea', 'cough', 'dyspnea', 'hemoptysi', 'pleurit', 'chest', 'pain', 'sputum', 'product', 'tachypnea', 'integumentari', 'abras', 'alopecia', 'anasarca', 'blister', 'edema', 'hirsut', 'itch', 'lacer', 'paresthesia', 'rash', 'urticaria', 'obstetr', 'gynaecolog', 'abnorm', 'vagin', 'bleed', 'bloodi', 'show', 'preced', 'onset', 'labour', 'pain', 'intercours', 'pelvic', 'pain', 'infertil', 'labour', 'pain', 'vagin', 'bleed', 'earli', 'pregnanc', 'miscarriag', 'vagin', 'bleed', 'late', 'pregnanc', 'vagin', 'discharg', 'vaginismus']

    no_duplicate_stemmed_symptoms = ['neck','dot','spot','sore', 'throat', 'hyperventil', 'code', 'help', 'edema', 'scratch', 'move', 'amusia', 'fecal', 'urinari', 'diarrhea', 'sleep', 'miscarriag', 'discharg', 'sleepi', 'convuls', 'onset', 'dyspnea', 'tire', 'gastrointestin', 'show', 'chorea', 'rash', 'sensat', 'vaginismus', 'hyperthermia', 'labour', 'black', 'under', 'stranguri', 'persecut', 'bradykinesia', 'dysphagia', 'ejacul', 'shoot', 'apnea', 'around', 'tinnitus', 'mydriasi', 'hiss', 'stop', 'dermatom', 'hypoventil', 'prosopagnosia', 'odynophagia', 'mania', 'vomit', 'walk', 'dyspepsia', 'bruis', 'loss', 'hematuria', 'like', 'rectal', 'edit', 'tachypnea', 'syncop', 'integumentari', 'list', 'cataplexi', 'malodor', 'pregnanc', 'lose', 'miosi', 'tic', 'alexia', 'side', 'vision', 'hallucin', 'vagin', 'flatul', 'anomia', 'weight', 'hemiballismus', 'back', 'infertil', 'sign', 'dysuria', 'see', 'paralysi', 'cachexia', 'ballismus', 'pass', 'proper', 'sciatica', 'arm', 'agoraphobia', 'depress', 'vertigo', 'paresthesia', 'constip', 'obstetr', 'stool', 'intercours', 'icd', 'earli', 'blur', 'claustrophobia', 'condit', 'gynaecolog', 'overdos', 'arrhythmia', 'sweati', 'ocular', 'acalculia', 'leg', 'late', 'asthenia', 'weak', 'akinesia', 'abras', 'tremor', 'impot', 'cough', 'bleed', 'anorexia', 'dysarthria', 'akathisia', 'abdomin', 'nausea', 'ach', 'paranoia', 'drug', 'malais', 'dri', 'thing', 'frequenc', 'sweat', 'confus', 'action', 'swallow', 'loud', 'blind', 'dalrympl', 'acrophobia', 'harm', 'hypothermia', 'claudic', 'feel', 'tweak', 'pulmonari', 'cramp', 'one', 'chronic', 'phobia', 'fatigu', 'urolog', 'ataxia', 'ring', 'urticaria', 'speak', 'urin', 'avail', 'use', 'earach', 'doubl', 'sputum', 'suicid', 'euphoria', 'breath', 'shiver', 'electr', 'nauseat', 'lacer', 'tachycardia', 'hemoptysi', 'headach', 'head', 'alopecia', 'bowel', 'muscl', 'deliber', 'fugax', 'sx', 'hear', 'gain', 'rememb', 'palpit', 'ear', 'spin', 'symptom', 'chill', 'sound', 'room', 'anosognosia', 'bloat', 'bradypnea', 'flu', 'proctalgia', 'anxieti', 'haematemesi', 'jaundic', 'neurolog', 'anasarca', 'hirsut', 'psycholog', 'retent', 'exophthalmo', 'retrograd', 'hematochezia', 'dizzi', 'cardiovascular', 'pelvic', 'general', 'dysgraphia', 'incomplet', 'anhedonia', 'amaurosi', 'thirsti', 'somnol', 'pyrosi', 'apraxia', 'pleurit', 'self', 'medic', 'deform', 'nystagmus', 'write', 'chest', 'preced', 'sick', 'belch', 'polyuria', 'appetit', 'lhermitt', 'smell', 'tingl', 'product', 'fever', 'pain', 'itch', 'normal', 'insomnia', 'swell', 'steatorrhea', 'wateri', 'dysdiadochokinesia', 'mouth', 'blood', 'numb', 'toothach', 'blister', 'expand', 'incontin', 'short', 'light', 'pyrexia', 'arachnophobia', 'bloodi', 'homicid', 'epistaxi', 'abnorm', 'dystonia', 'melena', 'bradycardia', 'tast', 'ideat', 'agnosia']

    disease_symptoms = {"Chicken Pox":[('blister', 1), ('scab',1), ('ulcer',1), ('dot', 3), ('spot', 3), ('fatigu', 1), ('fever',1), ('appetit',1), ('headach',1), ('itch',1), ('swell',1)], "Goitre": [('lump', 3), ('swell', 1), ('coughing',1), ('breath',1), ('throat', 3), ('neck', 3)]}

    actual_symptoms = set(stemmed_words).intersection(no_duplicate_stemmed_symptoms)

    id_symptoms = {133: 'Night cough', 136: 'Neck pain', 9: 'Headache', 10: 'Abdominal pain', 139: 'Cold sweats', 12: 'Pain in the limbs', 13: 'Sore throat', 14: 'Runny nose', 15: 'Cough', 16: 'Tiredness', 273: 'Dry eyes', 149: 'Hot flushes', 23: 'Weight gain', 153: 'Fast, deepened breathing', 28: 'Stuffy nose', 29: 'Shortness of breath', 30: 'Wheezing', 287: 'Eye pain', 33: 'Eye redness', 35: 'Lip swelling', 37: 'Palpitations', 140: 'Paralysis', 40: 'Increased thirst', 169: 'Swollen glands on the neck', 170: 'Cheek swelling', 44: 'Nausea', 45: 'Heartburn', 46: 'Burning in the throat', 175: 'Chills', 179: 'Stomach burning', 52: 'Sleeplessness', 181: 'Vomiting blood', 54: 'Reduced appetite', 56: 'weakness', 57: 'Going black before the eyes', 31: 'Chest tightness', 138: 'Sweating', 64: 'Sputum', 11: 'Fever', 73: 'Itching eyes', 75: 'Burning eyes', 76: 'Feeling of foreign body in the eye', 207: 'Dizziness', 211: 'Tears', 203: 'Pain on swallowing', 87: 'Earache', 92: 'Early satiety', 95: 'Sneezing', 96: 'Itching in the nose', 144: 'Unconsciousness, short', 101: 'Vomiting', 17: 'Chest pain', 104: 'Back pain', 235: 'Memory gap', 238: 'Anxiety', 112: 'Menstruation disorder', 114: 'Nervousness', 115: 'Tremor at rest', 244: 'Drooping eyelid', 248: 'Swollen glands in the armpits', 122: 'Hiccups', 123: 'Missed period', 124: 'Skin rash'}

    symptoms_having_ids = ['dizzi', 'weight', 'tired', 'feel', 'heartburn', 'back', 'menstruat', 'paralysi', 'skin', 'go', 'stomach', 'cold', 'miss', 'sleepless', 'eye', 'droop', 'earach', 'memori', 'nervous', 'hot', 'chest', 'lip', 'nausea', 'earli', 'headach', 'fever', 'pain', 'reduc', 'itch', 'swollen', 'burn', 'weak', 'stuffi', 'sneez', 'sore', 'hiccup', 'vomit', 'wheez', 'fast,', 'increas', 'tremor', 'cough', 'runni', 'chill', 'palpit', 'short', 'neck', 'sputum', 'tear', 'abdomin', 'cheek', 'dri', 'anxieti', 'sweat', 'night', 'unconsciousness,']

    symptom_to_id = {'dizzi': 207, 'weight': 23, 'tired': 16, 'feel': 76, 'heartburn': 45, 'back': 104, 'menstruat': 112, 'paralysi': 140, 'skin': 124, 'stomach': 179, 'sweat': 139, 'sleep': 52, 'eye': 33, 'droop': 244, 'earach': 87, 'memori': 235, 'nervous': 114, 'chest': 17, 'lip': 35, 'nausea': 44, 'earli': 92, 'headach': 9, 'fever': 11, 'appetit': 54, 'itch': 96, 'swollen': 169, 'burn': 46, 'weak': 56, 'stuffi': 28, 'sneez': 95, 'sore': 13, 'hiccup': 122, 'vomit': 181, 'wheez': 30, 'thirst': 40, 'tremor': 115, 'cough': 15, 'runni': 14, 'chill': 175, 'palpit': 37, 'neck': 136, 'sputum': 64, 'tear': 211, 'abdomin': 10, 'cheek': 170, 'dri': 273, 'anxieti': 238, 'sweat': 138, 'night': 133, 'unconsciousness,': 144}

    maxNum = 0.0
    final_disease = ""

    #Trying with the API

    the_real_symptoms_with_ids = list(set(symptoms_having_ids).intersection(stemmed_words))
    print(the_real_symptoms_with_ids)
    ids = []
    for i in the_real_symptoms_with_ids:
        ids.append(str(symptom_to_id[i]))
    return getPotentialDiseasesFromIds(ids, number)

"""
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
            maxNum = len(list_of_symptoms)




    return final_disease

"""
