# Biased exploration
LCS are being considered as self-adaptive and autonomous learners. However, in order to reach full autonomy, the credit assignment part must decide on their own when to exploit the existing knowledge by taking the most promising action and when to deliberately select an action that is not apparent best to potentially gain additional knowledge.

This decision is commonly referred as to as the explore/exploit dilemma, since obtaining new knowledge through exploration incurs a short-term performance loss, while too much exploitation risks staying on an unnecessary low level of performance in the long term {cite}`sutton2018reinforcement`. In a typical exploration phase the action is selected randomly with intention of an unbiased exploration.

For real-valued environments where the search space is presumably large, such exploration might be inefficient. Certain regions of space might be explored multiple times, while the other ones still remain unknown. Therefore, an approach towards optimizing the process of acquiring knowledge by suggesting more valuable actions is considered herein. 

At first, model learning capabilities in ALCS was enhanced by Stolzmann and Butz by using behavioral capabilities (internal reinforcement learning or lookahead action selection) in {cite}`stolzmann2000first` and by introducing the _action planning_ mechanism {cite}`stolzmann1999latent` {cite}`unold2019introducing`.

Later, Butz suggested that by using computationally inexpensive methods by biasing exploration towards specially chosen regions of search-space, the model can be learned locally {cite}`butz2001biasing`.

This chapter aims to narrow the existing gap in research by experimentally comparing four biased exploration strategies. Any ALCS agent operating large realm of observation space might take advantage of the possibility of improving the time needed to form an internal model. First, a baseline method - _epsilon-greedy_, which is a default option for LCS, will be described. Later two methods introduced by Butz - _action-delay_ and _knowledge-array_ bias. They examine the match set $[M]$ searching for indications which action might result in the highest information gain. Eventually, the latter approach is inspired by an "_Optimistic Initial Values_" approach described by Sutton in {cite}`sutton2018reinforcement`. This strategy turned out to be very effective for Multi-armed bandit problems, where the main objective is to select the most promising action and was never examined in any LCS domain.

------

**Epsilon-Greedy (EG)**

In the epsilon-greedy approach, the agent discovers all regions from the input-space equally, not favoring any specific behavior.  In each step, random action is executed with $p_{explr}$ probability. Then it is chosen uniform randomly from classifiers composing a match set $[M]$. In the case of $1-p_{explr}$, action from the most fitted classifier is executed. By doing so, the agent can occasionally perform the move he thinks is the best at a given time, reinforcing its beliefs about the consequences. 

**Action-Delay (AD)**

This bias is based on the _recency-based_ principle assuming that the action executed a long time ago, might introduce new situation-action-effect triples. To determine which action was executed most long ago at the current time $t$ the $t_{alp}$ field of all classifiers in match set $[M](t)$ is analyzed. For situation $\sigma(t)$ the action of classifier $cl$ with the lowest value of $t_{alp}$ is selected.

In case if there exists an action not represented by any classifier in $[M](t)$ that it is assumed to be experienced most long ago (if ever) and therefore chosen for execution.

**Knowledge Array (KA)**

This method, on the contrary, is based on the _error-based_ principle. For ACS2, a quality $q$ denoting the accuracy of predictions for each classifier can be used to measure it.

The bias generates the knowledge array KA from classifiers in a match set $[M]$ in which each entry specifies the averaged quality for the anticipation for each possible action - see Equation {math:numref}`ka-eq`.

```{math}
:label: ka-eq 

KA[a] = \frac{\sum_{cl \in [M] \wedge cl.A = a}cl.q \cdot cl.num}{\sum_{cl \in [M] \wedge cl.A = a} cl.num}
```

An action with the lowest value in the knowledge array is selected for execution. Similarly, as in the action delay bias, if there are actions not expressed by any classifiers, they are chosen first.

**Optimistic Initial Quality (OIQ)**

By default, newly created classifiers $cl$ have the initial quality set to $cl.q = 0.5$. It can be said that they are biased towards their initial quality. In practice, it should not be a problem because this value will converge to optimal ones over a set of trials. Changing this parameter provides an easy way of supplying the agent with the confidence of the generated classifiers.

In this method, the behavior of the agent was parametrized by an extra parameter - _initial quality_ - $q_0$. Every time a new classifier is generated, its quality is set to new value $cl.q = q_0$.

In all the experiments, there was fixed $q_0 = 0.8$, with the expectation that the agent will be able to build an internal model of knowledge representation faster (especially in early stages). For the action selection strategy, the default epsilon-greedy method was chosen.

## Experimental evaluation
This section presents the motivation, goals and set-up of the performed experiments, as well as their results.

### Research questions
The conducted research aims to answer the following question regarding rACS algorithm and the interval based representation

1. Does the biased exploration methods (AD, KA, OIQ) have the significantly accelerate agent's learning speed?
2. Can the OIQ method improve the performance in terms of ingesting knowledge or reducing classifier population size?

### Goals of the experiments
In all the experiments the difference between four exploration methods will be compared using the ACS2 agent.

```{admonition} _Experiment 1 - Single-step problem performance_
Similarly, as above but in this case a single step 6-bit [](section-topics-environments-rmpx) environment is used introducing much larger possible states space. Since calculating precise model knowledge is infeasible, the key indicators chosen are the average obtained reward and model size.
```

```{admonition} _Experiment 2 - Multiple-step problems performance_
Use two basic multistep environments ([](section-topics-environments-corridor) and [](section-topics-environments-grid)) to determine the differences between the rate of gaining knowledge, ability of building internal pool of classifiers and operating in the environments.
```

```{admonition} _Experiment 3 - Balacing the pole_
The methods will be evaluated on the [](section-topics-environments-cartpole) problem of balacing a pole on a cart. This is a novel problem for the LCS due to specific observation space (where two attributes span to infinity) and specific reward scheme based on how long the pole is kept upright.
```


### Experiments

```{tableofcontents}
```

### Answers to research questions
...

What is interesting is that Hansmeier and Platzner took effort to compare four strategies optimizating the time for alternating E/E  phases using the XCS algorithm {cite}`hansmeier2021experimental`.  It turned out that despite automized parameter tuning that none of the strategies is superior to the other. On the other side they noticed that certain multi-step environments with scarce reward signal become challenging due to the setting the classifier’s accuracy value too aggressively. Such problem with scarce reward and long action-chains is further discussed in the next chapter. 