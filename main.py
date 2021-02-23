import networkx as nx
import csv
from program_relationships import relationships as edges
import terminal_colors
import program

all_programs = {}

with open('programs.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            line_count += 1
        else:
            id = int(row[0])
            p = program.Program(id, row)
            all_programs[id] = p  #key = id, value = program obj
            line_count += 1

graph = nx.DiGraph()
graph.add_edges_from(edges)

print('Passes DAG check: ')
passes_dag_check = nx.is_directed_acyclic_graph(graph)
if passes_dag_check:
    print(f'{terminal_colors.colors.OK}{str(passes_dag_check)}{terminal_colors.colors.ENDC}')
    print('\n')
else:
    print(f'{terminal_colors.colors.FAIL}{str(passes_dag_check)}{terminal_colors.colors.ENDC}')
    exit()

# current state to desired destination
print('Shortest path: ')
print(nx.shortest_path(graph, 0, 5))
print('\n')

print('Topological sort: ')
print(list(nx.topological_sort(graph)))
print('\n')

print('Programs sorted by name: ')
sorted = sorted(all_programs, key=lambda id: all_programs[id].program_company)
for id in sorted:
    p = all_programs[id]
    print(f'\tProgram {p.id} with name {p.program_company} was added on {p.date_added}')
print('\n')

id_to_retrieve = 6
retrieved_program = all_programs[id_to_retrieve]
print('Info about a particular program: ')
print(f'\tProgram {retrieved_program.id} with name {retrieved_program.program_company} was added on {retrieved_program.date_added}')
print('\n')
