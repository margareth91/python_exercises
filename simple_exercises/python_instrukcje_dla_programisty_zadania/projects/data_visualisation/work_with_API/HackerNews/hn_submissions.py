import requests
from operator import itemgetter

# Wywolanie API i zachowanie odpowiedzi
url =  'https://hacker-news.firebaseio.com/v0/topstories.json'
r = requests.get(url)
print(f"Kod stanu: {r.status_code}")

# Przetworzenie informacji o kazdym artykule
submission_ids = r.json()
submission_dicts = []
for submission_id in submission_ids[:30]:
    # Przygotowanie oddzielnego wywolania API dla kazdego artykulu
    url = f"https://hacker-news.firebaseio.com/v0/item/{submission_id}.json"
    submission_r = requests.get(url)
    print(submission_r.status_code)
    response_dict = submission_r.json()

    submission_dict = {
        'title': response_dict['title'],
        'link': f"'http://news.ycombinator.com/item?id={submission_id}",
        'comments': response_dict.get('descendants', 0)
    }
    submission_dicts.append(submission_dict)

submission_dicts = sorted(submission_dicts, key=itemgetter('comments'), reverse=True)

for submission_dict in submission_dicts:
    print(f"\nTytul artykulu: {submission_dict['title']}")
    print(f"Lacze do dyskusji: {submission_dict['link']}")
    print(f"Liczba komentarzy: {submission_dict['comments']}")
    