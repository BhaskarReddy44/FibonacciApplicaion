from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


from django.shortcuts import render
from django.http import HttpResponse

from fibonacciapp.models import Fibonacci
from django.views import View
import time


def fibonacci(number):
    if number < 2:
        return 1

    else:
        number_1 = 1
        number_2 = 1

        for number in range(2, number):
            value = number_1 + number_2
            number_1 = number_2
            number_2 = value

        return number_2


class FibonacciView(View):

    def get(self, request):

        num = request.GET.get('value')

        if num is None:
            return render(request, 'base.html')

        else:
            start_time = time.time()
            number = int(num)
            output = fibonacci(number)
            end_time = time.time() - start_time
            latency_time= str(end_time)[0:3]

            fibonacci_qs = Fibonacci.objects.create(
                number=number,
                output=output,
                latency=latency_time
            )
            fibonacci_qs.save()

            data = {
                'number': number,
                'output': output,
                'latency': latency_time
            }

            return render(request, 'base.html', data)


