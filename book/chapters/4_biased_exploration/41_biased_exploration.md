# Biased exploration
LCS are being considered as self-adaptive and autonomous learners. However, in order to reach full autonomy, the credit assignment part must decide on their own when to exploit the existing knowledge by taking the most promising action and when to deliberately select an action that is not apparent best to potentially gain additional knowledge.

This decision is commonly referred as to as the explore/exploit dilemma, since obtaining new knowledge through exploration incurs a short-term performance loss, while too much exploitation risks staying on an unnecessary low level of performance in the long term {cite}`sutton2018reinforcement`. Moreover, a real-valued environment introduces a potentially much greater possible search space that makes the problem of acquiring knowledge more challenging and potentially time-consuming.

This chapter aims to narrow the existing gap in research by experimentally comparing four biased exploration strategies. An ALCS agent operating large realm of observation space  might take advantage of the possibility of improving the time needed to form an internal model.

------
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

What is interesting is that Hansmeier and Platzner took effort to compare four strategies optimizating the time for alternating E/E  phases using the XCS algorithm {cite}`hansmeier2021experimental`.  It turned out that despite automized parameter tuning that none of the strategies is superior to the other. On the other side they noticed that certain multi-step environments with scarce reward signal become challenging due to the setting the classifier’s accuracy value too aggressively. Such problem with scarce reward and long action-chains is further discussed in the next chapter. 