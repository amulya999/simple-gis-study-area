"""Core accessibility analysis module."""

import geopandas as gpd
import pandas as pd
from shapely.geometry import Point, Polygon
import numpy as np
from config import (
    INFRASTRUCTURE_BUFFERS,
    CRS_WGS84,
    CRS_PROJECTED,
    STUDY_AREA_BOUNDS
)


def create_study_area_polygon():
    """
    Create the study area boundary polygon.
    """
    bounds = STUDY_AREA_BOUNDS
    polygon = Polygon([
        (bounds["west"], bounds["south"]),
        (bounds["east"], bounds["south"]),
        (bounds["east"], bounds["north"]),
        (bounds["west"], bounds["north"]),
        (bounds["west"], bounds["south"])
    ])
    
    study_area = gpd.GeoDataFrame(
        {"name": ["Study Area"]},
        geometry=[polygon],
        crs=CRS_WGS84
    )
    
    return study_area


def calculate_accessibility_buffers(infrastructure_gdf):
    """
    Create buffer zones around infrastructure.
    Buffer represents the "accessible" area within defined distance.
    
    Returns: GeoDataFrame with buffer geometries
    """
    # Project to UTM for accurate distance calculations
    infrastructure_proj = infrastructure_gdf.to_crs(CRS_PROJECTED)
    
    # Create buffers based on infrastructure type
    buffers = []
    for idx, row in infrastructure_proj.iterrows():
        buffer_distance = INFRASTRUCTURE_BUFFERS.get(row['type'], 2.0) * 1000  # Convert km to meters
        buffer_geom = row.geometry.buffer(buffer_distance)
        buffers.append({
            'name': row['name'],
            'type': row['type'],
            'geometry': buffer_geom
        })
    
    buffer_gdf = gpd.GeoDataFrame(buffers, crs=CRS_PROJECTED)
    # Convert back to WGS84
    buffer_gdf = buffer_gdf.to_crs(CRS_WGS84)
    
    return buffer_gdf


def calculate_accessibility_coverage(study_area, infrastructure_gdf, buffer_gdf):
    """
    Calculate what percentage of study area has access to each infrastructure type.
    """
    study_area_proj = study_area.to_crs(CRS_PROJECTED)
    study_area_size = study_area_proj.geometry.area.iloc[0]
    
    coverage_stats = []
    
    # For each infrastructure type
    for infra_type in infrastructure_gdf['type'].unique():
        type_buffers = buffer_gdf[buffer_gdf['type'] == infra_type]
        
        if len(type_buffers) > 0:
            # Union all buffers of this type
            union_buffer = type_buffers.geometry.unary_union
            union_buffer_proj = gpd.GeoDataFrame(
                geometry=[union_buffer],
                crs=CRS_WGS84
            ).to_crs(CRS_PROJECTED)
            
            # Calculate intersection with study area
            intersection = study_area_proj.geometry.iloc[0].intersection(
                union_buffer_proj.geometry.iloc[0]
            )
            
            intersection_area = intersection.area
            coverage_percent = (intersection_area / study_area_size) * 100
            
            coverage_stats.append({
                'infrastructure_type': infra_type,
                'coverage_percentage': coverage_percent,
                'accessible_area_sq_km': intersection_area / 1_000_000,
                'total_study_area_sq_km': study_area_size / 1_000_000
            })
    
    return pd.DataFrame(coverage_stats)


def calculate_point_accessibility(point, infrastructure_gdf):
    """
    For a given point, calculate which infrastructure is accessible.
    Returns accessibility status and distances.
    """
    # Project both point and infrastructure to UTM
    point_proj = gpd.GeoDataFrame(
        geometry=[Point(point)],
        crs=CRS_WGS84
    ).to_crs(CRS_PROJECTED)
    
    infra_proj = infrastructure_gdf.to_crs(CRS_PROJECTED)
    
    accessibility = []
    for idx, infra in infra_proj.iterrows():
        distance_m = point_proj.geometry.iloc[0].distance(infra.geometry)
        distance_km = distance_m / 1000
        
        buffer_distance = INFRASTRUCTURE_BUFFERS.get(infra['type'], 2.0)
        is_accessible = distance_km <= buffer_distance
        
        accessibility.append({
            'name': infra['name'],
            'type': infra['type'],
            'distance_km': round(distance_km, 2),
            'accessible': is_accessible
        })
    
    return pd.DataFrame(accessibility)


if __name__ == "__main__":
    from data_generator import generate_infrastructure_data
    
    print("\n" + "="*60)
    print("🔍 INFRASTRUCTURE ACCESSIBILITY ANALYSIS")
    print("="*60)
    
    # Generate data
    infrastructure = generate_infrastructure_data()
    study_area = create_study_area_polygon()
    
    print(f"\n✅ Generated {len(infrastructure)} infrastructure locations")
    print(f"✅ Study area created: {study_area.geometry.area.iloc[0]:.4f} sq degrees")
    
    # Calculate buffers
    print("\n📍 Calculating accessibility buffers...")
    buffers = calculate_accessibility_buffers(infrastructure)
    print(f"✅ {len(buffers)} buffer zones created")
    
    # Calculate coverage
    print("\n📊 Calculating coverage statistics...")
    coverage = calculate_accessibility_coverage(study_area, infrastructure, buffers)
    print("\n" + coverage.to_string(index=False))
    
    # Test point accessibility
    print("\n🎯 Testing accessibility for a sample point (16.30, 80.44):")
    test_point = (80.44, 16.30)
    point_access = calculate_point_accessibility(test_point, infrastructure)
    print("\n" + point_access.to_string(index=False))
    
    print("\n" + "="*60)
    print("✅ Analysis Complete!")
    print("="*60)
