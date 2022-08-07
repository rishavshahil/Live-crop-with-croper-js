from django.shortcuts import render
from django.views import View
from .models import DemoUpload


class HomeView(View):
    template_name = 'index.html'
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

    def post(self, request, *args, **kwargs):
        image = request.FILES.get('photo')
        if image:
            upload = DemoUpload(image = image)
            upload.save()
        return render(request, self.template_name)



