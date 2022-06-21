from django.shortcuts import render
from random import sample


def generate_numbers(num):
    return sample(range(1, 10), 4)


secret_nums = generate_numbers(4)
game_history = []


def game_page(request):
    if request.method == 'GET':
        return render(request, 'input_form.html')
    else:
        user_input = {
            'numbers': request.POST.get('numbers')
        }
        if user_input['numbers']:
            pass
        else:
            output = "Error! No input! (Enter 4 unique numbers in range 1 and 9)"
        context = {
            'numbers': user_input['numbers'],
            'message': output
        }
        return render(request, 'input_form.html', context)


