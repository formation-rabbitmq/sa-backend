from django.shortcuts import render

from .models import Sentiment


def sentiment(request):
	if request.method == "POST":
		Sentiment.objects.create(message=request.POST["message"])
		success = True

	return render(request, "sentiment.html", locals())
