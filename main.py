import PySimpleGUI as sg

sg.theme('SystemDefaultForReal')   # Задаём системные цвета для приложения

# Все элементы приложения
layout = [
    [  # Слой 1 - в нём только Текст "Welcome to my app!"
        sg.Text( # Элемент текста
            'Welcome to my app!',
            font=('TT firs neue', 30)
        )
    ],
    [  # Слой 2 - в нём 2 элемента: текст и инпут
        sg.Text('Enter your name: '),   # Элемент текст
        sg.InputText()                  # Элемент инпута
    ],
    [  # Слой 3 - в нём 2 кнопки: Ok и Cancel
        sg.Button('Ok'),    # Кнопка Ok
        sg.Button('Cancel') # Кнопка Cancel
    ]
]

# Создаём окно
window = sg.Window('Window Title', layout, size=(500, 150))
# Цикл работы приложения + обработка событий (клик, ввод текста и тд)
while True:
    event, values = window.read()

    # По нажатию кнопки "Cancel" выходим из цикла приложения
    if event == sg.WIN_CLOSED or event == 'Cancel':
        break
    elif event == 'Ok':
        sg.Popup(f'Hello, {values[0]}!')

# Закрываем окно
window.close()