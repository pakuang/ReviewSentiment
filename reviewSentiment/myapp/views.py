from django.shortcuts import render, HttpResponse
from .models import BusinessItem
from .sentiment import get_avg_sentiment, get_reviews

# Create your views here.
def home(request):
    items = BusinessItem.objects.all()
    return render(request, "home.html", {"buses": items})

def business(request):
    items = BusinessItem.objects.all()

    for item in items:
        reviews = get_reviews(item.yelp_url)
        if reviews:
            avg_sentiment = round(get_avg_sentiment(reviews),3)
            item.avg_sentiment = avg_sentiment
            item.save()

    return render(request, "business.html", {"buses": items})

def about(request):
    return render(request, "about.html")

def contact(request):
    return render(request, "contact.html")

