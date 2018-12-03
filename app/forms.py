from django import forms


class AddForm(forms.Form):
    num1 = forms.FloatField()
    num2 = forms.FloatField()


class DoubleForm(forms.Form):
    num1 = forms.FloatField()


class SubtractForm(forms.Form):
    num1 = forms.FloatField()
    num2 = forms.FloatField()


class MultThreeForm(forms.Form):
    x = forms.FloatField()
    y = forms.FloatField()
    z = forms.FloatField()


class EarningsForm(forms.Form):
    a = forms.IntegerField()
    b = forms.IntegerField()
    c = forms.IntegerField()


class BothForm(forms.Form):
    x = forms.BooleanField(required=False)
    y = forms.BooleanField(required=False)


class WalkOrDriveForm(forms.Form):
    miles = forms.FloatField()
    isNiceWeather = forms.BooleanField(required=False)
