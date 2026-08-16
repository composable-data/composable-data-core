# composable-data-core

<img
src="https://raw.githubusercontent.com/composable-data/composable-data-core/main/docs/images/profile.png"
alt="profile logo"
width="110">

`composable-data-core` provides a small, typed decision grammar
for analytical work.

It records analytical meaning, consequential decisions and their rationale,
experimental evidence, and conclusions.

It performs no analytical operations.

## Purpose

Analytical projects repeatedly make the same kinds of decisions:

- What does one observation represent?
- What kind of prediction problem is this?
- Which features should be used, and why?
- How should the data be split, and why?
- Which model should be evaluated, and why?
- What evidence resulted?
- What conclusion does the evidence support?
- How should an identified data problem be resolved, and why?

`composable-data-core` gives these concepts a small, shared vocabulary
so they can be expressed consistently across projects.

## Design Decisions

- Core remains dependency-free.
- Domain and dataset semantics remain outside.
- Public names should teach established analytical language.

## Decision Grammar

The core grammar consists of:

- `Grain` - declares what one observation represents.
- `LearningMode` - records whether the experiment is supervised or unsupervised.
- `ProblemType` - records whether a supervised prediction problem is
  classification or regression.
- `ExperimentSpec` - declares the complete experiment specification known
  before execution: dataset, grain, learning mode, problem type, target,
  selected features and rationale, data resolution, split design, and
  baseline and candidate model plans.
- `SplitPlan` - declares how training and test observations are separated,
  including the split strategy and its rationale.
- `ModelPlan` - declares one model choice, its experimental role, configuration,
  and rationale.
- `Evaluation` - records metric results computed elsewhere.
- `ExperimentAssessment` - records the conclusion drawn from comparable
  experimental evidence.
- `Resolution` - records a declared policy for handling a known data-quality
  condition when that policy is part of the experiment specification.
- `Rationale` - provides free-form or structured reasoning for consequential
  analyst choices.

## Analytical Flow

The machine-learning grammar follows a simple progression:

```text
MEANING: Grain
    ↓
LEARNING MODE: LearningMode
    ↓
PROBLEM: ProblemType
    ↓
SPECIFICATION: ExperimentSpec
    ├── Resolution
    ├── SplitPlan
    ├── baseline ModelPlan
    └── candidate ModelPlan
    ↓
EXECUTION: performed by external analytical libraries
    ↓
EVIDENCE: Evaluation
    ↓
CONCLUSION: ExperimentAssessment
```

`Resolution` provides the corresponding decision declaration for data-quality
problems encountered during analytical work.

## Decisions, Facts, and Evidence

Not every declaration requires a rationale.
The grammar distinguishes among:

```text
Grain                   declared meaning
LearningMode            derived fact
ProblemType             derived fact

ExperimentSpec          experiment specification
Resolution              decision + rationale
SplitPlan               decision + rationale
ModelPlan               decision + rationale

Evaluation              recorded evidence

ExperimentAssessment    conclusion + rationale
```

The governing principle is:

> Derive what can be known. Record what happened.
> Require rationale where alternatives require analyst judgment.

The grammar does not require justifying facts that can be
derived or inventing explanations for observed measurements.

## Grain

`Grain` declares what one observation (entry, row) represents.

Examples include:

- one penguin
- one transaction
- one customer-month
- one county-year
- one sensor reading per device per timestamp
- one five-minute observation window

Grain provides a shared analytical concept across tabular data, databases,
business intelligence, machine learning, and streaming applications.

## Transitioning From Analytical Workflow to Grammar

The grammar is designed around a common analytical pattern:

1. Define the problem and target.
2. Load or inspect the data and identify the available features.
3. Validate that the declared selected features are available.
4. Use the selected features and rationale declared in `ExperimentSpec`.
5. Execute the declared split.
6. Execute the baseline and candidate model plans.
7. Record the resulting evaluation evidence.
8. Assess what the evidence supports, including limitations and possible next experiments.

`ExperimentSpec` contains only declarations knowable before execution.
Observed facts such as the features actually available in a loaded dataset
are discovered and validated during execution.

`composable-data-core` represents only the parts of this workflow that need
shared analytical meaning.

The analyst declares decisions and rationale.
External libraries perform the computation.
`Evaluation` records the resulting evidence.
`ExperimentAssessment` records the analyst's conclusion.

## Out of Scope

`composable-data-core` deliberately does not:

- load or transform DataFrames
- clean data
- split datasets
- construct or train models
- generate predictions
- calculate evaluation metrics
- create visualizations
- execute SQL
- export files
- provide framework-specific integrations

Those operations belong to established libraries and specialized tools.

For example, scikit-learn may perform a train/test split and train a model.
`composable-data-core` records the analytical meaning and
pre-run decisions that define the experiment.

A visualization package may display the resulting model performance.
`composable-data-core` records the experiment and its evidence.

## Design Boundary

`composable-data-core` is intentionally small.

Its central design rule is:

> Add a concept only when necessary to express one of the grammar's
> declarations.

This package is a **grammar** not a framework.

The shared vocabulary should be small enough to understand, inspect,
implement independently, and use across different analytical tools.

## Analytical Agency

The grammar may constrain vocabulary where the available choices are known, but
it does not make consequential analytical decisions.
The analyst chooses, for example:

- which features to use
- how to design an appropriate split
- which candidate model to investigate
- how to resolve ambiguous data problems
- what conclusions the experimental evidence supports

The grammar makes those decisions explicit and comparable.

## See Also

- [API](./api.md)
