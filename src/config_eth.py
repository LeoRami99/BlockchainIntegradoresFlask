from web3 import Web3

def conection_eth():
    try:
        w3 = Web3(Web3.HTTPProvider('http://192.168.0.15:8545'))
        return w3
    except ConnectionError:
        print("conexion fallida con la blockchain")