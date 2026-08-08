# Infrastructure Accessibility Tool

🗺️ A Python-based GIS tool to analyze infrastructure accessibility across a study area.

## 📋 Project Overview

This tool analyzes how accessible key infrastructure (hospitals, schools, markets, water sources) is across a geographic area. It generates:
- 📍 Infrastructure location maps
- 📏 Accessibility heatmaps
- 📊 Coverage analysis reports
- 🎨 Interactive and static visualizations

## 🎯 Features (Planned)

- [x] Step 1: Project structure & configuration
- [ ] Step 2: Infrastructure data generation
- [ ] Step 3: Accessibility analysis (distance calculations, buffers)
- [ ] Step 4: Static map visualization
- [ ] Step 5: Interactive web map (Folium)
- [ ] Step 6: Coverage reports and statistics
- [ ] Step 7: Advanced heatmap visualization

## 🛠️ Installation

```bash
# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

## 📁 Project Structure

```
.
├── requirements.txt           # Python dependencies
├── config.py                  # Configuration settings
├── data_generator.py          # Generate sample infrastructure data
├── accessibility_analysis.py  # Core accessibility calculations (coming)
├── visualizer.py              # Map visualization (coming)
├── main.py                    # Main script (coming)
├── output/                    # Output maps and reports
└── README_PROJECT.md          # This file
```

## 📊 Configuration

Edit `config.py` to customize:
- Study area boundaries
- Accessibility buffer distances
- Infrastructure types
- Output settings

## 🚀 Usage (Coming Soon)

```bash
python main.py
```

## 📚 Learning Resources

- [GeoPandas Documentation](https://geopandas.org/)
- [Shapely Geometry](https://shapely.readthedocs.io/)
- [Folium Interactive Maps](https://python-visualization.github.io/folium/)

## 📝 Next Steps

1. Generate infrastructure data
2. Calculate accessibility metrics
3. Create visualizations
4. Add interactive mapping

---

**Status:** 🔨 Under Development
