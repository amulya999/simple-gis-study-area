# Configuration for Infrastructure Accessibility Tool

# Study Area Configuration (Guntur, Andhra Pradesh)
STUDY_AREA_BOUNDS = {
    "north": 16.35,
    "south": 16.25,
    "east": 80.50,
    "west": 80.40
}

# Infrastructure Types and Their Buffer Radius (in km)
# This defines "accessible" area within this radius
INFRASTRUCTURE_BUFFERS = {
    "hospital": 5.0,        # Within 5 km of hospital
    "school": 2.0,          # Within 2 km of school
    "market": 3.0,          # Within 3 km of market
    "water_source": 2.0     # Within 2 km of water source
}

# Output Configuration
OUTPUT_DIR = "output"
MAP_DPI = 300
MAP_FIGSIZE = (14, 12)

# Color Scheme for Infrastructure Types
INFRA_COLORS = {
    "hospital": "red",
    "school": "blue",
    "market": "orange",
    "water_source": "cyan"
}

# Coordinate Reference System
CRS_WGS84 = "EPSG:4326"      # Global coordinates
CRS_PROJECTED = "EPSG:32644"  # UTM Zone 44N (for accurate distance calculations)
