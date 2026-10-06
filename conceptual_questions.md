# Conceptual Questions

## 1. Use Case for the Technical Exercise

A plausible use case for this project is to help New York City officials evaluate whether residents in different zip codes receive different levels of service when they submit 311 complaints.

By comparing complaint response times across zip codes, city officials can identify areas where complaints consistently take longer to resolve. This could help the city investigate possible causes such as differences in workload, staffing, or operational capacity, and support decisions about where additional resources or process improvements may be needed.


## 2. Refining the My Little Pony Question into a Data Science Question

### Original Question

> “We’d like to understand how much characters talk across the My Little Pony series.”

### Step 1 — Clarify What Is Meant by “Characters”

The original question does not specify which characters should be included.

To make the question operational, we can define characters as all named speakers that appear in the available transcript dataset.

### Step 2 — Clarify What Is Meant by “Talk”

“How much characters talk” is ambiguous, so we need a measurable definition.

A practical choice is to measure how much each character talks by counting the number of dialogue lines attributed to that character.

### Step 3 — Define the Scope of the Analysis

The question should specify which part of the series is included.

We can define the scope as all episodes available in the dataset rather than only selected seasons or episodes.

### Step 4 — Define the Comparison

Instead of only counting dialogue lines, we can compare characters by their total number of spoken lines and determine which characters contribute the most dialogue across the series.

### Final Data Science Question

Across all available episodes of *My Little Pony* in the dataset, how many dialogue lines are spoken by each named character, and which characters account for the largest share of the total dialogue?


## 3. Why Is State Maintenance Difficult in a Jupyter Notebook?

State maintenance is difficult in a Jupyter notebook because cells can be executed in any order and can also be executed multiple times.

The current values of variables therefore depend on the history of which cells were run and in what order, rather than only on the visible top-to-bottom order of the notebook. This can create hidden dependencies between cells.

For example, a notebook may appear to work because a variable was created by a cell that was run earlier, even if that cell is currently located later in the notebook.

As a result, another person may restart the kernel and run the notebook from top to bottom and get a different result or an error. This makes notebooks harder to keep reproducible unless the execution order and state are carefully controlled.


## 4. Why Can a Jupyter Notebook Be Better Than a README for Sharing a Data Science Project?

A Jupyter notebook can be better than a README for sharing a data science project with other data scientists because it combines explanation, executable code, outputs, tables, and visualizations in one place.

A future data scientist can follow the analysis step by step, inspect the code that produced each result, rerun the analysis, change parameters or code, and immediately see the updated outputs. This makes the workflow more transparent and easier to explore.

A README is still useful for describing the purpose of a project, setup instructions, dependencies, and how to run the code, but it is mainly static documentation.

It does not normally contain an interactive, executable record of the analysis itself. For a data scientist who may want to understand or extend the work later, a Jupyter notebook provides a more direct and reproducible view of how the analysis was performed.