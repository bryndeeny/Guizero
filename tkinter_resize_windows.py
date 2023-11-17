# cant resize a window
booking_window = Window(app, title="Settings.",bg = "white", height="760", width="1100")
booking_window.tk.resizable(False, False)

# changes text properties of text
country_title = Text(box4, text = "Choose a country.", color="#2596be")
country_title.tk.config(font=("Ariel", 16, "bold"))
