# Importing compiler
from brownie import accounts, config, StorageBox, network


def deploy_Storage_Box():
    account = get_account()

    storage_box = StorageBox.deploy({"from": account})
    stored_value = storage_box.retrieve()
    print("This is the First transaction",stored_value)

    
    transaction = storage_box.store(15, {"from": account})
    transaction.wait(1)
    upadated_stored_value = storage_box.retrieve()
    print("This is the Second transaction",upadated_stored_value)
     
    # account = accounts.load("Kellspell-account")
    # print(account)
    # account = accounts.add(config["wallets"]["from_key"])

# This functions only done to able to connect wth infura
def get_account():
    if network.show_active() == "development":
        return accounts[0]
    else:
        return accounts.add(config["wallets"]["from_key"])    


def main():
    deploy_Storage_Box()
