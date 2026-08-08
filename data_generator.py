"""Generate sample infrastructure data for the study area."""

import geopandas as gpd
import pandas as pd
from shapely.geometry import Point
from config import STUDY_AREA_BOUNDS, CRS_WGS84


def generate_infrastructure_data():
    """
    Generate sample infrastructure locations within the study area.
    Returns a GeoDataFrame with hospitals, schools, markets, and water sources.
    """
    
    # Define sample locations (latitude, longitude)
    hospitals = [
        {"name": "Central Hospital", "type": "hospital", "lat": 16.30, "lon": 80.44},
        {"name": "City Medical Center", "type": "hospital", "lat": 16.32, "lon": 80.47},
    ]
    
    schools = [
        {"name": "Primary School A", "type": "school", "lat": 16.28, "lon": 80.42},
        {"name": "High School B", "type": "school", "lat": 16.31, "lon": 80.45},
        {"name": "College C", "type": "school", "lat": 16.29, "lon": 80.48},
    ]
    
    markets = [
        {"name": "Main Market", "type": "market", "lat": 16.305, "lon": 80.435},
        {"name": "Local Market", "type": "market", "lat": 16.318, "lon": 80.455},
    ]
    
    water_sources = [
        {"name": "River", "type": "water_source", "lat": 16.27, "lon": 80.43},
        {"name": "Well", "type": "water_source", "lat": 16.34, "lon": 80.49},
    ]
    
    # Combine all data
    all_infrastructure = hospitals + schools + markets + water_sources
    
    # Convert to GeoDataFrame
    gdf = gpd.GeoDataFrame(
        all_infrastructure,
        geometry=[Point(item["lon"], item["lat"]) for item in all_infrastructure],
        crs=CRS_WGS84
    )
    
    return gdf


if __name__ == "__main__":
    # Test data generation
    infrastructure_data = generate_infrastructure_data()
    print("\n✅ Sample Infrastructure Data Generated:")
    print(infrastructure_data)
    print(f"\nTotal locations: {len(infrastructure_data)}")
    print(f"\nInfrastructure types:")
    print(infrastructure_data['type'].value_counts())
