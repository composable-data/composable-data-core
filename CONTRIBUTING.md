# Contributing

`composable-data-core` is intentionally small.

## Core Rule

Add a concept only when necessary to express one of the grammar's
declarations.

This package is a grammar not a framework.

## Current Grammar

- `Grain`
- `ProblemType`
- `ExperimentPlan`
- `SplitPlan`
- `ModelPlan`
- `Evaluation`
- `ExperimentAssessment`
- `Resolution`
- `Rationale`

## Dependency Direction

`rationale.py` and `grain.py` are shared substrate modules.

Declaration modules may depend on shared substrate modules.
Shared substrate modules must not import declaration modules.

## Out of Scope

Do not add model training, prediction, metric computation,
data cleaning execution, DataFrame operations, plotting,
exporting, SQL execution, streaming execution,
or framework adapters.

## Design Test

Before adding a public type, ask:

> Which existing grammar declaration
> cannot be expressed correctly without this?
