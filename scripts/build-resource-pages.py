"""Build curated resource profiles from the repository catalog and paper map."""
import csv
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

# Editorial guidance: exercises below are proposals, not upstream benchmark claims.
REPOS = {
    'qutip': ('Quantum dynamics foundation', 'Represent states, operators and time-dependent models, then propagate the dynamics before introducing an optimizer.', 'Validate a driven two-level system against a resonant analytic limit, then add a collapse operator.', 'Check units, solver tolerances, normalization, density-matrix trace and Hilbert-space truncation.', 'A dynamics solver supplies the physical evolution; it does not by itself choose an optimal pulse.'),
    'qtrl': ('Discretized pulse optimization', 'Use GRAPE or CRAB with a QuTiP model to search for controls that improve a state or gate objective.', 'Optimize bounded one-qubit state transfer and compare the optimized pulse against a constant-pulse baseline.', 'Check time slices, gradient accuracy, amplitude bounds, initial guesses and objective conventions.', 'Older examples may import qutip.control; consult the separate qutip-qtrl package documentation.'),
    'qoc': ('Parameterized control comparison', 'Explore GOAT and JOPT for analytic controls and compare with GRAPE or CRAB through qtrl.', 'Solve the same one-qubit gate problem using an analytic pulse and a discretized pulse.', 'Record parameter scaling, optional dependencies, integration tolerances and total evaluations.', 'The package builds on qutip-qtrl; do not treat all exposed methods as independent implementations.'),
    'krotov': ('Sequential field optimization', 'Study Krotov updates with objectives defined through states and target transformations.', 'Run a documented state-transfer example, then vary the update strength while keeping the physical model fixed.', 'Inspect discretization, running costs, convergence assumptions and supported QuTiP versions.', 'Monotonic convergence under stated assumptions does not guarantee a global optimum or hardware feasibility.'),
    'quocs': ('Custom optimization workflow', 'Connect an objective evaluator to pulse-search algorithms, including GRAPE, dCRAB and direct-search strategies.', 'Implement a simulated qubit objective and log every evaluation before adding uncertainty averaging.', 'Check parameter bounds, evaluation cost, stochastic noise, stopping rules and platform-specific dependencies.', 'Experimental optimization between trials is different from continuous measurement feedback during evolution.'),
    'dynamiqs': ('Differentiable simulation', 'Use JAX-based quantum propagation for differentiable workflows and batched parameter studies.', 'Simulate a small parameter ensemble and compare a custom gradient against finite differences.', 'Check numerical precision, memory use, solver differentiation and device support.', 'GPU availability does not establish a speed advantage for every model; benchmark your actual workload.'),
    'spinach': ('Native MATLAB spin control', 'Model spin dynamics and explore the optimal-control module in a MATLAB workflow.', 'Follow an upstream small-spin example, then inspect a GRAPE objective and its pulse penalties.', 'Check the upstream MATLAB release, required toolboxes, relaxation model and spin basis.', 'The original Spinach paper describes simulation foundations; current control features extend beyond that paper.'),
    'tutorials': ('Executable learning material', 'Use upstream notebooks to learn model construction, propagation and associated quantum tools.', 'Select one dynamics notebook and reproduce its figures in an isolated matching environment.', 'Inspect notebook age, dependency versions, execution order and random seeds.', 'A changing tutorial collection is not a frozen reproduction artifact for every QuTiP paper.'),
    'semiad': ('Paper-associated reproduction material', 'Inspect scripts, notebooks and data associated with the semi-automatic differentiation paper P13.', 'Start from the included data and plotting workflow before attempting to regenerate expensive benchmarks.', 'Read the Linux, Make, Julia and Jupyter setup requirements and the upstream runtime notes.', 'This is a mixed Julia/Python workflow outside the main Python/MATLAB stack; cloning does not reproduce the paper.'),
    'qi': ('Platform authentication and workflows', 'Use the Quantum Inspire SDK and CLI to authenticate and interact with supported platform resources.', 'Inspect the CLI help and backend capabilities before mapping any simulated protocol to a platform task.', 'Verify supported Python versions, authentication setup and backend interface.', 'A platform client is not a Hamiltonian pulse optimizer or a guarantee of arbitrary waveform access.'),
    'qi-qiskit': ('Qiskit platform integration', 'Connect Qiskit circuit workflows to Quantum Inspire backends.', 'Read the provider documentation and inspect a circuit-submission example.', 'Check Qiskit/provider versions and the selected backend instruction set.', 'A circuit-level provider must not be assumed to expose pulse-level control or continuous feedback.'),
    'qi-pennylane': ('PennyLane platform integration', 'Connect PennyLane workflows to Quantum Inspire systems.', 'Inspect a documented device or circuit example before designing a larger algorithm.', 'Check PennyLane/provider compatibility, supported operations and differentiation assumptions.', 'Differentiating circuit parameters is a different problem from optimizing a physical control waveform.'),
    'qi-examples': ('Platform example collection', 'Explore Python scripts and notebooks illustrating Quantum Inspire algorithms and integrations.', 'Read one notebook and identify the SDK/API generation and its dependencies before execution.', 'Check legacy APIs, ProjectQ requirements, account setup and backend availability.', 'An old notebook may remain educational even when its original execution environment is no longer current.'),
    'opensquirrel': ('Quantum program transformation', 'Study a Python quantum compiler as supporting infrastructure for program transformations.', 'Inspect the upstream examples and identify where a program representation is transformed.', 'Distinguish circuit/program transformations from physical Hamiltonian propagation.', 'Compilation tooling is adjacent to, rather than a replacement for, dynamical simulation and pulse optimization.'),
    'libqasm': ('cQASM language tooling', 'Use the upstream parser library as a reference for reading and analyzing cQASM programs.', 'Inspect a small upstream cQASM parsing example and its language-version assumptions.', 'Check parser version, supported syntax and diagnostics.', 'Parsing a program does not establish the physical dynamics of the hardware executing it.'),
    'openql': ('Programming and compilation framework', 'Explore C++/Python quantum programming and compilation infrastructure.', 'Follow an upstream example and identify its target platform and compilation configuration.', 'Check build requirements, platform configuration and output representation.', 'Keep compiler performance and pulse-control fidelity as separate evaluation questions.'),
    'quis': ('Instruction semantics reference', 'Consult the ecosystem instruction-set definition when interpreting supported quantum instructions.', 'Compare the instructions in a small program with the specification used by its tools.', 'Record specification and compiler versions together.', 'An instruction specification is not an executable dynamics simulator or control package.'),
    'qilib': ('Supporting utility reference', 'Inspect Quantum Inspire utility classes when studying supporting or older workflows.', 'Read the upstream README and dependency setup before choosing a relevant utility example.', 'Check storage dependencies and whether the utility is needed by your intended workflow.', 'Do not install this package merely because it shares the Quantum Inspire name; identify a concrete use first.'),
    'qi2': ('Historical SDK reference', 'Consult the archived SDK for historical context and migration investigations.', 'Compare its README with the current quantuminspire project rather than starting a new environment here.', 'Treat archived dependencies and APIs as historical unless independently verified.', 'Excluded from automatic downloads; prefer the current SDK for new platform work.'),
}

