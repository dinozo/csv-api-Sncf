import json

with open('stop_areas.json') as f:
  data = json.load(f)
print(json.dumps(data, indent = 4, sort_keys=True))


