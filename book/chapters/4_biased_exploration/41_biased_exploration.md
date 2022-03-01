# Biased exploration
LCS are being considered as self-adaptive and autonomous learners. However, in order to reach full autonomy, the credit assignment part must decide on their own when to exploit the existing knowledge by taking the most promising action and when to deliberately select an action that is not apparent best to gain additional knowledge potentially.

This decision is commonly referred to as the explore/exploit (E/E) dilemma, since obtaining new knowledge through exploration incurs a short-term performance loss, while too much exploitation risks staying on an unnecessarily low level of performance in the long term {cite}`sutton2018reinforcement`. In a typical exploration phase, the action is selected randomly with the intention of an unbiased exploration.

Such exploration might be inefficient for real-valued environments where the search space is presumably large. Certain regions of space might be explored multiple times, while the other ones remain unknown. Therefore, an approach towards optimizing the process of acquiring knowledge by suggesting more valuable actions is considered herein. 

At first, model learning capabilities in ALCS was enhanced by Stolzmann and Butz by using behavioural capabilities (internal reinforcement learning or lookahead action selection) in {cite}`stolzmann2000first` and by introducing the _action planning_ mechanism {cite}`stolzmann1999latent` {cite}`unold2019introducing`.

Later, Butz suggested that by using computationally inexpensive methods by biasing exploration towards specially chosen regions of search-space, the model can be learned locally {cite}`butz2001biasing`.

This chapter aims to narrow the existing gap in research by experimentally comparing four biased exploration strategies. Any ALCS agent operating a large realm of observation space might take advantage of the possibility of improving the time needed to form an internal model. First, a baseline method - _epsilon-greedy_, which is a default option for LCS, will be described. Later two methods were introduced by Butz - _action-delay_ and _knowledge-array_ bias. They examine the match set $[M]$ searching for indications of which action might result in the highest information gain. Eventually, the latter approach is inspired by an "_Optimistic Initial Values_" approach described by Sutton in {cite}`sutton2018reinforcement`. This strategy turned out to be very effective for Multi-armed bandit problems, where the main objective is to select the most promising action and was never examined in any LCS domain.
In most experiments, the rACS agent builds the population consisting primarily of Region 1 interval predicates. The amount of attributes represented as Region 3 and 4, spanning to the maximum value from the right side, tends to diminish. However, the results are correlated with the number of trials that were kept the same in all cases. More precise boundary representation naturally would require more trials to converge. However, for the first 4 bits, there is the following trend can be noticed when intensifying encoding resolution:

- Ratio of Region 1 attributes increases
- Ratio of Region 2, 3, 4 attributes decreases

This is caused by the lack of online rule compaction or consolidation mechanism. The only possibility for the agent to create a more general attribute is due to the mutation algorithm controlled by the $\epsilon_{mutation}$ parameter. However, this value must be set carefully because limitations of selected encoding resolution can inadvertently ignore its effect.

The other metrics also show the hypothesis about the need for more trials. The size of the overall population is correlated with the number of encoding bits, but it became more difficult for the agent to discriminate between reliable classifiers. For example, when using 5-bits encoding after {glue:}`32_e2_trials` trials, there is no single reliable classifier despite having a population with more than 10 thousand individuals.

The experiment with 1-bit encoding also confirms the situation when it is impossible to learn the environment with hyper-plane decision boundary successfully. Such representation cannot handle regularities, resulting in unreliable classifiers and random average rewards from exploit runs.


```{admonition} Epsilon-Greedy (EG)
:class: tip

In the epsilon-greedy approach, the agent equally discovers all regions from the input-space, not favouring any specific behaviour. In each step, random action is executed with $p_{explr}$ probability. Then it is chosen uniform randomly from classifiers composing a match set $[M]$. In the case of $1-p_{explr}$, action from the most fitted classifier is executed. By doing so, the agent can occasionally perform the move he thinks is the best at a given time, reinforcing its beliefs about the consequences. 
```

```{admonition} Action-Delay (AD)
:class: tip

This bias is based on the _recency-based_ principle assuming that the action executed a long time ago might introduce new situation-action-effect triples. To determine which action was executed most long ago at the current time $t$ the $t_{alp}$ field of all classifiers in a match set $[M](t)$ is analyzed. For situation $\sigma(t)$ the action of classifier $cl$ with the lowest value of $t_{alp}$ is selected.

In case there exists an action not represented by any classifier in $[M](t)$ that it is assumed to be experienced most long ago (if ever) and therefore chosen for execution.
```

