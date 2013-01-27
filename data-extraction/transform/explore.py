import json
catalog = json.slurps("catalog.json")
data = catalog[u'data']

positions = []
for top in data:
  for index, value in enumerate(top):
    if isinstance(value, basestring):
      print index
      print value






