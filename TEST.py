import numpy as np
from qiskit import QuantumCircuit, transpile
from qiskit import Aer
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt

def printMat(mat):
    for i in mat:
        print(" ".join(list(map(str, i))))
#F1
print("Función No 1: 0 -> 0, 1 -> 0")
print()
print("Matriz")
print()
printMat([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]])

# Prueba |00>
simulator = Aer.get_backend('qasm_simulator')
circuit = QuantumCircuit(2, 2)
circuit.barrier()
circuit.i(0)
circuit.i(1)
circuit.barrier()
circuit.measure([0, 1], [1, 0])
compiled_circuit = transpile(circuit, simulator)
job = simulator.run(compiled_circuit, shots=1000)
result = job.result()
counts = result.get_counts(circuit)
print(circuit)
plot_histogram(counts)
plt.show()
print()

# Prueba |01>
simulator = Aer.get_backend('qasm_simulator')
circuit = QuantumCircuit(2, 2)
circuit.x(1)
circuit.barrier()
circuit.i(0)
circuit.i(1)
circuit.barrier()
circuit.measure([0, 1], [1, 0])
compiled_circuit = transpile(circuit, simulator)
job = simulator.run(compiled_circuit, shots=1000)
result = job.result()
counts = result.get_counts(circuit)
print(circuit)
plot_histogram(counts)
plt.show()
print()

# Prueba |10>
simulator = Aer.get_backend('qasm_simulator')
circuit = QuantumCircuit(2, 2)
circuit.x(0)
circuit.barrier()
circuit.i(0)
circuit.i(1)
circuit.barrier()
circuit.measure([0, 1], [1, 0])
compiled_circuit = transpile(circuit, simulator)
job = simulator.run(compiled_circuit, shots=1000)
result = job.result()
counts = result.get_counts(circuit)
print(circuit)
plot_histogram(counts)
plt.show()
print()

# Prueba |11>
simulator = Aer.get_backend('qasm_simulator')
circuit = QuantumCircuit(2, 2)
circuit.x(0)
circuit.x(1)
circuit.barrier()
circuit.i(0)
circuit.i(1)
circuit.barrier()
circuit.measure([0, 1], [1, 0])
compiled_circuit = transpile(circuit, simulator)
job = simulator.run(compiled_circuit, shots=1000)
result = job.result()
counts = result.get_counts(circuit)
print(circuit)
plot_histogram(counts)
plt.show()
print()

# F2
print("Función No 2: 0 -> 0, 1 -> 1")
print()
print("Mat")
print()
printMat([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 0, 1], [0, 0, 1, 0]])

# Prueba con |00>
simulator = Aer.get_backend('qasm_simulator')
circuit = QuantumCircuit(2, 2)
circuit.cx(0, 1)
circuit.barrier()
circuit.measure([0, 1], [1, 0])
compiled_circuit = transpile(circuit, simulator)
job = simulator.run(compiled_circuit, shots=1000)
result = job.result()
counts = result.get_counts(circuit)
print(circuit)
plot_histogram(counts)
plt.show()

# Prueba con |01>
simulator = Aer.get_backend('qasm_simulator')
circuit = QuantumCircuit(2, 2)
circuit.x(1)
circuit.barrier()
circuit.cx(0, 1)
circuit.barrier()
circuit.measure([0, 1], [1, 0])
compiled_circuit = transpile(circuit, simulator)
job = simulator.run(compiled_circuit, shots=1000)
result = job.result()
counts = result.get_counts(circuit)
print(circuit)
plot_histogram(counts)
plt.show()

# Prueba con |10>
simulator = Aer.get_backend('qasm_simulator')
circuit = QuantumCircuit(2, 2)
circuit.x(0)
circuit.barrier()
circuit.cx(0, 1)
circuit.barrier()
circuit.measure([0, 1], [1, 0])
compiled_circuit = transpile(circuit, simulator)
job = simulator.run(compiled_circuit, shots=1000)
result = job.result()
counts = result.get_counts(circuit)
print(circuit)
plot_histogram(counts)
plt.show()

# Prueba con |11>
simulator = Aer.get_backend('qasm_simulator')
circuit = QuantumCircuit(2, 2)
circuit.x(0)
circuit.x(1)
circuit.barrier()
circuit.cx(0, 1)
circuit.barrier()
circuit.measure([0, 1], [1, 0])
compiled_circuit = transpile(circuit, simulator)
job = simulator.run(compiled_circuit, shots=1000)
result = job.result()
counts = result.get_counts(circuit)
print(circuit)
plot_histogram(counts)
plt.show()

# Función No 3
print("Función No 3: 0 -> 1, 1 -> 1")
print()
print("Mat")
print()
printMat([[0, 1, 0, 0], [1, 0, 0, 0], [0, 0, 0, 1], [0, 0, 1, 0]])

# Prueba |00>
simulator = Aer.get_backend('qasm_simulator')
circuit = QuantumCircuit(2, 2)
circuit.x(0)
circuit.cx(0, 1)
circuit.x(0)
circuit.barrier()
circuit.measure([0, 1], [1, 0])
compiled_circuit = transpile(circuit, simulator)
job = simulator.run(compiled_circuit, shots=1000)
result = job.result()
counts = result.get_counts(circuit)
print(circuit)
plot_histogram(counts)
plt.show()

# Prueba |01>
simulator = Aer.get_backend('qasm_simulator')
circuit = QuantumCircuit(2, 2)
circuit.x(1)
circuit.barrier()
circuit.x(0)
circuit.cx(0, 1)
circuit