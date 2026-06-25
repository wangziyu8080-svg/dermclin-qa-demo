# Demo Schema

Each sample follows a LLaVA-style two-turn conversation format:

```json
{
  "id": "demo-diagnosis-001",
  "task": "diagnosis",
  "image": "demo_images/demo_case_001_placeholder.jpg",
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

The demo examples are anonymized and use placeholder image names. They are intended only to illustrate file structure, task tags, and answer formatting.
