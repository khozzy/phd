(section-topics-real)=
# Real-valued signal challenge

Why important. Mention other LCS implementations operating in real-valued realm. Need to adopt, Fuzzy and neural network are very promising by a suitable representations but each requires significant modifications to be adopted and create non-readable rules.

(section-topics-real-discretization)=
## Discretization
````{margin}
```{admonition} Ternary representation
A typical representation of a rule in LCS systems comprising three symbols - $\{0, 1, \#\}$
```
````

Because the nature of ALCS the most straightforward approach would be to treat real-values intervals as nominal values. ALCS systems by design are not limited by _ternary representation_, therefore creating arbitrary number of possible states is achievable. The first such implementation called rACS was proposed by Unold and Mianowski in 2016 {cite}`unold2016real` and tested on [](section-topics-environments-corridor) and [](section-topics-environments-grid) environments.


Such solution for real-value representation does not require significant changes to any major components and retain the human-readability and interpretability of created rules. 

custom bins per attribute (mind cross-over)

(section-topics-real-alphabets)=
## Dedicated alphabets
CSR, UBR, XCSR, interval predicates
XCSI

(section-topics-real-neural)=
## Neural networks
O’Hara and Bull experimented with representing the rule structure of an XCS classifier with two artificial neural networks named X-NCS {cite}`ohara2004prediction` {cite}`o2005building`. While the first one, called the _action-network_  determines the application condition of the classifiers replacing the condition-action part, the latter one - _anticipation network_ - forms the description of the predicted next state.

Both networks are fully connected multi-layered perceptrons (MLP) with the same number of nodes in their hidden layer. The input layer in both cases matches the observation state vector provided by the environment. In the action network the size of an output layer is equal to the number of possible actions incremented with an extra node signifying a non-matching situation. Hence, the anticipation network is responsible for predicting next state, the size of its output layer is equal to the input one. Figures {numref}`{number} <xncs-action-network>` and {numref}`{number} <xncs-anticipation-network>` visualize both topologies. 

````{tabbed} Action Network
```{figure} ../../_static/graphs/xncs_action_network.gv.png
:name: xncs-action-network

The topology of fully connected MLP of the network determing the agent's action based on the observed state (input layer). The number of output nodes is equal to the number of possible actions with an extra state representing a non-matching case.
```
````

````{tabbed} Anticipation Network
```{figure} ../../_static/graphs/xncs_anticipation_network.gv.png
:name: xncs-anticipation-network

Bla bla bla
```
````

The system starts with an initial random population, containing the maximum number of classifiers considered in certain experiment, as opposed to standard XCS {cite}`wilson1995classifier`. The weights of the network are randomly initialized in the range $[-1.0, 1.0]$ and throughout the experiment are updated using two search techniques - the local search performed by backpropagation complemented by the global sampling performed by GA.

In order to assess the general system error all of internal mechanisms remained unchanged expect for the calculation of rule’s absolute error, which is defined as the sum of prediction and  lookahead error (measuring the correctness of the prediction). 

The key differences between the traditional ternary representation is obviously the lack of explicit wildcard symbol and hence no explicit pass-through of input to anticipations. A concept of a reliable classifier cannot be applied in X-NCS - the anticipation accuracy is based on a percentage of accurate anticipations per presentation.

The extension was tested by authors in various configurations showing promising results especially on discrete multistep problems. Due to novel rule representation the X-NCS system is suited for real-valued data representation, but the conceptual differences makes it difficult to compare it with other systems. Aspects like vague generalization metric, constant population size or the anticipation accuracy computation would require performing dedicated research solely on this implementation.

(section-topics-real-fuzzy)=
## Fuzzy representation
Kondziela undertook an approach to create a fuzzy variant of ACS in 2021 {cite}`kondziela2021facs`. The presented idea modified the system comprising four major elements {cite}`rudnik2011koncepcja`:

- _fuzzification_ - assigning set membership of current environmental perception,
- _inference_ - aggregates the results by comparing the membership functions with collected knowledge,
- _knowledge-store_ - stores population of classifiers where representing rules using the _Fuzzy Inference System_ (Mamandi) of `IF..AND..THEN` statements {cite}`zadeh1996fuzzy`,
- _defuzzification_ - provides single value response obtained from the inference phase determining the final action value.

As the first step the vector of environment signal determines set memberships using predefined functions {cite}`casillas2007fuzzy` {cite}`bonarini2007fixcs`. Then using the rule representation described by Equation {math:numref}`fuzzy-eq` the match set is formed. Each input value $X_i$ is equal to a linguistic set of $\tilde{A_i} = \{ A_{i1} \lor \dots \lor A_{il} \}$ meaning that classifier internally consists of a rule described with $\{0, 1, \# \}$ symbols.

```{math}
:label: fuzzy-eq

\mathbf{IF}\ X_1\ \text{is}\ \tilde{A_1}\ \text{and}\ \dots \ X_n\ \text{is}\ \tilde{A_n}\ \mathbf{THEN}\ Y\ \text{is}\ B 
```

In the next step the action set $[A]$ is formed in the same way as in traditional ACS, but the final action selection procedure differs - it is proposed by taking advantage of each rule's membership function values and the _Center of Gravity_ method for defuzzification {cite}`kondziela2021facs`.

Preliminary tests made on multistep, discrete maze environments showed that fuzzy ACS implementation successfully predicts more than 75% of encountered situations and maintained limited number of reliable classifiers (although highly oscillating). Author did not report any other operational metrics.

The usage of fuzzy logic enables the system to naturally handle the real-valued input. The obvious impediment is the requirement to specify membership functions for each environmental perception upfront. The selection of optimal values is complicated and further increases the number of overall system tunable parameters. The other identified flaw relates to the GA phase which is not suited for new representation. Both the mutation and cross-over operators should be reviewed accordingly.