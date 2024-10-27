from django.shortcuts import render
from .forms import UploadFileForm
from django.core.mail import send_mail
import pandas as pd


def handle_uploaded_file(file):
    df = pd.read_excel(file) if file.name.endswith('.xlsx') else pd.read_csv(file)
    summary = df.describe().to_string()
    return summary

def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            summary = handle_uploaded_file(request.FILES['file'])
            send_email(summary, request.FILES['file'].name)
            return render(request, 'summary.html', {'summary': summary})
    else:
        form = UploadFileForm()
    return render(request, 'upload.html', {'form': form})

def send_email(summary, filename):
    send_mail(
        f'Python Assignment - Your Name',
        summary,
        'your_email@example.com',
        ['tech@themedius.ai']
    )
