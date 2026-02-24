import os

users = []

loggedAs = False

def clearCMD():
  os.system('cls' if os.name == 'nt' else 'clear')

def getUsers():
  global loggedAs

  if not loggedAs:
    print('❌ Você precista estar logado par realizar essa ação.')
    return False

  if (not users):
    clearCMD()
    print('❌ Não há usuários cadastrados.')
  else:
    for user in users:
      print('================================')
      print(f'Usuário: {user["username"]}')
      print(f'Senha: {user["password"]}')
      print(f'Email: {user["email"]}')
      print('================================')

def existingUser(username):
  for user in users:
    if user['username'] == username:
      return True
  return False

def logout():
  global loggedAs
  loggedAs = False
  clearCMD()
  print('✅ Logout realizado com sucesso.')

def registerUser ():
  username = input('Digite o nome de usúario: ') 
  password = input('Digite uma senha: ') 
  email = input('Digite um email: ')

  if existingUser(username):
    print("❌ Já existe um usuário com esse login cadastrado.")
    return

  user = {
    'username': username,
    'password': password,
    'email': email 
  }

  users.append(user)
  clearCMD()
  print('✅ Usuário cadastrado com sucesso.')

def loginUser():
  global loggedAs
  username = input('Digite o nome de usúario: ') 
  password = input('Digite uma senha: ') 
  
  for user in users:
      if user['username'] == username: 
          if user['password'] == password:
              clearCMD()
              print('✅ Login efetuado com sucesso.')
              loggedAs = True
              return True
          else:
              print('❌ Senha incorreta.')
              return False
          
  print('❌ Usuário não encontrado.')
  return False
  
def removeUser():
  global loggedAs

  if not loggedAs:
    print('❌ Você precista estar logado par realizar essa ação.')
    return False
  
  username = input('Digite o nome de usúario que deseja remover: ') 

  for i, user in enumerate(users):
    if user['username'] == username:
      users.pop(i)
      print('✅ Usuário removido com sucesso.')
      return
  print('❌ Usuário não encontrado.')
  
def menu():
  
  print('================================')
  print('1. Cadastrar')
  print('2. Listar Usuários')
  print('3. Login')
  print('4. Remover Usuários')
  print('5. Sair')
  print('================================')
  try:
    option = int(input('Escolha uma opção do menu acima: '))
  except ValueError:
    clearCMD()
    print('⚠️ Digite um número.')
    return
  clearCMD()

  if option == 1:
    registerUser()
    return
  elif option == 2:
    getUsers()
    return
  elif option == 3:
    loginUser()
    return
  elif option == 4:
    removeUser()
    return
  elif option == 5:
    logout()
    clearCMD()
    print('✅ Você saiu do sistema com sucesso.')
    return 'sair'
  else:
    print('⚠️ Selecione uma opção válida.')

while True:
  choice = menu()
  if choice == 'sair':
    break