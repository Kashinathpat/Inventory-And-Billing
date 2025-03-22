def check_login(user_name:str, password: str) -> str:
    if user_name.strip() == "user123" and password.strip() == "12345678":
        return ""
    return "Invalid Username or Password.\nPlease check username and password and try Again."