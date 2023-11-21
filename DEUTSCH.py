import numpy as np
from qiskit import QuantumCircuit, transpile
from qiskit import Aer
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt

# Use Aer's qasm_simulator
simulator_1 = Aer.get_backend('qasm_simulator')
# Create a Quantum Circuit acting on the q register
circuit_1 = QuantumCircuit(2, 2)
# circuit.x(1) [01]
# circuit.x(0) [10]
# ->
# circuit.x(0). circuit.x [11]
circuit_1.barrier(0, 1)
# (0,1) -> (1,0)
circuit_1.x(0)
circuit_1.cx(0, 1)
circuit_1.x(0)
circuit_1.barrier(0, 1)
# Map the quantum measurement to the classical bits
circuit_1.measure([0, 1], [1, 0])
# compile the circuit down to low-level QASM instructions
# supported by the backend (not needed for simple circuits)
compiled_circuit_1 = transpile(circuit_1, simulator_1)
# Execute the circuit on the qasm simulator
job_1 = simulator_1.run(compiled_circuit_1, shots=1000)
# Grab results from the job
result_1 = job_1.result()
# Returns counts
counts_1 = result_1.get_counts(circuit_1)
print("\nTotal count for 00 and 11 are:", counts_1)
# Draw the circuit
print(circuit_1)
# Plot a histogram
plot_histogram(counts_1)
plt.show()

# Use Aer's qasm_simulator
simulator_2 = Aer.get_backend('qasm_simulator')
# Create a Quantum Circuit acting on the q register
circuit_2 = QuantumCircuit(2, 2)
# circuit.x(1) [01]
# circuit.x(0) [10]
# ->
# circuit.x(0) circuit.x [11]
circuit_2.barrier(0, 1)
# (0,1) -> (1,0)
circuit_2.i(0)
circuit_2.i(1)
# circuit.x(0)
circuit_2.barrier(0, 1)
# Map the quantum measurement to the classical bits
circuit_2.measure([1, 0], [0, 1])
# compile the circuit down to low-level QASM instructions
# supported by the backend (not needed for simple circuits)
compiled_circuit_2 = transpile(circuit_2, simulator_2)
# Execute the circuit on the qasm simulator
job_2 = simulator_2.run(compiled_circuit_2, shots=1000)
# Grab results from the job
result_2 = job_2.result()
# Returns counts
counts_2 = result_2.get_counts(circuit_2)
print("\nTotal count for 00 and 11 are:", counts_2)
# Draw the circuit
print(circuit_2)
# Plot a histogram
plot_histogram(counts_2)
plt.show()

# Use Aer's qasm_simulator
simulator_3 = Aer.get_backend('qasm_simulator')
# Create a Quantum Circuit acting on the q register
circuit_3 = QuantumCircuit(2, 2)
# circuit.x(1) [01]
# circuit.x(0) [10]
# ->
# circuit.x(0) circuit.x [11]
circuit_3.barrier(0, 1)
# (0,1) -> (0,|)
circuit_3.cx(0, 1)
# circuit.i(1)
# circuit.x(0)
circuit_3.barrier(0, 1)
# Map the quantum measurement to the classical bits
circuit_3.measure([1, 0], [0, 1])
# compile the circuit down to low-level QASM instructions
# supported by the backend (not needed for simple circuits)
compiled_circuit_3 = transpile(circuit_3, simulator_3)
# Execute the circuit on the qasm simulator
job_3 = simulator_3.run(compiled_circuit_3, shots=1000)
# Grab results from the job
result_3 = job_3.result()
# Returns counts
counts_3 = result_3.get_counts(circuit_3)
print("\nTotal count for 00 and 11 are:", counts_3)
# Draw the circuit
print(circuit_3)
# Plot a histogram
plot_histogram(counts_3)
plt.show()

# Use Aer's qasm_simulator
simulator_4 = Aer.get_backend('qasm_simulator')
# Create a Quantum Circuit acting on the q register
circuit_4 = QuantumCircuit(2, 2)
# circuit.x(1) [01]
# circuit.x(0) [10]
# ->
# circuit.x(0) circuit.x [11]
circuit_4.barrier(0, 1)
# (0,1) -> (1,1)
circuit_4.x(1)
circuit_4.barrier(0, 1)
# Map the quantum measurement to the classical bits
circuit_4.measure([1, 0], [0, 1])
# compile the circuit down to low-level QASM instructions
# supported by the backen
