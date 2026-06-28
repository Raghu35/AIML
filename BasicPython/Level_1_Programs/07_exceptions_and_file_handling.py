"""Level 1: Exceptions and file handling."""

import csv
import json
import os
import xml.etree.ElementTree as ET
from pathlib import Path


class ValueTooSmallError(Exception):
    pass


try:
    value = int("10")
    if value < 5:
        raise ValueTooSmallError("Value is too small")
    print("Parsed value:", value)
except ValueError as exc:
    print("Value error:", exc)
except ValueTooSmallError as exc:
    print("Custom error:", exc)
else:
    print("No exception occurred")
finally:
    print("This always runs")

folder = Path("BasicPython/Level_1_Programs/output")
folder.mkdir(parents=True, exist_ok=True)

text_path = folder / "sample.txt"
text_path.write_text("Hello from Python\n", encoding="utf-8")
print("Read text:", text_path.read_text(encoding="utf-8").strip())

csv_path = folder / "sample.csv"
with csv_path.open("w", newline="", encoding="utf-8") as handle:
    writer = csv.writer(handle)
    writer.writerow(["name", "age"])
    writer.writerow(["Asha", 21])

print("CSV written to:", csv_path)

json_path = folder / "sample.json"
with json_path.open("w", encoding="utf-8") as handle:
    json.dump({"name": "Asha", "age": 21}, handle)
print("JSON written to:", json_path)

xml_path = folder / "sample.xml"
root = ET.Element("student")
ET.SubElement(root, "name").text = "Asha"
ET.SubElement(root, "age").text = "21"
ET.ElementTree(root).write(xml_path, encoding="utf-8", xml_declaration=True)
print("XML written to:", xml_path)

try:
    import yaml  # type: ignore
except ImportError:
    print("PyYAML is not installed; install it with 'pip install pyyaml' to run YAML examples.")
else:
    yaml_path = folder / "sample.yaml"
    yaml.safe_dump({"name": "Asha", "skills": ["Python", "Data Science"]}, open(yaml_path, "w"), sort_keys=False)
    print("YAML written to:", yaml_path)
