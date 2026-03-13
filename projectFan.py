class Fan:
    
    temp_thresholds = [75, 85, 90, 95, 100]
    speeds = [0, 1, 2, 3, 4]

    def __init__(self, temp):
        self.current_temp = temp  

    def get_speed(self):
        
        if self.current_temp < self.temp_thresholds[0]:
            return self.speeds[0]
        else:
            for i in range(len(self.temp_thresholds)):
                if self.current_temp < self.temp_thresholds[i]:
                    return self.speeds[i-1]

        return self.speeds[-1]


try:
    temp_input = int(input("Enter the temperature: "))
    my_fan = Fan(temp_input)
    print("The speed of the fan is:", my_fan.get_speed())
except ValueError:
    print("Please enter a valid integer.")