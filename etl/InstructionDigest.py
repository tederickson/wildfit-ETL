from dataclasses import dataclass


@dataclass
class InstructionDigest:
    step_number: int
    instruction: str

    def __str__(self):
        text = "InstructionDigest: step_number={}, instruction='{}'"
        return text.format(self.step_number, self.instruction)

    def to_json_dictionary(self):
        json = {
            "stepNumber": self.step_number,
            "instruction": self.instruction
        }

        return json
