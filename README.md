# Rule-Based Expert System with Forward Chaining & Explanation Trees

A lightweight, production-grade Rule-Based Expert System written in Python. This repository explores the architectural pipeline of knowledge-based systems—progressing from low-level working memory components and handwritten Domain Specific Language (DSL) parsers, up to formal context-free grammar parsing (via `lark`) and structured explanation tracking (Provenance/Derivation Trees).

The system concludes with a modularized agricultural expert engine (`agroEngine`) designed to evaluate complex agronomic risk scenarios like `yield_risk` and answer *why* specific remediation strategies were triggered.

---

## 🚀 Quick Start & How to Open

# Build the Docker image (no cache)
docker compose build --no-cache

# Run the application
docker compose up

##  Final System: agroEngine
The final system integrates all modules into a complete expert system.

* **Input:** Environmental conditions such as `soil_moisture`, `rainfall`, `temperature`, and `humidity`.
* **Output:** Derived agricultural insights such as `drought_risk`, `pest_risk`, and `yield_risk`.
* **Key Feature:** Every inferred fact contains a full explanation chain showing how it was derived.

---

### 🙏 Reference
Learned from and inspired by [santabasnet/multi_facts_chat_engine
](https://github.com/santabasnet/multi_facts_chat_engine/tree/main).