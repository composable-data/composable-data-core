from composable_data_core import (
    ExperimentSpec,
    Grain,
    LearningMode,
    ModelPlan,
    ModelRole,
    ProblemType,
    Resolution,
    ResolutionAction,
    SplitMethod,
    SplitPlan,
)


def test_regression_experiment_grammar() -> None:
    grain = Grain("one country-year")

    split = SplitPlan(
        method=SplitMethod.RANDOM,
        test_size=0.20,
        seed=42,
        rationale="Use a reproducible random holdout for this example.",
    )

    resolution = Resolution(
        problem="Rows missing required modeling values cannot be used.",
        action=ResolutionAction.DROP,
        rationale="Drop rows missing the selected feature or target.",
    )

    baseline = ModelPlan(
        estimator="DummyRegressor",
        role=ModelRole.BASELINE,
        parameters={"strategy": "mean"},
        rationale="Use the training mean as the regression baseline.",
    )

    candidate = ModelPlan(
        estimator="LinearRegression",
        role=ModelRole.CANDIDATE,
        rationale="Evaluate a simple linear relationship between GDP and CO2.",
    )

    spec = ExperimentSpec(
        dataset="owid-co2-data-subset",
        grain=grain,
        learning_mode=LearningMode.SUPERVISED,
        problem_type=ProblemType.REGRESSION,
        target="co2",
        selected_features=("gdp",),
        feature_rationale="GDP was selected as the feature to investigate.",
        resolution=resolution,
        split=split,
        baseline_id="mean-baseline",
        baseline=baseline,
        candidate_id="linear-regression",
        candidate=candidate,
    )

    assert spec.dataset == "owid-co2-data-subset"
    assert spec.grain == grain
    assert spec.learning_mode is LearningMode.SUPERVISED
    assert spec.problem_type is ProblemType.REGRESSION
    assert spec.target == "co2"
    assert spec.selected_features == ("gdp",)
    assert spec.split == split
    assert spec.baseline == baseline
    assert spec.candidate == candidate

def test_resolution_grammar() -> None:
    resolution = Resolution(
        problem="Region value E is documented shorthand for East.",
        field="region",
        original_value="E",
        resolved_value="East",
        action=ResolutionAction.RECODE,
        rationale="The source documentation defines E as East.",
    )
    assert resolution.resolved_value == "East"
