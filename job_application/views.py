from django.shortcuts import render
from .forms import ApplicationForm
from .models import Form
from django.contrib import messages
from django.core.mail import EmailMessage


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


            #Code to enter data in db
            Form.objects.create(first_name=first_name, last_name=last_name,
                                email=email, date=date, occupation=occupation)
            messages.success(request, "Application submitted successfully!")


            #Code to send an email
            message = f"Your job application form is submitted successfully! Thank you, {first_name}"
            email_message = EmailMessage("Form submission successful!", message, to=[email])
            email_message.send()

        else:
            print("Form is not valid")
            print(form.errors)

    else:
        form = ApplicationForm()
        print("GET request")

    return render(request, "index.html", {'form': form})
