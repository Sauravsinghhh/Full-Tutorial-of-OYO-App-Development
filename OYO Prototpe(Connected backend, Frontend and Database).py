import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import mysql.connector
from mysql.connector import Error

root = tk.Tk()
root.title("OYO Login")
root.geometry("400x450")

background_image = Image.open("img6.jpg")
background_image = ImageTk.PhotoImage(background_image)

background_label = tk.Label(root, image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

title_logo = Image.open("img2.png.png")
title_logo = ImageTk.PhotoImage(title_logo)

root.iconphoto(False, title_logo)

login_frame = tk.Frame(root, bg="#FFF", highlightbackground="#CCC", highlightthickness=1)
login_frame.pack(pady=20, padx=20)

logo_label = tk.Label(login_frame, text="OYO", font=("Arial", 32, "bold"), fg="#FF0000")
logo_label.pack(pady=10)

welcome_label = tk.Label(login_frame, text="Welcome aboard!", font=("Arial", 16), fg="#000000")
welcome_label.pack()

offer_label = tk.Label(login_frame, text="Enjoy extra ₹100 off on your first stay!", font=("Arial", 14), fg="#000000")
offer_label.pack()

mobile_label = tk.Label(login_frame, text="Username", font=("Arial", 14), fg="#000000")
mobile_label.pack()
mobile_entry = tk.Entry(login_frame, font=("Arial", 14), width=20)
mobile_entry.insert(0, "admin121")
mobile_entry.pack(pady=5)

password_label = tk.Label(login_frame, text="Password", font=("Arial", 14), fg="#000000")
password_label.pack()
password_entry = tk.Entry(login_frame, font=("Arial", 14), width=20, show="*")
password_entry.insert(0, "1234")
password_entry.pack(pady=5)

def create_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="Saurav121@__",
        database="OYO"
    )

def search_hotels(identifier):
    conn = create_connection()
    if conn:
        try:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM Hotel WHERE Hname = %s OR Address = %s", (identifier, identifier))
            results = cursor.fetchall()
            return results
        except Error as e:
            print(f"Error: {e}")
            return []
        finally:
            cursor.close()
            conn.close()
    else:
        print("Failed to connect to the database")
        return []

def show_hotels():
    hotels_window = tk.Toplevel(root)
    hotels_window.title("Hotel List")
    hotels_window.geometry("400x300")

    conn = create_connection()
    if conn:
        try:
            cursor = conn.cursor()
            cursor.execute("SELECT Hname FROM Hotel")
            hotel_list = cursor.fetchall()
        except Error as e:
            print(f"Error: {e}")
            hotel_list = []
        finally:
            cursor.close()
            conn.close()
    else:
        hotel_list = []

    hotel_listbox = tk.Listbox(hotels_window, font=("Arial", 14))
    for hotel in hotel_list:
        hotel_listbox.insert(tk.END, hotel[0])
    hotel_listbox.pack(pady=20, padx=20, fill='both', expand=True)

    close_button = tk.Button(hotels_window, text="Close", command=hotels_window.destroy, font=("Arial", 14), bg="#FF0000", fg="#FFFFFF")
    close_button.pack(pady=10)

def search_and_display_results():
    identifier = search_entry.get()
    results = search_hotels(identifier)
    if results:
        result_window = tk.Toplevel(root)
        result_window.title("Search Results")
        result_window.geometry("400x300")

        result_text = tk.Text(result_window, font=("Arial", 14))
        result_text.pack(pady=20, padx=20, fill='both', expand=True)

        for result in results:
            result_text.insert(tk.END, f"Hotel Name: {result[1]}\nAddress: {result[2]}\n\n")
    else:
        messagebox.showinfo("Info", "No results found.")

