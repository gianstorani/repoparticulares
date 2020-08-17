from django.shortcuts import render

def post_list(request):
    return render(request, 'sitio/post_list.html', {})