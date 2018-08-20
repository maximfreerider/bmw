from django.shortcuts import render
from . import forms


def cars(request):
    name = "BMW m3"
    current_day = "13.05.2017"
    form = forms.UsersForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        print(form)
        print(form.cleaned_data)
        data = form.cleaned_data

        print(data["name"])

        new_1form = form.save()

    return render(request, 'cars/cars.html', locals())
