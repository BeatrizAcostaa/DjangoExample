from django.shortcuts import render
from django.http import HttpResponse
from .forms import BookingForm

def home(request):
    return HttpResponse("Welcome to Little Lemon!")

def booking_view(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'success.html', {'form': form})
    else:
        form = BookingForm()
    
    return render(request, 'booking.html', {'form': form})
