# Conclusions
This thesis focused on integrating anticipatory classifier systems with problems described by real-valued output. While this area was researched extensively in other LCS families, no major contribution was still made for the ALCS. The stated hypothesis - _"Anticipatory Classifiers Systems are capable of building the correct internal model of the environment using the real-valued input signal"_ is considered as valid by achieving the following goals:

**1. Propose modifications towards ALCS system capable of handling real-valued input and optimizing overall performance**

This intention was achieved and validated using two independent approaches:

1. Changing the rule's attribute representations to incorporate _interval predicates_, resulting in a proprietary system variation named rACS,
2. Perform signal discretization, keeping the most internal component interactions intact.

The first approach was based on the advancements made for the XCS systems. The rACS managed to show promising results. Nevertheless, because of the much richer rule complexity and the cooperation of components precisely forming the condition and effect parts, the obtained conclusion is that the nature of rACS is not aligned with the overall ALCS idea. The favoured implementation of ACS2, which is considered the most mature algorithm, is built upon the psychological theory of behavioural control, which was not investigated for this kind of problem. The algorithm performance, while being valid, is not elegant for the virtues of ALCS for creating the most general, compact and accurate rules.

The second approach maintains the characteristics and original intentions of investigated algorithms by affecting only the interface layer. Hopefully, the internal representation is not limited to the ternary alphabet (binary values and generalization symbol), so any nominal value can also be used. This enables the possibility of performing signal discretization _before_ an agent processes it. While promising results and better transparency, this approach was considered superior to interval formation and was pursued in consecutive experiments.

The proposition of the first approach was published in {cite}`kozlowski2019preliminary`, while the latent learning experiments in discretized environments article is awaiting peer review {cite}`kozlowski2022internalizing`.

**2. Propose relevant benchmarking problems and metrics for evaluating ALCS performance**

The nature of the performance was carefully reviewed in six problems using the continuous-valued signal as a description of an actual state. Most of them have been used as a toy-problems in LCS research, providing different problems of different natures, like:

- single and multiple steps,
- extensive mutual feature interaction,
- vast input space,
- the need for long-action chain building.

Moreover, a famous RL _Cart Pole_ benchmarking problem was investigated by the LCS for the first time, obtaining encouraging results with compact knowledge representation.

To highlight performance, five key metrics were selected that investigate the state of the systems from multiple angles. Aspects like the quality of evolving solutions, size, and effective application are emphasized throughout the research.

**3. Propose relevant improvements towards neoteric changes**

This work's primary effort is to investigate the ALCS behaviour with either interval-based rule representation (rACS) or by the use of discretization. The rACS adaptation requires redefining certain internal processes and introducing new system parameters. Preliminary tests revealed two possible limitations of the system that were further studied.

First, any form of continuous-valued representation increased the problem's search space, impeding the agent's learning speed. Four techniques probing for the most promising action selection were inspected, especially regarding knowledge acquisition rate. The novel approach, based on the promising approach of _Optimistic Initial Values_ in multi-armed bandits, named _Optimistic Initial Quality_ was proposed herein but did not provide substantial performance gains.

The other limitation relates to multistep problems, where certain signal discretization might demand the agent to perform a notably larger number of actions to receive the feedback signal. The default reward assignment component might distribute the signal incorrectly amongst participating classifiers when such long-action chains are experienced. An approach replacing the credit assignment with the undiscounted incentive distribution version resulted in a system named AACS2. The method showed performance improvements for specific problems.

The biased exploration research was published in {cite}`kozlowski2020investigating`, and the performance of long-action chaining in {cite}`kozlowski2021anticipatory`.

**4. Conduct an experimental evaluation of intended adjustments**

All the experiments were tried to illustrate the evolution of selected metrics throughout the agent's learning of selected problems. Such characteristics of investigated strategies of ALCS implementations were further smoothed by averaging multiple independent experiments.

Moreover, the Bayesian estimation approach emphasized the differences between investigated cases, allowing to draw non-biased conclusions. Often, selected environments were scaled up, where agents' behaviour was challenged with increased complexity. 

**5. Developing an open-sourced Python Machine Learning framework for evaluating various LCS algorithms**

LCS algorithms are still not recognized by many ML practitioners and researchers. Significant effort was put to implement the most famous ALCS algorithms using the tools used nowadays by data scientist communities. Despite a limited number of reference resources, the historical experiments were mostly reproduced, drastically simplifying newcomers learning curve.

By integrating with the industry standards, all algorithms share the same code base and operate with a commonly agreed interface enabling effortless benchmarking with other state-of-the-art systems. The incentives like open-source availability, a vast amount of usage examples, possibility of interactive execution are intended to shed more light on this promising yet underappreciated field of ML.

The developed _PyALCS_ framework was described in {cite}`kozlowski2018integrating` research paper.