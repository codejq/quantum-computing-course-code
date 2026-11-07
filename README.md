<p align="center">
  <img src="assets/logo.png" alt="Sommerfeld International University logo" width="320">
</p>

<h1 align="center">Quantum Computing Course: Code</h1>

<p align="center">
  Code for <b>Quantum Computing Made Simple</b>, the <b>Sommerfeld International University</b> course on YouTube.<br>
  <a href="https://www.youtube.com/playlist?list=PLHDG68xKse88">▶ Watch the full playlist on YouTube</a> · <a href="https://s-i-u.com">s-i-u.com</a>
</p>

---

## About

This repository holds the code shown in the course videos. Each lesson has its own folder, so you can open the code for the video you are watching and run it yourself.

## Lessons

| # | Lesson | Folder | What you build |
|---|--------|--------|----------------|
| 05 | [Your First Quantum Program: True Random Numbers](https://www.youtube.com/watch?v=3bVYE50kack&list=PLHDG68xKse88) | [lesson-05](lesson-05/) | A quantum random number generator on IBM Quantum (Qiskit) and Origin Quantum (pyqpanda3), plus von Neumann debiasing |

More lessons will be added as new videos come out.

## Getting started

You need Python 3.9 to 3.13.

```bash
git clone <this-repo-url>
cd quantum-computing-course-code/lesson-05

python -m venv .venv
# Windows:      .venv\Scripts\activate
# macOS/Linux:  source .venv/bin/activate

pip install -r requirements.txt
```

## Lesson 05: True Random Numbers

A qubit in the state (|0⟩ + |1⟩)/√2, made by a Hadamard gate, gives 0 or 1 at random when you measure it. Eight of these qubits give one random number from 0 to 255.

| File | Description |
|------|-------------|
| [qrng_ibm.py](lesson-05/qrng_ibm.py) | QRNG with Qiskit. Runs on the local Aer simulator by default. Set `USE_REAL_QPU = True` to run on a real IBM quantum computer. |
| [qrng_origin.py](lesson-05/qrng_origin.py) | QRNG with pyqpanda3. Runs on the local simulator by default. Set `USE_CLOUD = True` to run on Origin Quantum's cloud (`origin_wukong` chip or `full_amplitude` simulator). |
| [debias.py](lesson-05/debias.py) | von Neumann debiasing. Turns biased but independent bits from real hardware into fair bits. |

```bash
python qrng_ibm.py
python qrng_origin.py
python debias.py
```

### Using real quantum hardware

**IBM Quantum.** Create a free account at [quantum.cloud.ibm.com](https://quantum.cloud.ibm.com), copy your API key, and save it once:

```python
from qiskit_ibm_runtime import QiskitRuntimeService
QiskitRuntimeService.save_account(channel="ibm_quantum_platform",
                                  token="YOUR_IBM_API_KEY", set_as_default=True)
```

**Origin Quantum.** Get your API key from [qcloud.originqc.com.cn](https://qcloud.originqc.com.cn) and put it in an environment variable:

```bash
# Windows (PowerShell)
$env:ORIGIN_API_KEY = "your-key"
# macOS/Linux
export ORIGIN_API_KEY="your-key"
```

> Do not commit API keys to this repository.

## Contributing

Found a bug or a broken example? Please open an issue or a pull request.

---

<p align="center">
  <b>Sommerfeld International University</b> · <i>Scientia · Innovatio · Humanitas</i><br>
  Made by Quantum Billing · <a href="https://s-i-u.com">s-i-u.com</a>
</p>
