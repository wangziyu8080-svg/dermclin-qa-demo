# Demo Schema

Each sample follows a LLaVA-style two-turn conversation format:

```json
{
  "id": "demo-diagnosis-001",
  "language": "zh",
  "task": "diagnosis",
  "image": "demo_images/fitzpatrick17k_example.jpg",
  "source": {
    "dataset": "Fitzpatrick17k",
    "source_collection": "Atlas Dermatologico",
    "original_image_id": "source_image_id.jpg",
    "original_url": "https://example.org/source-image",
    "license": "CC BY-NC-SA 3.0",
    "license_url": "https://creativecommons.org/licenses/by-nc-sa/3.0/"
  },
  "prompt_source": "Dataframe/dermclin_qa/by_task_balanced_all/diagnosis/train.json",
  "conversations": [
    {
      "from": "human",
      "value": "<image>\n[task=diagnosis] 问题文本"
    },
    {
      "from": "gpt",
      "value": "答案文本"
    }
  ]
}
```

The optional `language` field indicates the supervision language:

- `zh`: Chinese prompt and answer text.
- `en`: English prompt and answer text.

The full dataset is designed to support Chinese-only, English-only, and merged bilingual training. Language-specific files keep the same task taxonomy, image identifiers, source metadata, and LLaVA-style two-turn conversation structure, so users can train separate Chinese and English models or merge both languages for bilingual supervision.

For multiple-choice differential diagnosis examples, an additional `mcq_meta` field may be present:

```json
{
  "answer_key": "B",
  "options": {
    "A": "候选诊断 A",
    "B": "候选诊断 B",
    "C": "候选诊断 C",
    "D": "候选诊断 D"
  }
}
```

The demo examples use redistributable Fitzpatrick17k images and intentionally expose only a few records. They are intended to illustrate file structure, task tags, language-specific prompts, answer formatting, and image attribution.

The descriptors task follows the experimental prompt used for descriptor training/evaluation: the human turn contains `<image>`, the task instruction, and the full 60-term descriptor vocabulary in the target language. In the current experimental JSON, this task does not include a `[task=descriptors]` prefix. The other tasks use explicit task tags: `[task=diagnosis]`, `[task=differential]`, `[task=management]`, and `[task=patient_concern]`.
