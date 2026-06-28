# Demo Schema

Each sample follows a LLaVA-style two-turn conversation format:

```json
{
  "id": "demo-diagnosis-001",
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

The demo examples use redistributable Fitzpatrick17k images and intentionally expose only a few records. They are intended to illustrate file structure, task tags, answer formatting, and image attribution.

The descriptors task follows the experimental prompt used for descriptor training/evaluation: the human turn contains `<image>`, the Chinese instruction, and the full 60-term descriptor vocabulary. In the current experimental JSON, this task does not include a `[task=descriptors]` prefix. The other tasks use explicit task tags: `[task=diagnosis]`, `[task=differential]`, `[task=management]`, and `[task=patient_concern]`.
