import geopandas as gpd
import matplotlib.pyplot as plt
import pandas as pd
from pathlib import Path

script_dir = Path(__file__).resolve().parent
shapefile_path = script_dir / "ne_110m_admin_0_countries.shp"


# data
data = {
    'country': [
        'Netherlands', 'United States of America', 'Germany', 'Canada', 'Brazil',
        'Finland', 'Costa Rica', 'United Kingdom', 'Sweden',
        'Nigeria', 'Argentina'
    ],
    'count': [11, 11, 9, 3, 2, 2, 1, 2, 1, 1, 1]  # UK = England + UK (unspez.)
}

# DataFrame
df = pd.DataFrame(data)

# Load World Map
world = gpd.read_file(shapefile_path)

# Merge
merged = world.merge(df, how='left', left_on='NAME', right_on='country')

# Plot
fig, ax = plt.subplots(figsize=(15, 10))
merged.plot(
    column='count',
    cmap='OrRd',
    linewidth=0.8,
    ax=ax,
    edgecolor='0.8',
    legend=True,
    missing_kwds={
        "color": "lightgrey",
        "label": "Keine Daten"
    }
)

plt.title("Verteilung der Stichprobe nach Ländern", fontsize=16)
ax.axis('off')

# Speichern
plt.savefig("verteilung_stichprobe.png", dpi=300, bbox_inches='tight')
plt.show()