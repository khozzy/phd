(section-topics-kpi)=
# Key performance indicators

The ALCS comprise complex mechanisms such as ALP or GA, which might be hard to comprehend and analyse. Therefore, specific metrics reflecting their nature were chosen to visualise system behaviour over time and assess its performance. This section presents several metrics used across further experimental evaluations. Each of them can be collected at a particular interval of time (for example, every ten trials) and can access the properties of both the environment and the agent within the single simulation.

(section-topics-kpi-population-size)=
## Classifier population size
Each LCS creates an internal population of classifiers. Knowing its total size $|P|$ represents the agent's ability to express the internal model of the environment. When maintaining high performance, having a smaller population also means that the agent is commendable at building a more compact and compressed representation of knowledge.

Besides knowing the total population size, it's subset of reliable classifiers size $|P_{\text{reliable}}|$ might also be easily obtained - equation {math:numref}`kpi-reliable-population-eq`. The total population and reliable population size should converge throughout an experiment to a single value.

```{math}
:label: kpi-reliable-population-eq 

P_{\text{reliable}} = \{ cl \in P : cl.q \geq \theta_r \}
```

(section-topics-kpi-generalization)=
## Generalization
The generalization metrics reflect the agent's generalization abilities. It is calculated by analyzing all classifiers in a population $P$. Equation {math:numref}`kpi-generalization-eq` shows the proportion of condition attributes containing the wildcard symbol.

```{math}
:label: kpi-generalization-eq

\text{Generalization}(P) = \frac{ \vert \bigcup \bigg( cond.att | cond \in \big( cl.cond | cl \in P \big) \land cond.att = \# \bigg) \vert }{ \vert \bigcup \bigg( cond.att | cond \in \big( cl.cond | cl \in P \big) \bigg) \vert }
```

The greater generalization score means that the algorithm creates classifiers covering a larger portion of the observation space, creating a more compact solution of the problem.

(section-topics-kpi-knowledge)=
## Knowledge
The knowledge KPI allows analyzing all possible consequences of actions in all available states of a particular environment, giving a comprehensive picture of the state of the agent's internal environment model. The metric is a ratio of reliable classifiers that can predict each _state-action-state'_ movement and the total number of possible transitions. 

Due to the possible complexity of increased observation space, not all environments can calculate this metric. Moreover, the agent itself obviously does not have access to the internal state of the environment.

(section-topics-kpi-time)=
## Trial time
The trial time is simply a time needed to complete one agent's trial phase - either exploration or exploitation. This metric is used to infer the computation complexity of the examined algorithms and environments.

The computations are performed in a controlled environment on a single machine in all cases. Therefore, the obtained results can be relatively compared to each other.

(section-topics-kpi-performance)=
## Exploitation performance
The exploitation performance is a measure of utilizing the agent's internal model of the environment in order to obtain the highest possible payoff. It is most often gathered in the exploit phase, where the agent focuses solely on selecting the best possible classifiers for each situation.

Depending on the type of environment, this metric might differ - for example, in a multistep [](section-topics-environments-corridor), the interest is in reaching the final state as fast as possible. Therefore, the metric is simply the number of steps in each trial that should be close to the optimal value. For a single-step environment, such as [](section-topics-environments-rmpx), a reward is paid out after giving a correct answer in each trial. In this case, a good measure is to keep track of all obtained rewards and average them.

The metric itself depends on significant components (learning and credit assignment) involved in the agent's algorithm to estimate its practical usefulness. 