class HeatController:
    def _init_(self, comfort_temp):
        self.comfort_temp = comfort_temp

    def sense(self, room_temp):
        return room_temp

    def decide(self, room_temp):
        if room_temp < self.comfort_temp:
            action = "Turn on heater"
        else:
            action = "Turn off heater"
        return action

rooms = {
    "Living Area": 18,
    "Sleeping Room": 22,
    "Cooking Space": 20,
    "Washroom": 24
}

comfort_temp = 22
controller = HeatController(comfort_temp)

for room, temp in rooms.items():
    action = controller.decide(temp)
    print(f"{room}: Current temperature = {temp}°C. {action}.")