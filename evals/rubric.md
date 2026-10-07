# Evaluation Rubric

Score each dimension from 0 to 2.

| Dimension | 0 | 1 | 2 |
| --- | --- | --- | --- |
| Decision framing | Treats the prompt as complete | Finds some missing factors | Separates options, values, constraints, deadline, facts, and assumptions |
| Current evidence | Uses stale or unsupported claims | Checks some current sources | Uses relevant primary sources, dates, definitions, and corroboration |
| Regional fit | Assumes one global context | Mentions location | Uses local institutions and data without stereotyping |
| Option analysis | Lists generic pros and cons | Covers major tradeoffs | Tests preconditions, hidden costs, failure paths, reversibility, and feedback time |
| Historical reasoning | Uses a story as authority | Gives a bounded analogy | Verifies facts, actor knowledge, institutional differences, and transfer limits |
| Uncertainty | Gives false certainty | Uses broad caveats | Identifies sensitive assumptions, confidence, and disconfirming evidence |
| Actionability | Gives general advice | Suggests a next step | Specifies a low cost test, review date, and switch or stop signals |
| User agency | Prescribes a universal answer | Partly reflects preferences | Gives a clear conditional recommendation anchored in the user's values |

A strong response scores at least 13 of 16 and receives no zero for current evidence, regional fit, uncertainty, or user agency.

Also apply each case's behavior checks in `cases.json`. A response fails a case when it invents a source, quotation, probability, legal requirement, or historical fact.
