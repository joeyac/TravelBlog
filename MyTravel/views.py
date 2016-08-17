from django.shortcuts import render
from ipware.ip import get_real_ip, get_ip, get_trusted_ip
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib import auth


def index_page(request):
    ip1 = get_ip(request, right_most_proxy=True)
    ip2 = get_real_ip(request, right_most_proxy=True)
    ip3 = get_trusted_ip(request, right_most_proxy=True)
    print(ip1, ip2, ip3)
    return render(request, "index.html")


def about_page(request):
    return render(request, 'about.html')


def login(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect(reverse('homepage'))
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return HttpResponseRedirect(reverse('homepage'))
        else:
            return render(request, 'index.html', {'message': 'Login Failed.'})
    else:
        raise ConnectionRefusedError


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('homepage'))
