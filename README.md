# Fact-Find Extractor


End-to-end pipeline that turns an adviser–client transcript into structured **Fact Find JSON** and benchmarks extraction accuracy on a synthetic test set.  

## Tasks

1. **Parse transcripts → JSON** (schema in `fact_finder.py`)
2. **Generate synthetic data** (`01_data_generator.ipynb`)
3. **Evaluate** G-Eval semantic scoring (`03_eval.ipynb`)

## Repo Layout

```
├── 01_data_generator.ipynb
├── 02_extractor.ipynb
├── 03_eval.ipynb
├── fact_finder.py
├── financial_dataset (generated synthetic data)
```

## Quick Start

To run the pipeline on a sample transcript and generate the JSON output:

```bash
pip install .
export OPENAI_API_KEY="sk-..."
python fact_finder.py sample_transcript.txt > out.json
```



## Latest Result

- GEval correctness: ↑ from 0.48 to 0.49 after adding chain-of-thought to the system prompt (see 03_eval.ipynb).

#### What changed?

- Added detailed prompt with extensive reasoning to the system prompt to reduce hallucinations and contradictions in the output.


#### After
**System prompt:** as in `fact_finder.py` - adds reasoning to the system prompt.

**Result:**
  - ❌ Correctness (GEval) (score: 0.4899010086693044, threshold: 0.5, strict: False, evaluation model: gpt-4o, reason: No contradiction but missing secondary client and additional details like last name and address. 'Salary' named as 'Employment Income', and additional objectives goals omitted., error: None)


#### Before

```python
SYSTEM_PROMPT = (
    "You are a certified paraplanner helping a financial advisor fill out a Customer "
    "Information Form (CIF). Extract the client's answers from the call transcript. "
    "Return your answer **strictly** as JSON that validates against the provided schema. "
    "If a field is missing, use null (do NOT invent)."
)
```
**Result:**

  - ❌ Correctness (GEval) (score: 0.47527727471344206, threshold: 0.5, strict: False, evaluation model: gpt-4o, reason: Missing personal details for both clients and no mention of 'Salary' in incomes. 'Liquid Savings' and 'Primary Residence' differ in capitalization, and absence of 'Mortgage'., error: None)


## Future improvements

### Data generation

- Generate longer transcripts (>30 minutes).
- Add filler words and other noise to replicate real-world scenarios.
- Add more complex scenarios with multiple clients, multiple assets, multiple liabilities, etc.
- Add numbers in such a way that LLM as to reason about the numbers such as total income, total assets, total liabilities, etc.

### Finding the facts (transcript to JSON)

- Improve the system prompt and use reasoning to extract the facts.
- Prompt to reduce hallucinations and contradictions in the output.


### Evaluation

- Do exact and fuzzy matching of the output with the ground truth for instant and faster evaluation for terms such as name, address, etc.
- Try JSON diffing to evaluate the correctness of the output.
- Evaluate the the amount of information extracted from the transcript.
- LLM as a judge to evaluate the correctness of the output.
