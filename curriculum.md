# Problem-Solving Curriculum — Complete Topic Map (v2, research-backed)

General-purpose prep for the whole board (FAANG / quant / Goldman / AI-ML labs); difficulty ceiling at Jane Street. Researched against CP-Algorithms, USACO Guide, Codeforces topic lists, Competitive Programmer's Handbook, DDIA, Chip Huyen, the Green Book, Jane Street materials.

**Tier tags (map to the spiral passes):**
- ✅ **core** — FAANG/interview-standard → Pass 1–2 (Easy→Intermediate). *Master all of these.*
- 🔶 **hard/CP** — Codeforces Div2 / advanced interview → Pass 2–3 (Hard).
- 🔴 **elite/impossible** — Codeforces Div1 / IOI / Jane Street puzzles / Putnam → Pass 3, target-dependent (do as the goal demands).

**Legend:** `[ ]` not started · `[~]` learning · `[x]` solid (solve fresh + explain cold).

---

# TRACK 1 — ALGORITHMS & DATA STRUCTURES (the daily core — taken care of fully)

## 1. Foundations
- [ ] ✅ complexity (Big-O, amortized, average-case) · recursion/call-stack · bit ops (AND/OR/XOR/shifts/masks)
- [ ] ✅ two pointers (same/opposite dir) · sliding window (fixed/variable) · prefix sums (1D/2D) · difference arrays
- [ ] 🔶 coordinate compression · submask enumeration · ternary search (unimodal)
- [ ] ✅ sorting (merge/quick/counting/radix, custom comparators) · binary search (sorted)
- [ ] 🔶 **parametric/predicate binary search (on answer)** · real-valued · parallel binary search 🔴

## 2. Arrays & Hashing
- [ ] ✅ hash map/set, frequency, anagram grouping · Kadane · Dutch-flag 3-way partition · Boyer-Moore majority
- [ ] 🔶 rolling/polynomial hashing · inversions (merge-sort) · MEX of subarrays
- [ ] 🔴 anti-hash tests · XOR/multiset hashing · MEX of all subarrays

## 3. Stacks, Queues, Monotonic
- [ ] ✅ stack/queue/deque · **monotonic stack** (next-greater, largest-rectangle) · **monotonic queue** (window min/max) · min-stack/min-queue

## 4. Linked Lists
- [ ] ✅ singly/doubly ops · **Floyd cycle** · reverse/merge/reorder · LRU/LFU cache · skip list 🔶

## 5. Trees & BST
- [ ] ✅ traversals (pre/in/post/level) · BST insert/delete/validate · diameter/height/path-sum · LCA (naive) · serialize/deserialize · self-balancing (AVL/RB conceptual)
- [ ] 🔶 **LCA — binary lifting** · **Euler tour (flatten)** · treap / implicit treap · **DP on trees** · rerooting DP
- [ ] 🔴 **heavy-light decomposition** · **centroid decomposition** · **DSU-on-tree (small-to-large)** · virtual tree · link-cut tree · Euler tour tree · splay tree

## 6. Tries
- [ ] ✅ standard trie (prefix) · word search/autocomplete
- [ ] 🔶 **binary/XOR trie (max-XOR)** · compressed/Patricia · persistent trie

## 7. Heaps
- [ ] ✅ binary heap · top-K / quickselect · merge-K · **two-heap median** · k-closest
- [ ] 🔶 meldable/leftist/skew heap · 🔴 Fibonacci heap

## 8. Union-Find (DSU)
- [ ] ✅ DSU (union-by-rank + path compression)
- [ ] 🔶 weighted/augmented DSU · **DSU with rollback** · DSU-on-tree
- [ ] 🔴 persistent DSU · offline/online dynamic connectivity

## 9. Range-Query Structures
- [ ] 🔶 **Fenwick/BIT** (point/range; 2D) · **segment tree** (point update, range query) · **lazy propagation** · **sparse table (RMQ)** · **sqrt decomposition** · **Mo's algorithm**
- [ ] 🔴 persistent segment tree · segment tree beats · merge-sort tree · Li-Chao tree · segment-tree merging · dynamic/sparse segtree · wavelet tree · Mo's on trees / with updates · fractional cascading

