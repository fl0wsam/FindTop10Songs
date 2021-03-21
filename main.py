import json

def _decode(o):
    # Note the "unicode" part is only for python2
    if isinstance(o, str) :
        try:
            return int(o)
        except ValueError:
            return o
    elif isinstance(o, dict):
        return {k: _decode(v) for k, v in o.items()}
    elif isinstance(o, list):
        return [_decode(v) for v in o]
    else:
        return o

with open('/home/saman/Desktop/songs.json') as f:
    songs = json.load(f, object_hook=_decode)

likes = []
rates = []
weight = []
names = []

for i in songs['details']:
    names.append(i['name'])
    likes.append(i['likes'])
    rates.append(i['rate'])

for j in range(len(names)):
    weight.append((int(likes[j]) / int(max(likes)) * 10) + int(rates[j]))

print(sorted(zip(weight, names), reverse=True)[:10])



