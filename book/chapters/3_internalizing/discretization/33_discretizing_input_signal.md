# Discretizing input signal

Previous chapter proved that ALCS are capable of operating in real-valued realm by using UBR interval representation. Due to the underlying foundations, certain limitations were reveled, requiring major rethinking in order to hold virtues like balancing compact population size while maintaining maximum accuracy and generalization.

But ALCS are not limited to ternary alphabets - they can be arbitrary extended to any discrete amount of symbols. This provides an opportunity to split the range of perception value into $k$ fixed-sized intervals (_buckets_). By performing such [](section-topics-real-discretization), each consecutive symbol represents a successive interval. The biggest benefit is that no modifications to internal components are needed for any of the investigated systems, just an additional layer between environment-agent interface. The interface is capable of executing any predefined signal transformation, like assigning each observation attributes using the same logic or having dedicated rules for each of them (in case when range of values varies significantly).

This chapter aims to contrast the latent learning capabilities of ACS, ACS2, YACS systems in both single- and multistep environments. Furthermore, they were compared to basic RL algorithm competent of building internal environmental model and lookahead planning - Dyna-Q {cite}`sutton2018reinforcement`.

```{admonition} Dyna Architecture
RL algorithms like Q-Learning cannot perform operations considered “cognitive”, such as reasoning and planning (because they do not learn an internal model of the environment’s dynamics). Dyna architecture is an online planning agent with internal environmental model.

Each $(S_t, A_t)$ tuple outputs a prediction of the resultant reward and next state $(R_{t+1}, S_{t+1})$. The environmental model is table-based and assumes the environment is deterministic. After each transition $(S_t, A_t) \rightarrow (R_{t+1}, S_{t+1})$ the model records in its table entry for $(S_t, A_t)$ the prediction that $(R_{t+1}, S_{t+1})$ will deterministically follow.

When interacting with the environment, real experiences are augmented by performing learning steps using the internal model. The planning here is the random-sample one-step tabular Q-learning method that only uses previously experienced samples.
```

## Experimental evaluation
This section presents the motivation, goals and set-up of the performed experiments, as well as their results.

### Research questions
The conducted research aims to answer the following questions about bucketing discretization:

1. Can popular ALCS systems build the internal model of the environment when discretizing the real-valued input signal into fixed-width buckets?
2. Which system creates the most compact and general population of classifiers?
3. What is the relative trial execution time for each evaluated system?
4. How selected  systems relates to the benchmark Dyna-Q algorithm?

### Goals of the experiments
```{admonition} _Experiment 3 - Single step environment performance_
The aim of this experiments is to determine the agents' latent learning competences using the [](section-topics-environments-rmpx) discretized into fixed amount of buckets.
```

```{admonition} _Experiment 4 - Multistep environments performance_
Corresponding comparison is performed for two multistep problems with similar regularities - [](section-topics-environments-corridor) and [](section-topics-environments-grid).
```

### Experiments

```{tableofcontents}
```

### Answers to research questions

#### Q1: Can popular ALCS systems build the internal model of the environment when discretizing the real-valued input signal into fixed-width buckets?
...

#### Q2: Which system creates the most compact and general population of classifiers?
...

#### Q3: What is the relative trial execution time for each evaluated system?
...

#### Q4: How selected  systems relates to the benchmark Dyna-Q algorithm?
...