from django.shortcuts import render, redirect
from .forms import ExcelUploadForm
from .models import Client
import pandas as pd
from django.core.mail import send_mail
from django.conf import settings

def upload_clients(request):
    if request.method == 'POST':
        form = ExcelUploadForm(request.POST, request.FILES)
        if form.is_valid():
            excel_file = request.FILES['file']
            df = pd.read_excel(excel_file)

            for _, row in df.iterrows():
                Client.objects.create(
                    name=row['Name'],
                    email=row['Email'],
                    service=row['Service'],
                    amount=row['Amount'],
                    date=row['Date']
                )
            return redirect('client_list')
    else:
        form = ExcelUploadForm()
    return render(request, 'invoice_app/upload.html', {'form': form})


def client_list(request):
    clients = Client.objects.all()
    return render(request, 'invoice_app/client_list.html', {'clients': clients})


def send_invoice(request, client_id):
    client = Client.objects.get(id=client_id)
    subject = f"Invoice for {client.service} - {client.date}"
    message = f"""
Hi {client.name},

This is a reminder that your invoice for {client.service} is ${client.amount}.
Please make the payment by {client.date}.

Thanks,
Your Company
"""
    send_mail(
        subject,
        message,
        settings.EMAIL_HOST_USER,
        [client.email],
        fail_silently=False,
    )
    return redirect('client_list')