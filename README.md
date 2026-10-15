# ⚛️ Quantum Dynamics & Optimal Control

<p align="center">
  <a href="https://github.com/qutip/qutip"><img src="https://avatars.githubusercontent.com/u/2517630?v=4" width="64" height="64" alt="QuTiP organization avatar"></a>&nbsp;&nbsp;
  <a href="https://github.com/Quantum-OCS/QuOCS"><img src="https://avatars.githubusercontent.com/u/80833925?v=4" width="64" height="64" alt="QuOCS organization avatar"></a>&nbsp;&nbsp;
  <a href="https://github.com/dynamiqs/dynamiqs"><img src="https://avatars.githubusercontent.com/u/135633837?v=4" width="64" height="64" alt="dynamiqs organization avatar"></a>&nbsp;&nbsp;
  <a href="https://github.com/QuTech-Delft/quantuminspire"><img src="https://avatars.githubusercontent.com/u/42680367?v=4" width="64" height="64" alt="QuTech organization avatar"></a>
</p>
<p align="center"><a href="https://github.com/qutip/qutip">QuTiP</a> · <a href="https://github.com/Quantum-OCS/QuOCS">QuOCS</a> · <a href="https://github.com/dynamiqs/dynamiqs">dynamiqs</a> · <a href="https://github.com/QuTech-Delft/quantuminspire">QuTech</a></p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3776AB?style=flat-square&amp;logo=python&amp;logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/MATLAB-e16737?style=flat-square" alt="MATLAB">
  <img src="https://img.shields.io/badge/Repositories-19-2563eb?style=flat-square" alt="19 repositories">
  <img src="https://img.shields.io/badge/Papers-14-7c3aed?style=flat-square" alt="14 papers">
</p>

**Language:** **English** · [Tiếng Việt](README.vi.md)

A research hub for **numerical quantum dynamics, pulse design, robust control, and quantum optimal control**, centered on Python and MATLAB. Quantum Inspire is retained as a platform-integration reference.

## 📊 At a glance

| Resource | Count | Scope |
| :--- | :--- | :--- |
| Simulation and control software | **7** | QuTiP, qtrl, qoc, Krotov, QuOCS, dynamiqs, Spinach |
| Tutorial / paper-artifact repositories | **2** | QuTiP tutorials and semi-automatic differentiation artifacts |
| Quantum Inspire ecosystem repositories | **10** | SDKs, providers, examples, compilers and historical references |
| Total repositories | **19** | Unique entries in [the catalog](catalog/repositories.csv) |
| Annotated papers | **14** | Reviews, methods, software and feedback theory |
| Proposed simulation benchmarks | **7** | One-qubit control through measurement feedback |

Counts describe this catalog, not all available resources. Source descriptions were checked online. No package compatibility test, benchmark or paper reproduction has been performed here.

**Explore:** [Papers](papers/README.md) · [Research guide](docs/RESEARCH_GUIDE.md) · [MATLAB](docs/MATLAB.en.md) · [Quantum Inspire](docs/QUANTUM_INSPIRE.en.md)

**Visual key:** ⚛️ simulation · 🎛️ control · 📓 tutorials · 🧪 reproduction artifacts · ☁️ platform · ⚙️ compiler · 📐 specification · 🗄️ historical

## 🧭 Find the right resource

| I want to… | Start here | Then explore |
| :--- | :--- | :--- |
| Simulate controlled quantum dynamics | [QuTiP profile](repositories/qutip.md) | [Simulation paper P03](papers/profiles/P03.md) |
| Optimize a time-discretized pulse | [qutip-qtrl profile](repositories/qtrl.md) | [GRAPE paper P04](papers/profiles/P04.md) |
| Compare sequential control updates | [Krotov profile](repositories/krotov.md) | [Krotov paper P05](papers/profiles/P05.md) |
| Design smooth parameterized pulses | [qutip-qoc profile](repositories/qoc.md) | [GOAT paper P08](papers/profiles/P08.md) |
| Use a custom objective or dCRAB | [QuOCS profile](repositories/quocs.md) | [QuOCS paper P10](papers/profiles/P10.md) |
| Use MATLAB for spin control | [Spinach profile](repositories/spinach.md) | [Spinach paper P11](papers/profiles/P11.md) |
| Study continuous measurement feedback | [Feedback paper P14](papers/profiles/P14.md) | [Research guide](docs/RESEARCH_GUIDE.md) |
| Browse everything with descriptions | [19 repository profiles](repositories/README.md) | [14 paper profiles](papers/PROFILES.md) |

Each repository profile covers **purpose, first exercise, checks, limitations and related literature**. Each paper profile covers **reading question, method focus, code relationship, follow-up exercise and reproduction status**. Suggested exercises are editorial guidance, not tested examples or reproduced paper results.

## 🎯 Research scope

The workflow is **physical model → reliable propagation → objective and constraints → pulse optimization → independent validation**. The focus is classical numerical simulation of controlled quantum systems. Circuit submission and platform integration are supporting topics.

The [research guide](docs/RESEARCH_GUIDE.md) covers Hamiltonian and Lindblad models, fidelity conventions, uncertainty ensembles, leakage, numerical convergence and fair comparisons. Its benchmark proposals are starting projects, not reproduced results.

## 🧰 Software map