## 10. Graphs
- [ ] ✅ DFS/BFS · connected components · cycle detection (dir/undir) · **topological sort (Kahn + DFS)** · bipartite/2-color · grid-as-graph (islands/flood-fill) · multi-source BFS
- [ ] ✅ **Dijkstra** · **Bellman-Ford** · **Floyd-Warshall** · **0-1 BFS** 🔶 · A*
- [ ] ✅ **MST — Kruskal & Prim** · 🔶 Boruvka · second-best MST · 🔴 directed MST (Chu-Liu) · Steiner tree · matrix-tree theorem
- [ ] 🔶 **bridges & articulation points (Tarjan)** · **SCC (Tarjan/Kosaraju)** + condensation · block-cut tree · **Eulerian path (Hierholzer)** · functional graphs
- [ ] 🔶 **2-SAT (implication graph + SCC)** · difference constraints
- [ ] 🔶 **max-flow (Dinic / Edmonds-Karp)** · **min-cut = max-flow** · bipartite matching (Kuhn) · Hopcroft-Karp · König / Hall · **Hungarian (assignment)**
- [ ] 🔴 min-cost-max-flow · flows with demands · max closure · Stoer-Wagner · Gomory-Hu · blossom (general matching) · dominator tree · Hamiltonian (bitmask)

## 11. Backtracking
- [ ] ✅ subsets/permutations/combinations · combination-sum · N-queens/sudoku · word search · palindrome partition · pruning
- [ ] 🔶 constraint propagation · branch-and-bound · meet-in-the-middle

## 12. Dynamic Programming  *(largest — highest ROI; algorithms backbone)*
- [ ] ✅ 1D (stairs/house-robber/decode) · 2D grid (paths/edit-distance/LCS) · **knapsack** (0/1, unbounded, subset-sum, partition) · **LIS** (O(n log n)) · coin change · interval DP (matrix-chain, burst-balloons) · DP on DAG
- [ ] 🔶 **bitmask DP (TSP/assignment)** · **digit DP** · probability/expected-value DP · DP on trees (combine subtrees) · rerooting
- [ ] 🔶 **SOS DP (sum over subsets)** · broken-profile/plug DP 🔴 · subset convolution 🔴
- [ ] 🔴 **DP optimizations:** convex-hull-trick (static+dynamic) · divide-and-conquer DP · Knuth · **slope trick** · **Aliens trick / WQS binary search** · 1D1D · Hirschberg space-opt

## 13. Greedy
- [ ] ✅ interval scheduling / activity selection · fractional knapsack · Huffman · jump game · gas station
- [ ] 🔶 **exchange-argument proofs** · scheduling (EDF/LLF) · greedy-on-graphs

## 14. Intervals
- [ ] ✅ merge/insert · meeting rooms · **sweep line** · min-arrows · interval tree (augmented BST) 🔶

## 15. Bit Manipulation
- [ ] ✅ XOR tricks / single-number · masks + popcount · subset enumeration via bits · power-of-two
- [ ] 🔶 XOR basis (linear basis) · bitset optimizations

## 16. Math & Number Theory
- [ ] ✅ GCD/LCM (Euclid) · modular arithmetic · **fast exponentiation** · combinatorics (nCr, Pascal, Catalan, stars-and-bars) · **inclusion-exclusion** · sieve of Eratosthenes
- [ ] 🔶 **extended Euclid / modular inverse** · linear Diophantine · **CRT** (+ Garner) · **Lucas' theorem** · **matrix exponentiation (recurrences)** · Euler totient · **Möbius function + inversion** · derangements · Stirling/Bell numbers · linear sieve · **Miller-Rabin** + **Pollard's rho** · game theory (**Nim / Sprague-Grundy**)
- [ ] 🔴 **FFT / NTT** · Walsh-Hadamard (XOR convolution) · **Berlekamp-Massey** · Lagrange interpolation · Gaussian elimination (+ mod 2) · determinant/rank/inverse · discrete log (BSGS) · Burnside/Pólya · LGV lemma · generating functions · Min-25 sieve · floor-sum · LTE lemma · Pell / Stern-Brocot / continued fractions · Schwartz-Zippel · Freivalds'

