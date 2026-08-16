from composable_data_core import (
    Evaluation,
    ExperimentAssessment,
    ExperimentPlan,
    Grain,
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
    plan = ExperimentPlan(
        dataset="owid-co2-data-subset",
        target="co2",
        available_features=("year", "population", "gdp", "co2_per_capita"),
        selected_features=("gdp",),
        problem_type=ProblemType.REGRESSION,
        feature_rationale="GDP was selected as the feature to investigate.",
    )
    split = SplitPlan(
        method=SplitMethod.RANDOM,
        test_size=0.20,
        seed=42,
        rationale="Use a reproducible random holdout for this example.",
    )
    baseline = ModelPlan(
        estimator="DummyRegressor",
        role=ModelRole.BASELINE,
        rationale="Provide a simple performance floor.",
    )
    candidate = ModelPlan(
        estimator="LinearRegression",
        role=ModelRole.CANDIDATE,
        rationale="Test whether a straight line is a useful description.",
    )
    evaluation = Evaluation(
        model_id="linear-regression",
        metrics={"r2": 0.81, "mae": 123.4},
    )
    assessment = ExperimentAssessment(
        comparison="LinearRegression versus DummyRegressor on the same test set",
        conclusion="The candidate outperformed the baseline.",
        rationale="The candidate produced better held-out evaluation results.",
        winner_model_id="linear-regression",
        baseline_beaten=True,
    )

    assert grain.observation == "one country-year"
    assert plan.problem_type is ProblemType.REGRESSION
    assert split.seed == 42
    assert baseline.role is ModelRole.BASELINE
    assert candidate.role is ModelRole.CANDIDATE
    assert evaluation.metrics["r2"] == 0.81
    assert assessment.baseline_beaten is True


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
