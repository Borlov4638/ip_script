import ipaddress

def exclude_address(network_str, exclude):
    network = ipaddress.ip_network(network_str, strict=False)
    addresses = list(network.subnets(new_prefix=32))

    if exclude:
        exclude_address = ipaddress.ip_network(exclude)
        try:
            addresses.remove(exclude_address)
        except ValueError:
            print(f"Подсеть {exclude} не входит в подсеть {network_str}.")
    else:
        exclude_address = ipaddress.ip_network(network_str[:-3] + '/32')
        try:
            addresses.remove(exclude_address)
        except ValueError:
            print(f"Подсеть {exclude} не входит в подсеть {network_str}.")

    
    return addresses[1:-1]

def input_data():
    network_str = input("Введите подсеть в формате x.x.x.x/prefix (например '90.154.2.226/30'): ")
    exclude = input("\nВведите адрес CE, если CE и адрес подсети представлены отьельно \n(Если CE и префикс защищаемой подсети предствалены вместе нажмите Enter): ")
    result = ''
    for subnet in exclude_address(network_str, exclude):
        result += str(subnet) + ', '

    print('\n'+result[:-2])

input_data()