PAPERS = {
    'P01': ('Review / research orientation', 'How does optimal control connect controllability, open systems and quantum technologies?', 'Map the assumptions behind the physical system, control resources and intended application.', 'Write a one-page scope statement identifying your system, target and constraints.', 'A broad strategic review does not prescribe one optimizer for every problem.'),
    'P02': ('Review / practical methods', 'Which control formulation and algorithm family fits a practical task?', 'Compare objective design, constraints, robustness and the different search strategies.', 'Create a decision table for GRAPE, Krotov, reduced-basis and analytic-control approaches.', 'Method selection still requires numerical experiments on the chosen physical model.'),
    'P03': ('Software / simulation', 'What numerical infrastructure supports modern QuTiP quantum-dynamics workflows?', 'Study the solver and data-layer ecosystem and where control extensions fit.', 'Run a small upstream dynamics example and record solver settings and dependency versions.', 'A software paper and an evolving tutorial collection need not describe identical versions.'),
    'P04': ('Method / GRAPE', 'How can control amplitudes be optimized for coupled spin dynamics?', 'Understand discretized controls, propagators and gradients of the target objective.', 'Build a bounded one-qubit transfer baseline, then check the gradient on a small instance.', 'Later implementations may use different derivatives, optimizers and conventions from the original paper.'),
    'P05': ('Method and software / Krotov', 'How can sequential field updates solve state and gate control tasks?', 'Read the formulation, running-cost choices and assumptions behind monotonic improvement.', 'Follow a documented state-transfer example and inspect the effect of update strength.', 'Convergence statements depend on assumptions and discretization; they do not establish global optimality.'),
    'P06': ('Method / CRAB', 'Can a reduced pulse basis make a control search more compact?', 'Focus on pulse parameterization and the relation between simulation resolution and search dimension.', 'Compare a reduced-basis pulse with a time-grid baseline under an equal evaluation budget.', 'Results depend on the basis, coefficient constraints and initial guesses; there is no universal performance ordering.'),
    'P07': ('Method / dCRAB', 'How can changes in a truncated basis help a constrained control search?', 'Read the landscape assumptions and the role of bandwidth and additional constraints.', 'Study dCRAB basis updates and compare repeated starts on one fixed model.', 'Landscape arguments should not be extended into a blanket guarantee for arbitrary experimental restrictions.'),
    'P08': ('Method / GOAT', 'How can analytic pulse parameters and their sensitivities be optimized together?', 'Connect physical pulse parameters, sensitivity propagation and hardware-oriented constraints.', 'Compare an analytic-pulse gate optimization with a discretized baseline.', 'qutip-qoc provides a later extended implementation; match definitions before comparing results.'),
    'P09': ('Comparison / DYNAMO', 'How do different update schemes compare within a common control framework?', 'Identify what is held fixed when comparing GRAPE and Krotov-type schemes.', 'Design a comparison sheet with common objectives, initial pulses and evaluation budgets.', 'DYNAMO here is a historical MATLAB control framework; no current GitHub mirror was verified in this catalog.'),
    'P10': ('Software / QuOCS', 'How can one framework connect model-based and experimental pulse optimization?', 'Trace how pulse parameters, an objective evaluator and the optimization strategy interact.', 'Implement a simulated objective interface before connecting to any experiment.', 'Closed-loop optimization between trials is not the same as feedback driven by a continuous measurement record.'),
    'P11': ('Software / spin dynamics', 'How can spin-dynamics simulation be organized for larger spin systems?', 'Study the simulation representation and the physical assumptions behind the model.', 'Run a small upstream spin simulation before adding control objectives.', 'Current Spinach optimal-control capabilities extend beyond this original simulation paper.'),
    'P12': ('Method / autodiff and GPU', 'How can automatic differentiation support richer control costs and accelerated computation?', 'Examine intermediate-time objectives, leakage-related criteria and computational tradeoffs.', 'Define a small custom penalty and verify a numerical gradient before measuring speed.', 'The reported speedups belong to the paper setup; they are not guaranteed for another machine or framework.'),
    'P13': ('Method and artifacts / semi-automatic differentiation', 'Can propagation derivatives and objective differentiation be separated efficiently?', 'Follow the chain-rule separation and compare it with differentiating the entire propagation.', 'Inspect the associated data and plotting code before attempting benchmark regeneration.', 'The artifact setup uses Julia/Python and its own environment; do not treat it as a drop-in Python or MATLAB package.'),
    'P14': ('Theory / measurement feedback', 'How do direct Markovian feedback and state-estimate-based feedback differ?', 'Identify the monitored two-level model, measurement assumptions and stabilization target.', 'Specify a conditional stochastic model and measurement record for a separate feedback study.', 'This catalog verifies no paper-specific code; an unconditional master-equation simulation alone does not implement measurement feedback.'),
}

