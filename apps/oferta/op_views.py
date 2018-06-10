from django.shortcuts import render

def oferta_list(request):
        return render(request, 'op/oferta/oferta/lista.html', {})
