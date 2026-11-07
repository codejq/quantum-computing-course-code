# Quantum Random Number Generator with pyqpanda3 (Origin Quantum, China)
# Sommerfeld International Academy · made by Quantum Billing · s-i-u.com
#
# pip install pyqpanda3        (Python 3.9 to 3.13)
# Get your API key from your account page at https://qcloud.originqc.com.cn

import os, time
from pyqpanda3 import core
from pyqpanda3.qcloud import QCloudService, QCloudOptions, DataBase, JobStatus

USE_CLOUD = False      # False = simulator on your laptop, True = Origin Quantum cloud
BACKEND = "origin_wukong"   # real 72-qubit chip; use "full_amplitude" for the cloud simulator
N_QUBITS = 8
SHOTS = 1000

# 1. Build the program: H on every qubit, then measure every qubit
prog = core.QProg()
for q in range(N_QUBITS):
    prog.append(core.H(q))
prog.append(core.measure(list(range(N_QUBITS)), list(range(N_QUBITS))))

# 2. Run it
if not USE_CLOUD:
    qvm = core.CPUQVM()
    qvm.run(prog, SHOTS)
    counts = qvm.result().get_counts()
else:
    service = QCloudService(os.environ["ORIGIN_API_KEY"])
    backend = service.backend(BACKEND)
    if BACKEND == "full_amplitude":
        job = backend.run(prog, SHOTS)
    else:
        options = QCloudOptions()
        options.set_mapping(True)        # place our qubits on the chip
        options.set_optimization(True)   # simplify the circuit
        options.set_amend(False)         # keep the raw measurement results
        job = backend.run(prog, SHOTS, options)
    while job.status() not in (JobStatus.FINISHED, JobStatus.FAILED):
        time.sleep(5)
    counts = job.result().get_counts(base=DataBase.Binary)

# 3. Each measured bitstring is one random number from 0 to 255
print("Different outcomes seen:", len(counts))
for bits, n in list(counts.items())[:10]:
    print(bits, "->", int(bits, 2), "seen", n, "times")
