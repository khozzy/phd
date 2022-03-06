# Introduction
With the advancement of understanding our world, sometimes the simple structures used for its description like linear models or decision trees become staggeringly insufficient. The innumerable systems that our world encompasses are composed of interconnected parts, exhibiting imperceptible properties that interact with each other non-linearly. By having the capacity to change over time and learn from experience, such systems become complex and adaptive.

More than three decades ago, Holland proposed a conceptual rule-based system {cite}`holland1976progress` comprising a set of "IF condition THEN action" rules covering different situations - calling it the cognitive systems {cite}`holland1978cognitive`. From the holistic perspective, it can be viewed as a group of collaborating "agents" represented by a collection of simple rules. The rules are formed when interacting with the external "environment" and might take, for example, the following forms:

- IF _no cars on the street_ THEN _walk forward_,
- IF _stock share price is dropping for 3 days_ THEN _buy_,
- IF _colour of the mushroom is red_ THEN _do not pick_

The general idea is that seeking a single, omnibus and complex rule is less desirable than evolving a population of them to model the environment behaviour collectively. Such an idea gave rise to the concept of _Learning Classifier Systems_ (LCS), introducing a new abstract term - a _classifier_, which encompasses a rule itself width additional statistics (such as its quality). Despite their somewhat misleading name, LCSs are not only systems suitable for classification problems but maybe instead viewed as a very general, distributed optimization technique.

They can be used in a variety of fields {cite}`bull2004applications` like data mining {cite}`witten2002data` {cite}`bernado2001xcs` {cite}`bacardit2003data` {cite}`abbass2004online` {cite}`dam2007evolutionary` (discovering patterns in data), supervised or reinforcement learning tasks. Examples of such problems would include fighter aircraft manoeuvres {cite}`smith2004fighter`, medical domains {cite}`holmes2000learning`, robotic control, game strategy, environmental navigation, modelling complex time-dependent systems (e.g., stock market) {cite}`browne2004development` or design optimization (e.g., engineering applications).

The desired outcome after running an LCS is a set of classifiers being able to model an intelligent decision-maker collectively. Two biological metaphors - _evolution_ and _learning_ {cite}`dam2007neural` are employed to accomplish this intention. A pair of internal mechanisms - the _genetic algorithm_ and the _learning mechanism_ embody them respectively by actively interacting with the outside environment, which in this work is considered as an independent source of data for an LCS algorithm.

At this moment, plentiful different LCS variations exist {cite}`urbanowicz2009learning`, but according to Holmes {cite}`holmes2002learning`, the following four major components are considered universal:

1. a finite population of classifiers representing current knowledge of the system,
2. a performance component regulating the interaction between the environment and classifier population,
3. a reinforcement (or credit assignment) component distributing the reward from the environment to particular classifiers,
4. a discovery component using various operators to discover better rules and improve existing ones

However, this work is directed on a specific niche, called the Anticipatory Learning Classifier System (ALCS), capable of learning a generalized predictive model {cite}`tolman1948cognitive` of the environment online. In contrast to the traditional IF-THEN rule structure, they also have a state prediction or _anticipatory_ part that predicts the environmental changes caused when executing the specified action in the specified context. Forming such an internal structure might facilitate the agent's thought processes, such as planning or reflection, without any immediate behaviour. Thus, beliefs about the future control the decision-making process and behaviour in the present. This architecture also allows disambiguating perceptual aliasing problems, where the same observation is obtained in distinct states requiring different actions.

The capabilities of ALCS were exhaustively examined in environments with discrete and manageable _observation spaces_ - such as navigating an agent in a maze or correctly determining an answer in a binary multiplexer problem. No comparative research focused on the problems where the observation space contains the attributes expressed as real-valued numbers - for example, a car's speed ranging from 0 to 200 km/h or a particular temperature range have not been performed yet.

This thesis demonstrates that certain families of ALCS can be adjusted to new problem domains. Despite the complicated and interconnected components hurdle, facilitating certain modifications allows them to be taking advantage of benefits associated with internal knowledge representation and prediction mechanisms. In his anticipatory systems book {cite}`rosen1985anticipatory`, Rosen goes one step further by putting the idea of anticipations in a mathematical framework and later identifying them as the essence of life {cite}`rosen1991life`.

```{epigraph}
In anticipatory systems, as I have defined them, the present change of state depends on a future state, which is predicted from the present circumstances on the basis of some model. Anticipatory, model-based behavior provided one basis for what I later called complexity, and which I defined in "Life Itself" on the basis of non-computability or nonformalizability of models of a system of this kind.

-- Robert Rosen in {cite}`rosen1991life`
```

While this work does not pursue such a big claim, it proves that a greater realm of possible problems can be expressed by ALCS frameworks, therefore benefiting from more comprehensive, intrinsic representation.