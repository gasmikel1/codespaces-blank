def fan(temperature):

        print("temperature:x")
        x = input()
        print("Temperature is: ", x)
        while True:
                if temperature > 80:
                    print("Fan is running at high speed")
                elif temperature > 70:
                    print("Fan is running at medium speed")
                elif temperature > 60:
                    print("Fan is running at low speed")
                else:
                    print("Fan is off")
                break
fan(50)
#note to self use break!



