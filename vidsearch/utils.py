from django.conf import settings


MINUTE_SECONDS = 60
HOUR_SECONDS = 60 * MINUTE_SECONDS

def seconds_to_time(seconds):
    hour = seconds // HOUR_SECONDS
    seconds -= HOUR_SECONDS * hour

    minute = seconds // MINUTE_SECONDS
    seconds -= MINUTE_SECONDS * minute

    return f'{hour}:{minute}:{seconds}'
        
def format_results(url, results, results_idx):
    results_formatted = []
    for result, idx in zip(results, results_idx):
        seconds = settings.CHUNK_SECONDS * idx
        time = seconds_to_time(seconds)
        results_formatted.append(f'{time} || {result}')

    return results_formatted
        
