from src.control.simulator_controller import SimulatorController

def run():
    width = 600
    height = 600
    cells_x = 40
    cells_y = 40

    controller = SimulatorController(width, height, cells_x, cells_y)
    controller.run()

if __name__ == '__main__':
    run()