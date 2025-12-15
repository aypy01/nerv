from django.shortcuts import render
from .forms import TitanicForm, IrisForm, Cifar10Form, SentimentsForm
from tensorflow.keras.models import load_model
import numpy as np
from PIL import Image
import tensorflow as tf
from keras.preprocessing.sequence import pad_sequences
from keras.datasets import imdb

# Load the Titanic model once at module level
titanic_model = load_model('nerv/models/titanic.keras')
iris_model=load_model('nerv/models/iris.keras')
cifar10_model=load_model('nerv/models/CIFAR10.keras')
sentiments_model=load_model('nerv/models/sentiments_biderectional.keras')

def index(request):
    return render(request, 'nerv/index.html')

def predict_titanic(request):
    prediction = None
    is_predicted = False

    github_link = "https://github.com/aypy01/tensorflow/blob/main/module-2.ipynb"

    if request.method == 'POST':
        form = TitanicForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            age = data['age']
            sibsp = data['sibsp']
            parch = data['parch']
            sex = data['sex']
            pclass = data['pclass']

            sex_female = 1 if sex == 1 else 0
            sex_male = 1 if sex == 0 else 0
            class_First = 1 if pclass == 1 else 0
            class_Second = 1 if pclass == 2 else 0
            class_Third = 1 if pclass == 3 else 0

            input_data = np.array([[age, sibsp, parch,
                                    sex_female, sex_male,
                                    class_First, class_Second, class_Third]])

            pred = titanic_model.predict(input_data)
            prediction = 'Survived' if pred[0][0] > 0.5 else 'Did not survive'

            is_predicted = True
    else:
        form = TitanicForm()

    return render(request, 'nerv/titanic.html', {
        'form': form,
        'prediction': prediction,
        'is_predicted': is_predicted,
        'github_link': github_link,
    })


    
def predict_iris(request):
    prediction = None
    github_link = "https://github.com/aypy01/tensorflow/blob/main/module-2.ipynb"

    if request.method == 'POST':
        form = IrisForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data

            # Extract form data
            sepal_length = data['sepal_length']
            sepal_width = data['sepal_width']
            petal_length = data['petal_length']
            petal_width = data['petal_width']

            # Create input in the exact same order as training
            input_data = np.array([[sepal_length , sepal_width, petal_length ,petal_width]])

            # Model prediction
            pred = iris_model.predict(input_data)
            class_idx = np.argmax(pred, axis=1)[0]
            classes = ['Setosa', 'Versicolor', 'Virginica']
            prediction = classes[class_idx]

    else:
        form = IrisForm()

    return render(request, 'nerv/iris.html', {
        'form': form,
        'prediction': prediction,
        'github_link': github_link,

    })

def predict_image(request):
    prediction = None
    github_link = "https://github.com/aypy01/tensorflow/blob/main/module-3.ipynb"


    if request.method == 'POST':
        form = Cifar10Form(request.POST, request.FILES)

        if form.is_valid():
            uploaded_image = form.cleaned_data['image']

            image = Image.open(uploaded_image).convert("RGB")
            w, h = image.size

            crop_size = min(w, h)
            left = (w - crop_size) // 2
            top = (h - crop_size) // 2
            right = left + crop_size
            bottom = top + crop_size
            image = image.crop((left, top, right, bottom))

            final_image = image.resize((32, 32))

            arr = np.array(final_image) / 255.0
            arr = arr.reshape(1, 32, 32, 3)

            pred = cifar10_model.predict(arr)
            class_idx = np.argmax(pred)

            labels = [
                'airplane', 'automobile', 'bird', 'cat', 'deer', 'dog',
                'frog', 'horse', 'ship', 'truck'
            ]

            prediction = labels[class_idx]

    else:
        form = Cifar10Form()

    return render(request, 'nerv/image_classification.html', {
        'form': form,
        'prediction': prediction,
        'github_link': github_link,

    })





def predict_sentiments(request):
    prediction = None
    github_link = "https://github.com/aypy01/tensorflow/blob/main/sentiments.ipynb"

    
    max_features = 20000      # embedding input_dim
    maxlen = 200
    index_from = 3            # IMDB uses 0,1,2 for PAD, START, OOV

    # 1️⃣ Load and TRIM vocabulary to size used during training
    raw_index = imdb.get_word_index()
    word_index = {w: idx + index_from for w, idx in raw_index.items()
                  if (idx + index_from) < max_features}

    if request.method == 'POST':
        form = SentimentsForm(request.POST)

        if form.is_valid():
            text = form.cleaned_data['text']
            tokens = text.lower().split()

            seq = []
            for word in tokens:
                seq.append(word_index.get(word, 2))  # 2 = OOV token

            padded = pad_sequences([seq], maxlen=maxlen)

            pred = sentiments_model.predict(padded)
            score = float(pred[0][0])

            prediction = "Positive" if score > 0.5 else "Negative"

    else:
        form = SentimentsForm()

    return render(request, 'nerv/sentiments.html', {
        'form': form,
        'prediction': prediction,
        'github_link': github_link,

    })


    

