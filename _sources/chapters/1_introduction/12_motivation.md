(section-motivation)=
# Motivation and challenges
ALCS systems were designed and thoroughly tested in problems where the concept or a function sought is essentially "logical" - meaning that it can be expressed by a combination of logical operators applied to attribute values {cite}`wilson2000mining`. However, in many problems the solution can't be conveyed solely by _and_, _or_, _not_ operators, because it's discrimination surface is oblique - neither parallel nor perpendicular to the attribute axes. If the problem's discrimination surface is oblique the classifier rule are capable of capturing parts of space within hyper-rectangles, that can only approximate the function shape using numerous distinct classifiers.

`````{margin}
````{admonition} S-expression
An **s-expression**, also known as a **sexpr** or **sexp**, is a way to represent a nested list of data. It stands for "symbolic expression," and it is commonly encountered in the Lisp programming language. It use s-expressions to represent the computer program, and the program's data.


For example, the simple mathematical expression "five times the sum of seven and three" can be written as a s-expression with prefix notation. In Lisp, the s-expression might look like the example below

```
(* 5 (+ 7 3))
```
[source](https://www.computerhope.com/jargon/s/s-expression.htm)
````
`````

The most popular family of LCS, and the ALCS predecessor - [](section-topics-history-xcs) was comprehensively evaluated for problems with non-linear decision surface. In 1999 Lanzi took approach to use _S-classifiers_ {cite}`lanzi1999extending`, where the classifier's condition part are Lisp S-expressions and can be based on arithmetic function primitives. In 2000 Wilson focuses solely on continuous value inputs introducing XCSR implementation {cite}`wilson1999get`. There the condition attribute was an interval represented by a pair of number - it's center and the spread. He examined if the optimal decisive thresholds are found automatically in a modified Multiplexer benchmark problem. In the same year he introduced a XCSI system {cite}`wilson2000mining`, focusing on forming bounded intervals for integer inputs. One year later, in 2001, another an implementation named XCSF {cite}`wilson2001function` allowing piecewise-linear function approximation was proposed. For a function $y=f(x)$ the system assumed that $x$ is the input, $y$ the payoff and after sufficient amount of sampling the input space XCSF should converge to a population of rule, that over their respective input ranges, predict payoff well. In 2003 Stone and Bull scrupulously addressed the limitations of XCSR system {cite}`stone2003real` and introduced two new interval representations alongside more versatile benchmark problem. 

The following thesis aims to evaluate the possible behaviour of the ALCS systems when interacting with real-valued environments.

- Paragraph 2: Why it is important (biased exploration, long action chains)
- Paragraph 3: Real world example (noisy environments)
- Paragraph 4: Brief literature recap
- Paragraph 5: Proposed solution (bridge the gap of XCS advancemens for handling continuous input and ACS)
