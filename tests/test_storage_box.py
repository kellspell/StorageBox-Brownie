from brownie import StorageBox, accounts

# in this test we're checking for the first value of our deploy script start at the [0] index
# testing in python are separeted in three categories 
# Arrange
# Act
# Assert
def test_deploy():

# Arrange
    account = accounts[0]

# Act
    storage_box = StorageBox.deploy({"from": account})
    startting_value = storage_box.retrieve()
    expected = 0

# Assert
    assert startting_value == expected

# lets nao check for our updates value 
def test_updated_storage():
    # Arrange
    account = accounts[0]
    storage_box = StorageBox.deploy({"from": account})

    # Act
    expected = 15
    storage_box.store(expected,{"from": account})

    # Assert
     assert expected == storage_box.retrieve()