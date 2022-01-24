# Biased exploration

Increase the speed of gaining knowledge by determining the most valuable regions of the input-space. Tell why it is important for the real-valued case. Describe the action selection, methods (epsilon-greedy, action delay, knowledge-array and OIQ - novel).

## Experimental evaluation
This section presents the motivation, goals and set-up of the performed experiments, as well as their results.

## Research questions
The conducted research aims to answer the following question regarding rACS algorithm and the interval based representation

1. Does the biased exploration methods (AD, KA, OIQ) have the significantly accelerate agent's learning speed?
2. Can the OIQ method improve the performance in terms of ingesting knowledge or reducing classifier population size?

## Goals of the experiments
In all the experiments the difference between four exploration methods will be compared using the ACS2 agent.

```{admonition} _Experiment 1 - Multi-steps problems performance_
Use two basic multistep environments ([](section-topics-environments-corridor) and [](section-topics-environments-grid)) to determine the differences between the rate of gaining knowledge, ability of building internal pool of classifiers and operating in the environments.
```

```{admonition} _Experiment 2 - Single-step problem performance_
Similarly, as above but in this case a single step 6-bit [](section-topics-environments-rmpx) environment is used introducing much larger possible states space. Since calculating precise model knowledge is infeasible, the key indicators chosen are the average obtained reward and model size.
```

```{admonition} _Experiment 3 - Balacing the pole_
The methods will be evaluated on the [](section-topics-environments-cartpole) problem of balacing a pole on a cart. This is a novel problem for the LCS due to specific observation space (where two attributes span to infinity) and specific reward scheme based on how long the pole is kept upright.
```


## Experiments

```{tableofcontents}
```

## Answers to research questions
...