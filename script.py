import ipaddress


def input_data():
    network_str = input("Введите подсеть в формате x.x.x.x/prefix (например '90.154.2.226/30'): ")
    
    network = ipaddress.ip_network(network_str, strict=False)
    addresses = list(network.subnets(new_prefix=32))

    if(network_str == str(network)):
        exclude = input("\nВведите адрес CE, если CE и адрес подсети представлены отьельно \n(Если CE и префикс защищаемой подсети предствалены вместе нажмите Enter): ")

        
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

    

    result = ''
    for subnet in addresses[1:-1]:
        result += str(subnet) + ', '

    print('\n'+result[:-2])

input_data()
