from django.shortcuts import render
from .forms import NumberF  # corrected import statement

def max_number(request):
    if request.method == 'POST':
        form = NumberForm(request.POST)
        if form.is_valid():
            numbers = form.cleaned_data.get('numbers')
            maximum = max(numbers)
            return render(request, 'maxnumber/result.html', {'maximum': maximum})
    else:
        form = NumberForm()
    return render(request, 'maxnumber/number_form.html', {'form': form})

from django.http import HttpResponse

def max_number(request):
    numbers = [10, 20, 30, 40, 50]  # Example numbers, you can replace them with your own input
    maximum = max(numbers)
    return HttpResponse(f"The maximum number is: {maximum}")

