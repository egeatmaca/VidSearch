from django.shortcuts import render
from django.views.decorators.csrf import csrf_protect
from django.conf import settings
from vidsearch.services.youtube import download_audio
from vidsearch.services.speech_to_text import chunked_speech_to_text
from vidsearch.services.semantic_search import semantic_search
from vidsearch.utils import format_results
import os


@csrf_protect
def index(request):
    if request.method == 'GET':
        return render(request, 'index.html')
    elif request.method == 'POST':
        url = request.POST.get('url')
        query = request.POST.get('query')

        file_path = download_audio(url)

        texts = chunked_speech_to_text(file_path, interval_sec=settings.CHUNK_SECONDS)

        video_title = os.path.sep.join(
            file_path.split(os.path.sep)[-1].split('.')[:-1]
        )
        os.remove(file_path)
        
        results, results_idx = semantic_search(query, texts)
        results = format_results(results, results_idx)

        context = {
            'video_title': video_title,
            'query': query,
            'results': results
        }

        return render(request, 'index.html', context)