## 17. Strings
- [ ] ✅ trie · **Rabin-Karp (rolling hash)** · balanced brackets · expression parsing 🔶
- [ ] 🔶 **KMP / prefix function** · **Z-algorithm** · **Manacher (palindromes)** · Lyndon / Duval
- [ ] 🔴 **Aho-Corasick** · **suffix array + LCP (Kasai)** · **suffix automaton (DAWG)** · suffix tree (Ukkonen) · palindromic tree (eertree) · string matching via FFT

## 18. Geometry
- [ ] 🔶 primitives (dot/cross product, orientation) · polar sort · segment intersection · **shoelace area** · **point-in-polygon (winding)** · Pick's theorem · Manhattan↔Chebyshev
- [ ] 🔶 **convex hull (Andrew/Graham)** · **sweep line (segment intersection, closest pair, rectangle union)**
- [ ] 🔴 rotating calipers · min enclosing circle (Welzl) · half-plane intersection · Minkowski sum · Delaunay/Voronoi · 3D geometry · geometric median · simulated annealing

## 19. Randomized & Misc
- [ ] ✅ randomized quickselect · reservoir sampling · Fisher-Yates shuffle · Josephus
- [ ] 🔶 meet-in-the-middle · offline-query tricks · static-to-dynamic · invariants/monovariants · interactive problems
- [ ] 🔴 CDQ divide-and-conquer · matroid intersection · LP / simplex + duality · min-plus convolution · SMAWK · Schreier-Sims

---

# TRACK 1b — MATH / PROBABILITY / QUANT  *(top-bar leg: JS · quant · Goldman)*

