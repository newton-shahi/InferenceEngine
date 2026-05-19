# Rule-Based Expert System with Forward Chaining & Explanation Trees

A lightweight, production-grade Rule-Based Expert System written in Python. This repository explores the architectural pipeline of knowledge-based systems—progressing from low-level working memory components and handwritten Domain Specific Language (DSL) parsers, up to formal context-free grammar parsing (via `lark`) and structured explanation tracking (Provenance/Derivation Trees).

The system concludes with a modularized agricultural expert engine (`agroEngine`) designed to evaluate complex agronomic risk scenarios like `yield_risk` and answer *why* specific remediation strategies were triggered.

---

## 🚀 Quick Start & How to Open

### Prerequisites
- **Python 3.10+** (leveraging structural typing, explicit type hints, and advanced pattern matching components)
- **Lark Suite**: For managing formal grammar evaluations.

## 🧠 Project Architecture (Learning Progression)
This project is built incrementally, where each module improves the previous system.

### G21 — Working Memory System
*Core fact storage layer.*
* Defines `Fact` objects
* Stores current world state
* **Supports:** `assert fact`, `query fact`, and `retract fact`

### G22 — Handwritten DSL Parser
*First rule parsing implementation.*
* Parses rules using string logic: `IF`, `THEN`, `AND`, `IS`
* Converts raw text $\rightarrow$ structured rules

### G23 — File-Based Rule Loader
*Adds external rule support.*
* Loads rules from `.txt` files
* Supports batch rule ingestion
* **Example:** `agro_rules.txt`

### G24 — Formal Grammar (Lark)
*Replaces manual parsing.*
* Uses EBNF grammar
* Produces structured parse trees
* More robust and scalable parsing

### G25 — AST Transformer Layer
*Converts parse tree into executable objects.*
* Parse tree $\rightarrow$ Rule
* Parse tree $\rightarrow$ Condition
* Separates syntax from logic execution

### G26 — Rule Evaluation Engine
*Evaluates rule conditions.*
* Matches facts in working memory
* Returns boolean condition satisfaction
* Prepares rules for inference cycle

### G27 — Forward Chaining Engine
*Core inference mechanism.*
* Iteratively evaluates rules
* Fires matching rules
* Adds new inferred facts
* Repeats until no new facts (fixed point)

### G28 — Explanation Tree System
*Adds explainability layer.*
* Tracks rule firing history
* Stores parent-child fact relationships
* Builds derivation trees
* Enables “why” explanations for any fact

---

##  Final System: agroEngine
The final system integrates all modules into a complete expert system.

* **Input:** Environmental conditions such as `soil_moisture`, `rainfall`, `temperature`, and `humidity`.
* **Output:** Derived agricultural insights such as `drought_risk`, `pest_risk`, and `yield_risk`.
* **Key Feature:** Every inferred fact contains a full explanation chain showing how it was derived.

---

### 🙏 Reference
Learned from and inspired by [santabasnet/multi_facts_chat_engine
](https://github.com/santabasnet/multi_facts_chat_engine/tree/main).