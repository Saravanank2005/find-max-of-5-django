from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .forms import NumberForm

def find_max(request):
    if request.method == 'POST':
        form = NumberForm(request.POST)
        if form.is_valid():
            numbers = [int(num) for num in form.cleaned_data['numbers'].split(',')]
            maximum = max(numbers)
            return render(request, 'result.html', {'maximum': maximum})
    else:
        form = NumberForm()
    return render(request, 'number_form.html', {'form': form})

from django.http import HttpResponse

def max_number(request):
    numbers = [10, 20, 30, 40, 50]  # Example numbers, you can replace them with your own input
    maximum = max(numbers)
    return HttpResponse(f"The maximum number is: {maximum}")

