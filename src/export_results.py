import json
import platform
import datetime
from collections import Counter

def export_to_json(file_data, output_file="scan_results.json"):
    if not file_data:
        print("No data to export!")
        return None

    file_sizes = [f["size"] for f in file_data]
    total_files = len(file_sizes)
    total_size = sum(file_sizes)

    extensions = [f["extension"] for f in file_data if f["extension"]]
    no_ext_count = sum(1 for f in file_data if not f["extension"])
    ext_counter = Counter(extensions)
    ext_sizes = {}
    for f in file_data:
        ext = f["extension"] if f["extension"] else "no_ext"
        if ext not in ext_sizes:
            ext_sizes[ext] = {"total_size": 0, "count": 0}
        ext_sizes[ext]["total_size"] += f["size"]
        ext_sizes[ext]["count"] += 1

    top_20_by_count = [
        {
            "extension": ext,
            "file_count": count,
            "percentage": round((count / total_files) * 100, 2)
        }
        for ext, count in ext_counter.most_common(20)
    ]

    ext_size_list = [(ext, data["total_size"], data["count"]) for ext, data in ext_sizes.items()]
    ext_size_list.sort(key=lambda x: x[1], reverse=True)

    top_20_by_size = [
        {
            "extension": ext,
            "total_size_bytes": size,
            "total_size_gb": round(size / (1024 * 1024 * 1024), 4),
            "file_count": count,
            "percentage_of_disk": round((size / total_size) * 100, 2),
            "avg_size_kb": round((size / count) / 1024, 2)
        }
        for ext, size, count in ext_size_list[:20]
    ]

    system_info = {
        "os": platform.system(),
        "os_version": platform.version(),
        "platform": platform.platform(),
        "architecture": platform.machine(),
        "processor": platform.processor(),
        "python_version": platform.python_version(),
        "scan_date": datetime.datetime.now().isoformat()
    }

    export_data = {
        "system_info": system_info,
        "summary": {
            "total_files": total_files,
            "total_size_bytes": total_size,
            "total_size_gb": round(total_size / (1024 * 1024 * 1024), 2),
            "unique_extensions": len(ext_counter),
            "files_without_extension": no_ext_count
        },
        "top_20_extensions_by_count": top_20_by_count,
        "top_20_extensions_by_size": top_20_by_size
    }

    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(export_data, f, indent=2, ensure_ascii=False)

    print(f"\n[SUCCESS] Results exported to: {output_file}")
    return export_data


def create_summary_report(export_data):
    print("\n" + "=" * 70)
    print("EXPORT SUMMARY")
    print("=" * 70)

    sys_info = export_data["system_info"]
    print(f"\nSystem: {sys_info['os']} ({sys_info['platform']})")
    print(f"Scan Date: {sys_info['scan_date']}")

    summary = export_data["summary"]
    print(f"\nTotal Files: {summary['total_files']:,}")
    print(f"Total Size: {summary['total_size_gb']:.2f} GB")
    print(f"Unique Extensions: {summary['unique_extensions']}")
    print(f"Files without Extension: {summary['files_without_extension']}")

    print("\n" + "=" * 70)
