
class MainPageSelectors:

    # header selectors
    button_logo = {
        "data-testid": "",
        "selector": ".min-w-\\[162px\\].lg\\:min-w-\\[172px\\].h-\\[48px\\]",
        "description": "Кнопка logo"
    }

    button_favorite = {
        "data-testid": "button-favorite",
        "selector": "",
        "description": "Кнопка favorite"

    }

    button_enter = {
        "data-testid": "button",
        "selector": "#id_button",
        "role": "button",
        "description": "Кнопка 'Войти'",
        "text": "Войти"
    }

    login_email_field = {
        "selector": "#email_input",
        "data-testid": "logo",
        "role": "textbox",
        "description": "Поле ввода email",
        "placeholder": "Введите email",
        "type": "email",
        "required": True
    }

    login_password_field = {
        "selector": "#password_input",
        "role": "textbox",
        "description": "Поле ввода пароля",
        "placeholder": "Введите пароль",
        "type": "password",
        "required": True
    }
