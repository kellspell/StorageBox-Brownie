from brownie import accounts, config, StorageBox

def read_contract():
    storage_box = StorageBox[-1]
    print(storage_box.retrieve())

def main():
    read_contract()