from dataclasses import dataclass


@dataclass
class InstructionDigest:
    step_number: int
    instruction: str

    def to_json_dictionary(self):
        json = {
            "stepNumber": self.step_number,
            "instruction": self.instruction
        }

        return json
