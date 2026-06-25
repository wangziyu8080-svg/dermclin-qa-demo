# dermclin-qa-demo

This repository is a **public demo preview** of DermClin-CVQA / dermclin-qa, a Chinese-language multi-task dermatology visual question answering dataset.

The demo is released before paper publication to document the task format and data schema while protecting the full benchmark annotations. It is **not** the full dataset and should not be used to reproduce the paper results.

## What Is Included

- `examples/demo_samples.json`: a small set of anonymized, format-only examples.
- `docs/SCHEMA.md`: the LLaVA-style conversation schema used by the dataset.
- `docs/RELEASE_POLICY.md`: release and licensing notes.
- `scripts/validate_demo.py`: a lightweight JSON schema sanity check.

## What Is Not Included

- No raw clinical images.
- No full train/test split files.
- No full diagnosis or differential label mapping.
- No complete task annotations.
- No source-image file list that would enable bulk reconstruction.

## Dataset Preview

The full dataset is organized around five dermatologist-informed tasks:

| Task | Purpose | Demo status |
|------|---------|-------------|
| `descriptors` | Lesion morphology and distribution terms | Format-only example |
| `diagnosis` | Normalized coarse diagnosis | Format-only example |
| `differential` | Candidate-conditioned differential diagnosis | Format-only example |
| `management` | Management direction for research evaluation | Format-only example |
| `patient_concern` | Patient-facing concern and communication QA | Format-only example |

The full benchmark contains 12,415 unique image identifiers and 34,440 task-level QA records. The complete release will be provided after the paper status permits public distribution.

## Image Policy

This demo does not copy, package, display, or redistribute raw dermatology case images. The `image` fields in the demo examples are synthetic placeholders such as:

```text
demo_images/demo_case_001_placeholder.jpg
```

They are included only to show the expected JSON structure.

## Quick Check

```bash
python3 scripts/validate_demo.py examples/demo_samples.json
```

## Citation

The paper citation will be added after publication.

## License

The demo metadata and documentation are released under Apache-2.0. Use of any future full dataset release must also follow the original licenses and terms of the underlying public dermatology image sources.
