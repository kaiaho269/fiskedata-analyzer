# FA Strategy

## Mission

Fiskedata Analyzer (FA) is a personal fisheries intelligence and analysis tool.

The first purpose of FA is simple:

> Help me ask better questions about fisheries data and make better fishing decisions.

FA is not being built as a commercial product first. It is being built because it is useful to me.

**Strategy: personal utility first. Generality second. Commercialization last.**

If FA later becomes useful to other fishermen, researchers, journalists, politicians, organizations, or the public, that is a consequence of building a genuinely useful analytical system.

---

## Core principles

### 1. Questions before dashboards

FA should make questions easy, not make charts impressive.

The purpose of a visualization is to help answer a question. A dashboard is not the product by itself.

The deeper goal is:

> FA should help users discover questions they did not know they could ask.

### 2. Analysis before presentation

The analytical engine is more important than the current user interface.

The current architecture should therefore keep these responsibilities separate:

```text
UI
 ↓
FA analytical engine
 ↓
DuckDB / data
```

`app.py` should not become the place where all analytical logic lives.

### 3. Evidence over assumptions

FA must distinguish between:

- what the data shows
- what can reasonably be inferred
- what is unknown
- what is speculation

Numbers should come from the analytical engine, not from an AI model improvising an answer.

### 4. Measure before optimizing

If FA is slow, first identify where the time is spent.

Do not rewrite working architecture merely because something feels slow.

A 15–30 second analysis can be acceptable if the user understands what FA is doing and receives meaningful progress information.

The long-term target is not merely:

> Make it fast.

It is:

> Make computation understandable, measurable, and appropriately fast.

### 5. Technology is replaceable; analytical knowledge is the asset

Python, Streamlit, DuckDB, Parquet, Rust, another UI, or another database may change.

The valuable assets are:

- domain knowledge
- analytical logic
- data model
- reproducible analysis
- trustworthy results
- understanding of the questions fishermen actually need answered

FA should therefore avoid unnecessary dependence on a particular programming language, UI framework, or AI provider.

---

## FAQuery — long-term direction

FAQuery is a future natural-language interface to FA.

Its purpose is to allow a non-expert to investigate complex fisheries questions through ordinary language, while FA remains responsible for the actual data analysis and numerical truth.

Conceptually:

```text
User
  ↓
FAQuery
(multilingual AI analyst)
  ↓
structured query
  ↓
FA analytical engine
  ↓
DuckDB / data
  ↓
results
  ↓
FAQuery explanation
  ↓
User
```

The AI should not be the source of numerical truth.

**LLM = language, reasoning, question formulation and explanation.**

**FA engine = filtering, calculations, aggregation and numerical truth.**

This separation is fundamental.

### Multilingual by design

The user should not need to learn:

- database terminology
- FA's internal query language
- the language in which the source data happens to be documented

Finnish, Lithuanian, German, Ukrainian, Italian, Norwegian, English and other languages should ultimately be interfaces to the same analytical system.

The language layer translates human intent into canonical FA concepts.

For example:

```text
Finnish / German / Ukrainian / Italian
                ↓
        canonical FA query
                ↓
              DuckDB
```

Numbers and analytical definitions must never depend on the language used to ask the question.

### AI provider independence

FAQuery should not be designed around an expensive subscription to one AI provider.

Possible future implementations include:

- low-cost cloud API models
- local open-weight models
- the RTX 3090 already available for local experimentation
- a hybrid of local and cloud models

The architecture should allow the AI component to be replaced without rebuilding FA.

Most importantly, the AI should never receive the entire raw fisheries dataset merely to answer a question.

Instead:

```text
Large dataset
    ↓
FA / DuckDB
    ↓
small structured result
    ↓
AI
```

This keeps costs low and preserves analytical control.

---

## Architecture direction

The preferred long-term separation is:

```text
             FAQuery
                │
        language / intent
                │
                ▼
          FA query layer
                │
                ▼
       FA analytical engine
                │
                ▼
        DuckDB / Parquet
                │
                ▼
              data
```

The current Python + Streamlit implementation is entirely appropriate for this stage.

A future system could replace or supplement parts of it with:

- a different frontend
- a CLI
- an API
- Rust or another language for selected performance-critical components
- different storage formats

No such migration is required now.

---

## Development philosophy

FA is an exploratory engineering project.

The complete final scope is deliberately unknown.

Therefore:

- do not estimate the entire project
- estimate individual pieces when they become sufficiently understood
- use focused sprints
- measure before making architectural changes
- keep the code understandable
- preserve useful history in Git
- document important decisions
- validate analytical results

A sprint is a focused development session. It may contain:

- coding
- investigation
- refactoring
- testing
- documentation
- performance analysis
- architectural evaluation

A sprint that proves an idea is wrong is still a successful sprint.

The working cycle is intentionally flexible: roughly one hour of focused work followed by a break, with multiple sprints possible in a day when useful.

---

## What does "finished" mean?

FA does not need a permanent state called "finished".

Instead, meaningful milestones can define progress.

Possible future milestones:

### Personal Alpha
FA can investigate the user's own fishing questions reliably.

### Personal 1.0
FA reliably helps support better fishing decisions.

### Research Tool
FA can support broader fisheries investigations with reproducible analysis.

### Public Tool
FA can be used safely by people who do not know the underlying data structure.

FAQuery belongs primarily to the later stages. The analytical foundation comes first.

---

## Current strategic position

The immediate priority is **not** to build FAQuery.

The immediate priority is to make FA's analytical engine:

- correct
- understandable
- reproducible
- reasonably efficient
- separated from the UI
- capable of answering real fisheries questions

Every improvement to that foundation makes a future FAQuery more powerful.

The strategic sequence is therefore:

```text
Trustworthy FA
     ↓
Better query capabilities
     ↓
Natural-language interface
     ↓
FAQuery
     ↓
Potentially broader platform
```

We build the useful thing first.

The larger possibilities remain open.
