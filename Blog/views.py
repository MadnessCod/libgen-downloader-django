from django.shortcuts import render
from .forms import UserInputForm
from .models import ScrapperData
from .scraper import main


def scrape_and_display(request):

    if request.method == 'POST':
        form = UserInputForm(request.POST)
        if form.is_valid():
            phrase = form.cleaned_data['phrase']
            scrape_data = main(phrase)
            for key, value in scrape_data.items():
                if key.startswith('data'):
                    ScrapperData.objects.create(
                        number=value[0],
                        author=value[1],
                        title=value[2],
                        publisher=value[3],
                        year=value[4],
                        page=value[5],
                        language=value[6],
                        size=value[7],
                        type=value[8],
                        path=value[9],
                    )
        else:
            form = UserInputForm()
    else:
        form = UserInputForm()

    return render(request, 'enter_phrase.html', {'form': form})
