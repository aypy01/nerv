from django import forms

class TitanicForm(forms.Form):
    PCLASS_CHOICES = [
        (1, '1st Class'),
        (2, '2nd Class'),
        (3, '3rd Class'),
    ]
    SEX_CHOICES = [
        (0, 'Male'),
        (1, 'Female'),
    ]

    pclass = forms.TypedChoiceField(
        choices=PCLASS_CHOICES,
        label='Passenger Class',
        coerce=int
    )
    sex = forms.TypedChoiceField(
        choices=SEX_CHOICES,
        label='Sex',
        coerce=int
    )
    age = forms.FloatField(label='Age', min_value=0,widget=forms.NumberInput(attrs={
        'placeholder': 'Input the Age'}))
    sibsp = forms.IntegerField(label='Siblings/Spouses Aboard', min_value=0,
    widget=forms.NumberInput(attrs={
        'placeholder': 'Number of Siblings/Spouses abroad'
    }))
    parch = forms.IntegerField(label='Parents/Children Aboard', min_value=0,widget=forms.NumberInput(attrs={
        'placeholder': 'Number Parents/Children Abroad'
    }))

    def clean(self):
        cleaned_data = super().clean()
        return cleaned_data
class IrisForm(forms.Form):
    sepal_length = forms.FloatField(label='Sepal Length', min_value=0,widget=forms.NumberInput(attrs={
        'placeholder': 'Input Sepal length in centimeters(cm)'
    }))
    sepal_width = forms.FloatField(label='Sepal Width', min_value=0,widget=forms.NumberInput(attrs={
        'placeholder': 'Input Sepal width in centimeters(cm)'
    }))
    petal_length = forms.FloatField(label='Petal Length',  min_value=0,widget=forms.NumberInput(attrs={
        'placeholder': 'Input Petal length in centimeters(cm)'
    }))
    petal_width = forms.FloatField(label='Petal Width', min_value=0, widget=forms.NumberInput(attrs={
        'placeholder': 'Input Petal Width in centimeters(cm)'
    }))
    
    

    def clean(self):
        cleaned_data = super().clean()
        return cleaned_data 

class Cifar10Form(forms.Form):
    image = forms.ImageField(label="Upload an image")

    def clean(self):
        cleaned_data = super().clean()
        return cleaned_data 

class SentimentsForm(forms.Form):
    text = forms.CharField(
        widget=forms.Textarea(attrs={
            'rows': 5,
            'placeholder': "Start Yapping here"
        })
    )

    def clean_text(self):
        data = self.cleaned_data["text"]

        # Remove accidental tuple/whitespace issues
        if isinstance(data, tuple):
            data = " ".join(data)

        data = data.strip()

        return data
