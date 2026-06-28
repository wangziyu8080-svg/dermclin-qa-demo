# dermclin-qa-demo

This repository is a **public demo preview** of DermClin-CVQA / dermclin-qa, a Chinese-language multi-task dermatology visual question answering dataset.

The demo is released before paper publication to document the task format and data schema while protecting the full benchmark annotations. It is **not** the full dataset and should not be used to reproduce the paper results.

## What Is Included

- `examples/demo_samples.json`: a small set of demo examples following the experimental task prompt format.
- `demo_images/`: two redistributable Fitzpatrick17k example images with attribution.
- `docs/SCHEMA.md`: the LLaVA-style conversation schema used by the dataset.
- `docs/RELEASE_POLICY.md`: release and licensing notes.
- `scripts/validate_demo.py`: a lightweight JSON schema sanity check.

## What Is Not Included

- No restricted raw clinical images.
- No full train/test split files.
- No full diagnosis or differential label mapping.
- No complete task annotations.
- No source-image file list that would enable bulk reconstruction.

## Dataset Preview

The full dataset is organized around five dermatologist-informed tasks:

| Task | Purpose | Demo status |
|------|---------|-------------|
| `descriptors` | Lesion morphology and distribution terms | Experimental-format prompt example |
| `diagnosis` | Normalized coarse diagnosis | Experimental-format prompt example |
| `differential` | Candidate-conditioned differential diagnosis | Experimental-format prompt example |
| `management` | Management direction for research evaluation | Experimental-format prompt example |
| `patient_concern` | Patient-facing concern and communication QA | Experimental-format prompt example |

The full benchmark contains 12,415 unique image identifiers and 34,440 task-level QA records. The complete release will be provided after the paper status permits public distribution.

## Image Policy

This demo includes only two source-licensed Fitzpatrick17k example images. They are provided to make the public JSON examples directly inspectable, not to release the full image set. Restricted sources such as DDI are not redistributed here.

The full benchmark release is planned to follow a link/identifier-based policy for source images where needed. See `demo_images/ATTRIBUTION.md` for image-level attribution.

## Prompt Policy

The demo prompts are copied from the local experimental JSON format used by the project. The `descriptors` task uses the full 60-term candidate list and therefore does not use a `[task=descriptors]` prefix; the other four tasks use explicit task tags such as `[task=diagnosis]`.

## Quick Check

```bash
python3 scripts/validate_demo.py examples/demo_samples.json
```

## Citation

The paper citation will be added after publication.

## License

The demo metadata, scripts, and documentation are released under Apache-2.0. The two demo images remain under their original CC BY-NC-SA 3.0 source-image license. Use of any future full dataset release must also follow the original licenses and terms of the underlying public dermatology image sources.
