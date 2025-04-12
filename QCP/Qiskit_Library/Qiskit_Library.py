def pretty_print_real_number(x):
	eps = 0.00001
	xi = round(x)
	if abs(x - xi) <= eps:
		print(xi, end = "")
	else:
		print(x, end = "")
def pretty_print_complex_number(x):
	eps = 0.00001
	if abs(x) <= eps:
		print(0, end = "")
	elif abs(x.imag) <= eps:
		pretty_print_real_number(x.real)
	elif abs(x.real) <= eps:
		pretty_print_real_number(x.imag)
		print("i", end = "")
	else:
		pretty_print_real_number(x.real)
		print("+", end = "")
		pretty_print_real_number(x.imag)
		print("i", end = "")
def display_circuit_info(qc):
	print(f"{qc.depth() = }")
	print(qc.draw())
def print_image(qc, non_zero_only = True):
	eps = 0.00001
	from qiskit.quantum_info import Operator
	matrix = Operator(qc).data
	if non_zero_only:
		print("[", end = "")
		for i in range(2**qc.num_qubits):
			if abs(matrix[i][0]) > eps:
				pretty_print_complex_number(matrix[i][0])
				print("|" + str(i) + "⟩", end = ", ")
		print("]")
	else:
		for i in range(2**qc.num_qubits):
			pretty_print_complex_number(matrix[i][0])
			print(end = " ")
		print()
def print_matrix(qc, non_zero_only = True):
	eps = 0.00001
	from qiskit.quantum_info import Operator
	matrix = Operator(qc).data
	if non_zero_only:
		print("[", end = "")
		for i in range(2**qc.num_qubits):
			for j in range(2**qc.num_qubits):
				if abs(matrix[i][j]) > eps:
					pretty_print_complex_number(matrix[i][j])
					print("|" + str(i) + "⟩⟨" + str(j) + "|", end = ", ")
		print("]")
	else:
		for i in range(2**qc.num_qubits):
			for j in range(2**qc.num_qubits):
				pretty_print_complex_number(matrix[i][j])
				print(end = " ")
			print()
