from collections import defaultdict
import itertools            


from typing import Union, List, Any
class Obj:
    def __init__(self, location, value):
        self.location = location
        self.value = value

nodes_dict = {}
node_num = 0
def AND_2IP(i1, i2):
    if i1 == 1:
        i3 = i2
    elif i1 == 0:
        i3 = 0
    elif i1 == 'D':
        if i2 == 0:
            i3 = 0
        elif i2 == 'x':
            i3 = 'x'
        elif i2 == 'Dbar':
            i3 = 0
        else:i3 = 'D'
    elif i1 == 'Dbar':
        if i2 == 0:
            i3 = 0
        elif i2 == 'x':
            i3 = 'x'
        elif i2 == 'D':
            i3 = 0
        else:i3 = 'Dbar'
    elif i2 == 0:
        i3 = 0
    else:
        if i2 == 0:
            i3 = 0
        else:
            i3 = 'x'
    return i3

def NAND_2IP(i1, i2):

    tmp = AND_2IP(i1, i2)
    if tmp == 'x':
        i3 = 'x'
    elif tmp == 'D':
        i3 = 'Dbar'
    elif tmp == 'Dbar':
        i3 = 'D'
    else: i3 = int(not (int(tmp)))
    return i3

def OR_2IP(i1, i2):
    if i1 == 0:
        i3 = i2
    elif i1 == 1:
        i3 = 1
    elif i1 == 'D':
        if i2 == 1:
            i3 = 1
        elif i2 == 'x':
            i3 = 'x'
        elif i2 == 'Dbar':
            i3 = 1
        else:
            i3 = 'D'
    elif i1 == 'Dbar':
        if i2 == 1:
            i3 = 1
        elif i2 == 'x':
            i3 = 'x'
        elif i2 == 'D':
            i3 = 1
        else:
            i3 = 'Dbar'
    elif i2 == 1:
        i3 = 1
    else:
        if i2 == 1:
            i3 = 1
        else:
            i3 = 'x'
    return i3

def NOR_2IP(i1, i2):
    tmp = OR_2IP(i1, i2)
    if tmp == 'x':
        i3 = 'x'
    elif tmp == 'D':
        i3 = 'Dbar'
    elif tmp == 'Dbar':
        i3 = 'D'
    else:
        i3 = int(not (int(tmp)))
    return i3

def BUFFER(i1) :
    return i1

def INV(i1):
    if i1 == 'x':
        i2 = 'x'
    elif i1 == 0:
        print("inp to inv is 0")
        i2 = 1
    elif i1 == 1:
        i2 = 0
    elif i1 == 'D':
        i2 = 'Dbar'
    elif i1 == 'Dbar':
        i2 = 'D'
    else:print("inp to inv is ELSE")

    return i2

def AND_3IP(i1, i2, i3):
    tmp = AND_2IP(i1, i2)
    i4 = AND_2IP(tmp,i3)
    return i4

def OR_3IP(i1, i2, i3):
    tmp = OR_2IP(i1, i2)
    i4 = OR_2IP(tmp,i3)
    return i4

def NAND_3IP(i1,i2,i3):
    return int(not(int(AND_3IP(i1, i2, i3))))

def NOR_3IP(i1,i2,i3):
    return int(not(int(OR_3IP(i1, i2, i3))))



