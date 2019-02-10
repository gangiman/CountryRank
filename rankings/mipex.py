import requests
import json


def get_mipex():
    headers = {
        'Accept': 'application/json, text/plain, */*',
        'Referer': 'http://www.mipex.eu/play/%7B%7BexportIframeSrc%7D%7D',
        'X-Requested-With': 'XMLHttpRequest',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36',
    }
    params = (
        ('filters[13][0]', '826'),
        ('filters[17][0]', '1215'),
        ('groupBy', '1'),
        ('charttype', 'map'),
    )

    response = requests.get('http://www.mipex.eu/data/', headers=headers, params=params)
    return json.loads(response.content)

data = get_mipex()
# response = requests.get('http://www.mipex.eu/data/?filters\[13\]\[0\]=826&filters\[17\]\[0\]=1215&groupBy=1&charttype=map', headers=headers)

