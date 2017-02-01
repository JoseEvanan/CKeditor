from django.shortcuts import render
from django.views import generic
from django.http import JsonResponse
from equation.models import TextEquation

# Create your views here.
class SaveEquation(generic.View):
	def get(self, request):
		return render(request, 'equation/prueba.html')


class AjaxSaveData(generic.View):
	def get(self, request):
		print('ewewewewewew')
		head = request.GET['head']
		eq = request.GET['equation']

		print(head + ' ' + eq)

		quest = TextEquation(head=head, equation=eq)
		quest.save()

		#return JsonResponse({'head': str(quest.head), 'equation': str(quest.equation)})
		return JsonResponse({'head': 'qwe'})


class AjaxGetData(generic.View):
	def get(self, request):

		questions = TextEquation.objects.last()
		print(questions)

		return JsonResponse({'questions': questions})

class AjaxUpload(generic.View):
	def get(self, request,  *args, **kwargs):
		print("Upload get")
		print(kwargs)

	def post(self, request,  *args, **kwargs):
		print("Upload post")
		print(args)
		print(kwargs)

		return JsonResponse({'questions': 'True'})

class AjaxBrowser(generic.View):
	def get(self, request,  *args, **kwargs):
		print("browser get")
		print(kwargs)

	def post(self, request,  *args, **kwargs):
		print("browser post")
		print(kwargs)

		return JsonResponse({'questions': 'True'})

