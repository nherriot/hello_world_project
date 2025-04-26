from django.shortcuts import render


def hello_world(request):
    return render(request, 'hello_world.html', {'message': 'Hello World Nick!'})