def write(path, text):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding='utf-8')

repos = list(csv.DictReader((ROOT / 'catalog/repositories.csv').open(encoding='utf-8-sig')))
paper_text = (ROOT / 'papers/README.md').read_text(encoding='utf-8-sig')
paper_rows = {}
for line in paper_text.splitlines():
    if re.match(r'^\| P\d{2} \|', line):
        cells = [s.strip() for s in line.strip('|').split('|')]
        paper_rows[cells[0]] = cells

repo_index = ['# Repository profiles', '', '[Home](../README.md) · [Papers](../papers/README.md) · [Tiếng Việt](../README.vi.md)', '',
              'Each profile explains the role, a suggested first exercise, numerical checks and its boundary within a control research workflow. Exercises are editorial proposals, not claims of tested results.', '',
              '| Repository | Language | Research role | Profile |', '| :--- | :--- | :--- | :--- |']
for repo in repos:
    rid = repo['id']
    role, purpose, exercise, checks, boundary = REPOS[rid]
    related = repo['paper_ids'].split(';') if repo['paper_ids'] else []
    paper_links = ', '.join(f'[{p}](../papers/profiles/{p}.md)' for p in related) or 'No specific paper association asserted in this catalog.'
    source = f"https://github.com/{repo['repository']}"
    name = repo['repository'].split('/')[-1]
    repo_index.append(f"| [{repo['repository']}]({source}) | {repo['language']} | {role} | [Read profile]({rid}.md) |")
    write(ROOT / 'repositories' / f'{rid}.md', f'''# {name}

[All repositories](README.md) · [Home](../README.md) · [Source]({source})

| Field | Description |
| :--- | :--- |
| Upstream | [{repo['repository']}]({source}) |
| Language / ecosystem | {repo['language']} |
| Catalog category | {repo['category']} |
| Download group | {repo['priority']} |
| Research role | {role} |

## What this repository contributes

{purpose}

## Suggested first exercise

{exercise}

This is a proposed starting task. Consult the upstream README, examples and supported dependencies for executable instructions.

## What to check

{checks}

## Scope and limitations

{boundary}

## Related literature

{paper_links}

## Evidence and provenance

The capability summary refers to the [upstream project]({source}). The workflow suggestions are this catalog's editorial guidance. This profile does not claim an installation test, benchmark or paper reproduction. Read the upstream LICENSE and NOTICE at the version you use.
''')
write(ROOT / 'repositories/README.md', '\n'.join(repo_index) + '\n')

