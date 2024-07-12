from django.shortcuts import render
from django.http import HttpRequest, JsonResponse
from .forms import TemplateForm
from django.views import View

def template_view(request):
    if request.method == "GET":
        return render(request, 'landing/index.html')
    if request.method == "POST":
        form = TemplateForm(request.POST)
        print(form)
        if form.is_valid():

            return JsonResponse({
                    'name': form.cleaned_data.get('name'),
                    'email': form.cleaned_data.get('email'),
                    'message': form.cleaned_data.get('message')
                })


class TemplView(View):

    def get(self, request):
            return render(request, 'landing/index.html')

    def post(self, request):
        form = TemplateForm(request.POST)
        print(form)
        if form.is_valid():
            x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
            if x_forwarded_for:
                ip = x_forwarded_for.split(',')[0]  # Получение IP
            else:
                ip = request.META.get('REMOTE_ADDR')  # Получение IP

            user_agent = request.META.get('HTTP_USER_AGENT')
            return JsonResponse({
                    'name': form.cleaned_data.get('name'),
                    'email': form.cleaned_data.get('email'),
                    'message': form.cleaned_data.get('message'),
                    'ip': ip,
                    'user_agent': user_agent
                }, json_dumps_params={
                'ensure_ascii': False,
                'indent': 4
            })
