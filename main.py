from src.control.simulator_controller import SimulatorController
import yaml
import csv

def run():
    width = 900
    height = 600
    cells_x = 90
    cells_y = 60

    # Config
    with open("./config/entities.yaml", "r") as f:
        entities = yaml.safe_load(f)
    
    # convertir la lista a diccionario usando 'id' como llave
    entities_list = entities["basic-entities"]
    entities_dict = {entity["id"]: entity for entity in entities_list}
    
    map_conf = []
    with open("./config/maps/city-01.csv", newline="") as f:
        reader = csv.reader(f)
        for fila in reader:
            numbers = [int(x) for x in fila]  # convertir a enteros
            map_conf.append(numbers)

    transposed_map = list(map(list, zip(*map_conf)))

    controller = SimulatorController(width, height, cells_x, cells_y, entities_dict, transposed_map)
    controller.run()

if __name__ == '__main__':
    run()