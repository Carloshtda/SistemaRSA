class fileTreatment:
    '''Faz o tratamento da manipulação das entradas e saídas por arquivos de texto'''
    def __init__(self):
        self.file = None
        self.users = []
        self.keys = []
    #Lê o txt, e caso possua, dá valor aos atribbutos
    def read_file(self, file_name):
        try:
            self.file = open(file_name, 'r', encoding='utf8')
            content = self.file.read().splitlines()
        except OSError.filename:
            print('You must have a bd.txt file in the same folder of this program to run properly.')
            content = []
        if len(content) == 0:
            self.users = []
        else:
            self.keys = content[0].split()
            for i in range(1, len(content), 3):
                self.users.append([content[i], content[i+1], content[i+2]])
        self.file.close()

    # Salva as chaves atuais e os usuário, sendo os últimos de forma encriptda.
    def write_file(self, system_rsa, list_users, file_name):
        self.file = open(file_name, 'w')
        keys = system_rsa.keys_toString()
        self.file.write(keys)
        self.file.write('\n')
        content = []
        for i in range(len(list_users)):
            user_name = list_users[i].get_encrypted_name(system_rsa)
            self.file.write(user_name)
            self.file.write('\n')
            user_username = list_users[i].get_encrypted_username(system_rsa)
            self.file.write(user_username)
            self.file.write('\n')
            user_password = list_users[i].get_encrypted_password(system_rsa)
            self.file.write(user_password)
            self.file.write('\n')
        self.file.close()


