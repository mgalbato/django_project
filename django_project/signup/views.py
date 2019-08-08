from django.shortcuts import render, redirect
from .models import City, Subscriber
from .related.helper import format_cities, deformat_city
from django.core.validators import validate_email
from django.core.exceptions import ValidationError


def home(request):
    context = {
        'cities': format_cities(City.objects.all()),
        'email_taken': False,
        'email_invalid': False
    }

    if request.method == 'POST':
        email_given = request.POST['email']
        loc_given = request.POST['city']

        if Subscriber.objects.filter(email= email_given).count() > 0: # email already exists
            context['email_taken'] = True
            return render(request, 'signup/home.html', context)
        else:
            try:
                validate_email(email_given)
            except ValidationError: # email is invalid
                context['email_invalid'] = True
                return render(request, 'signup/home.html', context)
            else: # email is valid
                loc_dict = deformat_city(loc_given)
                loc_obj = City.objects.filter(city= loc_dict['city'], state= loc_dict['state']).first()
                Subscriber(email= email_given, location= loc_obj).save()
                return redirect('signup-confirm')
    else:
        return render(request, 'signup/home.html', context)

def confirm(request):
    return render(request, 'signup/confirm.html')
