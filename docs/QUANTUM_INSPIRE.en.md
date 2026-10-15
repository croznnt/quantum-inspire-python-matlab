# Quantum Inspire ecosystem

[Research hub](../README.md) · [Tiếng Việt](QUANTUM_INSPIRE.vi.md)

This supporting catalog preserves the 10 original platform references. It is separate from the simulation/control software list. Checked October 15, 2026.

| Repository | Role | Research relevance |
| :--- | :--- | :--- |
| [quantuminspire](https://github.com/QuTech-Delft/quantuminspire) | Python SDK and CLI | Authentication and platform workflows |
| [qiskit-quantuminspire](https://github.com/QuTech-Delft/qiskit-quantuminspire) | Qiskit provider | Circuit integration |
| [pennylane-quantuminspire](https://github.com/QuTech-Delft/pennylane-quantuminspire) | PennyLane provider | Algorithm integration |
| [quantum-inspire-examples](https://github.com/QuTech-Delft/quantum-inspire-examples) | Python examples and notebooks | Check older APIs and ProjectQ dependencies |
| [OpenSquirrel](https://github.com/QuTech-Delft/OpenSquirrel) | Python quantum compiler | Program transformation |
| [libqasm](https://github.com/QuTech-Delft/libqasm) | cQASM parsing | Language tooling |
| [OpenQL](https://github.com/QuTech-Delft/OpenQL) | C++/Python programming framework | Compilation research |
| [QuIS](https://github.com/QuTech-Delft/QuIS) | Instruction set specification | Ecosystem instruction reference |
| [qilib](https://github.com/QuTech-Delft/qilib) | Utility library | Supporting historical workflows; inspect dependencies |
| [quantuminspire2](https://github.com/QuTech-Delft/quantuminspire2) | Archived SDK | Historical reference, excluded from downloads |

## Platform setup

Follow the SDK README and supported Python versions. Its documented CLI route is `pipx install quantuminspire`, followed by `qi --help` and `qi login`. The CLI environment is separate from notebook environments. Use provider-specific documentation for [Qiskit](https://qutech-delft.github.io/qiskit-quantuminspire/) and [PennyLane](https://qutech-delft.github.io/pennylane-quantuminspire/).

From the repository root, `./scripts/clone-sources.ps1 -Group platform` downloads the 9 non-historical references without installing or executing them.

## Control boundary

A circuit provider is not a numerical Hamiltonian-control solver. Do not assume arbitrary waveform upload, real-time measurement access, or feedback support from the presence of a provider. Verify the actual backend interface before mapping a simulated control protocol onto hardware. Use the [research guide](RESEARCH_GUIDE.md) for the simulation route and [MATLAB guide](MATLAB.en.md) for native Spinach or Python interoperability.

These links identify upstream projects, not a claim that all packages share compatible versions. Preserve their licenses and notices when reusing source code.
