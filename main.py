import input_treatment
import user
import rsa
import file_treatment

control = input_treatment.InputTreatment()

file_control = file_treatment.fileTreatment()
file_control.read_file('bd.txt')

system_rsa = rsa.Rsa()


users = []
actual_user = None
print('Welcome to the RSA Encrypt/Decrypt system.')
print('Input:')
print('         1. for a system with saved settings.')
print('         0. for a brand new system.')
control.limited_int_input(0, 1)
if control.input == 1:
    system_rsa.file_setup(file_control)
    for i in range(len(file_control.users)):
        saved_user = user.User()
        user_name = system_rsa.decrypt(file_control.users[i][0])
        user_username = system_rsa.decrypt(file_control.users[i][1])
        user_password = system_rsa.decrypt(file_control.users[i][2])
        saved_user.set_file_user(user_name, user_username, user_password)
        users.append(saved_user)
    system_rsa.file_setup(file_control)

while True:

    print('RSA Encrypt/Decrypt System Menu:')
    print('       1. Sign in.')
    print('       2. Sign Up.')
    print('       0. Exit')
    control.limited_int_input(0,  2)
    if control.input == 1:
        print("Input your USERNAME:")
        username = input()
        print("Input our Password")
        password = input()
        actual_user = user.logIn(username, password, users)

        if actual_user is None:
            print('User not found.')
        else:
            print('Hello {}!'.format(actual_user.get_name()))
            while True:
                print('Options: ')
                print('       1.  Setup RSA keys.')
                print('       2.  Encrypt Message.')
                print('       3.  Decrypt Message.')
                print('       4.  View User List.')
                print('       5.  Delete Account.')
                print('       0.  Logoff')
                control.limited_int_input(0, 5)
                if control.input == 1:
                    public_key = system_rsa.setup()
                    actual_user.set_keys(public_key)
                    print("Public Key is: {}".format(public_key))
                elif control.input == 2:
                    if system_rsa.get_public_n() == 0:
                        print('You must SETUP the RSA first!')
                    else:
                        print("Input the message you want to encrypt:")
                        msg = control.message_input()
                        encrypted_msg = system_rsa.encrypt(msg)
                        print('The encrypted message is: {}'.format(encrypted_msg))

                elif control.input == 3:
                    print("Input the encrypted message:")
                    encrypted_msg = control.message_input()
                    msg = system_rsa.decrypt(encrypted_msg)
                    print('The decrypted message is: {}'.format(msg))
                elif control.input == 4:
                    user.displayUsers(users)
                elif control.input == 5:
                    users = user.deleteUser(actual_user.get_username(), users)
                    print('Deletion complete')
                    actual_user = None
                    break
                else:
                    actual_user = None
                    break

    elif control.input == 2:
        actual_user = user.User()
        actual_user.set_user(users)
        users.append(actual_user)
    else:
        print('Do you wish o ENCRYPT and SAVE the system settings?')
        print('Input:')
        print('        1. Yes')
        print('        0. No')
        control.limited_int_input(0, 1)
        if control.input == 1:
            file_control.write_file(system_rsa, users, 'bd.txt')
        print("Closing the program...")
        break

