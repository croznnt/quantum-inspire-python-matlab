# Quantum Inspire: Python and MATLAB

**Language / Ngôn ngữ:** [Tiếng Việt](README.md) · **English**

A curated catalog of source code, notebooks, and tools in the Quantum Inspire ecosystem, with a focus on Python and ways to connect MATLAB.

**Survey updated:** October 15, 2026 · **Account:** `croznnt` · **Proposed repository:** `quantum-inspire-python-matlab`

## 📊 Catalog overview

| Metric | Count | Scope |
| :--- | :--- | :--- |
| Repositories cataloged | **10** | Repositories in the three tables below |
| Primary Python sources | **6** | SDK, integrations, examples, compiler, and utilities |
| Supporting tools and specifications | **3** | OpenQL, libqasm, and QuIS; OpenQL also provides a Python interface |
| Historical repositories | **1** | Archived quantuminspire2 SDK |
| Verified official MATLAB SDKs | **0** | None identified within this survey |
| Repositories in the download script | **9** | Excludes quantuminspire2 |

These groups help readers navigate the catalog. They are not a survey of all GitHub repositories. Counts describe this catalog, not maintenance activity or tested compatibility.

**Quick links:** [Python sources](#python-sources) · [Supporting tools](#supporting-tools) · [MATLAB](#matlab) · [Download](#download) · [Publish to GitHub](#publish)

<a id="python-sources"></a>

## 🐍 Python sources

Python is the main source language in this catalog. Start with the SDK, choose Qiskit or PennyLane, then explore the notebooks.

| Repository | Source type | Purpose | Suggested use |
| :--- | :--- | :--- | :--- |
| [quantuminspire](https://github.com/QuTech-Delft/quantuminspire) | SDK and CLI | Authenticate and interact with the platform | **Start here** |
| [qiskit-quantuminspire](https://github.com/QuTech-Delft/qiskit-quantuminspire) | Qiskit integration | Work with quantum circuits through Qiskit | For Qiskit workflows |
| [pennylane-quantuminspire](https://github.com/QuTech-Delft/pennylane-quantuminspire) | PennyLane integration | Connect backends to PennyLane workflows | For PennyLane workflows |
| [quantum-inspire-examples](https://github.com/QuTech-Delft/quantum-inspire-examples) | Python and Jupyter notebooks | Learn algorithms through examples | Check older APIs, Qiskit, and ProjectQ dependencies |
| [OpenSquirrel](https://github.com/QuTech-Delft/OpenSquirrel) | Python compiler | Process and transform quantum programs | Compiler research |
| [qilib](https://github.com/QuTech-Delft/qilib) | Utility library | Explore Quantum Inspire utility classes | Check dependencies separately |

### Getting started with Python

1. Read the `quantuminspire` README and supported Python versions.
2. Install the CLI using the official instructions with `pipx install quantuminspire`, then run `qi --help` and `qi login`.
3. Choose Qiskit or PennyLane and follow that integration's documentation. The CLI's pipx environment is separate from the Python environment containing notebooks and integrations.
4. Use separate environments for older examples. Do not assume all repositories can share one environment.

Documentation: [Qiskit](https://qutech-delft.github.io/qiskit-quantuminspire/) and [PennyLane](https://qutech-delft.github.io/pennylane-quantuminspire/).

<a id="supporting-tools"></a>

## 🧩 Supporting tools and specifications

| Repository | Technology or content | Role |
| :--- | :--- | :--- |
| [OpenQL](https://github.com/QuTech-Delft/OpenQL) | C++ and Python | Quantum programming and compilation framework |
| [libqasm](https://github.com/QuTech-Delft/libqasm) | cQASM parsing library | Reference for processing cQASM |
| [QuIS](https://github.com/QuTech-Delft/QuIS) | Instruction set specification | Reference for instructions used in the ecosystem |

### Historical sources

| Repository | Status | Purpose |
| :--- | :--- | :--- |
| [quantuminspire2](https://github.com/QuTech-Delft/quantuminspire2) | Archived | Explore SDK history; prefer quantuminspire for new projects |

<a id="matlab"></a>

## 🔬 MATLAB and Python support

| Criterion | Python | MATLAB |
| :--- | :--- | :--- |
| Sources in this catalog | SDK, integrations, and notebooks | No official SDK verified |
| Starting point | quantuminspire | Python connection guide below |
| Suggested workflow | Follow each repository's documentation | Call Python or exchange JSON |
| Tested in this project | No | No |

Searches for `quantuminspire matlab` and `quantum-inspire matlab` did not identify an official MATLAB SDK on GitHub. This does not establish that no community projects exist.

The proposed approach is to call Python from MATLAB or exchange results through JSON. This is an architectural suggestion, not a tested integration. See the [MATLAB guide](docs/MATLAB.en.md).

<a id="download"></a>

## 📥 Download source repositories

Run from the repository directory in PowerShell:

```powershell
./scripts/clone-sources.ps1
```

The script clones the main repositories into `sources/`, skips existing paths, and does not install packages or run code from those repositories. Each repository retains its own history and license. The `sources/` directory is excluded from this catalog's Git history.

### Directory structure

```text
.
├── README.md                  Vietnamese catalog and statistics
├── README.en.md               English version
├── docs/
│   ├── MATLAB.md              Vietnamese MATLAB guide
│   └── MATLAB.en.md           English MATLAB guide
├── scripts/
│   └── clone-sources.ps1       Downloads 9 source repositories
└── sources/                   Created after download, ignored by Git
```

<a id="publish"></a>

## ☁️ Publish to GitHub

After installing GitHub CLI and signing in with `gh auth login`, run from the project directory:

```powershell
gh repo create croznnt/quantum-inspire-python-matlab --private --source . --remote origin --push
```

Use this command for the initial publication: it creates a private repository and pushes existing commits to GitHub. Once the `origin` remote exists, use `git push` for subsequent updates.

## Sources and copyright

When changing the catalog, counts, or instructions, update both `README.md` and `README.en.md`. The MATLAB guide is also maintained in both languages under `docs/`.

This catalog prioritizes repositories from the QuTech Delft organization. Each table entry links to its source. Status and APIs may change after the survey date. The catalog text was written separately; third-party source code is not copied here. Before reusing code, read LICENSE and NOTICE at the relevant source revision and preserve the copyright notices required by that repository.
