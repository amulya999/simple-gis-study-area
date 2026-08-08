"""Visualization module for maps and coverage analysis."""

import geopandas as gpd
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import Rectangle
import folium
from folium.plugins import HeatMap
import os
from config import (
    OUTPUT_DIR,
    MAP_DPI,
    MAP_FIGSIZE,
    INFRA_COLORS,
    CRS_WGS84,
    STUDY_AREA_BOUNDS
)


def create_output_directory():
    """Create output directory if it doesn't exist."""
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)
        print(f"✅ Created output directory: {OUTPUT_DIR}")


def create_static_map(study_area, infrastructure_gdf, buffer_gdf):
    """
    Create a static map showing infrastructure locations and buffers.
    Saves as PNG.
    """
    create_output_directory()
    
    fig, ax = plt.subplots(figsize=MAP_FIGSIZE)
    
    # Plot study area
    study_area.plot(
        ax=ax,
        facecolor="lightyellow",
        edgecolor="darkblue",
        alpha=0.3,
        linewidth=2,
        label="Study Area"
    )
    
    # Plot buffers by type
    for infra_type in buffer_gdf['type'].unique():
        type_buffers = buffer_gdf[buffer_gdf['type'] == infra_type]
        type_buffers.plot(
            ax=ax,
            facecolor=INFRA_COLORS.get(infra_type, "gray"),
            alpha=0.15,
            edgecolor=INFRA_COLORS.get(infra_type, "gray"),
            linewidth=1
        )
    
    # Plot infrastructure locations
    for infra_type in infrastructure_gdf['type'].unique():
        type_infra = infrastructure_gdf[infrastructure_gdf['type'] == infra_type]
        type_infra.plot(
            ax=ax,
            color=INFRA_COLORS.get(infra_type, "black"),
            markersize=150,
            marker="o",
            edgecolor="black",
            linewidth=1.5,
            label=infra_type.replace("_", " ").title()
        )
        
        # Add labels
        for idx, row in type_infra.iterrows():
            ax.annotate(
                row['name'],
                xy=(row.geometry.x, row.geometry.y),
                xytext=(5, 5),
                textcoords="offset points",
                fontsize=9,
                bbox=dict(boxstyle="round,pad=0.3", facecolor="white", alpha=0.7)
            )
    
    ax.set_title(
        "Infrastructure Accessibility Map\nGuntur, Andhra Pradesh",
        fontsize=16,
        fontweight="bold",
        pad=20
    )
    ax.set_xlabel("Longitude", fontsize=12)
    ax.set_ylabel("Latitude", fontsize=12)
    ax.grid(True, linestyle="--", alpha=0.4)
    ax.legend(loc="upper right", fontsize=10)
    
    plt.tight_layout()
    output_path = os.path.join(OUTPUT_DIR, "infrastructure_accessibility_map.png")
    plt.savefig(output_path, dpi=MAP_DPI, bbox_inches="tight")
    print(f"✅ Static map saved: {output_path}")
    plt.close()


def create_interactive_map(infrastructure_gdf, buffer_gdf, study_area):
    """
    Create an interactive Folium map.
    Saves as HTML.
    """
    create_output_directory()
    
    # Calculate center of study area
    bounds = STUDY_AREA_BOUNDS
    center_lat = (bounds["north"] + bounds["south"]) / 2
    center_lon = (bounds["east"] + bounds["west"]) / 2
    
    # Create base map
    m = folium.Map(
        location=[center_lat, center_lon],
        zoom_start=12,
        tiles="OpenStreetMap"
    )
    
    # Add study area boundary
    for idx, row in study_area.iterrows():
        folium.GeoJson(
            data=row.geometry,
            style_function=lambda x: {
                'color': 'blue',
                'weight': 2,
                'opacity': 0.5
            }
        ).add_to(m)
    
    # Add infrastructure locations
    for idx, row in infrastructure_gdf.iterrows():
        color = INFRA_COLORS.get(row['type'], 'gray')
        folium.CircleMarker(
            location=[row.geometry.y, row.geometry.x],
            radius=8,
            popup=f"<b>{row['name']}</b><br>Type: {row['type'].replace('_', ' ').title()}",
            color=color,
            fill=True,
            fillColor=color,
            fillOpacity=0.8,
            weight=2
        ).add_to(m)
    
    # Add buffer zones as circles
    for idx, row in buffer_gdf.iterrows():
        folium.GeoJson(
            data=row.geometry,
            style_function=lambda x: {
                'color': INFRA_COLORS.get(row['type'], 'gray'),
                'weight': 1,
                'opacity': 0.3,
                'fillOpacity': 0.1
            }
        ).add_to(m)
    
    # Add legend
    legend_html = '''
    <div style="position: fixed; 
                bottom: 50px; right: 50px; width: 250px; height: auto; 
                background-color: white; border:2px solid grey; z-index:9999; 
                font-size:14px; padding: 10px">
        <p style="margin: 0; font-weight: bold; border-bottom: 2px solid grey; padding-bottom: 5px;">
            🏥 Infrastructure Types
        </p>
        <p style="margin: 5px 0;"><span style="background-color: red; width: 12px; height: 12px; display: inline-block; border-radius: 50%;"></span> Hospital</p>
        <p style="margin: 5px 0;"><span style="background-color: blue; width: 12px; height: 12px; display: inline-block; border-radius: 50%;"></span> School</p>
        <p style="margin: 5px 0;"><span style="background-color: orange; width: 12px; height: 12px; display: inline-block; border-radius: 50%;"></span> Market</p>
        <p style="margin: 5px 0;"><span style="background-color: cyan; width: 12px; height: 12px; display: inline-block; border-radius: 50%;"></span> Water Source</p>
    </div>
    '''
    m.get_root().html.add_child(folium.Element(legend_html))
    
    output_path = os.path.join(OUTPUT_DIR, "infrastructure_accessibility_interactive.html")
    m.save(output_path)
    print(f"✅ Interactive map saved: {output_path}")


def create_coverage_report(coverage_stats):
    """
    Create a text report of coverage statistics.
    """
    create_output_directory()
    
    report_path = os.path.join(OUTPUT_DIR, "coverage_report.txt")
    
    with open(report_path, 'w') as f:
        f.write("="*70 + "\n")
        f.write("INFRASTRUCTURE ACCESSIBILITY COVERAGE REPORT\n")
        f.write("Study Area: Guntur, Andhra Pradesh\n")
        f.write("="*70 + "\n\n")
        
        for idx, row in coverage_stats.iterrows():
            f.write(f"📍 {row['infrastructure_type'].upper().replace('_', ' ')}\n")
            f.write(f"   Coverage: {row['coverage_percentage']:.2f}% of study area\n")
            f.write(f"   Accessible Area: {row['accessible_area_sq_km']:.2f} sq km\n")
            f.write(f"   Total Study Area: {row['total_study_area_sq_km']:.2f} sq km\n\n")
    
    print(f"✅ Coverage report saved: {report_path}")


if __name__ == "__main__":
    print("Visualization module loaded.")
