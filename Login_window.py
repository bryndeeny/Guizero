# login window
login_window = Window(app, title="login Page", bg = "white", height="650")
login_window.tk.resizable(False, False)
space = Text(login_window, text = "", size="5")
picture = Picture(login_window, image="logo.png", width = 120, height = 120)
space = Text(login_window, text = "", size="10")
login_title = Text(login_window, text = "PLEASE LOGIN TO YOUR BOOKER ACCOUNT")
space = Text(login_window, text = "", size="20")
login_username = Text(login_window, text = "Enter Your Username:")
space = Text(login_window, text = "", size="5")
username_box_1 = TextBox(login_window, width="23")
space = Text(login_window, text = "", size="2")
sign_up_password = Text(login_window, text = "Enter Your Password:")
space = Text(login_window, text = "", size="2")
password_box_1 = TextBox(login_window, width="23", hide_text = True)
space = Text(login_window, text = "", size="20")
submit = PushButton(login_window, text = "Submit", command=login_details, width="17")
space = Text(login_window, text = "", size="2")
forgot_password = PushButton(login_window, text = "Forgot password?", command=login_forgot_password, width="17")
space = Text(login_window, text = "", size="2")
back_button2 = PushButton(login_window, text = "Back", command=go_back_main, width="17")
login_window.hide()