def initialization():
    global input_vector
    input_vector = []
    global primary_input_pins
    primary_input_pins = []
    global primary_output_pins
    primary_output_pins = []
    global output_vector
    output_vector = []
    global logic_values
    logic_values = []
    global nodes_dict
    nodes_dict = {}

    f1 = open('inputvector.txt', 'r')
    while (1):
        node_num = 0
        input_file = f1.readline()
        line = input_file.strip()
        input_vector = line.split()
        if not input_vector:
            break
        
        f2 = open('Netlist.txt', 'r')
        num_gates = 0
        num_outputs = 0
        for data in f2:
            data = data.strip()  # to remove leading and trailing white spaces
            node_data = data.split()  # to seperate words in each data string
            
            if node_data[0] == 'INPUT':
                i = 0
                
                primary_input_pins = node_data[1:-1]
                print("Primary input pins are:",primary_input_pins)
                

                if (len(primary_input_pins) != len(input_vector)):
                    print("Input vector length does not match!")
                    exit()
                
                else:
                    while (1):
                        node_num = node_data[1 + i]
                        nodes_dict[node_num] = {}
                        nodes_dict[node_num]['Gate Type'] = "INPUT"
                        nodes_dict[node_num]['num_inp'] = -1
                        nodes_dict[node_num]['num_out'] = -1
                        nodes_dict[node_num]['inputs'] = ""
                        nodes_dict[node_num]['outputs'] = ""
                        nodes_dict[node_num]['level'] = 0
                        
                        if(node_num == FL):
                            if(FV == '0'):
                                nodes_dict[node_num]['value'] = 'D'
                            elif(FV == '1'):
                                nodes_dict[node_num]['value'] = 'Dbar'
                        else: nodes_dict[node_num]['value'] = 'x'
                        nodes_dict[node_num]['done'] = 1
                        
                        i = i + 1
                        if (i >= len(primary_input_pins)):
                            break

            
            elif node_data[0] == 'OUTPUT':
                
                num_outputs = num_outputs + 1
                i = 1
                while (node_data[i] != '-1'):
                    primary_output_pins.append(node_data[i])
                    node_num = node_data[i]
                    nodes_dict[node_num]['value'] = 'x'
                    i += 1
                print("These are primary output pins:", primary_output_pins)

                


            
            else:
                
                num_gates = num_gates + 1
                
                k = 0
                while (k < num_gates):
                    node_num = node_data[-1]
                    nodes_dict[node_num] = {}
                    nodes_dict[node_num]['Gate Type'] = node_data[0]
                    nodes_dict[node_num]['num_inp'] = len(node_data[1:-1])
                    nodes_dict[node_num]['num_out'] = 1
                    nodes_dict[node_num]['inputs'] = [node_data[1], node_data[2]]
                    nodes_dict[node_num]['outputs'] = [node_data[-1]]
                    if nodes_dict[node_num]['num_inp'] == 1:
                        nodes_dict[node_num]['level'] = 1 + int(nodes_dict[nodes_dict[node_num]['inputs'][0]]['level'])
                    else:
                        nodes_dict[node_num]['level'] = 1 + max(
                            int(nodes_dict[nodes_dict[node_num]['inputs'][0]]['level']),
                            int(nodes_dict[nodes_dict[node_num]['inputs'][1]]['level']))
                    # print("For",nodes_dict[node_num]['Gate Type'],nodes_dict[node_num]['level'],"is the max level")
                    nodes_dict[node_num]['value'] = 'x'
                    nodes_dict[node_num]['done'] = 0
                    k = k + 1

        print("Dictionary after reading netlist:", nodes_dict)
        

        f2.close()
    f1.close()

