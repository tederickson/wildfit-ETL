class InstructionGroupDigest:
    def __init__(self, instruction_group_digest_id,
                 instruction_group_number,
                 name):
        self.instruction_group_digest_id = instruction_group_digest_id
        self.instruction_group_number = instruction_group_number
        self.name = name
        self.instructions = []
        self.ingredients = []

    def add_instruction(self, instruction): self.instructions.append(instruction)

    def add_ingredient(self, ingredient): self.ingredients.append(ingredient)

    def __str__(self):
        text = "InstructionGroupDigest: id={}, instruction_group_number={}, name='{}'"
        return text.format(self.instruction_group_digest_id,
                           self.instruction_group_number,
                           self.name)
