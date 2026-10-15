# Simulation and control research guide

[Home](../README.md) · [Tiếng Việt](RESEARCH_GUIDE.vi.md) · [Papers](../papers/README.md)

## Define the model before choosing an optimizer

Use a controlled Hamiltonian of the form

$$H(t)=H_0+\sum_k u_k(t)H_k.$$

For a closed system, propagate $\dot\psi=-iH\psi$ with $\hbar=1$. For a Markovian open system, a common model is

$$\dot\rho=-i[H,\rho]+\sum_j\left(L_j\rho L_j^\dagger-\tfrac12\{L_j^\dagger L_j,\rho\}\right).$$

State units explicitly. If detuning is in rad/s, do not supply a value in Hz without the factor of $2\pi$. Collapse operators include square roots of rates. A Lindblad model assumes a suitable Markovian description; it is not a universal description of arbitrary environmental memory.

The method summaries are guided by [P02](https://arxiv.org/abs/2205.15574) and the [qutip-qtrl guide](https://qutip.readthedocs.io/projects/qutip-qtrl/en/stable/guide/guide-control.html). The projects below are proposed exercises, not reproduced paper results.

## Choose a stack

| Goal | Starting stack | Reason and limitation |
| :--- | :--- | :--- |
| Learn state and density-matrix dynamics | QuTiP + tutorials | Inspect solver accuracy before optimization |
| Establish a GRAPE or CRAB baseline | qutip-qtrl | Dedicated control package; older tutorials may import qutip.control |
| Compare analytic controls | qutip-qoc | GOAT and JOPT, with GRAPE/CRAB through qtrl; inspect optional dependencies |
| Study sequential field updates | krotov | Good method documentation; check its supported QuTiP version independently |
| Optimize a custom numerical or experimental objective | QuOCS | Supports multiple search strategies; execution costs depend on the objective |
| Differentiate simulations or batch parameter sweeps | dynamiqs | JAX-based simulation; benchmark precision, memory, and device support |
| Work in MATLAB on spin systems | Spinach | Native spin simulation and optimal control; check MATLAB/toolbox requirements |
| Submit circuits to Quantum Inspire | Quantum Inspire SDK/providers | A platform integration layer, not an arbitrary waveform-control interface |

Follow each project's own installation instructions. Use separate environments for QuTiP control, Krotov, and JAX experiments until their dependency requirements have been checked. This catalog supplies no universal dependency lockfile and does not claim cross-package compatibility.

## Benchmark ladder

| Stage | Model and task | Baseline | Optimization extension | Evidence to save |
| :--- | :--- | :--- | :--- | :--- |
| B01 | One qubit, state transfer from ground to excited state | Constant resonant pulse | Bounded GRAPE | Populations, pulse, objective vs evaluations |
| B02 | One-qubit X gate | Analytic rotation | GRAPE vs GOAT or CRAB | Gate fidelity, duration, amplitude and smoothness |
| B03 | Detuning and amplitude uncertainty | Nominal B02 pulse | Ensemble-averaged robust control | Mean, minimum and distribution on a held-out uncertainty grid |
| B04 | Dissipative one-qubit state transfer | Unitary optimized pulse evaluated with damping | Optimize the Lindblad model | Density-matrix trace, positivity tolerance, population, purity |
| B05 | Coupled two-qubit entangling gate | Fixed drift evolution | Multi-channel bounded optimization | Gate metric, entanglement, runtime and dimension |
| B06 | Three-level weakly anharmonic model | Pulse from a two-level approximation | Leakage-penalized optimization | Leakage at final and intermediate times; truncation convergence |
| B07 | Monitored two-level system | Uncontrolled stochastic trajectories | Measurement feedback policy | Trajectory distributions, confidence intervals, efficiency and delay |

Begin with B01 and B02. B03 and B04 establish robustness and dissipation. B05 and B06 add model complexity. B07 is a separate feedback project, requiring a conditional stochastic model and explicit measurement record; a deterministic master-equation run alone is not a feedback simulation.

## Objective and constraint checklist

1. Define the task: state transfer, full gate, entangler, observable, or stabilization.
2. Specify the fidelity convention. For pure-state transfer, squared overlap is a common choice. For unitary gates on a full d-dimensional model, $|\mathrm{Tr}(U_\mathrm{target}^\dagger U)|^2/d^2$ is a phase-insensitive overlap, not automatically the same as average gate fidelity. A projected leaky evolution need not be unitary.
3. Report terminal infidelity separately from fluence, slew-rate, smoothness, leakage, and robustness penalties. An improved total cost does not imply every physical metric improved.
4. Enforce amplitude, bandwidth, duration, channel and sampling restrictions consistently. Clipping after optimization changes the simulated control.
5. Treat optimizer convergence as a numerical termination condition. It does not establish global optimality or hardware feasibility.

## Verification and fair comparisons

1. Validate the uncontrolled model against an analytic limit where possible. Check state norm or density-matrix trace and physicality.
2. Re-evaluate the optimized pulse with a finer propagation grid or tighter tolerances. Increase the Hilbert-space cutoff for oscillator or leakage models.
3. Check gradients against finite differences on a small instance before trusting a custom gradient implementation.
4. Compare the same Hamiltonian, time horizon, initial guesses, parameter bounds and physical objective. Report function/gradient evaluations, wall time, precision and hardware; iteration counts alone are not comparable.
5. Use multiple seeds and hold out uncertain parameters for robustness evaluation. Separate optimization samples from validation samples.
6. Save source commit hashes, dependency versions, solver configuration, pulse arrays and units, raw trajectories, optimizer logs and plotting code.

## Current evidence level

Repository and paper descriptions are based on linked primary sources. No package was installed or benchmark executed as part of this catalog expansion. No hardware job was submitted. Use upstream tutorials for executable starting points; all benchmark rows above are proposals.