def continue_button_clicked():
    username = mobile_entry.get()
    password = password_entry.get()
    if username == "admin121" and password == "1234":
        root.withdraw()

        home_page_window = tk.Toplevel(root)
        home_page_window.title("Home Page")
        home_page_window.geometry("600x600")

        home_background_image = Image.open("img5.jpg")
        home_background_image = ImageTk.PhotoImage(home_background_image)

        home_background_label = tk.Label(home_page_window, image=home_background_image)
        home_background_label.place(x=0, y=0, relwidth=1, relheight=1)

        search_frame = tk.Frame(home_page_window, bg="#FFFFFF", highlightbackground="#CCCCCC", highlightthickness=1)
        search_frame.pack(pady=20, padx=20, fill='x')

        search_label = tk.Label(search_frame, text="Search", font=("Arial", 14), fg="#000000")
        search_label.pack(side='left', padx=10)

        global search_entry
        search_entry = tk.Entry(search_frame, font=("Arial", 14), width=30)
        search_entry.pack(side='left', padx=10)

        search_button = tk.Button(search_frame, text="Search", command=search_and_display_results, font=("Arial", 14), bg="#FF0000", fg="#FFFFFF")
        search_button.pack(side='left', padx=10)

        options_frame = tk.Frame(home_page_window, bg="#FFFFFF", highlightbackground="#CCCCCC", highlightthickness=1)
        options_frame.pack(pady=50, padx=20, fill='x')

        view_hotels_button = tk.Button(options_frame, text="View Hotels", command=show_hotels, font=("Arial", 14), bg="#FF0000", fg="#FFFFFF", width=20, height=2)
        view_hotels_button.pack(pady=20)

        cities_button = tk.Button(options_frame, text="Cities", command=lambda: messagebox.showinfo("Info", "Cities button clicked!"), font=("Arial", 14), bg="#FF0000", fg="#FFFFFF", width=20, height=2)
        cities_button.pack(pady=20)

        home_icon = ImageTk.PhotoImage(Image.open("home_icon.png").resize((24, 24)))
        bookings_icon = ImageTk.PhotoImage(Image.open("bookings_icon.png").resize((24, 24))) 
        search_icon = ImageTk.PhotoImage(Image.open("search_icon.png").resize((24, 24)))
        oyo_serviced_icon = ImageTk.PhotoImage(Image.open("oyo_serviced_icon.png").resize((24, 24)))
        need_help_icon = ImageTk.PhotoImage(Image.open("help_icon.png").resize((24, 24)))

        taskbar_frame = tk.Frame(home_page_window, bg="#FFFFFF", highlightbackground="#CCCCCC", highlightthickness=1)
        taskbar_frame.pack(side='bottom', fill='x')

        home_button = tk.Button(taskbar_frame, image=home_icon, command=lambda: messagebox.showinfo("Info", "Home button clicked!"), bg="#FFFFFF")
        home_button.pack(side='left', padx=10, pady=5)

        bookings_button = tk.Button(taskbar_frame, image=bookings_icon, command=lambda: messagebox.showinfo("Info", "Bookings button clicked!"), bg="#FFFFFF")
        bookings_button.pack(side='left', padx=10, pady=5)

        search_taskbar_button = tk.Button(taskbar_frame, image=search_icon, command=lambda: messagebox.showinfo("Info", "Search button clicked!"), bg="#FFFFFF")
        search_taskbar_button.pack(side='left', padx=10, pady=5)

        oyo_serviced_button = tk.Button(taskbar_frame, image=oyo_serviced_icon, command=lambda: messagebox.showinfo("Info", "OYO Serviced button clicked!"), bg="#FFFFFF")
        oyo_serviced_button.pack(side='left', padx=10, pady=5)

        need_help_button = tk.Button(taskbar_frame, image=need_help_icon, command=lambda: messagebox.showinfo("Info", "Need Help button clicked!"), bg="#FFFFFF")
        need_help_button.pack(side='left', padx=10, pady=5)

        home_page_window.mainloop()
    else:
        messagebox.showerror("Error", "Invalid username or password")

continue_button = tk.Button(login_frame, text="Continue", command=continue_button_clicked, font=("Arial", 14), bg="#FF0000", fg="#FFFFFF", width=20, height=2)
continue_button.pack(pady=10)

or_label = tk.Label(login_frame, text="OR", font=("Arial", 14), fg="#000000")
or_label.pack()

google_button = tk.Button(login_frame, text="Continue with Google", command=lambda: messagebox.showinfo("Info", "Google button clicked!"), font=("Arial", 14), bg="#FFFFFF", fg="#000000", width=20, height=2)
google_button.pack(pady=10)

signup_later_button = tk.Button(login_frame, text="I'll signup later", command=lambda: messagebox.showinfo("Info", "Signup later button clicked!"), font=("Arial", 12), bg="#FFFFFF", fg="#000000", width=20, height=1)
signup_later_button.pack(pady=10)

root.mainloop()
