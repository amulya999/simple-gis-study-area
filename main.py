"""Main execution script for Infrastructure Accessibility Tool."""

from data_generator import generate_infrastructure_data
from accessibility_analysis import (
    create_study_area_polygon,
    calculate_accessibility_buffers,
    calculate_accessibility_coverage,
    calculate_point_accessibility
)
from visualizer import (
    create_static_map,
    create_interactive_map,
    create_coverage_report
)


def main():
    print("\n" + "="*70)
    print("🚀 INFRASTRUCTURE ACCESSIBILITY TOOL")
    print("="*70)
    
    # Step 1: Generate infrastructure data
    print("\n📍 Step 1: Generating infrastructure data...")
    infrastructure = generate_infrastructure_data()
    print(f"   ✅ Generated {len(infrastructure)} locations")
    print(f"\n   Infrastructure Summary:")
    print(infrastructure.groupby('type').size())
    
    # Step 2: Create study area
    print("\n📍 Step 2: Creating study area...")
    study_area = create_study_area_polygon()
    print(f"   ✅ Study area boundary created")
    
    # Step 3: Calculate accessibility buffers
    print("\n📍 Step 3: Calculating accessibility buffers...")
    buffers = calculate_accessibility_buffers(infrastructure)
    print(f"   ✅ {len(buffers)} buffer zones created")
    
    # Step 4: Calculate coverage statistics
    print("\n📍 Step 4: Analyzing coverage...")
    coverage_stats = calculate_accessibility_coverage(study_area, infrastructure, buffers)
    print("\n   Coverage Statistics:")
    print(coverage_stats.to_string(index=False))
    
    # Step 5: Test point accessibility
    print("\n📍 Step 5: Testing point accessibility...")
    test_point = (80.44, 16.30)  # (longitude, latitude)
    print(f"   Test point: {test_point}")
    point_access = calculate_point_accessibility(test_point, infrastructure)
    print("\n   Accessibility Results:")
    print(point_access.to_string(index=False))
    
    # Step 6: Create visualizations
    print("\n📍 Step 6: Creating visualizations...")
    create_static_map(study_area, infrastructure, buffers)
    create_interactive_map(infrastructure, buffers, study_area)
    create_coverage_report(coverage_stats)
    
    print("\n" + "="*70)
    print("✅ ANALYSIS COMPLETE!")
    print("="*70)
    print("\n📂 Output files generated in 'output/' directory:")
    print("   - infrastructure_accessibility_map.png")
    print("   - infrastructure_accessibility_interactive.html")
    print("   - coverage_report.txt")
    print("\n" + "="*70 + "\n")


if __name__ == "__main__":
    main()
