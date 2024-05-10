
from fuelingSystem import FuelingSystem
from component import Component
from plasma import Plasma
from breedingBlanket import BreedingBlanket
from componentMap import ComponentMap
from matplotlib import pyplot as plt
from simulate import Simulate
from tools.utils import visualize_connections

LAMBDA = 1.73e-9 # Decay constant for tritium
N_burn = 9.3e-7 # Tritium burn rate in the plasma
TBR = 1.1
tau_ofc = 2 * 3600
tau_ifc = 5 * 3600
I_startup = 2
TBE = 0.02
final_time = 2.1 * 3600 * 24 * 365 # NB: longer than doubling time

q = 0.25
t_res = 24 * 3600
I_reserve = N_burn / TBE * q * t_res


# Define components
fueling_system = FuelingSystem("Fueling System", N_burn, TBE, initial_inventory=I_startup)
BB = BreedingBlanket("BB", tau_ofc, initial_inventory=0, N_burn = N_burn, TBR = TBR)
plasma = Plasma("Plasma", N_burn, TBE, initial_inventory=0)
IFC = Component("IFC", tau_ifc)


# Define ports
port1 = fueling_system.add_output_port("Fueling to Plasma")
port2 = plasma.add_input_port("Port 2")
port3 = plasma.add_output_port("Plasma to IFC")
port4 = IFC.add_input_port("Port 4")
port5 = IFC.add_output_port("IFC to Fueling System")
port6 = BB.add_output_port("OFC to Fueling System")
port7 = fueling_system.add_input_port("Port 7")
port8 = fueling_system.add_input_port("Port 8")

# Add components to component map
component_map = ComponentMap()
component_map.add_component(fueling_system)
component_map.add_component(BB)
component_map.add_component(plasma)
component_map.add_component(IFC)

# Connect ports
component_map.connect_ports(fueling_system, port1, plasma, port2)
component_map.connect_ports(plasma, port3, IFC, port4)
component_map.connect_ports(IFC, port5, fueling_system, port7)
component_map.connect_ports(BB, port6, fueling_system, port8)

component_map.print_connected_map()
visualize_connections(component_map)
print(f'Startup inventory is: {fueling_system.tritium_inventory}')
simulation = Simulate(dt=0.1, final_time=final_time, I_reserve=I_reserve, component_map=component_map)
t, y = simulation.run()
plt.figure()
plt.plot(t, y)
plt.legend(component_map.components.keys())
print(f"Component inventories {y[-1]}")