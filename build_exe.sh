#!/bin/bash

# Переход в директорию скрипта
cd "$(dirname "$0")"

# проверка установки PyInstaller
check_pyinstaller() {
    if ! command -v pyinstaller &> /dev/null
    then
        echo "PyInstaller не найден. Устанавливаем PyInstaller..."
        pip install pyinstaller
        if [ $? -ne 0 ]; then
            echo "Не удалось установить PyInstaller. Проверьте подключение к интернету и повторите попытку."
            exit 1
        fi
    fi
}

# создание виртуального окружения
setup_virtualenv() {
    if [ ! -d "venv" ]; then
        echo "Создаем виртуальное окружение..."
        python -m venv venv
        if [ $? -ne 0 ]; then
            echo "Не удалось создать виртуальное окружение."
            exit 1
        fi
    fi
    source venv/Scripts/activate
    if [ -f "requirements.txt" ]; then
        echo "Устанавливаем зависимости из requirements.txt..."
        pip install -r requirements.txt
        if [ $? -ne 0 ]; then
            echo "Не удалось установить зависимости."
            exit 1
        fi
    fi
}

# Основной процесс сборки
build_exe() {
    pyinstaller --onefile --windowed main.py

    if [ $? -eq 0 ]; then
        echo ""
        echo "Исполняемый файл успешно создан в папке 'dist'."
    else
        echo ""
        echo "Произошла ошибка при создании исполняемого файла."
    fi
}

main() {
    check_pyinstaller
    setup_virtualenv
    build_exe
}

main

