# Discretizing input signal
The previous chapter proved that ALCS could operate in a real-valued realm using UBR interval representation. Due to the underlying foundations, certain limitations were revealed, requiring major rethinking to hold virtues like balancing compact population size while maintaining maximum accuracy and generalization.

Nevertheless, ALCS are not limited to ternary alphabets - they can be arbitrarily extended to any discrete number of symbols. This provides an opportunity to split the range of perception value into $k$ fixed-sized intervals (_buckets_). Each consecutive symbol represents a successive interval by performing such [](section-topics-real-discretization). The most significant advantage is that no modifications to internal components are needed for any of the investigated systems - just an additional layer between the environment-agent interface. The interface is capable of executing any predefined input transformation, like assigning each observation attribute using the same logic or having dedicated rules for each of them (in a case when a range of values varies significantly). Each experiment uses an external _discretizer_, capable of transforming raw environmental signal $\sigma \rightarrow \Sigma$ using desired attribute resolution. All investigated ALCS algorithms share a similar behavioural act cycle; therefore, it is possible to use a shared implementation of an external discretizer in each of the investigated systems in a standardized approach. The difference between approach suggested by Unold and Mianowski {cite}`unold2016real` is the distinct separation of discretization component that can be applied independently in any of the ALCS algorithms.

This chapter aims to contrast the latent learning capabilities of ACS, ACS2, YACS systems in both single- and multistep environments. Furthermore, they were compared to basic RL algorithm competent of building internal environmental model and lookahead planning - Dyna-Q {cite}`sutton2018reinforcement`.

```{admonition} Dyna Architecture
RL algorithms like Q-Learning cannot perform operations considered “cognitive”, such as reasoning and planning (because they do not learn an internal model of the environment’s dynamics). Dyna architecture is an online planning agent with an internal environmental model.

Each $(S_t, A_t)$ tuple outputs a prediction of the resultant reward and next state $(R_{t+1}, S_{t+1})$. The environmental model is table-based and assumes the environment is deterministic. After each transition $(S_t, A_t) \rightarrow (R_{t+1}, S_{t+1})$ the model records in its table entry for $(S_t, A_t)$ the prediction that $(R_{t+1}, S_{t+1})$ will deterministically follow.

Real experiences are augmented by performing learning steps using the internal model when interacting with the environment. The planning here is the random-sample one-step tabular Q-learning method that only uses previously experienced samples.
```

## Experimental evaluation
This section presents the motivation, goals and setup of the performed experiments, as well as their results.

### Research questions
The conducted research aims to answer the following questions about bucketing discretization:

1. Can popular ALCS systems build the internal model of the environment when discretizing the real-valued input into fixed-width buckets?
2. Which system creates the most compact and general population of classifiers?
3. What is the relative trial execution time for each evaluated system?
4. How selected systems relate to the benchmark Dyna-Q algorithm?

### Goals of the experiments
```{admonition} _Experiment 3 - Single-step environment performance_
This experiments aim to determine the agents' latent learning competencies using the [](section-topics-environments-rmpx) discretized into a fixed amount of buckets.
```

```{admonition} _Experiment 4 - Multiple-step environments performance_
Corresponding comparison is performed for two multistep problems with similar regularities - [](section-topics-environments-corridor) and [](section-topics-environments-grid).
```

### Experiments

```{tableofcontents}
```

### Answers to research questions
#### Q1: Can popular ALCS systems build the internal model of the environment when discretizing the real-valued input into fixed-width buckets?
All investigated ALCS systems with common rule structure (ACS, ACS2, YACS) managed to deal with real-valued input represented as a vector of nominal values. The corresponding changes affected only the interface layer, leaving agent mechanisms intact. Moreover, the nature of the _don't care_ and _pass-through_ symbol was fully preserved, which additionally increased model interpretability.  

#### Q2: Which system creates the most compact and general population of classifiers?
ACS2 with GA enhancement proved to evolve the most general and compact population of classifiers diligently. However, specific problems were discovered in ACS, which was unable to progress by creating novel classifiers or YACS that suffers from insufficient heuristics and lacks a dedicated generalization mechanism. 

#### Q3: What is the relative trial execution time for each evaluated system?
Due to its simplicity, Dyna-Q was the fastest algorithm in all comparisons. However, for the ALCS family, the ACS and ACS2 are much faster than YACS, mainly due to YACS processes where each visited state is stored internally despite generalization. Those states are processed in each trial, which for large problem spaces might squander computational resources. 

#### Q4: How selected systems relates to the benchmark Dyna-Q algorithm?
The Dyna-Q is a traditional benchmarking RL problem capable of representing the consequences of certain actions in particular states. The most obvious difference is the lack of generalization capabilities, which forces the Dyna-Q to model all encountered transitions explicitly. This leads to a larger internal model size and potentially slower formation of an optimal policy. However, on the other side, a lack of sophisticated, interacting components results in more transparent workflow and swifter execution.