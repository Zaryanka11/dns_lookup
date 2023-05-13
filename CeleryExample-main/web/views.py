from django.shortcuts import render
from .tasks import send_email_task
from .forms import EmailForm
from django.contrib import messages


def send_email_view(request):
    if request.method == 'POST':
        form = EmailForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            send_email_task.delay(
                email)
            return render(request, 'web/front.html', {'form': form, 'message': 'Отправлено успешно!', 'flag': True})
    else:
        form = EmailForm()
    return render(request, 'web/front.html', {'form': form, 'flag': False})
