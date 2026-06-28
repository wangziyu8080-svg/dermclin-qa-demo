#!/usr/bin/env python3
import json
import sys
from pathlib import Path


VALID_TASKS = {
    "descriptors",
    "diagnosis",
    "differential",
    "management",
    "patient_concern",
}


def main() -> int:
    if len(sys.argv) != 2:
        print("Usage: python3 scripts/validate_demo.py examples/demo_samples.json")
        return 2

    path = Path(sys.argv[1])
    repo_root = path.resolve().parents[1]
    data = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(data, list) or not data:
        raise ValueError("Demo file must contain a non-empty JSON list.")

    for i, item in enumerate(data):
        for key in ("id", "task", "image", "conversations"):
            if key not in item:
                raise ValueError(f"sample {i} missing key: {key}")
        if item["task"] not in VALID_TASKS:
            raise ValueError(f"sample {i} has unknown task: {item['task']}")
        conv = item["conversations"]
        if not isinstance(conv, list) or len(conv) != 2:
            raise ValueError(f"sample {i} must have exactly two conversation turns")
        if conv[0].get("from") != "human" or conv[1].get("from") != "gpt":
            raise ValueError(f"sample {i} has invalid conversation roles")
        if "<image>" not in conv[0].get("value", ""):
            raise ValueError(f"sample {i} human prompt must contain <image>")
        image_path = repo_root / item["image"]
        if not image_path.is_file():
            raise ValueError(f"sample {i} image file does not exist: {item['image']}")
        source = item.get("source")
        if source:
            for key in ("dataset", "original_image_id", "license", "license_url"):
                if key not in source:
                    raise ValueError(f"sample {i} source missing key: {key}")

    print(f"OK: {len(data)} demo samples validated.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
