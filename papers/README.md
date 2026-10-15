# Papers: quantum dynamics and optimal control

[Home](../README.md) · [Tiếng Việt](README.vi.md) · [Repository catalog](../catalog/repositories.csv)

**Detailed reading:** [Browse all 14 paper profiles](PROFILES.md) · [Browse 19 repository profiles](../repositories/README.md)

The reading map below is a compact index. Each detailed profile adds a central question, what to extract from the paper, software connections, a proposed exercise and limits of interpretation.

Selection checked on October 15, 2026. These are annotated entry points, not a systematic literature review. Years below are preprint years for arXiv entries and publication years for DOI-only entries. A software link can be a later implementation of a method; it is not necessarily the authors' original code or a reproduction of all paper results.

## Reading map

| ID | Paper and authors | Year | Why read it? | Code relationship |
| :--- | :--- | :--- | :--- | :--- |
| P01 | Koch et al., [Quantum optimal control in quantum technologies. Strategic report on current status, visions and goals for research in Europe](https://arxiv.org/abs/2205.12110) | 2022 | Broad map of controllability, open systems, applications, and research challenges | Review; no single reproduction repository asserted |
| P02 | Mahesh, Batra and Ram, [Quantum Optimal Control: Practical Aspects and Diverse Methods](https://arxiv.org/abs/2205.15574) | 2022 | Accessible comparison of objectives, constraints, robustness, and method families | Review; compare methods using the catalog |
| P03 | Lambert et al., [QuTiP 5: The Quantum Toolbox in Python](https://arxiv.org/abs/2412.04705) | 2024 | Numerical dynamics, solver ecosystem, and control extensions | [QuTiP](https://github.com/qutip/qutip), [tutorial collection](https://github.com/qutip/qutip-tutorials); tutorials evolve independently |
| P04 | Khaneja, Reiss, Kehlet, Schulte-Herbrüggen and Glaser, [Optimal control of coupled spin dynamics: design of NMR pulse sequences by gradient ascent algorithms](https://doi.org/10.1016/j.jmr.2004.11.004) | 2005 | Foundational GRAPE paper: optimize discretized control amplitudes for spin dynamics | Later implementations: [qutip-qtrl](https://github.com/qutip/qutip-qtrl), [Spinach](https://github.com/IlyaKuprov/Spinach) |
| P05 | Goerz et al., [Krotov: A Python implementation of Krotov's method for quantum optimal control](https://arxiv.org/abs/1902.11284) | 2019 | Sequential pulse updates, state transfer, gates, and convergence assumptions | Paper-associated package: [krotov](https://github.com/qucontrol/krotov) |
| P06 | Caneva, Calarco and Montangero, [Chopped random-basis quantum optimization](https://arxiv.org/abs/1103.0855) | 2011 | Search a reduced pulse basis rather than every time sample | Later implementation: [qutip-qtrl](https://github.com/qutip/qutip-qtrl) |
| P07 | Rach, Müller, Calarco and Montangero, [Dressing the chopped-random-basis optimization: a bandwidth-limited access to the trap-free landscape](https://arxiv.org/abs/1506.04601) | 2015 | Understand basis updates in dCRAB and the role of control constraints | Later implementation: [QuOCS](https://github.com/Quantum-OCS/QuOCS) |
| P08 | Machnes, Assémat, Tannor and Wilhelm, [Gradient optimization of analytic controls: the route to high accuracy quantum optimal control](https://arxiv.org/abs/1507.04261) | 2015 | GOAT for analytic pulse parameterizations and sensitivities | Later extended implementation: [qutip-qoc](https://github.com/qutip/qutip-qoc) |
| P09 | Machnes et al., [Comparing, Optimising and Benchmarking Quantum Control Algorithms in a Unifying Programming Framework](https://arxiv.org/abs/1011.4874) | 2010 | Compare GRAPE and Krotov update schemes; introduces MATLAB DYNAMO | Historical code location is linked by the paper; no GitHub mirror verified here |
| P10 | Rossignolo et al., [QuOCS: The Quantum Optimal Control Suite](https://arxiv.org/abs/2212.11144) | 2022 | Connect numerical objectives and experimental optimization workflows | Paper-associated package: [QuOCS](https://github.com/Quantum-OCS/QuOCS); [journal DOI](https://doi.org/10.1016/j.cpc.2023.108782) |
| P11 | Hogben et al., [Spinach: A software library for simulation of spin dynamics in large spin systems](https://doi.org/10.1016/j.jmr.2010.11.008) | 2011 | Spin dynamics and Liouville-space simulation foundations | Current project: [Spinach](https://github.com/IlyaKuprov/Spinach); current control features extend beyond the original paper |
| P12 | Leung, Abdelhafez, Koch and Schuster, [Speedup for quantum optimal control from automatic differentiation based on graphics processing units](https://arxiv.org/abs/1612.04929) | 2016 | Autodiff, intermediate-time penalties, leakage, and computational cost | Method reference; no original code repository verified in this catalog |
| P13 | Goerz, Carrasco and Malinovsky, [Quantum Optimal Control via Semi-Automatic Differentiation](https://arxiv.org/abs/2205.15044) | 2022 | Separate propagation derivatives from objective differentiation | Author-associated [scripts, notebooks and data](https://github.com/ARLQCI/2022-04_semiad_paper), Julia / Python; [published paper](https://quantum-journal.org/papers/q-2022-12-07-871/) |
| P14 | Wiseman, Mancini and Wang, [Bayesian feedback versus Markovian feedback in a two-level atom](https://arxiv.org/abs/quant-ph/0201145) | 2002 | Distinguish state-estimate feedback from direct measurement feedback | Theory reference; implementing a controller and validating its measurement model are separate tasks |

## Method selection

| Method | Optimization variables | Useful first problem | What to inspect |
| :--- | :--- | :--- | :--- |
| GRAPE | Pulse amplitudes on a time grid | One-qubit state transfer or unitary gate | Derivative accuracy, time discretization, bounds, initial guess |
| Krotov | Sequential field updates | State transfer with a running pulse cost | Update equation, discretization, step size; monotonicity assumptions do not imply a global optimum |
| CRAB / dCRAB | Coefficients of a truncated pulse basis | Smooth pulses with limited search dimension | Basis bandwidth, restarts, coefficient bounds, evaluation budget |
| GOAT | Parameters of analytic pulse functions | Smooth calibrated gate pulses | Sensitivity equations, parameter scaling, constraints |
| Autodiff / JOPT | Differentiable control parameters | Custom leakage and robustness objectives | Memory, numerical precision, solver differentiation, gradient checks |
| Measurement feedback | Control policy driven by measurement records or a state estimate | Stabilization of a monitored two-level system | Detection efficiency, backaction, feedback delay, trajectory statistics |

Experimental closed-loop pulse optimization evaluates and updates a pulse between trials. Measurement-based feedback changes the control using measurements during evolution. Open-system dynamics concerns coupling to an environment. These are different distinctions; an open quantum system may still use open-loop control.

## Suggested reading order

1. Read P02 and the scope of P01; define a physical model and the intended task.
2. Use P03 and QuTiP tutorials to validate uncontrolled dynamics.
3. Read P04 and optimize a bounded pulse with qutip-qtrl.
4. Read P05 and P09 to compare update rules under the same objective and simulation accuracy.
5. Read P06, P07, P08 and P10 for reduced pulse bases and parameterized controls.
6. Read P12 and P13 when custom objectives or larger computational budgets justify autodiff.
7. Read P11 for MATLAB spin simulations, or P14 for a separate feedback-control study.

## Reproduction record

No paper result is claimed reproduced here. For each attempted reproduction, record the exact figure or table, paper revision, code commit, dependency lockfile, units, initial and target states, Hilbert-space truncation, controls, noise model, solver tolerances, objective convention, random seeds, restart count, evaluation budget, and hardware. Save raw results together with the plotting script and explain any differences from the paper.

Link to publisher or author-hosted copies. Do not assume that a publicly readable PDF permits redistribution. Export formal BibTeX from the linked publisher or arXiv record when citing a specific version.
