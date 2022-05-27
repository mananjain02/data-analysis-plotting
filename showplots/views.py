from django.http import Http404
from django.shortcuts import render
 
allplots = {
    "exploratory_data_analysis": [
        "../../static/showplots/plot 1.png",
        "../../static/showplots/plot 2.png",
        "../../static/showplots/plot 3.png",
        "../../static/showplots/plot 4.png",
        "../../static/showplots/plot 5.png",
        "../../static/showplots/plot 6.png",
        "../../static/showplots/plot 7.png",
        "../../static/showplots/plot 8.png",
        "../../static/showplots/plot 9.png",
        "../../static/showplots/plot 10.png"
    ],

    "price_prediction_linear_regression": [
        "../../static/showplots/plot 11.png",
        "../../static/showplots/plot 12.png"
    ],

    "k_means_clustering": [
    "../../static/showplots/plot 13.png",
    "../../static/showplots/plot 14.png",
    "../../static/showplots/plot 15.png",
    "../../static/showplots/plot 16.png",
    "../../static/showplots/plot 17.png",
    "../../static/showplots/plot 18.png",
    "../../static/showplots/plot 19.png",
    "../../static/showplots/plot 20.png",
    "../../static/showplots/plot 21.png",
    "../../static/showplots/plot 22.png",
    "../../static/showplots/plot 23.png",
    "../../static/showplots/plot 24.png",
    "../../static/showplots/plot 25.png"
]
}

# Create your views here.
def index(request, slug):
    try: 
        return render(request, 'showplots/index.html', {
            "page_title": slug,
            "plots": list(allplots[slug])
        })
    except:
        raise Http404

def starting_page(request):
    return render(request, 'showplots/starting_page.html', {
        "all_sections": list(allplots.keys())
    })