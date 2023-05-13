from django.shortcuts import render
import socket

def index(request):
    domain_name = request.GET.get('domain_name')
    ip_address = None

    if domain_name:
        try:
            ip_address = socket.gethostbyname(domain_name)
        except socket.gaierror:
            pass

    return render(request, 'index.html', {'ip_address': ip_address})