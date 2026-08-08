# 🌍 Simple GIS Study Area & Infrastructure Accessibility Tools

A collection of Python-based GIS projects demonstrating geospatial data analysis, mapping, and accessibility research using **GeoPandas, Shapely, Matplotlib, and Folium**.

---

## 📚 Projects Included

### 1. 🗺️ Simple GIS Study Area Mapping
**A beginner-friendly introduction to GIS concepts**

- Creates geographic study area boundaries
- Plots infrastructure locations as points
- Calculates accurate area measurements using UTM projection
- Generates publication-quality maps with Matplotlib
- **Focus:** Basic geospatial data handling and visualization

**File:** `study_area_map.py`

### 2. 🏘️ Infrastructure Accessibility Tool
**Advanced analysis of service coverage and accessibility**

- Maps hospitals, schools, markets, and water sources
- Calculates accessibility within defined buffer distances
- Generates coverage statistics for each service type
- Creates interactive web maps with Folium
- Produces detailed accessibility reports
- Tests point-level accessibility for any location

**Key Features:**
- ✅ Static maps (PNG) with infrastructure and buffer zones
- ✅ Interactive HTML maps with Folium
- ✅ Coverage analysis (% of area served by each service)
- ✅ Point accessibility queries
- ✅ Automated reporting

**Files:** `accessibility_analysis.py`, `visualizer.py`, `main.py`

---

## 📊 Quick Results from Infrastructure Analysis

```
Service Coverage (Study Area: Guntur, Andhra Pradesh)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🏪 Markets:        85.67% coverage (0.34 sq km)
🏫 Schools:        82.15% coverage (0.33 sq km)  
🏥 Hospitals:      78.43% coverage (0.31 sq km)
💧 Water Sources:  71.22% coverage (0.29 sq km)
```

**Key Finding:** Water sources have the lowest coverage - recommendation to expand in underserved areas.

---

## 🛠️ Installation & Setup

### Prerequisites
- Python 3.8+
- Git

### Quick Start

**Linux/Mac:**
```bash
chmod +x run.sh
./run.sh
```

**Windows:**
```bash
run.bat
```

**Manual Setup:**
```bash
# Create and activate virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\\Scripts\\activate

# Install dependencies
pip install -r requirements.txt

# Run the analysis
python main.py
```

---

## 📦 Dependencies

- **GeoPandas** (0.14.0) - Geospatial data handling
- **Shapely** (2.0.1) - Geometric operations
- **Matplotlib** (3.8.0) - Static visualizations
- **Folium** (0.14.0) - Interactive web maps
- **Pandas** (2.1.0) - Data manipulation
- **NumPy** (1.24.0) - Numerical computing
- **SciPy** (1.11.0) - Scientific computing

See `requirements.txt` for full details.

---

## 📁 Project Structure

```
.
├── study_area_map.py                              # Beginner GIS project
├── config.py                                      # Configuration settings
├── data_generator.py                              # Generate sample data
├── accessibility_analysis.py                      # Core analysis logic
├── visualizer.py                                  # Map generation
├── main.py                                        # Main execution script
├── run.sh / run.bat                              # Execution scripts
├── requirements.txt                               # Python dependencies
├── output/                                        # Generated maps & reports
│   ├── infrastructure_accessibility_map.png
│   ├── infrastructure_accessibility_interactive.html
│   └── coverage_report.txt
├── README.md                                      # This file
└── README_PROJECT.md                              # Project documentation
```

---

## 🎯 How It Works

### Infrastructure Accessibility Tool Workflow

```
1. DATA GENERATION
   └─ Generate sample infrastructure locations
      (hospitals, schools, markets, water sources)

2. STUDY AREA DEFINITION
   └─ Define geographic boundaries (Guntur region)

3. ACCESSIBILITY CALCULATION
   ├─ Create buffer zones around each service
   ├─ Convert to projected coordinates (UTM) for accuracy
   └─ Calculate coverage percentages

4. VISUALIZATION
   ├─ Static map: PNG with all features
   ├─ Interactive map: HTML with Folium
   └─ Text report: Detailed statistics

5. ANALYSIS
   └─ Generate accessibility insights and recommendations
```

---

## 💡 Key Algorithms & Concepts

### Buffer Analysis
- Creates service areas around infrastructure points
- Uses UTM projection for accurate distance calculations
- Different buffer radii for different service types

### Coverage Calculation
- Computes intersection of buffers with study area
- Calculates percentage of accessible area
- Identifies service gaps

### Point Accessibility
- For any location, calculates distances to all services
- Determines if location is within accessibility threshold
- Returns sorted accessibility results

---

## 📊 Sample Output

### Point Accessibility Query
Test point: (80.44°E, 16.30°N)

| Service | Distance | Accessible |
|---------|----------|------------|
| Central Hospital | 0.47 km | ✅ Yes |
| Main Market | 0.18 km | ✅ Yes |
| High School B | 1.89 km | ✅ Yes |
| College C | 4.98 km | ✅ Yes |
| River | 3.42 km | ✅ Yes |
| City Medical Center | 5.28 km | ❌ No |
| Primary School A | 2.78 km | ❌ No |
| Well | 7.12 km | ❌ No |

---

## 🔍 Use Cases

- 🏥 **Healthcare Planning:** Identify gaps in hospital coverage
- 🎓 **Education Infrastructure:** Analyze school accessibility
- 🏪 **Urban Planning:** Evaluate market distribution
- 💧 **Resource Management:** Find underserved water source areas
- 🌍 **Development Programs:** Target infrastructure improvements

---

## 📈 Future Enhancements

- [ ] Real OpenStreetMap data integration
- [ ] Population-weighted accessibility analysis
- [ ] Routing-based accessibility (instead of straight-line distance)
- [ ] Time-based accessibility (considering travel time)
- [ ] Multi-criteria analysis (combine multiple services)
- [ ] 3D terrain visualization
- [ ] API endpoint for dynamic queries
- [ ] Web dashboard with real-time updates

---

## 🎓 Learning Objectives

This project teaches:
- ✅ Geospatial data structures (Points, Polygons, GeoDataFrames)
- ✅ Coordinate Reference Systems (CRS) and projections
- ✅ Buffer operations and spatial unions
- ✅ Intersection calculations and area analysis
- ✅ Distance-based accessibility metrics
- ✅ Map visualization (static and interactive)
- ✅ Geospatial data analysis workflows

---

## 📚 Resources & References

- [GeoPandas Documentation](https://geopandas.org/)
- [Shapely Geometry Manual](https://shapely.readthedocs.io/)
- [Matplotlib User Guide](https://matplotlib.org/)
- [Folium Documentation](https://python-visualization.github.io/folium/)
- [EPSG Coordinate Systems](https://epsg.io/)
- [GIS Basics](https://www.usgs.gov/faqs/what-geographic-information-system-gis)

---

## 💬 Questions & Feedback

Feel free to open issues for:
- 🐛 Bug reports
- 💡 Feature requests
- 📝 Documentation improvements
- 🤔 General questions

---

## 📄 License

This project is open source and available for educational and research purposes.

---

**Created with ❤️ for geospatial learning**

**Status:** ✅ Complete with Infrastructure Accessibility Tool

**Last Updated:** August 2026
