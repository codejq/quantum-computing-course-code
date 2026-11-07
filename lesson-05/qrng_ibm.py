# Quantum Random Number Generator with Qiskit (IBM Quantum)
# Sommerfeld International Academy · made by Quantum Billing · s-i-u.com
#
# pip install qiskit qiskit-aer qiskit-ibm-runtime
#
# One-time setup (run once, then delete the key from your code):
#   from qiskit_ibm_runtime import QiskitRuntimeService
#   QiskitRuntimeService.save_account(channel="ibm_quantum_platform",
#                                     token="YOUR_IBM_API_KEY", set_as_default=True)

from qiskit import QuantumCircuit
from qiskit.transpiler import generate_preset_pass_manager
from qiskit_aer import AerSimulator
from qiskit_ibm_runtime import QiskitRuntimeService
from qiskit_ibm_runtime.executor_sampler import Sampler

USE_REAL_QPU = False   # False = simulator on your laptop, True = real IBM quantum computer
N_QUBITS = 8           # 8 quantum coins = one random number from 0 to 255
SHOTS = 10             # how many random numbers we want

# 1. Build the circuit: every qubit starts in |0>, H puts it in (|0> + |1>)/sqrt(2)
qc = QuantumCircuit(N_QUBITS, N_QUBITS)
qc.h(range(N_QUBITS))
qc.measure(range(N_QUBITS), range(N_QUBITS))
print(qc.draw())

# 2. Choose where to run it
if USE_REAL_QPU:
    service = QiskitRuntimeService()
    backend = service.least_busy(operational=True, simulator=False)
else:
    backend = AerSimulator()
print("Running on:", backend.name)

# 3. Translate the circuit into the gates this machine really has
pm = generate_preset_pass_manager(backend=backend, optimization_level=1)
isa_circuit = pm.run(qc)

# 4. Run it
sampler = Sampler(mode=backend)
job = sampler.run([isa_circuit], shots=SHOTS)
result = job.result()[0]

# 5. Read the bits, one bitstring per shot, in order
bitstrings = result.data.c.get_bitstrings()
numbers = [int(b, 2) for b in bitstrings]
print("Bitstrings:", bitstrings)
print("Random numbers (0-255):", numbers)
