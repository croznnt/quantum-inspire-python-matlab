# Working from MATLAB

**Language / Ngôn ngữ:** [Tiếng Việt](MATLAB.md) · **English** · [Home](../README.md)

## Native simulation and optimal control

[Spinach](https://github.com/IlyaKuprov/Spinach) is a native MATLAB spin-dynamics simulation library with an [optimal-control module](https://spindynamics.org/wiki/index.php?title=Optimal_control_module), including GRAPE workflows and pulse penalties. Start with its upstream examples and tutorials. Check the current README for the required MATLAB release and toolboxes; a MATLAB license alone may not cover the required setup.

Read [P11 and P04](../papers/README.md#reading-map), then use the [research guide](RESEARCH_GUIDE.md) to define a small spin-control benchmark. DYNAMO is another historical MATLAB framework discussed in P09; a current GitHub source mirror has not been verified here.

No official Quantum Inspire MATLAB SDK was verified within this survey. This concerns platform integration, not the availability of MATLAB simulation/control tools. The optional interoperability route below is a proposed approach, not a tested integration.

## Calling Python

1. Install a Python version compatible with your MATLAB release and the required Quantum Inspire packages.
2. In MATLAB, check `pyenv` and configure the correct interpreter before calling Python.
3. Authenticate through the CLI as described in the SDK documentation. Do not store tokens in `.m` files, notebooks, or Git.
4. Write a small Python wrapper that performs the task and returns simple data types. Call it from MATLAB through the `py` interface.
5. Verify the workflow with simulated data before submitting real jobs to the platform.

Environment check, without submitting a quantum circuit:

```matlab
pe = pyenv;
disp(pe);
qi = py.importlib.import_module('quantuminspire');
disp(qi);
```

If the import fails, check that the package is installed in the environment used by `pyenv`. The CLI's pipx environment does not automatically become MATLAB's Python environment.

## Exchanging JSON

Python can submit jobs, retrieve results, and save JSON. MATLAB can then read the file with `jsondecode(fileread('results.json'))`. Define the schema, bit ordering, shot count, and probability representation before analyzing results.

## Verification limits

MATLAB has not been run, Quantum Inspire authentication has not been tested, and no real jobs have been submitted. Version compatibility is not guaranteed. Consult the repository READMEs linked in the main catalog and the Python interface documentation for your MATLAB release.
