(section-topics-kpi)=
# Key performance indicators

The ALCS comprise complex mechanisms such as ALP or GG, which might be hard to comprehend and analyse. Therefore, in order to visualize system behaviour over time and assess its performance certain metrics reflecting their nature were chosen. This section presents several metrics used across further experimental evaluations. Each of them can be collected at a particular interval of time (for example every ten trials) and can access the properties of both the environment and the agent within the single simulation.

(section-topics-kpi-population-size)=
## Classifier population size
Each LCS creates an internal population of classifiers. Knowing it's total size $|P|$ represents the agent's ability to express the internal model of the environment. Having a smaller population size, when maintaining a high performance also means that the agent is commendable at building more compact and compressed representation of knowledge.

Besides knowing the total population size, it's subset of reliable classifiers size $|P_{\text{reliable}}|$ might also be easily obtained - equation {math:numref}`kpi-reliable-population-eq`. Both the total population and reliable population size should converge over the course of an experiment to a single value.

```{math}
:label: kpi-reliable-population-eq 

P_{\text{reliable}} = \{ cl \in P : cl.q \geq \theta_r \}
```

(section-topics-kpi-generalization)=
## Generalization
The generalization metrics reflect the agent's generalization abilities. It is calculated by analyzing all classifiers in a population $P$. The proportion of condition attributes containing the wildcard symbol is calculated using the equation {math:numref}`kpi-generalization-eq`

```{math}
:label: kpi-generalization-eq

\text{Generalization}(P) = \frac{ \vert \bigcup \bigg( cond.att | cond \in \big( cl.cond | cl \in P \big) \land cond.att = \# \bigg) \vert }{ \vert \bigcup \bigg( cond.att | cond \in \big( cl.cond | cl \in P \big) \bigg) \vert }
```

The greater generalization score means that the algorithm tends to create classifiers covering larger portion of the observation space, therefore creating more compact solution of the problem.

(section-topics-kpi-knowledge)=
## Knowledge
The knowledge KPI allows to analyze all possible consequences of actions in all available states of a certain environment. That gives a comprehensive picture of a state of agent's internal environment model. The metric is a ratio of reliable classifiers being able to predict each _state-action-state'_ movement and the total number of possible transitions. 

Due to possible complexity of increased observation space not all environments are feasible for calculating this metric. And obviously the agent itself does not have access to the internal state of the environment. 

(section-topics-kpi-time)=
## Trial time
The trial time is simply a time needed to complete one agent's trial phase - either exploration or exploitation. This metric is used to infer about the computation complexity of the examined algorithms and environments.

In all cases the computations are performed in controlled environment on a single machine. Therefore, the obtained results can be relatively compared to each other.

(section-topics-kpi-performance)=
## Exploitation performance
The exploitation performance is a measure of utilizing agent's internal model of the environment in order to obtain the highest possible payoff. It is most often gathered in the exploit phase, where the agent focuses solely on selecting the best possible classifiers for each situation.

Depending on the type of environment this metric might differ - for example in a multistep [](section-topics-environments-corridor) the interest is in reaching the final state as fast as possible. Therefore, the metric is simply a number of step in each trial that should be close to the optimal value. For a single-step environment, such as [](section-topics-environments-rmpx) a reward is paid out after giving a correct answer in each trial. In this case a good measure is to keep track of all obtained rewards and averaging them.

The metric itself is depends on major components (learning and credit assignment) involved in the agent's algorithm providing an estimate of its practical usefulness. 