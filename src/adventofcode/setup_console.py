from rich import console, theme, traceback

traceback.install()

CUSTOM_THEME = theme.Theme(
    {
        "success": "bold bright_green",
        "error": "bold bright_red",
        "info": "bold steel_blue",
    }
)

console = console.Console(theme=CUSTOM_THEME)


def log_success(message):
    success_message = f":heavy_check_mark: {message} "
    console.log(success_message, style="success")


def log_info(message):
    info_message = f":information: {message}"
    console.log(info_message, style="info")


def log_error(message):
    error_message = f":cross_mark::exclamation_mark: {message}"
    console.log(error_message, style="error")
