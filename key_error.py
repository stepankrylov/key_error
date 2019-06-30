documents = [
        {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
        {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
        {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"},
        
]
directories = {
        '1': ['2207 876234', '11-2'],
        '2': ['10006'],
        '3': []
} 

def people():
  document_number = str(input('Введите номер документа: № '))
  for document_card in documents:
    if document_number == document_card.get("number"):
      print(document_card.get("name"))
      break
  else:
    print('Документ не найден')    

def list_doc():
  list_document = []
  for document_card in documents:
    list_document += [[document_card.get("type"), document_card.get("number"), document_card.get("name")], ]
  print(list_document)  

def shelf_doc():
  document_number = str(input('Введите номер документа: № '))
  for shelf in directories:
    if document_number in directories.get(shelf):
      print('Полка № ', shelf)

def add_doc():
  type_add_doc = str(input('Введите тип документа: '))
  num_add_doc = str(input('Введите номер документа: № '))
  name_add_doc = str(input('Введите имя владельца документа: '))
  n = str(input('Введите номер полки: № '))
  for shelf in directories:
    if shelf == n:
      directories.get(shelf).append(num_add_doc)
      new_document_card = {"type": type_add_doc, "number": num_add_doc, "name": name_add_doc}
      documents.append(new_document_card)
      break
  else:
    print(f'Полки с № {n} не существует. Выберете из существующих или используйте команду "as" для создания новой полки')  
  print(directories)
  print(documents)

def delete_doc():
  num_del_doc = str(input('Введите номер удаляемого документа: № '))
  for document_card in documents:
    if num_del_doc == document_card.get("number"):
      documents.remove(document_card)
  print(documents)
  for shelf in directories:
    if num_del_doc in directories.get(shelf):
      directories.get(shelf).remove(num_del_doc)
  print(directories)

def move_doc():
  num_move_doc = str(input('Введите номер перемещаемого документа: № '))
  n = str(input('Введите номер целевой полки: № '))
  for shelf in directories:
    if n in directories.keys():
      if num_move_doc in directories.get(shelf):
        directories.get(shelf).remove(num_move_doc)
        directories.get(n).append(num_move_doc)
        break 
  else:
    print('Ошибка! Неправильно заполнен(ы) номер(а) документа и/или полки')   
  print(directories)

def add_shelf():
  add_sh = str(input('Введите номер новой полки: № ')) 
  if add_sh in directories.keys():
    print(f'Полка с № {add_sh} существует. Выберите другой номер для новой полки.')
  else:
    directories[add_sh] = []
  print(directories)

def command():
  comand = input('Выберите команду из предложенного списка:\n p - получить имя владельца документа по номеру документа;\n l - получить список всех документов;\n s - получить номер полки по номеру документа;\n a - добавить новый документ;\n d - удалить документ;\n m - переместить документ на другую полку;\n as - добавить полку.\n Ваша команда: ')
  if comand == 'p':
    people()
  elif comand == 'l':
    list_doc()
  elif comand == 's':
    shelf_doc()
  elif comand == 'a':
    add_doc()
  elif comand == 'd':
    delete_doc()
  elif comand == 'm':
    move_doc()
  elif comand == 'as':
    add_shelf()
  else:
    print("Ошибка ввода")

Hello = input('Приветствую, чтобы воспользоваться прложением нажмите "y",\nчтобы выйти нажмите любую другу клавишу: ')
if Hello == 'y':
  command()
else:
  print('До свидания!')