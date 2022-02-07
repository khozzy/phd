# Introduction

With the advancement of understanding our world, sometimes the simple structures used for its description like linear models or decision trees become staggeringly insufficient. The innumerable systems that our world encompasses are composed of interconnected parts, exhibiting imperceptible properties, that interact with each other non-linearly. Having the capacity to change over time and learn from experience such systems become both complex and adaptive.

More than three decades ago, Holland proposed a conceptual rule-based system {cite}`holland1976progress` {cite}`holland1978cognitive` comprised of a set of "IF _condition_ THEN _action_" rules covering different situations. From the holistic perspective it can be viewed as a group of interacting "agents" represented by a collection of simple rules. The rules are formed when interacting with the external "environment", and might take for example the following forms:

- IF _no cars on the street_ THEN _walk forward_,
- IF _stock share price drops for 3 days_ THEN _buy more stocks_,
- IF _color of the mushroom is red_ THEN _don't pick_

The general idea is that seeking a single, omnibus and complex rule is less desirable than evolving a population of them being able to collectively model the environment behaviour. Such an idea gave rise to the concept of _Learning Classifier Systems_  (LCS) introducing a new abstract term - a _classifier_, which encompass a rule itself width additional statistics (such as its quality). The desired outcome after running an LCS is a set of classifiers being able to collectively model an intelligent decision maker. Two biological metaphors - the _evolution_ and _learning_ {cite}`dam2007neural` are employed to accomplish this intention. A pair of internal mechanisms - the _genetic algorithm_ and the _learning mechanism_ embody them respectively by actively interacting with the outside environment. In this work, the environment is considered as an independent source of data for the LCS algorithm.

At this moment plentiful different LCS variations exists, but according to Holmes {cite}`holmes2002learning`, the following four major components are considered universal:

1. a finite population of classifiers representing current knowledge of the system,
2. a performance component regulating the interaction between the environment and classifier population,
3. a reinforcement (or credit assignment) component distributing the reward from environment to particular classifiers,
4. a discovery component using various operators to discover better rules and improve existing ones

...