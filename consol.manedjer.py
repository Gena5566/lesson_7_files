import os
import shutil
import platform
import random

def create_folder():
    folder_name = input("Введите название папки: ")
    try:
        os.mkdir(folder_name)
        print(f"Папка '{folder_name}' создана.")
    except FileExistsError:
        print(f"Папка '{folder_name}' уже существует.")

def delete_file_or_folder():
    file_or_folder_name = input("Введите название файла или папки для удаления: ")
    try:
        if os.path.isfile(file_or_folder_name):
            os.remove(file_or_folder_name)
            print(f"Файл '{file_or_folder_name}' удален.")
        elif os.path.isdir(file_or_folder_name):
            shutil.rmtree(file_or_folder_name)
            print(f"Папка '{file_or_folder_name}' удалена.")
    except FileNotFoundError:
        print(f"Файл или папка '{file_or_folder_name}' не найдены.")

def copy_file_or_folder():
    src = input("Введите путь к файлу или папке, которую нужно скопировать: ")
    dst = input("Введите путь к месту назначения: ")
    try:
        if os.path.isfile(src):
            shutil.copy(src, dst)
            print(f"Файл '{src}' скопирован в '{dst}'.")
        elif os.path.isdir(src):
            shutil.copytree(src, os.path.join(dst, os.path.basename(src)))
            print(f"Папка '{src}' скопирована в '{dst}'.")
    except FileNotFoundError:
        print(f"Файл или папка '{src}' не найдены.")
    except FileExistsError:
        print(f"Файл или папка '{os.path.basename(src)}' уже существуют в '{dst}'.")

def list_directory():
    files_and_folders = os.listdir()
    for item in files_and_folders:
        print(item)

def list_folders():
    files_and_folders = os.listdir()
    for item in files_and_folders:
        if os.path.isdir(item):
            print(item)

def list_files():
    files_and_folders = os.listdir()
    for item in files_and_folders:
        if os.path.isfile(item):
            print(item)

def show_os_info():
    print(f"Операционная система: {platform.system()}")
    print(f"Версия: {platform.release()}")

def show_author():
    print("Автор: Ваше имя")

def save_directory_contents():
    files_and_folders = os.listdir()
    with open("directory_contents.txt", "w") as f:
        for item in files_and_folders:
            f.write(item + "\n")
    print("Содержимое рабочей директории сохранено в файле 'directory_contents.txt'.")

while True:
    print("1. Создать папку")
    print("2. Удалить файл или папку")
    print("3. Скопировать файл или папку")
    print("4. Просмотр содержимого рабочей директории")
    print("5. Сохранить содержимое рабочей директории в файл")
    print("6. Показать информацию об операци")

    print("Автор: Ваше имя")

    choice = input('Выберите пункт меню: ')
    if choice == '1':
        create_folder()
    elif choice == '2':
        delete_file_or_folder()
    elif choice == '3':
        copy_file_or_folder
    elif choice == '4':
        list_directory()
    elif choice == '5':
        save_directory_contents()
    elif choice == '6':
        show_os_info()
        break
    else:
        print('Неверный пункт меню')
    break