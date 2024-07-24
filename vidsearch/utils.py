from django.conf import settings


MINUTE_SECONDS = 60
HOUR_SECONDS = 60 * MINUTE_SECONDS

def seconds_to_time(seconds):
    seconds = int(seconds)

    hour = seconds // HOUR_SECONDS
    seconds -= HOUR_SECONDS * hour
    hour = '0' + str(hour) if len(str(hour)) < 2 else hour

    minute = seconds // MINUTE_SECONDS
    seconds -= MINUTE_SECONDS * minute
    minute = '0' + str(minute) if len(str(minute)) < 2 else minute

    seconds = '0' + str(seconds) if len(str(seconds)) < 2 else seconds

    return f'{hour}:{minute}:{seconds}'
        
def format_results(results, results_idx):
    results_formatted = []
    for result, idx in zip(results, results_idx):
        seconds = settings.CHUNK_SECONDS * idx
        time = seconds_to_time(seconds)
        results_formatted.append(f'{time} || {result}')

    return results_formatted
        
