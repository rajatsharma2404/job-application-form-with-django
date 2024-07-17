from django.shortcuts import render
from .forms import ApplicationForm
from .models import Form
from django.contrib import messages


def index(request):
    if request.method == "POST":
        form = ApplicationForm(request.POST)
        print("Form submitted")

        if form.is_valid():
            print("Form is valid")
            first_name = form.cleaned_data["first_name"]
            last_name = form.cleaned_data["last_name"]
            email = form.cleaned_data["email"]
            date = form.cleaned_data["date"]
            occupation = form.cleaned_data["employment"]

            Form.objects.create(first_name=first_name, last_name=last_name,
                                email=email, date=date, occupation=occupation)
            messages.success(request, "Application submitted successfully!")

        else:
            print("Form is not valid")
            print(form.errors)

    else:
        form = ApplicationForm()
        print("GET request")

    return render(request, "index.html", {'form': form})
