class LogicGate:

    def __init__(self, label):
        self.label = label
        self.output = None

    def get_label(self):
        return self.label

    def get_output(self):
        self.output = self.perform_gate_logic()
        return self.output

class UnaryGate(LogicGate):

    def __init__(self, label):
        LogicGate.__init__(self, label)
        self.pin = None

    def get_pin(self):
        if self.pin == None:
            self.pin = int(input(f"Enter pin input for gate {self.label}: "))
            return self.pin
        else:
            return self.pin.get_from_gate().get_output()

    def set_next_pin(self, source):
        if self.pin == None:
            self.pin = source
        else:
            raise RuntimeError("NO EMPTY PIN")

class BinaryGate(LogicGate):

    def __init__(self, label):
        LogicGate.__init__(self, label)
        self.pin_a = None
        self.pin_b = None

    def get_pin_a(self):
        if self.pin_a == None:
            self.pin_a = int(input(f"Enter pin A input for gate {self.label}: "))
            return self.pin_a
        else:
            return self.pin_a.get_from_gate().get_output()

    def get_pin_b(self):
        if self.pin_b == None:
            self.pin_b = int(input(f"Enter pin B input for gate {self.label}: "))
            return self.pin_b
        else:
            return self.pin_b.get_from_gate().get_output()

    def set_next_pin(self, source):
        if self.pin_a == None:
            self.pin_a = source
        elif self.pin_b == None:
            self.pin_b = source
        else:
            raise RuntimeError("NO EMPTY PIN")

class AndGate(BinaryGate):

    def perform_gate_logic(self):
        a = self.get_pin_a()
        b = self.get_pin_b()
        if a == b == 1:
            return 1
        else:
            return 0

class NandGate(BinaryGate):

    def perform_gate_logic(self):
        a = self.get_pin_a()
        b = self.get_pin_b()
        if a == b == 1:
            return 0
        else:
            return 1

class OrGate(BinaryGate):

    def perform_gate_logic(self):
        a = self.get_pin_a()
        b = self.get_pin_b()
        if a == 1 or b == 1:
            return 1
        else:
            return 0

class NorGate(BinaryGate):

    def perform_gate_logic(self):
        a = self.get_pin_a()
        b = self.get_pin_b()
        if a == 1 or b == 1:
            return 0
        else:
            return 1

class XorGate(BinaryGate):

    def perform_gate_logic(self):
        a = self.get_pin_a()
        b = self.get_pin_b()
        if a == b:
            return 0
        else:
            return 1

class NotGate(UnaryGate):

    def perform_gate_logic(self):
        pin = self.get_pin()
        if pin == 1:
            return 0
        else:
            return 1

class Connector:

    def __init__(self, fgate, tgate):
        self.from_gate = fgate
        self.to_gate = tgate

        tgate.set_next_pin(self)

    def get_from_gate(self):
        return self.from_gate

    def get_to_gate(self):
        return self.to_gate

def main():
    g1 = AndGate("G1")
    g2 = AndGate("G2")
    g3 = OrGate("G3")
    g4 = NotGate("G4")
    c1 = Connector(g1, g3)
    c2 = Connector(g2, g3)
    c3 = Connector(g3, g4)
    print(g4.get_output())

def half_adder():
    g1 = AndGate("G1")
    g2 = XorGate("G2")


main()
