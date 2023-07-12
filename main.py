from Gate_io_add_to_wl import *
from config import *
import web3

if __name__ == "__main__":
    print('''

''')


    with open("address.txt") as file:
        addr = list(map(web3.Web3.to_checksum_address, [i.strip() for i in file]))

    ################### // Генерация переменных \\ ####################
    notes = generate(note(len(addr)))                                 #
    count = generate(addr)                                            #
    chains = generate_chain_curr_type(chain, len(addr))               #
    curr_types = generate_chain_curr_type(curr_type, len(addr))       #
    # ############################################################### #

    cookies = add_wl()

    for repeat in range(len(count)):
        sess(cookies, count, notes, chains, curr_types, repeat)