| Project | Language | Capabilities | Starting use | Paper IDs |
| :--- | :--- | :--- | :--- | :--- |
| [QuTiP](https://github.com/qutip/qutip) | Python | Time-dependent dynamics and open-system solvers | Validate a physical model | P03 |
| [qutip-qtrl](https://github.com/qutip/qutip-qtrl) | Python | GRAPE and CRAB | Bounded pulse optimization baseline | P04, P06 |
| [qutip-qoc](https://github.com/qutip/qutip-qoc) | Python | GOAT, JOPT; GRAPE/CRAB via qtrl | Analytic pulse parameterizations | P08 |
| [krotov](https://github.com/qucontrol/krotov) | Python | Krotov updates | State transfer and gate objectives | P05 |
| [QuOCS](https://github.com/Quantum-OCS/QuOCS) | Python | GRAPE, dCRAB, direct search | Custom numerical or experimental objectives | P07, P10 |
| [dynamiqs](https://github.com/dynamiqs/dynamiqs) | Python / JAX | Differentiable, batched simulation | Parameter sweeps and custom gradients | See upstream citation |
| [Spinach](https://github.com/IlyaKuprov/Spinach) | MATLAB | Spin dynamics and optimal control including GRAPE | Native MATLAB spin-control studies | P04, P11 |

This is a capability map, not a performance ranking. qutip-qoc builds on qutip-qtrl; they are not independent implementations of every listed algorithm. Follow each project's installation instructions and use separate environments until dependency compatibility has been checked.

### Tutorials and reproduction artifacts

| Repository | Language | Contents |
| :--- | :--- | :--- |
| [qutip-tutorials](https://github.com/qutip/qutip-tutorials) | Python / notebooks | Upstream tutorials; match dependencies to your environment |
| [2022-04_semiad_paper](https://github.com/ARLQCI/2022-04_semiad_paper) | Julia / Python | Scripts, notebooks and data associated with P13, outside the primary Python/MATLAB stack |

## 📚 Literature and reading path

The [annotated paper collection](papers/README.md) provides titles, authors, dates, primary-source links, method notes and explicit paper-to-code relationships.

| Track | Papers | Intended outcome |
| :--- | :--- | :--- |
| Orientation | P01, P02 | Define the system, task and constraints |
| Simulation | P03, P11 | Understand propagation and spin modeling |
| Gradient methods | P04, P05, P09 | Compare GRAPE and Krotov on a shared task |
| Reduced / analytic controls | P06, P07, P08, P10 | Choose CRAB, dCRAB or GOAT parameterizations |
| Differentiable optimization | P12, P13 | Evaluate autodiff and semi-automatic differentiation |
| Measurement feedback | P14 | Design a conditional-dynamics study |

Start with **P02 → P03 → P04**, then [B01 and B02](docs/RESEARCH_GUIDE.md#benchmark-ladder). Continue with uncertainty, dissipation and leakage before claiming practical robustness. Experimental closed-loop pulse optimization between trials differs from feedback during evolution; open-system dynamics is a separate distinction.

## 🔬 MATLAB and Quantum Inspire

**Spinach** provides a native MATLAB route for spin simulation and control. Check its upstream MATLAB and toolbox requirements. No official MATLAB SDK specifically for Quantum Inspire was verified; this does not mean MATLAB lacks quantum-control tools.

See the [MATLAB guide](docs/MATLAB.en.md) and [original platform catalog](docs/QUANTUM_INSPIRE.en.md). Circuit submission must not be assumed to expose arbitrary waveform control or continuous measurement feedback.

## 📥 Download selected sources

Run in PowerShell from this repository:

```powershell
# Recommended starting set: 7 repositories
./scripts/clone-sources.ps1
# All 9 research software, tutorial and paper-artifact entries
./scripts/clone-sources.ps1 -Group research
# Original ecosystem, excluding archived quantuminspire2
./scripts/clone-sources.ps1 -Group platform
# All 18 non-historical entries
./scripts/clone-sources.ps1 -Group all
# Show selection without downloads
./scripts/clone-sources.ps1 -Group all -ListOnly
```

The script reads [repositories.csv](catalog/repositories.csv), clones into `sources/<owner>/<repo>`, and skips existing paths. It does not install dependencies, execute downloaded code, update or delete existing clones. Historical quantuminspire2 is excluded from downloads.

## 🗂 Documentation layout

| Path | Contents |
| :--- | :--- |
| [README.vi.md](README.vi.md) | Vietnamese landing page |
| [papers/](papers/README.md) | Annotated literature and Vietnamese companion |
| [catalog/](catalog/repositories.csv) | Machine-readable source inventory |
| [Research guide](docs/RESEARCH_GUIDE.md) | Models, objectives, constraints and benchmark proposals |
| [Vietnamese research guide](docs/RESEARCH_GUIDE.vi.md) | Vietnamese research companion |
| [MATLAB guide](docs/MATLAB.en.md) | Native MATLAB and optional Python/JSON routes |
| [Quantum Inspire catalog](docs/QUANTUM_INSPIRE.en.md) | Original 10 ecosystem references |
| [Download script](scripts/clone-sources.ps1) | Selective cloning, no installations |

## 📋 Reproducibility and contributions

1. Add resources with a concrete control/simulation use case and a primary-source link.
2. Distinguish paper-associated software, later method implementations, and reproduction artifacts.
3. Keep counts, catalog entries, download groups and both language entry pages consistent.
4. Record exact versions, commits, seeds, units, model definitions, solver tolerances, pulses, objective conventions, logs and raw data when claiming results.
5. Respect upstream LICENSE and NOTICE files. Link to papers instead of redistributing PDFs without permission.

English is the default; Vietnamese companions are available through language links. This repository contains original annotations and links. Upstream code and paper results remain attributed to their respective authors.
