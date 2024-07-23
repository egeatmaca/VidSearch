from vidsearch.services.youtube import download_audio
from vidsearch.services.speech_to_text import chunked_speech_to_text
from vidsearch.services.semantic_search import semantic_search
import os
from time import time

if __name__ == '__main__':
    url = 'https://www.youtube.com/watch?v=7VYP_2t4CJw'
    query = 'open-source'

    start_time = time()
    file_path = download_audio(url)
    print(f'Download completed in {time()-start_time}s!')

    start_time = time()
    texts = chunked_speech_to_text(file_path)
    print(f'Speech to text completed in {time()-start_time}s!')
    
    start_time = time()
    search_results = semantic_search(query, texts)
    print(f'Semantic search completed in {time()-start_time}s!')

    os.remove(file_path)

    print(search_results)
