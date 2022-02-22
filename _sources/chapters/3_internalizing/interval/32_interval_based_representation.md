# Interval-based representation
There are several possible ways of representing intervals as described in Section "[](section-topics-real-interval)". This chapter deliberately selects the UBR approach introduced by Stone and Bull for XCS {cite}`stone2003real`, since it supersedes both CSR and OBR encodings and tries to apply it to the ACS2 algorithm. 

The agents however cannot be adapted to UBR just by changing the communication layer with the environment. Therefore, because of its maturity and the huge amount of tightly interacting components, ACS2 algorithm was elected as a representative candidate of the ALCS family.

Moreover, in order to limit the flourishing population size a hybrid approach was taken to represent intervals, where each boundary is represented using nominal integer value. It is assumed that the input attribute perception $\sigma_i$ is defined as $\sigma_i \in [0, 1]$. {numref}`hybrid-interval-table` demonstrates an example of encoding real value signal using particular encoding resolutions.

```{table} Examples of encoded values for different perceptions $\sigma$. Maximum resolution is calculated with $2^n$, where $n$ is the number of bits used. E.g. a range $[0.3;0.6]$ encoded with 7 bits would be $[38; 76]$ for OBR/UBR or $[76,38]$ for UBR encoding (order is irrelevant).
:name: hybrid-interval-table

| Perception $\sigma$ | 1-bit | 2-bit | 3-bit | ... | 7-bits | ... |
|---|---|---|---|---|---|---|
| 0.0 | 0 | 0 | 0 | ... | 0 | ... | 
| 0.1 | 0 | 0 | 0 | ... | 12 | ... | 
| 0.2 | 0 | 0 | 1 | ... | 25 | ... | 
| 0.3 | 0 | 1 | 2 | ... | 38 | ... | 
| 0.4 | 0 | 1 | 3 | ... | 51 | ... | 
| 0.5 | 1 | 2 | 4 | ... | 64 | ... | 
| 0.6 | 1 | 2 | 4 | ... | 76 | ... | 
| 0.7 | 1 | 2 | 5 | ... | 89 | ... | 
| 0.8 | 1 | 3 | 6 | ... | 102 | ... | 
| 0.9 | 1 | 3 | 7 | ... | 115 | ... | 
| 1.0 | 1 | 3 | 7 | ... | 127 | ... | 
```

The proprietary variation of ACS2 system was named rACS {cite}`kozlowski2019preliminary` and can be distinguished from the native implementation by:

- **Don't care symbol**. In rACS the feature attributes consists solely of interval ranges. The _"don't care"_ and _"pass-through"_ symbols are represented as a full-ranged interval (e.g. using 4 bit encoding - $\textrm{UBR}(0, 15)$ or $\textrm{UBR}(15, 0)$).
- **Covering** - The covering process introduces randomness when a new classifiers is added into population. A new parameter - _covering noise_ $\epsilon_{cover}$ defines the maximum noise that can alter current perception. The noise $\epsilon$ is drawn from uniform random distribution $U[0, \epsilon_{cover}]$. When creating a new classifier each condition and effect attribute is spread $\textrm{UBR}(x_1 - \epsilon, x_2 + \epsilon)$ accordingly.
- **Mutation** - Similarly, a new parameter - _mutation noise_ $\epsilon_{mutation}$ is used for introducing slight disturbances. For each attribute of condition and effect perception string a noise $\epsilon$ is drawn from uniform distribution $U[-\epsilon_{mutation}, \epsilon_{mutation}$] and added to the current value.
- **Subsumption** - The mechanism was extended accordingly to analyze incorporating ranges.
- **Marking** - Classifier's mark stores only single encoded exceptional perceptions (not intervals).

## Experimental evaluation
This section presents the motivation, goals and set-up of the performed experiments, as well as their results.

### Research questions
The conducted research aims to answer the following question regarding the rACS algorithm and the usage of interval based representation

1. Can the rACS algorithm form the internal model of the environment and exploit it successfully?

### Goals of the experiments

```{admonition} _Experiment 1 - Encoding precision_
The impact of using different values of bits for creating UBR ranges will be contrasted with the ability of exploiting the single-step [](section-topics-environments-rmpx) environment. Due to the environment's increasing complexity a simple 3-bit variant is sufficient to demonstrate the potential pitfalls of using interval based representation
```

```{admonition} _Experiment 2 - Nature of the intervals_
The main goal of the experiment is to investigate the nature and the evolution of condition intervals. An experiment using the [](section-topics-environments-checkerboard) environment will highlight major differences between conditional attributes but also the overall performance in this environment will be analyzed.
```

### Experiments

```{tableofcontents}
```

### Answers to research questions
Check if figure from other document can be referenced, like Fig {numref}`{number} <rmpx3bit-enc2bit-fig>`.

It is obvious that for low encoding values certain perception attributes are indistinguishable (see {numref}`hybrid-interval-table`).