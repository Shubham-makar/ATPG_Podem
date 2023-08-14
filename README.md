# ATPG_Podem
ATPG (Automatic Test Pattern Generation) is a critical component in the field of digital integrated circuit testing. Its primary objective is to automatically generate a set of test patterns that can effectively detect and diagnose faults or defects within digital circuits. These faults could arise from manufacturing defects, design errors, or environmental factors.
PODEM Algorithm:

Initialization:
Identify a target fault in the circuit. This is the specific fault that needs to be detected by the generated test pattern.
Initialize a backtrace tree, which is a data structure used to keep track of decision points and backtrack when necessary.

Objective:
The main objective of PODEM is to find a test pattern that will activate the target fault and propagate its effect to at least one observable primary output.

Path Sensitization:
Begin by selecting an undetected fault and determining which primary outputs are affected by it.
Use a process called path sensitization to identify the primary inputs that need to be set in order to activate the fault effect and propagate it through the circuit.

Backtrace:
If path sensitization fails to provide a solution, backtrack to previous decision points in the backtrace tree.
Modify inputs at these decision points to explore different possibilities and continue the search for a valid test pattern.

Decision Making:
At each decision point, choose a primary input value that maximizes the chances of reaching the desired fault effect.
If a decision results in a contradiction (inconsistency in the circuit behavior), backtrack to the previous decision point.

Termination:
Continue the process of path sensitization, decision making, and backtracking until either a valid test pattern is found or it is determined that no solution exists.

Multiple Test Patterns:
In some cases, PODEM might generate multiple test patterns to cover different sensitizable paths to the fault.
