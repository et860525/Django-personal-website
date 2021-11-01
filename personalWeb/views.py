from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from django.conf import settings
from .forms import ContactForm

# Create your views here.
def home_page(request):
	return render(request, 'personalWeb/home.html')

def project_page(request):
	return render(request, 'personalWeb/project.html')

def contact_page(request):
	form = ContactForm()

	if request.method == 'POST':
		form = ContactForm(request.POST)
		if form.is_valid():
			# Let html transform to string, for email body.
			template = render_to_string(r'personalWeb/email_template.html', {
				'name': request.POST['name'],
				'email': request.POST['email'],
				'message': request.POST['message'],
			})
			
			email = EmailMessage(
				'MangoStudio來信',  # 電子郵件標題
				template,  # 電子郵件內容
				settings.EMAIL_HOST_USER,  # 寄件者
				['et860525@gmail.com']  # 收件者
            )

			email.send(fail_silently=False)
			return redirect("email_send_result")

		return redirect("home_page")

	return render(request, 'personalWeb/contact.html', {'form': form})

def email_send_result(request):	
	return render(request, 'personalWeb/email_send_result.html')

def about_page(request):
	return render(request, 'personalWeb/about.html')