def simulate(FL,FV):
        nets_done = []
        nets_done.clear()
        print("After clear nets_done-->", nets_done)
        print("Inside simulate-->",FL, FV)
        tmp = int(not(int(FV)))
        FV = tmp
        file = open("Netlist.txt",'r')
        no_of_lines = 0
        output_nodes = []
        data = file.read()
        line = data.split("\n")

        for i in line:
            if i:
                no_of_lines += 1
        num_outputs = len(primary_output_pins)
        x = len(primary_output_pins) + no_of_lines + len(input_vector) - 2
        
        ############################################## Simulation ######################################################

        logic_values = [0] * x

        f3 = open('Netlist.txt', 'r')
        
        nets_done = list(primary_input_pins)
        print("PI-->", primary_input_pins)
        print("Nets done:",nets_done)
        i = 1
        for i in nets_done:
            print("PI values:", i,":",nodes_dict[i]['value'])


        for gates in f3:
            gates = gates.strip()
            gates_data = gates.split()
            net_indices = []
            net_indices_str = []

            if (gates_data[0] == 'INPUT' or gates_data[0] == 'OUTPUT'):
                pass
            else:
                net_indices_str = gates_data[1:]
                net_indices = list(map(int, net_indices_str))

            if gates_data[0] == 'INV':
                if (gates_data[1] in nets_done):
                    print("inp of inv--", nodes_dict[str(gates_data[1])]['value'])
                    nodes_dict[str(gates_data[2])]['value'] = INV((nodes_dict[str(gates_data[1])]['value']))
                    if gates_data[2] == FL:
                        if (nodes_dict[str(gates_data[2])]['value'] == 0) and (FV == 0):
                            nodes_dict[str(gates_data[2])]['value'] = 'Dbar'
                        elif (nodes_dict[str(gates_data[2])]['value'] == 1) and (FV == 1):
                            nodes_dict[str(gates_data[2])]['value'] = 'D'
                        else: print("Obj not satisfied")

                    nodes_dict[str(gates_data[2])]['done'] = '1'
                    nets_done.append(gates_data[2])
            

            if gates_data[0] == 'AND':
                 if (gates_data[1] in nets_done) and (gates_data[2] in nets_done):
                     nodes_dict[str(gates_data[3])]['value'] = AND_2IP(nodes_dict[str(gates_data[1])]['value'],nodes_dict[str(gates_data[2])]['value'])
                     if gates_data[3] == FL:
                         if (nodes_dict[str(gates_data[3])]['value'] == 0) and (FV == 0):
                             print("Obj satisfied")
                             nodes_dict[str(gates_data[3])]['value'] = 'Dbar'
                         elif (nodes_dict[str(gates_data[3])]['value'] == 1) and (FV == 1):
                             print("Obj satisfied")
                             nodes_dict[str(gates_data[3])]['value'] = 'D'
                         else: print("Obj not satisfied")
                     nodes_dict[str(gates_data[3])]['done'] = '1'
                     nets_done.append(gates_data[3])
                 

            if gates_data[0] == 'NAND':
                nodes_dict[str(gates_data[3])]['value'] = NAND_2IP(nodes_dict[str(gates_data[1])]['value'],nodes_dict[str(gates_data[2])]['value'])
                if gates_data[3] == FL:
                    print("NAND gate o/p is faulty", nodes_dict[str(gates_data[3])]['value'], FV)
                    if ((nodes_dict[str(gates_data[3])]['value'] == 0) and (FV == 0)):
                        print("Obj satisfied")
                        nodes_dict[str(gates_data[3])]['value'] = 'Dbar'
                    elif (nodes_dict[str(gates_data[3])]['value'] == 1) and (FV == 1):
                        print("Obj satisfied")
                        nodes_dict[str(gates_data[3])]['value'] = 'D'
                    else:
                        pass
                nodes_dict[str(gates_data[3])]['done'] = '1'
                nets_done.append(gates_data[3])
                

            if gates_data[0] == 'OR':
                nodes_dict[str(gates_data[3])]['value'] = OR_2IP(nodes_dict[str(gates_data[1])]['value'],
                                                                  nodes_dict[str(gates_data[2])]['value'])
                if gates_data[3] == FL:
                    if (nodes_dict[str(gates_data[3])]['value'] == 0) and (FV == 0):
                        print("Obj satisfied")
                        nodes_dict[str(gates_data[3])]['value'] = 'Dbar'
                    elif (nodes_dict[str(gates_data[3])]['value'] == 1) and (FV == 1):
                        print("Obj satisfied")
                        nodes_dict[str(gates_data[3])]['value'] = 'D'
                    else:
                        print("Obj not satisfied")
                nodes_dict[str(gates_data[3])]['done'] = '1'
                nets_done.append(gates_data[3])
                

            if gates_data[0] == 'NOR':
                if (gates_data[1] in nets_done) and (gates_data[2] in nets_done):
                    nodes_dict[str(gates_data[3])]['value'] = NOR_2IP(nodes_dict[str(gates_data[1])]['value'],
                                                                      nodes_dict[str(gates_data[2])]['value'])
                    if gates_data[3] == FL:
                        if (nodes_dict[str(gates_data[3])]['value'] == 0) and (FV == 0):
                            print("Obj satisfied")
                            nodes_dict[str(gates_data[3])]['value'] = 'Dbar'
                        elif (nodes_dict[str(gates_data[3])]['value'] == 1) and (FV == 1):
                            print("Obj satisfied")
                            nodes_dict[str(gates_data[3])]['value'] = 'D'
                        else:
                            print("Obj not satisfied")
                    
                    nodes_dict[str(gates_data[3])]['done'] = '1'
                    nets_done.append(gates_data[3])
                    

        nets_done_sorted = []
        
        nets_done_sorted = [int(i) for i in nets_done]
        nets_done_sorted.sort()
        

        j = 0
        
        print("Final logic values:", end=" ")
        for j in nets_done:
            print(j, ":", nodes_dict[j]['value'], "    ", end=" ")
        print(" ")

        i = 0
        
        while( i < num_outputs):
            
            output_nodes.append(nodes_dict[primary_output_pins[i]]['value'])
            i += 1
        
        if ('D' in output_nodes) or ('Dbar' in output_nodes):
            fault_tested = 1
        else: fault_tested = 0
        
        return fault_tested


