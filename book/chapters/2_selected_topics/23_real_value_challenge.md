(section-topics-real)=
# Real-valued signal challenge

Why important. Mention other LCS implementations operating in real-valued realm. Need to adopt, Fuzzy and neural network are very promising by a suitable representations but each requires significant modifications to be adopted.

(section-topics-real-discretization)=
## Discretization
XCSI, custom bins per attribute

(section-topics-real-alphabets)=
## Dedicated alphabets
CSR, UBR, XCSR, interval predicates

(section-topics-real-neural)=
## Neural networks
O’Hara and Bull experimented with representing the rule structure of an XCS classifier with two artificial neural networks named X-NCS {cite}`ohara2004prediction` {cite}`o2005building`. While the first one, called the _action-network_  determines the application condition of the classifiers replacing the condition-action part, the latter one - _anticipation network_ - forms the description of the predicted next state.

Both networks are fully connected multi-layered perceptrons (MLP) with the same number of nodes in their hidden layer. The input layer in both cases matches the observation state vector provided by the environment. In the action network the size of an output layer is equal to the number of possible actions incremented with an extra node signifying a non-matching situation. Hence, the anticipation network is responsible for predicting next state, the size of its output layer is equal to the input one. Figures {numref}`{number} <xncs-action-network>` and {numref}`{number} <xncs-anticipation-network>` visualize both topologies. 

````{tabbed} Action Network
```{figure} ../../_static/graphs/xncs_action_network.png
:name: xncs-action-network

The topology of fully connected MLP of the network determing the agent's action based on the observed state (input layer). The number of output nodes is equal to the number of possible actions with an extra state representing a non-matching case.
```
````

````{tabbed} Anticipation Network
```{figure} ../../_static/graphs/xncs_anticipation_network.png
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
...