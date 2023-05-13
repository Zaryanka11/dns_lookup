from django.shortcuts import render
import socket
from django.shortcuts import render

def home(request):
    if request.method == 'POST':
        domain = request.POST.get('domain', '')
        try:
            ip_address = socket.gethostbyname(domain)
        except socket.gaierror:
            ip_address = 'Не удалось найти IP-адрес для заданного домена.'

        context = {
            'domain': domain,
            'ip_address': ip_address
        }
        return render(request, 'dns_app/result.html', context)

    return render(request, 'dns_app/home.html')
