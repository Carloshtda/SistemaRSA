import input_treatment
class User:
    ''' Representação dos Usuários do Sistema'''
    def __init__(self):
        self.__username = None
        self.__password = None
        self.__name = None
        self.__keys = None

    # Métodos de comparação
    def compare_username(self, compared):
        if compared == self.__username:
            return True
        return False

    def compare_password(self, compared):
        if compared == self.__password:
            return True
        return False

    # Métodos get's e set's necessários
    def get_username(self):
        return self.__username

    def get_name(self):
        return self.__name

    def get_keys(self):
        return self.__keys

    def set_keys(self, keys):
        self.__keys = keys

    # Métodos que atribui valores aos atributos de User de acordo com a entrada do usuário
    def set_user(self, atual_users):
        control = input_treatment.InputTreatment()
        print("Enter your NAME:")
        name = control.message_input()
        while True:
            try:
                print("Enter your USERNAMER:")
                username = control.message_input()
                for i in range(len(atual_users)):
                    if atual_users[i].compare_username(username) is True:
                        raise RuntimeError
                break
            except RuntimeError:
                print('Username already exist.')
        print("Enter your PASSWORD:")
        password = control.message_input()
        self.__username = username
        self.__name = name
        self.__password = password

    # Métodos que atribui valores diretos aos atributos de User
    def set_file_user(self, name, username, password):
        self.__username = username
        self.__password = password
        self.__name = name

    # Métodos que retornam os atributos de User encriptados
    def get_encrypted_password(self, system_rsa):
        return system_rsa.encrypt(self.__password)

    def get_encrypted_username(self, system_rsa):
        return system_rsa.encrypt(self.__username)

    def get_encrypted_name(self, system_rsa):
        return system_rsa.encrypt(self.__name)
#Função responsável pelo Login
def logIn(username, password, users_list):
    for i in range(len(users_list)):
        if users_list[i].compare_username(username) is True and users_list[i].compare_password(password) is True:
            return users_list[i]
    return None
#Função que deleta um usuário pelo username
def deleteUser(username, users_list):
    for i in range(len(users_list)):
        if users_list[i].compare_username(username) is True:
            users_list.pop(i)
            return users_list
    return users_list
#Função que mostra todos os usuários cadastradso no momento
def displayUsers(users_list):
    size = len(users_list)
    if size == 0:
        print('No users registered')
    for i in range(size):
        if i == 0:
            print('Users registered:')
        print(users_list[i].get_name())