paper_index = ['# Detailed paper profiles', '', '[Paper map](README.md) · [Home](../README.md) · [Repositories](../repositories/README.md)', '',
               'Titles and bibliographic links come from the main paper map. Profiles add reading questions and proposed exercises; they are not full-text critical reviews or reproduced results.', '',
               '| ID | Paper | Type | Profile |', '| :--- | :--- | :--- | :--- |']
for pid, row in paper_rows.items():
    kind, question, focus, exercise, limitation = PAPERS[pid]
    _, citation, year, motivation, relationship = row
    title = re.search(r'\[([^\]]+)\]\(', citation).group(1)
    related = [r for r in repos if pid in r['paper_ids'].split(';')]
    code_links = ', '.join(f"[{r['repository']}](../../repositories/{r['id']}.md)" for r in related) or 'No linked implementation is asserted in the structured catalog.'
    # Original map links use absolute web URLs, so remain valid inside profiles.
    paper_index.append(f'| {pid} | {citation} | {kind} | [Read profile](profiles/{pid}.md) |')
    write(ROOT / 'papers/profiles' / f'{pid}.md', f'''# {pid}: {title}

[All papers](../README.md) · [Detailed index](../PROFILES.md) · [Home](../../README.md)

| Field | Description |
| :--- | :--- |
| Citation / primary source | {citation} |
| Year in catalog | {year} |
| Type | {kind} |
| Main relevance | {motivation} |

Year follows the main catalog convention: arXiv submission year for preprints and publication year for DOI-only entries. Export the formal citation from the primary record for your chosen version.

## Central reading question

{question}

## What to extract while reading

{focus}

Record the physical system, objective definition, control parameterization, assumptions and numerical validation used by the authors. Do not assume an abstract establishes implementation details not checked in the full text.

## Connection to software

{relationship}

Profiles in this catalog: {code_links}

## Suggested follow-up exercise

{exercise}

This exercise is proposed by the catalog. It is not necessarily an experiment or figure reported in the paper.

## Limits of interpretation

{limitation}

## Reproduction status

**Not reproduced in this repository.** Before making a reproduction claim, identify the exact paper revision and target figure, then preserve the code commit, environment, model parameters, seeds, numerical settings, raw results and analysis scripts. A later implementation of the same method is not automatically the paper's original code.
''')
write(ROOT / 'papers/PROFILES.md', '\n'.join(paper_index) + '\n')
print(f'Built {len(repos)} repository profiles and {len(paper_rows)} paper profiles.')
