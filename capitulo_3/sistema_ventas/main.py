import sys

clients = [
    {
        "name": "Pablo",
        "company": "google",
        "email": "pablo@google.com",
        "position": "software engineer",
    },
    {
        "name": "Ricardo",
        "company": "facebook",
        "email": "ricardo@facebook.com",
        "position": "data engineer",
    }
]


def create_client(client):
    global clients

    if client not in clients:
        clients.append(client)
    else:
        print('Client already is in the client\'s list')


def list_clients():
    global clients

    print("UID  |   Name  |   Company |   Email   |   Position")
    for  idx, client in enumerate(clients):
        print('{uid} | {name} | {company} | {email} | {position}'.format(
            uid=idx,
            name=client['name'],
            company=client['company'],
            email=client['email'],
            position=client['position']
        ))


def update_client(client_index, updated_client):
    global clients
    
    try:
        clients[int(client_index)] = updated_client 
    except :
        print("Client is not in client\'s list")


def delete_client(client_index):
    global clients
    try:
        clients.pop(int(client_index))
    except:
        print('Client is not in client\'s list') 


def search_client(client_name):
    global clients

    for client in clients:
        if client != client_name:
            continue
        else:
            return True


def _get_client_field(field_name):
    field = None

    while not field:
        field = input('What is the client {}? '.format(field_name))
        if field == 'exit':
            field = None
            break

    if not field:
        sys.exit()

    return field


def _get_client_name():
    client_name = None
    while not client_name:
        client_name = input("What is client name? ") 
        if client_name == 'exit':
            client_name = None
            break

    if not client_name:
            sys.exit()
    
    return client_name


def _print_welcome(): 
    print("Bienvenidos a Ventas")
    print("*" * 50)
    print("What would you like to do today?")
    print("[C]reate client")
    print("[L]ist clients")
    print("[U]pdate client")
    print("[D]elete client")
    print("[S]earch client")


if __name__ == '__main__':
    _print_welcome()

    command = input()
    command.upper()

    if command == "C":
        client = {
            "name": _get_client_field('name'),
            "company": _get_client_field('company'),
            "email" : _get_client_field('email'),
            "position": _get_client_field('position'),
        }
        create_client(client)
        list_clients()
    elif command == "L":
        list_clients()
    elif command == "D":
        client_name = _get_client_field('uid')
        delete_client(client_name)
        list_clients()
    elif command == "U":
        client_id = _get_client_field('uid')
        updated_client = {
            "name" : _get_client_field('name'),
            "company": _get_client_field('company'),
            "email" : _get_client_field('email'),
            "position": _get_client_field('position'),
        }
        update_client(client_id, updated_client)
        list_clients() 
    elif command == "S":
        client_name = _get_client_name()
        found = search_client(client_name)

        if found:
            print("The client is in the client\'s list")
        else:
            print('The client {} is not in our client\'s list'.format(client_name))
    else:
        print("Invalid command")