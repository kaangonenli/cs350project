import json
import sys

def load_json_result(filepath):
    """Load a JSON result file"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"Error: File not found: {filepath}")
        return None
    except json.JSONDecodeError:
        print(f"Error: Invalid JSON in file: {filepath}")
        return None


def compare_two_systems(file1, file2):
    """
    Compare two system scan results and generate comparison report
    """
    data1 = load_json_result(file1)
    data2 = load_json_result(file2)

    if not data1 or not data2:
        return

    print("\n" + "=" * 80)
    print("SYSTEM COMPARISON REPORT")
    print("=" * 80)

    # System info comparison
    print("\n### SYSTEM INFORMATION ###\n")
    print(f"System 1: {data1['system_info']['os']} - {data1['system_info']['platform']}")
    print(f"System 2: {data2['system_info']['os']} - {data2['system_info']['platform']}")

    # Summary comparison
    print("\n### SUMMARY COMPARISON ###\n")
    s1 = data1['summary']
    s2 = data2['summary']

    print(f"{'Metric':<30} {'System 1':>20} {'System 2':>20}")
    print("-" * 72)
    print(f"{'Total Files':<30} {s1['total_files']:>20,} {s2['total_files']:>20,}")
    print(f"{'Total Size (GB)':<30} {s1['total_size_gb']:>20.2f} {s2['total_size_gb']:>20.2f}")
    print(f"{'Unique Extensions':<30} {s1['unique_extensions']:>20} {s2['unique_extensions']:>20}")
    print(f"{'Files w/o Extension':<30} {s1['files_without_extension']:>20} {s2['files_without_extension']:>20}")

    # Top extensions comparison by count
    print("\n### TOP-20 EXTENSIONS BY FILE COUNT ###\n")
    print(f"{'Rank':<6} {'System 1 Extension':<20} {'Count':>12} {'System 2 Extension':<20} {'Count':>12}")
    print("-" * 72)

    top1_count = data1['top_20_extensions_by_count']
    top2_count = data2['top_20_extensions_by_count']

    for i in range(20):
        ext1 = top1_count[i] if i < len(top1_count) else {"extension": "-", "file_count": 0}
        ext2 = top2_count[i] if i < len(top2_count) else {"extension": "-", "file_count": 0}

        print(f"{i+1:<6} {ext1['extension']:<20} {ext1['file_count']:>12,} {ext2['extension']:<20} {ext2['file_count']:>12,}")

    # Top extensions comparison by size
    print("\n### TOP-20 EXTENSIONS BY DISK USAGE ###\n")
    print(f"{'Rank':<6} {'System 1 Extension':<20} {'Size (GB)':>12} {'System 2 Extension':<20} {'Size (GB)':>12}")
    print("-" * 72)

    top1_size = data1['top_20_extensions_by_size']
    top2_size = data2['top_20_extensions_by_size']

    for i in range(20):
        ext1 = top1_size[i] if i < len(top1_size) else {"extension": "-", "total_size_gb": 0}
        ext2 = top2_size[i] if i < len(top2_size) else {"extension": "-", "total_size_gb": 0}

        print(f"{i+1:<6} {ext1['extension']:<20} {ext1['total_size_gb']:>12.2f} {ext2['extension']:<20} {ext2['total_size_gb']:>12.2f}")

    # Common extensions analysis
    print("\n### COMMON EXTENSIONS ANALYSIS ###\n")

    ext1_set = {item['extension'] for item in top1_count}
    ext2_set = {item['extension'] for item in top2_count}

    common = ext1_set & ext2_set
    only_1 = ext1_set - ext2_set
    only_2 = ext2_set - ext1_set

    print(f"Common extensions in Top-20: {len(common)}")
    print(f"Extensions only in System 1: {len(only_1)} - {sorted(only_1)}")
    print(f"Extensions only in System 2: {len(only_2)} - {sorted(only_2)}")

    print("\n" + "=" * 80)


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python compare_systems.py <result1.json> <result2.json>")
        sys.exit(1)

    compare_two_systems(sys.argv[1], sys.argv[2])
