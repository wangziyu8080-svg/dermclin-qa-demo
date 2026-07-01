# Demo Release Policy

This repository is a limited public preview of the bilingual dermclin-qa dataset.

## Rationale

The full dataset is associated with an unpublished manuscript. Before paper publication, the demo repository exposes only the minimum information needed for readers to understand:

- the five-task organization,
- the conversation-style JSON format,
- the Chinese and English supervision format,
- the limited use of two redistributable demo images,
- the planned release policy.

## Excluded From This Demo

The following assets are intentionally excluded:

- full task-level annotation files,
- source image identifiers or links at scale,
- full diagnosis mapping tables,
- full differential diagnosis candidate resources,
- construction scripts that would reproduce the complete dataset,
- raw clinical case images beyond the two source-licensed demo examples.

## Demo Images

This repository includes two Fitzpatrick17k example images from Atlas Dermatologico. They are included only to make the JSON examples directly inspectable and remain governed by the original CC BY-NC-SA 3.0 source-image license. Restricted image sources are not redistributed in this demo.

## Full Release

The full release is planned after paper publication or when the authors determine that public distribution is appropriate. The full release is planned to include language-specific Chinese and English annotation files so that users can train Chinese-only, English-only, or merged bilingual models. The full release will follow a source-link/identifier-based design: users must obtain original images from the corresponding public datasets and comply with their licenses.