## P1. Probability fundamentals
- [ ] ✅ sample spaces, axioms, addition/multiplication rules · **conditional probability + law of total probability** · **Bayes** (medical-test, sequential updating) · independence (pairwise vs mutual; zero-cov ≠ independent)
## P2. Combinatorics
- [ ] ✅ permutations/combinations/multinomial · **inclusion-exclusion** · stars-and-bars · pigeonhole · derangements · Catalan · generating functions (PGF) 🔶
## P3. Expectation
- [ ] ✅ **linearity of expectation** (the #1 technique) · **indicator-variable method** · **law of total expectation (tower)** · conditional expectation as a random variable · **Wald's identity** 🔶 · **optional stopping theorem** 🔴
## P4. Variance / moments
- [ ] ✅ variance, covariance, correlation, Var of sums · Cauchy-Schwarz · MGF / characteristic functions 🔶
## P5. Distributions
- [ ] ✅ Bernoulli/Binomial/Geometric(+memoryless)/Poisson/Uniform/Exponential(+memoryless)/Normal(68-95-99.7) · negative-binomial, hypergeometric · joint/marginal/conditional 🔶 · **order statistics** 🔶 · **Poisson process (merging/thinning/conditioning, PASTA)** 🔴
## P6. Stochastic processes
- [ ] 🔶 **Markov chains** (stationary dist, absorbing, fundamental matrix, hitting times) · **random walks** (recurrence 1D/2D/3D, reflection principle, ballot problem) · **gambler's ruin**
- [ ] 🔴 **martingales + OST** · Brownian motion / Itô / Black-Scholes (Goldman/research) · **branching processes (Galton-Watson)** · **renewal theory / PASTA / inspection paradox** · **Polya urn / exchangeability**
## P7. Classic puzzles
- [ ] ✅ expected-flips-to-pattern (HH/HTH) · **coupon collector** · birthday · **secretary / optimal stopping (1/e)** · Monty Hall · two-envelope · St. Petersburg · broken-stick / meeting / Buffon · **ants-on-polygon** · rope-burning · **hat puzzles / 100 prisoners (cycle strategy)** · **blue-eyes / common knowledge** · pirate/division · weighing · light-switch · 25-horses · egg-drop · Bertrand paradox 🔴 · Sleeping Beauty 🔴
## P8. Game theory / market-making  *(JS/Optiver/SIG differentiator)*
- [ ] 🔶 EV games / making two-sided markets / Bayesian mid-game update · **Kelly criterion (derivation + fractional)** · auction theory (1st/2nd-price, revenue equivalence, winner's curse) · Nash equilibrium · pot odds (SIG) · prediction markets / calibration · market microstructure (adverse selection, inventory, spread) 🔴
## P9. Mental math / estimation
- [ ] ✅ **Zetamac daily** (Optiver "80 in 8") · 2-digit mult / squaring tricks · log/exp estimation (ln2, rule of 72) · **Fermi problems**
## P10. Statistics
- [ ] 🔶 descriptive · sampling/estimators (unbiased, n-1) · **MLE** · **hypothesis testing** (Type I/II, p-value, t/z/chi-sq, power) · confidence intervals (+ misinterpretation trap) · **CLT** vs LLN · regression (OLS, Ridge/Lasso, logistic) · Bayesian vs frequentist · time series (AR/MA/ARMA, stationarity, cointegration, GARCH) 🔴
## P11. Linear algebra
- [ ] 🔶 matrix ops/det/inverse · **eigenvalues/eigenvectors** + diagonalization (Markov long-run) · covariance matrix / PCA / Cholesky · least squares
## P12. Information theory (research)
- [ ] 🔴 entropy · KL divergence · mutual information · Kelly–entropy connection

---

# TRACK 2 — SYSTEM DESIGN  *(weekly; all companies)*

## SD1. Framework & foundations
- [ ] ✅ 6-step framework (clarify → estimate → API/data model → high-level → deep-dive → bottlenecks) · **back-of-envelope** (QPS, storage, bandwidth) · **latency numbers** · SLA/availability tiers · seniority signal: "where does this NOT need to scale?"
## SD2. Networking
- [ ] ✅ TCP vs UDP · HTTP/1.1/2/3(QUIC) · TLS/mTLS · REST vs **gRPC** vs GraphQL · **WebSockets / SSE / long-polling** · WebRTC (STUN/TURN) · DNS / GeoDNS / anycast · **CDN** (push/pull, invalidation, edge) · **load balancing (L4 vs L7, algorithms)** · reverse proxy / API gateway / service mesh
## SD3. Consistency & distributed theory
- [ ] ✅ **CAP** + 🔶 **PACELC** · consistency spectrum (eventual → causal → linearizable → strict-serializable) · **ACID vs BASE** + isolation levels + anomalies (write-skew, phantom)
## SD4. Databases
- [ ] ✅ SQL vs NoSQL decision framework · indexing (B-tree/hash/composite/covering) · **B-tree vs LSM-tree internals** (compaction, SSTable, WAL, bloom filters, write amplification) · **MVCC / snapshot isolation** · NoSQL types (KV/doc/wide-column/graph/time-series/search/**vector**)
- [ ] 🔶 **replication** (single/multi-leader, leaderless, quorum W+R>N, read-repair, anti-entropy/Merkle) · **partitioning/sharding** (range/hash/**consistent hashing**, hot shards, scatter-gather) · **CDC** (Debezium, dual-write problem)
## SD5. Caching
- [ ] ✅ cache tiers · strategies (cache-aside, read/write-through, write-behind) · eviction (LRU/LFU) · **failure modes (thundering herd, penetration, avalanche)** + fixes · Redis (data structures, persistence, cluster, Redlock)
## SD6. Messaging & streaming
- [ ] 🔶 queues vs pub/sub · delivery semantics (at-most/least/exactly-once) · DLQ · **Kafka** (partitions/offsets/consumer-groups/compaction/exactly-once) · stream processing (Flink, windowing, watermarks) · **event sourcing + CQRS** · **backpressure**
## SD7. Consensus & coordination
- [ ] 🔶 **Raft** (leader election, log replication) · Paxos (conceptual) · leader election (ZK/etcd) · distributed locks + **fencing tokens** · **2PC / Saga (choreography vs orchestration) / Outbox-Inbox** · **vector/Lamport clocks** · gossip protocol · quorum
## SD8. Reliability
- [ ] ✅ failover (active-passive/active-active, RTO/RPO) · **idempotency keys** · **rate limiting (token/leaky bucket, sliding window)** · **circuit breaker / bulkhead** · retry+backoff+jitter · graceful degradation / load shedding
## SD9. Storage & probabilistic DS
- [ ] 🔶 object/blob storage (S3, pre-signed URLs, erasure coding) · distributed FS (HDFS/GFS) · time-series DB · search/inverted index (BM25) · vector DB (HNSW/IVF)
- [ ] 🔶 **bloom filter · count-min sketch · HyperLogLog · Merkle tree · skip list · CRDTs · geohash/quadtree/S2**
## SD10. Observability / security / architecture
- [ ] 🔶 metrics/logs/traces · **SLI/SLO/SLA + error budgets** · auth (JWT/OAuth2/PKCE) · mTLS · RBAC/ABAC · secrets mgmt · monolith vs microservices · service discovery · BFF/strangler/sidecar
## SD11. Finance / low-latency  *(JS / Goldman)*
- [ ] 🔴 **order matching engine** (price-time priority, order book) · **FIX protocol** · low-latency (lock-free, **LMAX Disruptor**, CPU pinning, kernel bypass) · pre-trade risk · audit logging / event sourcing · 5-nines design
## SD12. LLM/ML system design (see Track 3) + canonical problems
- [ ] **Tier 1:** URL shortener · rate limiter · KV store · distributed cache · consistent hashing · unique-ID (Snowflake)
- [ ] **Tier 2:** news feed · chat · notifications · typeahead · web crawler · video streaming · file storage · Instagram/Twitter
- [ ] **Tier 3:** Uber/ride-share · proximity service · maps/ETA · reservation system · message queue · **payment system** · digital wallet · ad-click aggregation · metrics monitoring · S3
- [ ] **Tier 4:** **stock exchange/matching** · leaderboard · collab editing (OT/CRDT) · video conferencing (WebRTC, SFU/MCU) · distributed lock service · CI/CD system · search engine · recommendation · fraud detection · ChatGPT-style LLM service

---

# TRACK 3 — ML SYSTEM DESIGN  *(weekly; AI/ML roles incl. JS ML-Engineer)*

## ML1. Framework & formulation
- [ ] ✅ 8-step framework (clarify → ML-vs-non-ML → **business vs model metrics** → scale → architecture (offline+online) → deep-dive → eval plan → failure modes) · task selection (rank/classify/regress/retrieve/generate) · proxy-label / surrogate-objective traps · multi-task formulation
## ML2. Data
- [ ] ✅ sources (implicit/explicit/human/synthetic) · augmentation · labeling (HITL, weak supervision/Snorkel, active learning, **inter-annotator agreement**) · sampling & imbalance (SMOTE, class-weight, **hard-negative mining**, **debiased negative sampling**, reservoir, **temporal split**)
- [ ] 🔶 data quality/validation (schema, KS/chi-sq) · **point-in-time correctness** · **target vs feature leakage** · lineage/provenance
## ML3. Features
- [ ] ✅ numerical/categorical/text/image/temporal/graph/sequential/cross features · encoding (one-hot/target/hashing) · **embeddings** (Word2Vec, SBERT, two-tower, CLIP)
- [ ] 🔶 **feature store** (offline/online, point-in-time joins) · **training-serving skew** (the #1 prod failure) · feature versioning · pipelines (batch/stream, Lambda/Kappa, watermarks) · embedding drift
## ML4. Modeling
- [ ] ✅ baseline-first · inductive biases · GBDT (XGBoost/LightGBM) · two-stage retrieve-rank · multi-task (MMoE/PLE) · **calibration (Platt/isotonic/temperature)** · uncertainty (epistemic vs aleatoric, conformal)
- [ ] 🔶 training pipelines (mixed precision, grad accumulation, LR schedules, regularization, loss functions: focal/triplet/contrastive/InfoNCE)
- [ ] 🔶 **distributed training:** **DDP/data-parallel (ring-allreduce)** · tensor/pipeline parallelism · **ZeRO 1/2/3** · **FSDP** · 3D parallelism · NCCL/comm bottlenecks · elastic/fault-tolerant training
- [ ] 🔶 HPO (Bayesian/Optuna, Hyperband/ASHA, PBT) · NAS · **Chinchilla compute-optimal scaling**
## ML5. Offline evaluation
- [ ] ✅ precision/recall/F1, AUC-ROC/PR, **MAP@K/NDCG@K**, RMSE/MAE, BLEU/ROUGE/BERTScore, calibration (ECE) · **slicing analysis** · error analysis (FP/FN cost asymmetry)
- [ ] 🔶 **offline-online gap / Goodhart** · test-set construction (temporal/stratified, contamination) · **counterfactual eval (IPS)**
## ML6. Serving & inference
- [ ] ✅ online vs batch vs streaming · serving frameworks (Triton/TF-Serving/TorchServe/**vLLM**/TGI/TensorRT)
- [ ] 🔶 **dynamic batching** · **continuous batching** · **KV-cache** · **PagedAttention** · **speculative decoding** · **quantization (INT8/INT4, GPTQ/AWQ)** · distillation · pruning · torch.compile/ONNX · CUDA graphs · **prefill vs decode (compute vs memory-bound)** · chunked prefill · **Flash Attention** · hardware (A100/H100, TPU, roofline, memory-bandwidth wall)
## ML7. Retrieval & ranking
- [ ] 🔶 **ANN (FAISS/HNSW/ScaNN/DiskANN, IVF+PQ, LSH)** · vector DBs · hybrid search (dense+BM25, RRF) · **two-tower / dual-encoder** (in-batch/hard/debiased negatives, InfoNCE) + its cross-feature limitation · **multi-stage ranking (L1/L2/L3)** · learning-to-rank (pointwise/pairwise/listwise, LambdaMART) · position-bias correction (IPW) · diversity (MMR/DPP)
## ML8. LLM-specific
- [ ] 🔶 transformer internals (attention, **RoPE/ALiBi**, pre/post-norm, **GQA/MQA**, **MoE** routing) · context extension (YaRN, sliding window)
- [ ] 🔶 fine-tuning/alignment (**SFT**, **LoRA/QLoRA/DoRA**, **RLHF/PPO**, **DPO**, **GRPO/RLVR**, catastrophic forgetting) · KL-penalty / reward-hacking · Constitutional AI / RLAIF
- [ ] 🔶 **RAG at scale** (chunking, query rewrite/HyDE, hybrid retrieval, rerank, multi-hop, **faithfulness/groundedness**, metadata filtering, table-aware chunking) · prompt pipelines + **semantic caching** + injection defense · **LLM eval (LLM-as-judge + its biases, hallucination detection, RAG triad)** · **agentic systems** (tool-calling, ReAct, multi-agent, memory, planning, failure modes) · guardrails (PII, toxicity, schema, latency cost)
## ML9. MLOps
- [ ] 🔶 experiment tracking (W&B/MLflow) + model registry · orchestration (Airflow/Kubeflow/Metaflow) · **CI/CD for ML** (validation gate, **shadow/canary/blue-green**, soak period) · data versioning (DVC, Delta/Iceberg)
## ML10. Monitoring & continual learning
- [ ] 🔶 **drift** (data/covariate, concept, label, upstream) · detection (KS, **PSI**, JS-divergence, embedding drift) · monitoring metrics · **feedback-loop amplification** · retraining triggers · online learning / replay buffers
## ML11. Responsible AI
- [ ] 🔴 fairness (demographic parity/equalized odds, **impossibility theorem**) · privacy (**differential privacy / DP-SGD**, federated learning, membership-inference) · interpretability (SHAP/LIME, faithfulness vs plausibility)
## ML12. Canonical ML designs
- [ ] recsys (video/feed/product/music/jobs/PYMK) · search/ranking (web/e-commerce/visual/code) · ads (CTR/CVR, auction, **explore-exploit: UCB/Thompson**) · trust&safety (fraud/spam/bot/moderation, adversarial) · CV (visual search, detection, OCR) · NLP (translation, QA, summarization, NER) · forecasting (ETA, demand, price) · matching (ride/marketplace) · **LLM designs** (ChatGPT-scale serving, enterprise RAG, coding assistant, multi-agent research, moderation, eval pipeline)

---

## Cadence & how to use
- **Algorithms (Track 1):** daily 3 problems via the selection rule in `CLAUDE.md`. **Spiral:** Pass 1 = all ✅ to Intermediate (≈4 wks) → Pass 2 = ✅ Hard + 🔶 → Pass 3 = 🔴 as the goal demands. Do NOT chase 🔴 before ✅ breadth exists.
- **Quant (Track 1b):** Zetamac daily now; fold probability into the daily weak-area slot from Pass 2; 🔴 only for JS/quant depth.
- **System + ML System Design (Tracks 2–3):** 1 each per week, narrated end-to-end → `progress/design-log.md`. ✅ first, then 🔶.
- **Tiering rule of thumb:** ✅ everyone needs · 🔶 = the real interview differentiator (FAANG-hard + Codeforces Div2) · 🔴 = Jane-Street-puzzle / Codeforces-Div1 / research ceiling — pursue per target, not exhaustively.
