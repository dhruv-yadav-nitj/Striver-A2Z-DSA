# https://medium.com/@neeraj_swe/low-level-design-of-an-elevator-system-e7fc018f356e

class Elevator:
    def __init__(self, id, total_floors) -> None:
        self.id = id
        self.total_floors = total_floors
        self.curr_floor = 0

    def move_down(self):
        if self.curr_floor > 0:
            self.curr_floor -= 1

    def move_up(self):
        if self.curr_floor < self.total_floors:
            self.curr_floor += 1

    def open_doors(self):
        print(f"Elevator {self.id} is opening doors!")

    def close_doors(self):
        print(f"Elevator {self.id} is closing doors!")


class Request:
    def __init__(self, floor) -> None:
        self.floor = floor


class Controller:
    def __init__(self) -> None:
        self.elevators = [Elevator(i, 10) for i in range(3)]

    def handle_request(self, request: Request):
        for elevator in self.elevators:
            if elevator.curr_floor == request.floor:
                elevator.open_doors()
                elevator.close_doors()
                return
            elif elevator.curr_floor < request.floor:
                while elevator.curr_floor != request.floor:
                    elevator.move_up()
                elevator.open_doors()
                elevator.close_doors()
                return
            else:
                while elevator.curr_floor != request.floor:
                    elevator.move_down()
                elevator.open_doors()
                elevator.close_doors()
                return


def main():
    controller = Controller()
    while True:
        floor_req = int(input())
        if 0 <= floor_req <= 10:
            controller.handle_request(Request(floor_req))


if __name__ == "__main__":
    main()
