# Quantum Computing Fundamentals with Qiskit

## By Swayam Shakya

A circuit-first, beginner-friendly journey from one qubit to entanglement, quantum algorithms, teleportation, and noise. The project uses **Qiskit as its main quantum framework** and **Qiskit Aer** for dynamic circuits and noise. Explanations are conversational; every Python comment begins with an **-ing** word.

[Start with the notebook](qiskit_fundamentals_colab.ipynb) · [Python export](qiskit_fundamentals.py) · [Validation record](VALIDATION.md)

![Qiskit Bell circuit](assets/09_bell_circuit.png)

## Run in Google Colab

1. Extract the ZIP.
2. Open [Google Colab](https://colab.research.google.com/).
3. Select **File → Upload notebook**, and upload `qiskit_fundamentals_colab.ipynb`.
4. Choose a fresh **Python 3 CPU** runtime, then **Runtime → Run all**.
5. Let the first cell finish installing Qiskit, Aer, and circuit-drawing support.
6. Read the results and try the six exercises before their solutions.

Only the notebook is needed: it generates its own figures and CSV files. No IBM account, API key, Drive mount, GPU, or external data is required. The initial package installation needs internet access. Existing NumPy and Matplotlib versions are preserved in Colab, and the actual environment is printed and saved.

Use the Files sidebar to download `qiskit_generated_results.zip` after a run. Use **File → Download → Download .ipynb** to save your executed notebook. Colab's temporary filesystem is not saved merely by saving the notebook.

**Live Colab verification remains pending authentication.** The connected browser reached Colab but is signed out. The supplied outputs and test results are from successful local execution, not a Google Colab run. This distinction is also recorded in [VALIDATION.md](VALIDATION.md).

## Learning roadmap

| Lesson | What you implement | Qiskit tools |
|---|---|---|
| 0–1 | Installation, versions, reusable helpers | Qiskit 2.6.1, Aer 0.18.2 |
| 2 | Qubits, amplitudes, Born probabilities | `QuantumCircuit`, `initialize`, `Statevector` |
| 3 | Shots, repeated measurement, reset | `StatevectorSampler`, `AerSimulator` |
| 4 | X/Y/Z/H/S/T, gate order, inverse | Circuit gates, `Operator`, `inverse` |
| 5 | Rx/Ry/Rz, Bloch sphere, angle sweep | `Parameter`, `assign_parameters`, `Pauli` |
| 6 | Global/relative phase and interference | `p`, `global_phase`, state equivalence |
| 7 | Bit ordering, CNOT, SWAP, Toffoli | `cx`, `swap`, `ccx` |
| 8 | Bell and GHZ states, reduced states | `partial_trace`, `DensityMatrix` |
| 9 | Deutsch's algorithm and phase kickback | Gate-based oracles |
| 10 | Grover's four-item search | `cz` phase oracle and diffuser |
| 11 | Teleportation with measurements and corrections | `if_test`, conditional density-matrix saves |
| 12 | Mixtures, coherence, purity, bit-flip noise | Aer `pauli_error`, Qiskit channels |
| 13 | Compilation and basis gates | `transpile`, `count_ops`, `depth` |
| 14–15 | Exercises, checked solutions, result export | Assertions and artifact export |

Allow about 2–3 hours with exercises. The scope is a fundamentals introduction, not every quantum algorithm or a complete error-correction course.

## Important Qiskit conventions

- **q0 is the top circuit wire but the rightmost bit in ordinary state/result strings.** Two-qubit states are displayed as `q1q0`.
- Classical strings use the same significance convention: teleportation's message is `c1c0`, or `b a`.
- `Statevector` is used for unmeasured unitary/preparation circuits; the reference `StatevectorSampler` supports final measurement, not mid-circuit measurement.
- Aer executes the repeated-measurement, reset, teleportation, and noise demonstrations.
- Qiskit computes quantum states and channels. NumPy is used for angles, plotting arrays, expected-value comparisons, and a few explicitly described state preparations.
- These are classical simulations, not hardware experiments or evidence of practical speedup.

## Tested environment and evidence

| Component | Recorded value |
|---|---|
| Author | Swayam Shakya |
| Python | 3.12.14 |
| Qiskit | 2.6.1 |
| Qiskit Aer | 0.18.2 |
| NumPy | 2.5.4 |
| Matplotlib | 3.11.2 |
| pylatexenc | 2.10 |
| Executed code cells | 16, all completed without errors |
| Successful assertions | 303, including state-normalization checks |
| Notebook Python comments | 50, all starting with an -ing word |
| Figures | 21 PNG and 21 matching SVG files |
| Teleportation coverage | 6 input states × all 4 classical branches |
| First execution | Local in-process IPython, in notebook order |
| Google Colab execution | Pending sign-in; not claimed as completed |
| Review date | 2026-10-28 |

Qiskit 2.6.1 and Aer 0.18.2 were checked against current official/package documentation and installed for this run. The notebook pins those releases. Other future versions are not guaranteed. Exact installed packages are recorded in `requirements-tested.txt`; notebook verification dependencies are in `requirements-dev.txt`.

No errors or stderr warnings were recorded in the delivered notebook outputs. Check details are in [results/checks.json](results/checks.json), and actual package versions are in [results/environment.json](results/environment.json).

## Publish the repository on GitHub

Upload the **contents** of the extracted project folder, keeping `README.md`, the notebook, `assets/`, `results/`, and `tools/` together at the repository root. Do not upload only the ZIP if you want GitHub to render the notebook and images. All image links are relative and already match this folder layout.

After uploading, use Colab's GitHub tab with your repository URL. A repository-specific Colab badge is not hard-coded because no GitHub username/repository name was supplied. Nothing has been published automatically.

## Run or verify locally

Use Python 3.12 for the recorded environment. Create and activate a virtual environment, then:

```bash
python -m pip install -r requirements-tested.txt
python qiskit_fundamentals.py
```

For automated verification:

```bash
python -m pip install -r requirements-dev.txt
python tools/verify_notebook.py
```

The verifier runs all code in an empty temporary directory, checks all Python-comment prefixes, validates the notebook structure, and checks that every PNG/SVG is generated. It does not overwrite the delivered notebook outputs. The Python export uses IPython's display helper for figure presentation; IPython is included in the requirements.

## Repository contents

| File or folder | Purpose |
|---|---|
| `qiskit_fundamentals_colab.ipynb` | Complete lesson, saved outputs, and embedded images |
| `qiskit_fundamentals.py` | Equivalent runnable Python export |
| `README.md` | Instructions, all figure images, interpretation, output transcript |
| `assets/` | 21 generated figures in PNG and SVG |
| `results/` | CSV values, environment, checks, captions, console transcript |
| `tools/verify_notebook.py` | Independent verification from an empty output directory |
| `requirements*.txt` | Runtime and verification dependencies |
| `VALIDATION.md` | Actual test evidence and the pending Colab step |
| `.gitignore` | Excluding local caches and generated result ZIPs |

## Results gallery

Every image below is an actual output of the delivered Qiskit notebook. Circuit diagrams are generated by Qiskit's Matplotlib drawer, not manually drawn approximations. SVGs are provided for crisp resizing; CSVs expose numerical data where relevant.

### 01 Qubit Probabilities

![01 Qubit Probabilities](assets/01_qubit_probabilities.png)

Qiskit calculates amplitudes and Born probabilities for all four preparations.

[SVG](assets/01_qubit_probabilities.svg) · [Numerical data](results/01_qubit_probabilities.csv)

### 02 Measurement Histogram

![02 Measurement Histogram](assets/02_measurement_histogram.png)

Sampling is finite-shot; exact theoretical probabilities are 0.5 and 0.5.

[SVG](assets/02_measurement_histogram.svg) · [Numerical data](results/02_measurement_histogram.csv)

### 03 Repeated Measurement Circuit

![03 Repeated Measurement Circuit](assets/03_repeated_measurement_circuit.png)

Aer simulates two measurements of one qubit; count strings display c1c0.

[SVG](assets/03_repeated_measurement_circuit.svg)

### 04 Gate Amplitudes

![04 Gate Amplitudes](assets/04_gate_amplitudes.png)

H maps |+> to |0>; phase gates change relative phase in different ways.

[SVG](assets/04_gate_amplitudes.svg) · [Numerical data](results/04_gate_amplitudes.csv)

### 05 Rotation Curve

![05 Rotation Curve](assets/05_rotation_curve.png)

Ry(0) gives zero probability of 1; Ry(pi) gives probability 1.

[SVG](assets/05_rotation_curve.svg) · [Numerical data](results/05_rotation_curve.csv)

### 06 Bloch Sphere

![06 Bloch Sphere](assets/06_bloch_sphere.png)

Qiskit plots the prepared state; its Bloch vector has unit length.

[SVG](assets/06_bloch_sphere.svg) · [Numerical data](results/06_bloch_sphere.csv)

### 07 Phase Interference

![07 Phase Interference](assets/07_phase_interference.png)

Relative phase changes the final probability; the input Z-basis probabilities remain 50/50.

[SVG](assets/07_phase_interference.svg) · [Numerical data](results/07_phase_interference.csv)

### 08 Toffoli Circuit

![08 Toffoli Circuit](assets/08_toffoli_circuit.png)

Starting from 011, CCX with controls q0 and q1 produces 111 (q2q1q0).

[SVG](assets/08_toffoli_circuit.svg)

### 09 Bell Circuit

![09 Bell Circuit](assets/09_bell_circuit.png)

Qiskit draws q0 on the top wire; H then CX prepares the Bell state.

[SVG](assets/09_bell_circuit.svg)

### 10 Entanglement Comparison

![10 Entanglement Comparison](assets/10_entanglement_comparison.png)

For these two preparations, X-basis results reveal Bell coherence that Z-basis counts alone cannot establish.

[SVG](assets/10_entanglement_comparison.svg) · [Numerical data](results/10_entanglement_comparison.csv)

### 11 Ghz Histogram

![11 Ghz Histogram](assets/11_ghz_histogram.png)

The ideal GHZ circuit produces only 000 and 111; finite counts fluctuate.

[SVG](assets/11_ghz_histogram.svg) · [Numerical data](results/11_ghz_histogram.csv)

### 12 Deutsch Results

![12 Deutsch Results](assets/12_deutsch_results.png)

Both constant functions give q0=0; both balanced functions give q0=1 with certainty in the ideal circuit.

[SVG](assets/12_deutsch_results.svg) · [Numerical data](results/12_deutsch_results.csv)

### 13 Deutsch Circuit

![13 Deutsch Circuit](assets/13_deutsch_circuit.png)

The identity oracle is CX(q0,q1); the auxiliary q1 begins in |->.

[SVG](assets/13_deutsch_circuit.svg)

### 14 Grover Results

![14 Grover Results](assets/14_grover_results.png)

One iteration concentrates probability on 10; two return to a uniform distribution in this four-item example.

[SVG](assets/14_grover_results.svg) · [Numerical data](results/14_grover_results.csv)

### 15 Grover Circuit

![15 Grover Circuit](assets/15_grover_circuit.png)

The left block marks 10; the right block amplifies it through interference.

[SVG](assets/15_grover_circuit.svg)

### 16 Teleportation Results

![16 Teleportation Results](assets/16_teleportation_results.png)

All four corrected branches have fidelity 1; their sampled frequencies are near 0.25.

[SVG](assets/16_teleportation_results.svg) · [Numerical data](results/16_teleportation_results.csv)

### 17 Teleportation Circuit

![17 Teleportation Circuit](assets/17_teleportation_circuit.png)

Qiskit if_test blocks execute X conditioned on c1, then Z conditioned on c0.

[SVG](assets/17_teleportation_circuit.svg)

### 18 Noise And Purity

![18 Noise And Purity](assets/18_noise_and_purity.png)

Mixing is strongest at p=0.5. A certain flip at p=1 returns to a pure state.

[SVG](assets/18_noise_and_purity.svg) · [Numerical data](results/18_noise_and_purity.csv)

### 19 Noise Histogram

![19 Noise Histogram](assets/19_noise_histogram.png)

Sampled frequencies approach 0.8 for 0 and 0.2 for 1; they are not exact probabilities.

[SVG](assets/19_noise_histogram.svg) · [Numerical data](results/19_noise_histogram.csv)

### 20 Coherence Comparison

![20 Coherence Comparison](assets/20_coherence_comparison.png)

H maps |+> to |0>, while the maximally mixed state remains 50/50.

[SVG](assets/20_coherence_comparison.svg) · [Numerical data](results/20_coherence_comparison.csv)

### 21 Transpiled Circuit

![21 Transpiled Circuit](assets/21_transpiled_circuit.png)

The compiled circuit implements the same Bell preparation with the selected gate basis.

[SVG](assets/21_transpiled_circuit.svg)

## Complete printed outputs

These values are extracted from the executed notebook. Graphs and circuit diagrams appear above and inside the notebook.

<details>
<summary>Cell 1: 0. Installing the tested Qiskit stack</summary>

```text
Qiskit, Aer, and circuit-drawing dependencies are ready.
```

</details>

<details>
<summary>Cell 2: 1. Preparing a small learning workspace</summary>

```text
Environment: {'python': '3.12.14', 'qiskit': '2.6.1', 'qiskit_aer': '0.18.2', 'numpy': '2.5.4', 'matplotlib': '3.11.2', 'pylatexenc': '2.10'}
Ready: Qiskit circuits, simulator, plotting helpers, and checks.
```

</details>

<details>
<summary>Cell 3: 2. Meeting qubits and the Born rule</summary>

```text
Zero: amplitudes=[1.+0.j 0.+0.j], probabilities=[1. 0.]
One: amplitudes=[0.+0.j 1.+0.j], probabilities=[0. 1.]
Equal superposition: amplitudes=[0.707+0.j 0.707+0.j], probabilities=[0.5 0.5]
Biased state: amplitudes=[0.866+0.j 0.5  +0.j], probabilities=[0.75 0.25]
```

</details>

<details>
<summary>Cell 4: 3. Sampling and measuring twice</summary>

```text
Hadamard counts: {'0': 515, '1': 509}
Repeated measurements, c1c0: {'00': 526, '11': 498}
After reset: {'0': 1024}
```

</details>

<details>
<summary>Cell 5: 4. Applying X, Y, Z, H, S, and T</summary>

```text
ID on |+>: [0.707+0.j 0.707+0.j]
X on |+>: [0.707+0.j 0.707+0.j]
Y on |+>: [0.-0.707j 0.+0.707j]
Z on |+>: [ 0.707+0.j -0.707+0.j]
H on |+>: [1.+0.j 0.+0.j]
S on |+>: [0.707+0.j    0.   +0.707j]
T on |+>: [0.707+0.j  0.5  +0.5j]
X then H: [ 0.707+0.j -0.707+0.j]
H then X: [0.707+0.j 0.707+0.j]
```

</details>

<details>
<summary>Cell 6: 5. Rotating and binding a circuit parameter</summary>

```text
Bloch coordinates (X,Y,Z): [0.612 0.612 0.5  ]
```

</details>

<details>
<summary>Cell 7: 6. Revealing phase through interference</summary>

```text
HH|0> probabilities: [1. 0.]
HZH|0> probabilities: [0. 1.]
Global phase leaves the physical state unchanged.
```

</details>

<details>
<summary>Cell 8: 7. Reading bit order and controlled gates</summary>

```text
X on q0 gives: {np.str_('01'): np.float64(1.0)}
CNOT: 00 -> 00
CNOT: 01 -> 11
CNOT: 10 -> 10
CNOT: 11 -> 01
SWAP result: {np.str_('10'): np.float64(1.0)}
Toffoli result: {np.str_('111'): np.float64(1.0)}
```

</details>

<details>
<summary>Cell 9: 8. Creating a Bell pair and a GHZ state</summary>

```text
Bell counts: {'00': 515, '11': 509}
Reduced state of q0:
 [[0.5+0.j 0. +0.j]
 [0. +0.j 0.5+0.j]]
Reduced-state purity: 0.4999999999999998
GHZ counts: {'000': 515, '111': 509}
```

</details>

<details>
<summary>Cell 10: 9. Solving Deutsch’s problem with circuit oracles</summary>

```text
constant zero : q0 probabilities = [1. 0.]
constant one : q0 probabilities = [1. 0.]
identity : q0 probabilities = [0. 1.]
opposite : q0 probabilities = [0. 1.]
```

</details>

<details>
<summary>Cell 11: 10. Searching four labels with Grover’s algorithm</summary>

```text
0 iterations: [0.25 0.25 0.25 0.25]
1 iterations: [0. 0. 1. 0.]
2 iterations: [0.25 0.25 0.25 0.25]
Grover target 10 counts: {'10': 1024}
```

</details>

<details>
<summary>Cell 12: 11. Teleporting with actual measurements and classical control</summary>

```text
complex input: c1c0=00, count=239, fidelity=1.000000
complex input: c1c0=01, count=254, fidelity=1.000000
complex input: c1c0=10, count=278, fidelity=1.000000
complex input: c1c0=11, count=253, fidelity=1.000000
All six input states passed all four branch-fidelity checks.
```

</details>

<details>
<summary>Cell 13: 12. Exploring density matrices and a bit-flip channel</summary>

```text
Noisy density matrix:
 [[0.8+0.j 0. +0.j]
 [0. +0.j 0.2+0.j]]
Probabilities: [0.8 0.2]
Purity: 0.6800000000000002
Noisy counts (4096 shots): {'0': 3307, '1': 789}
Superposition after H : [1. 0.]
Mixture after H : [0.5 0.5]
```

</details>

<details>
<summary>Cell 14: 13. Compiling a circuit without changing its meaning</summary>

```text
Original operations: {'h': 1, 'cx': 1} depth: 2
Compiled operations: {'rz': 2, 'sx': 1, 'cx': 1} depth: 4
```

</details>

<details>
<summary>Cell 15: 14. Trying six small exercises</summary>

```text
1. Probabilities: [0.2 0.8]
2. Inverse rotation returns |0>.
3. X-basis probabilities: [0. 1.] [1. 0.]
4. The outcomes are 01 and 10.
5. Every marked target is measured with certainty after one iteration.
6. X, Y, Z expectations: [0. 1. 0.]
```

</details>

<details>
<summary>Cell 16: 15. Saving your results</summary>

```text
Passed 303 checks; created 21 figures.
Author: Swayam Shakya
Quantum framework: Qiskit + Qiskit Aer
Created qiskit_generated_results.zip
```

</details>

## Interpreting the results honestly

Seeds fix the included samples for the recorded environment. Counts can vary with versions, seeds, and simulator settings; exact statevector probabilities and tolerance-based identities are the core checks. Tiny floating-point values are expected. A total of 303 assertions includes repeated normalization checks during parameter sweeps, not 303 different algorithms.

The teleportation protocol genuinely performs mid-circuit measurements and classically conditioned corrections in Aer. Its saved density matrices are simulator diagnostics unavailable from single hardware shots. The six tested inputs include basis states, real superpositions, an imaginary-phase superposition, and a generic complex state. Each observed classical branch has fidelity 1 within floating-point tolerance.

Deutsch and Grover use explicitly constructed toy oracles. Their educational query-model advantages do not mean these small classical simulations outperform classical computing. Entanglement does not enable faster-than-light signaling, and teleportation does not clone an unknown state.

## Troubleshooting

- **Different Qiskit version already imported:** start a fresh Colab runtime, then Run all from the installation cell.
- **Missing package or circuit-drawing error:** confirm the installation cell finished, including `pylatexenc`.
- **NameError:** run earlier cells; the lesson is designed to run in order.
- **AssertionError after editing:** check whether the new circuit still has the expected result.
- **Colab disconnects:** reconnect and rerun; download important generated files before ending the session.
- **Unexpected bit string:** read labels right to left for increasing qubit indices; q0 is rightmost.
- **README pictures missing:** preserve the `assets/` paths and filenames when uploading to GitHub.
- **Installation network failure:** the package registry must be reachable; package installation cannot be guaranteed offline.

## Primary references

- [Qiskit bit ordering](https://quantum.cloud.ibm.com/docs/en/guides/bit-ordering)
- [StatevectorSampler API](https://quantum.cloud.ibm.com/docs/en/api/qiskit/qiskit.primitives.StatevectorSampler)
- [Qiskit package releases](https://pypi.org/project/qiskit/)
- [Aer simulator tutorial](https://qiskit.github.io/qiskit-aer/tutorials/1_aersimulator.html)
- [Aer noise-model tutorial](https://qiskit.github.io/qiskit-aer/tutorials/3_building_noise_models.html)
- [Aer conditional density-matrix saving](https://qiskit.github.io/qiskit-aer/stubs/qiskit_aer.library.save_density_matrix.html)
- [IBM Quantum Learning](https://quantum.cloud.ibm.com/learning)
- [Google Colab FAQ](https://research.google.com/colaboratory/faq.html)

## Author

**Swayam Shakya**

No repository license has been selected on the author's behalf. Choose one before inviting redistribution or external contributions.
