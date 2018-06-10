from django.shortcuts import render

def PulpitView(request):
        return render(request, 'op/pulpit.html', {})
