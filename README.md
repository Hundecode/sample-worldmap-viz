# sample-worldmap-viz
Visualization of samples on a world map

# Workflow
## Virtual Environment
```bash
python3 -m venv venv
```

## Activate (macOS/Linux)
```bash
source venv/bin/activate
```

## Jetzt innerhalb der Umgebung installieren:
```bash
pip3 install geopandas matplotlib pandas
```

## edit file
edit the data in worldmap.py
e.g.
```python
data = {
    'country': [
        'Netherlands', 'United States of America', 'Germany', 'Canada', 'Brazil',
        'Finland', 'Costa Rica', 'United Kingdom', 'Sweden',
        'Nigeria', 'Argentina'
    ],
    'count': [11, 11, 9, 3, 2, 2, 1, 2, 1, 1, 1]  # UK = England + UK (unspez.)
}
```

## run script
```bash
python3 worldmap.py
```

## after running the script
```bash
deactivate
```