class InstructionDigest:
    def __init__(self,
                 step_number,
                 instruction):
        self.instruction_digest_id = 0
        self.step_number = step_number
        self.instruction = instruction

    def __str__(self):
        text = "InstructionDigest: id={}, step_number={}, instruction='{}'"
        return text.format(self.instruction_digest_id,
                           self.step_number,
                           self.instruction)
