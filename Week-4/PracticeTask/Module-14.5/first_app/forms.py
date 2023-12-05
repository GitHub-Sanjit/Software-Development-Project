from django import forms
from django.forms.widgets import NumberInput

import datetime

# Create your forms here.

BIRTH_YEAR_CHOICES = ["1980", "1981", "1982"]
FAVORITE_COLORS_CHOICES = [
    ("blue", "Blue"),
    ("green", "Green"),
    ("black", "Black"),
]


class ExampleForm(forms.Form):
    name = forms.CharField()
    comment = forms.CharField(widget=forms.Textarea)
    comment_2 = forms.CharField(widget=forms.Textarea(attrs={"rows": 3}))
    email = forms.EmailField()
    agree = forms.BooleanField()
    date = forms.DateField()
    birth_date = forms.DateField(widget=NumberInput(attrs={"type": "date"}))
    birth_year = forms.DateField(
        widget=forms.SelectDateWidget(years=BIRTH_YEAR_CHOICES)
    )
    value = forms.DecimalField()
    first_name = forms.CharField(initial="Your First Name")
    agree_2 = forms.BooleanField(initial=True)
    day = forms.DateField(initial=datetime.date.today)
    favorite_color = forms.ChoiceField(choices=FAVORITE_COLORS_CHOICES)
    favorite_color_2 = forms.ChoiceField(
        widget=forms.RadioSelect, choices=FAVORITE_COLORS_CHOICES
    )
    favorite_color_3 = forms.MultipleChoiceField(choices=FAVORITE_COLORS_CHOICES)
    favorite_color_4 = forms.MultipleChoiceField(
        widget=forms.CheckboxSelectMultiple, choices=FAVORITE_COLORS_CHOICES
    )

    # GeeksForGeeks forms fields

    title = forms.CharField()
    description = forms.CharField()
    first_name_2 = forms.CharField(max_length=200)
    last_name = forms.CharField(max_length=200)
    roll_number = forms.IntegerField(help_text="Enter 6 digit roll number")
    password = forms.CharField(widget=forms.PasswordInput())
