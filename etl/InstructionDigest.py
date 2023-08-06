class InstructionDigest:
    def __init__(self,
                 step_number,
                 instruction):
        self.step_number = step_number
        self.instruction = instruction

    def __str__(self):
        text = "InstructionDigest: step_number={}, instruction='{}'"
        return text.format(self.step_number, self.instruction)
