from rest_framework import viewsets
from .models import Sign
from .serializers import SignSerializer
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import SignForm
from django.conf import settings
import pytz
from django.utils.timezone import now


class SignViewSet(viewsets.ModelViewSet):
    queryset = Sign.objects.all()
    serializer_class = SignSerializer



def upload_sign(request):
    sa_time_zone = pytz.timezone('Africa/Johannesburg')  # Pretoria/Harare time zone

    if request.method == 'POST':
        form = SignForm(request.POST, request.FILES)
        if form.is_valid():
            sign = form.save(commit=False)
            sign.date_taken = now().astimezone(sa_time_zone)
            sign.last_updated = now().astimezone(sa_time_zone)
            sign.save()
            messages.success(request, 'Sign uploaded successfully!')
            return redirect('/')  # Redirect to home page
        else:
            messages.error(request, 'Failed to upload sign. Please check the form.')
    else:
        form = SignForm()

    return render(request, 'signs/upload.html', {'form': form, 'signs': Sign.objects.all()})