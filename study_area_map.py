import geopandas as gpd
import matplotlib.pyplot as plt
from shapely.geometry import Polygon, Point

# 1. Create a sample study-area boundary near Guntur, Andhra Pradesh
study_area_polygon = Polygon([
    (80.42, 16.29),
    (80.46, 16.29),
    (80.46, 16.33),
    (80.42, 16.33),
    (80.42, 16.29)
])

study_area = gpd.GeoDataFrame(
    {"name": ["Study Area - Guntur"]},
    geometry=[study_area_polygon],
    crs="EPSG:4326"
)

# 2. Create sample locations within the study area
locations = gpd.GeoDataFrame(
    {
        "location": ["College", "Hospital", "Water body"],
        "type": ["Education", "Health", "Water"]
    },
    geometry=[
        Point(80.435, 16.315),
        Point(80.450, 16.305),
        Point(80.445, 16.325)
    ],
    crs="EPSG:4326"
)

# 3. Calculate area accurately in square kilometres
study_area_projected = study_area.to_crs("EPSG:32644")
area_sq_km = study_area_projected.geometry.area.iloc[0] / 1_000_000

print(f"Study area: {area_sq_km:.2f} sq. km")

# 4. Create the map
fig, ax = plt.subplots(figsize=(9, 8))

study_area.plot(
    ax=ax,
    facecolor="lightgreen",
    edgecolor="darkgreen",
    alpha=0.5,
    linewidth=2
)

locations.plot(
    ax=ax,
    color=["blue", "red", "cyan"],
    markersize=100,
    marker="o",
    edgecolor="black"
)

# 5. Add labels to sample locations
for x, y, label in zip(
    locations.geometry.x,
    locations.geometry.y,
    locations["location"]
):
    ax.annotate(
        label,
        xy=(x, y),
        xytext=(5, 5),
        textcoords="offset points",
        fontsize=10
    )

ax.set_title(
    f"Simple GIS Study Area Map — Guntur\nArea: {area_sq_km:.2f} sq. km",
    fontsize=14,
    fontweight="bold"
)

ax.set_xlabel("Longitude")
ax.set_ylabel("Latitude")
ax.grid(True, linestyle="--", alpha=0.5)

# 6. Save the map
plt.tight_layout()
plt.savefig("study_area_map.png", dpi=300)
plt.show()
