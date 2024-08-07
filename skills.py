import minecraft_data
from math import floor

mc_data = minecraft_data("1.13") 

def is_block_type_known(block_type):
    """
    Checks if the block exists
    :param block_type: Nane of the block
    :return: True if exists, False otherwise
    """
    return block_type.lower() in mc_data.blocks

# code snippet from mindcraft
def place_block(bot, block_type, x, y, z, place_on='bottom'):
    """
    Places a block in minecraft
    :param bot: The bot that will place the block
    :param block_type: Name of the block
    :param x: X-coordinate of the block
    :param y: Y-coordinate of the block
    :param z: Z-coordinate of the block
    :param place_on:
    :return: True if block is placed, False otherwise
    """
    msg = f'/setblock {floor(x)} {floor(y)} {floor(z)} {block_type}'
    bot.chat(msg)
    return True
    # if is_block_type_known(block_type):
    #     print(f"Invalid block type: ${block_type}.")
    #     return False
    
    # # Precompute target coordinates
    # fx, fy, fz = floor(x), floor(y), floor(z)
    # target_dest = (fx, fy, fz)

    # # Invert the facing direction
    # face = {
    #     'north': 'south',
    #     'south': 'north',
    #     'east': 'west',
    #     'west': 'east'
    # }.get(place_on, '')

    # # Modify block_type based on conditions
    # if 'torch' in block_type and place_on != 'bottom':
    #     block_type = block_type.replace('torch', 'wall_torch')
    #     if place_on not in ['side', 'top']:
    #         block_type += f'[facing={face}]'

    # elif 'button' in block_type or block_type == 'lever':
    #     block_type += f'[face={"ceiling" if place_on == "top" else "floor" if place_on == "bottom" else f"facing={face}"}]'

    # elif block_type in ['ladder', 'repeater', 'comparator']:
    #     block_type += f'[facing={face}]'

    # # Send the main command to set the block
    # bot.chat(f'/setblock {fx} {fy} {fz} {block_type}')

    # # Handle special cases with additional commands
    # if 'door' in block_type:
    #     bot.chat(f'/setblock {fx} {fy + 1} {fz} {block_type}[half=upper]')
    # elif 'bed' in block_type:
    #     bot.chat(f'/setblock {fx} {fy} {fz - 1} {block_type}[part=head]')

    # print(bot, f'Used /setblock to place {block_type} at {target_dest}.')

    # return True