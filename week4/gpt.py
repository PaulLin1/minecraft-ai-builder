import os
from openai import OpenAI
from dotenv import load_dotenv, find_dotenv

class GPT:
    def __init__(self):
        self.template = """
            You are an expert in building highly detailed structures in Minecraft using Python. 
            Your job is to generate accurate and well-structured code for building Minecraft structures. 
            The structures should include features such as doors, windows, roofs, and interiors where applicable.
            You have access to a place_block function that looks like this:
            def place_block(bot, block_type, x, y, z, place_on='bottom').
            The bot's position is stored in bot.entity.position.
            Ensure that the buildings are complete and structurally sound.
            Avoid using variables that are not declared in the provided code. Provide just the Python code.
            Respond in executable python code. Not latex
            import any packages you use
        """

        self.messages=[
            {"role": "system", "content": self.template},
            {"role": "user", "content": "build a dirt house"},
            {"role": "assistant", "content": "pos = self.bot.entity.position\nstartX = position.x\nstartY = position.y\nstartZ = position.z\nwidth = 7\ndepth = 7\nheight = 4\n\n# Build the walls\nfor x in range(startX, startX + width):\n    for y in range(startY, startY + height):\n        for z in range(startZ, startZ + depth):\n            if x == startX or x == startX + width - 1 or y == startY or y == startY + height - 1 or z == startZ or z == startZ + depth - 1:\n                place_block(self.bot, 'oak_planks', x, y, z)"},
            {"role": "user", "content": "build a giant cow"},
            {"role": "assistant", "content": "pos = self.bot.entity.position\n\nfor x in range(8):\n    for y in range(7):\n        for z in range(14):\n            blockType = \"white_wool\" if (y != 2 or z % 2 == 0) else \"black_wool\"\n            place_block(self.bot, blockType, pos.x + x, pos.y + y, pos.z + z)\n\nlegs = [(1, 1), (1, 12), (6, 1), (6, 12)]\nfor leg_x, leg_z in legs:\n    for y in range(4):\n        for dx in range(2):\n            for dz in range(2):\n                place_block(self.bot, \"black_wool\", pos.x + leg_x + dx, pos.y + y, pos.z + leg_z + dz)\n\nfor x in range(2, 7):\n    for y in range(4, 8):\n        for z in range(14, 19):\n            blockType = \"white_wool\" if not (y == 5 and (x == 3 or x == 5)) else \"black_wool\"\n            place_block(self.bot, blockType, pos.x + x, pos.y + y, pos.z + z)\n\nplace_block(self.bot, \"black_wool\", pos.x + 3, pos.y + 6, pos.z + 18)\nplace_block(self.bot, \"black_wool\", pos.x + 5, pos.y + 6, pos.z + 18)\n\nplace_block(self.bot, \"black_wool\", pos.x + 1, pos.y + 7, pos.z + 16)\nplace_block(self.bot, \"black_wool\", pos.x + 2, pos.y + 7, pos.z + 16)\nplace_block(self.bot, \"black_wool\", pos.x + 6, pos.y + 7, pos.z + 16)\nplace_block(self.bot, \"black_wool\", pos.x + 7, pos.y + 7, pos.z + 16)\n\nplace_block(self.bot, \"black_wool\", pos.x + 3, pos.y + 4, pos.z + 19)\nplace_block(self.bot, \"black_wool\", pos.x + 4, pos.y + 4, pos.z + 19)\nplace_block(self.bot, \"black_wool\", pos.x + 5, pos.y + 4, pos.z + 19)\n\nfor y in range(3, 5):\n    place_block(self.bot, \"black_wool\", pos.x + 4, pos.y + y, pos.z - 2)\nplace_block(self.bot, \"black_wool\", pos.x + 4, pos.y + 4, pos.z - 3)\n"}
        ]
        
        _ = load_dotenv(find_dotenv())
        self.client = OpenAI(
            api_key=os.environ.get('OPEN_AI_KEY')
        )

    def send_to_llm(self, message):
        messages = self.messages
        messages.append({"role": "user", "content": message})

        completion = self.client.chat.completions.create(
            model="gpt-4o-mini",
            messages=messages
        )

        return completion.choices[0].message.content