################################################# Objective Function ###################################################
def objective(FL,FV,L,V):
    global D_frontier
    D_frontier = []
    if L == FL:
        tmp = int(not(int(FV)))
        loc = FL
    else:

        fx = open('Netlist.txt', 'r')
        for data in fx:
            data = data.strip()  # to remove leading and trailing white spaces
            node_data = data.split()

            if (node_data[0] != "INPUT") and (node_data[0] != "OUTPUT"):
                inp_nets = node_data[1:-1]  # stores input nets of this particular gate
                out_nets = node_data[-1]

                if nodes_dict[out_nets]['value'] == 'x':
                    for nets in inp_nets:
                        if (nodes_dict[nets]['value'] == 'D') or (nodes_dict[nets]['value'] == 'Dbar'):
                            D_frontier.append(node_data[-1])
        print("D-Frontier is:",D_frontier)
        
        if not D_frontier:
            
            print("No DF")
        else:
            
            for gates in D_frontier:
                inputs = []
                outputs = []
                gate_type = nodes_dict[gates]['Gate Type']
                inputs = nodes_dict[gates]['inputs']
                outputs = nodes_dict[gates]['outputs']

                for i in inputs:
                    
                    if (nodes_dict[i]['value'] == 'x'):
                        
                        loc = i
                        if (gate_type == 'AND') or (gate_type == 'NAND'):
                            
                            tmp = 1
                        if (gate_type == 'OR') or (gate_type == 'NOR'):
                            
                            tmp = 0
                    else:
                        print("value already set")
    print("Objective set:",loc,"->",tmp)

    
    return loc,tmp

############################################### Backtrace Function #####################################################
def backtrace(L, V):
    TV = []
    
    inputs = []
    inv_cnt = 0
    inputs = nodes_dict[L]['inputs']
    gate = nodes_dict[L]['Gate Type']
    
    i = 0
    
    if gate == 'AND':
        if V == 0:
            min_ip_to_set = 1
        else: min_ip_to_set = 2
    elif gate == 'NAND':
        
        inv_cnt += 1
        if V == 0:
            min_ip_to_set = 2
        
        else: min_ip_to_set = 1
    elif gate == 'OR':
        if V == 0:
            min_ip_to_set = 2
        else: min_ip_to_set = 1
    elif gate == 'NOR':
        inv_cnt += 1
        if V == 0:
            min_ip_to_set = 1
        else: min_ip_to_set = 2
    elif gate == 'INV':
        inv_cnt += 1
        min_ip_to_set = 1

    i = 0
    
    while(i < min_ip_to_set):
        
        if inputs[i] in primary_input_pins:
            
            if inv_cnt%2 == 0:
                nodes_dict[inputs[i]]['value'] = V
                TV.append(inputs[i])
                TV.append(int(V))
            else:
                nodes_dict[inputs[i]]['value'] = not(V)
                TV.append(inputs[i])
                TV.append(int(not(V)))
        else:
            
            Obj2 = Obj(-1, -1)
            if inv_cnt%2 == 0:
                Obj2.location, Obj2.value = objective(L, V, inputs[i], V)
            else:
                print(inputs[i])
                Obj2.location, Obj2.value = objective(L,V,inputs[i],not(V))
        
        i += 1
        #print("updated i:",i)
    stack.append(TV)
    print("TV:", TV)
    print("stack:", stack)
    

if __name__ == '__main__':
    global FL
    global FV
    FL = input("Enter Fault location:")
    FV = input("Enter 1 for SA1 fault and 0 for SA0 fault :")
    initialization()
    global stack
    stack = []

    fault_tested = 0
    L = FL
    V = FV
    Obj1 = Obj(-1, -1)
    flag = 0
    i = 0


    while(flag == 0):
        Obj1.location, Obj1.value = objective(FL, FV, L, V)
        L = Obj1.location
        V = Obj1.value
        if (L not in primary_input_pins):
            backtrace(L, V)
        elif (L != FL):
            nodes_dict[L]['value'] = V
        fault_tested = simulate(FL, FV)
        for i in primary_output_pins:
            if 'D' in nodes_dict[i].values():
                print("Do_exist")
                flag = 1
            elif ('Dbar' in nodes_dict[i].values()):
                print("Do_exist")
                flag = 1
            else:
                flag = 0
        L = 0

  