````{admonition} Knowledge Array (KA)
:class: tip

This method, on the contrary, is based on the _error-based_ principle. For ACS2, a quality $q$ denoting the accuracy of predictions for each classifier can be used to measure it.

The bias generates the knowledge array KA from classifiers in a match set $[M]$ in which each entry specifies the averaged quality for the anticipation for each possible action - see Equation {math:numref}`ka-eq`.

```{math}
:label: ka-eq 

KA[a] = \frac{\sum_{cl \in [M] \wedge cl.A = a}cl.q \cdot cl.num}{\sum_{cl \in [M] \wedge cl.A = a} cl.num}
```

An action with the lowest value in the knowledge array is selected for execution. Similarly, as in the action delay bias, if any classifiers do not express actions, they are chosen first.
````

```{admonition} Optimistic Initial Quality (OIQ)
:class: tip

By default, newly created classifiers $cl$ have the initial quality set to $cl.q = 0.5$. It can be said that they are biased towards their initial quality. In practice, it should not be a problem because this value will converge to optimal ones over a set of trials. Changing this parameter provides an easy way of supplying the agent with the confidence of the generated classifiers.

In this method, the agent's behaviour was parametrized by an extra parameter - _initial quality_ - $q_0$. Every time a new classifier is generated, its quality is set to new value $cl.q = q_0$.

In all the experiments, there was fixed $q_0 = 0.8$, expecting the agent to build an internal model of knowledge representation faster (especially in the early stages). For the action selection strategy, the default epsilon-greedy method was chosen.
```

Interestingly, Hansmeier and Platzner made an effort to compare four strategies optimizing the time for alternating E/E  phases using the XCS algorithm {cite}`hansmeier2021experimental`. It turned out that despite automized parameter tuning that none of the strategies is superior to the other. On the other side, they noticed that specific multi-step environments with scarce reward signals become challenging due to setting the classifier’s accuracy value too aggressively. Such problem with scarce reward and long action-chains is further discussed in the following chapter. 

## Experimental evaluation
This section presents the motivation, goals and setup of the performed experiments and their results.

### Research questions
The conducted research aims to answer the following question regarding the rACS algorithm and the interval-based representation

1. Does the biased exploration methods (AD, KA, OIQ) significantly accelerate the agent's learning speed?
2. Can the OIQ method improve the performance of ingesting knowledge or reducing classifier population size?

### Goals of the experiments
The difference between the four exploration methods will be compared using the ACS2 agent in all the experiments.

```{admonition} _Experiment 1 - Single-step problem performance_
Similarly, as above but in this case, a single step 6-bit [](section-topics-environments-rmpx) environment is used, introducing much larger possible states space. Since calculating precise model knowledge is infeasible, the key performance indicators chosen are the average obtained reward and model size.
```

```{admonition} _Experiment 2 - Multiple-step problems performance_
Use two basic multistep environments ([](section-topics-environments-corridor) and [](section-topics-environments-grid)) to determine the differences between the rate of gaining knowledge, the ability to build an internal pool of classifiers and operating in the environments.
```

```{admonition} _Experiment 3 - Balacing the pole_
The methods will be evaluated on the [](section-topics-environments-cartpole) problem of balancing a pole on a cart. This is a novel problem for the LCS due to specific observation space (where two attributes span to infinity) and a specific reward scheme based on how long the pole is kept upright.
```


### Experiments

```{tableofcontents}
```

### Answers to research questions
#### Q1: Does the biased exploration methods (AD, KA, OIQ) have significantly accelerate the agent's learning speed?
Conducted research showed that biased exploration methods like AD and KA positively impact the knowledge evolution process. The OIQ performance was correlated with the basic EG method and did not yield any competitive performance. 

#### Q2: Can the OIQ method improve the performance in terms of ingesting knowledge or reducing classifier population size?
The impact of initializing classifier quality with a higher (positive) value resulted in having a neglectable effect on all evaluated metrics. The OIQ, in theory, can perform better when forming a population of reliable classifiers, but for the investigated problems, the performance was highly correlated with a default EG method.
