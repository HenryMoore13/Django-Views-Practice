from django.shortcuts import render
from django.views import View
from . import forms


class Add(View):
    def get(self, request):
        form = forms.AddForm(data=request.GET)
        if form.is_valid():
            num1 = form.cleaned_data['num1']
            num2 = form.cleaned_data['num2']
            answer = num1 + num2
            return render(request, 'app/add.html', {'answer': answer})
        else:
            return render(request, 'app/add.html')

    # def get(self, request):
    #     try:
    #         num1 = float(request.GET.get('num1'))
    #         num2 = float(request.GET.get('num2'))

    #     except:
    #         return render(request, 'app/add.html')
    #     else:
    #         answer = num1 + num2
    #         return render(request, 'app/add.html', {'answer': answer})


class Double(View):
    def get(self, request):
        form = forms.DoubleForm(data=request.GET)
        if form.is_valid():
            num1 = form.cleaned_data['num1']
            answer = num1 + num1
            return render(request, 'app/double.html', {'answer': answer})
        else:
            return render(request, 'app/double.html')
        # try:
        #     num1 = float(request.GET.get('num1'))
        # except:
        #     return render(request, 'app/double.html')
        # else:
        #     answer = num1 + num1
        #     return render(request, 'app/double.html', {'answer': answer})


class Subtract(View):
    def get(self, request):
        form = forms.SubtractForm(data=request.GET)
        if form.is_valid():
            num1 = form.cleaned_data['num1']
            num2 = form.cleaned_data['num2']
            answer = num1 - num2
            return render(request, 'app/subtract.html', {'answer': answer})
        else:
            return render(request, 'app/subtract.html')

    #     try:
    #         num1 = float(request.GET.get('num1'))
    #         num2 = float(request.GET.get('num2'))
    #     except:
    #         return render(request, 'app/subtract.html')
    #     else:
    #         answer = num1 - num2
    #         return render(request, 'app/subtract.html', {'answer': answer})


class MultThree(View):
    def get(self, request):
        form = forms.MultThreeForm(data=request.GET)
        if form.is_valid():
            x = form.cleaned_data['x']
            y = form.cleaned_data['y']
            z = form.cleaned_data['z']
            answer = (x * y) * z
            return render(request, 'app/multThree.html', {'answer': answer})
        else:
            return render(request, 'app/multThree.html')

        # try:
        #     num1 = float(request.GET.get('num1'))
        #     num2 = float(request.GET.get('num2'))
        #     num3 = float(request.GET.get('num3'))
        # except:
        #     return render(request, 'app/multThree.html')
        # else:
        #     answer = (num1 * num2) * num3
        #     return render(request, 'app/multThree.html', {'answer': answer})


class Earnings(View):
    def get(self, request):
        form = forms.EarningsForm(data=request.GET)
        if form.is_valid():
            a = form.cleaned_data['a']
            b = form.cleaned_data['b']
            c = form.cleaned_data['c']
            answer = (a * 15) + (b * 12) + (c * 9)
            return render(request, 'app/earnings.html', {'answer': answer})
        else:
            return render(request, 'app/earnings.html')
        # try:
        #     num1 = float(request.GET.get('num1'))
        #     num2 = float(request.GET.get('num2'))
        #     num3 = float(request.GET.get('num3'))
        # except:
        #     return render(request, 'app/earnings.html')
        # else:
        #     answer = (num1 * 15) + (num2 * 12) + (num3 * 9)
        #     return render(request, 'app/earnings.html', {'answer': answer})


class Both(View):
    def get(self, request):
        form = forms.BothForm(data=request.GET)
        if form.is_valid():
            x = form.cleaned_data['x']
            y = form.cleaned_data['y']
            if x and y:
                answer = 'true'
                return render(request, 'app/both.html', {'answer': answer})
            else:
                answer = 'false'
                return render(request, 'app/both.html', {'answer': answer})
        return render(request, 'app/both.html')

        # try:
        #     input1 = (request.GET.get('input1')).lower().strip()
        #     input2 = (request.GET.get('input2')).lower().strip()
        # except:
        #     return render(request, 'app/both.html')
        # else:
        #     if input1 and input2 == 'true':
        #         answer == 'true'


class WalkOrDrive(View):
    def get(self, request):
        form = forms.WalkOrDriveForm(data=request.GET)
        if form.is_valid():
            miles = form.cleaned_data['miles']
            isNiceWeather = form.cleaned_data['isNiceWeather']
            if miles <= .25 and isNiceWeather == True:
                answer = 'walk'
                return render(request, 'app/walkordrive.html',
                              {'answer': answer})
            else:
                answer = 'drive'
                return render(request, 'app/walkordrive.html',
                              {'answer': answer})
        else:
            return render(request, 'app/walkordrive.html')
