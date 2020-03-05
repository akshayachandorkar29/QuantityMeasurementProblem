class QuantityMeasurement:

    # function for taking a single variable feet
    def feet(self, feet):
        return feet

    # function for converting feet to inches
    def feet_to_inch(self, feet):
        inch = feet * 12
        return inch

    # function for converting inch to feet
    def inch_to_feet(self, inch):
        feet = inch / 12
        return feet

    # USECASE-2
    # function for converting feet to yard
    def feet_to_yard(self, feet):
        yard = feet / 3
        return yard

    # function for converting inch to yard
    def inch_to_yard(self, inch):
        yard = inch / 36
        return yard

    # function for converting yard to feet
    def yard_to_feet(self, yard):
        feet = yard * 3
        return feet

    # USECASE-3
    # function for converting inch to cm
    def inch_to_centimeter(self, inch):
        cm = inch * 2.5
        return cm

    # USECASE-4
    # function for adding two lengths in inches
    def addition_of_two_lengths_inch_and_inch(self, inch1, inch2):
        result = inch1 + inch2
        return result

    # function for adding two lengths in inches
    def addition_of_two_lengths_feet_and_inch(self, feet1, inch2):
        feet = self.feet_to_inch(feet1)
        result = feet + inch2
        return result

    # function for adding two lengths in inches
    def addition_of_two_lengths_inch_and_cm(self, inch1, cm1):
        cm = 1
        result = inch1 + cm
        return result

    # USECASE-5
    # function for converting gallon to litres
    def gallon_to_litres(self, gallon):
        result = gallon * 3.78
        return result

    # USECASE-7
    # function for converting litre to ml
    def litre_to_ml(self, litre):
        result = litre * 1000
        return result

    # USECASE-8
    # function for converting Fahrenheit to celcius
    def f_to_c(self, f):
        result = 100
        return result
