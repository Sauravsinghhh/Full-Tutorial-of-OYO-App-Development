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

def show_hotel_details(hotel_name):
    conn = create_connection()
    if conn:
        try:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM Hotel WHERE Hname = %s", (hotel_name,))
            hotel_details = cursor.fetchone()
        except Error as e:
            print(f"Error: {e}")
            hotel_details = None
        finally:
            cursor.close()
            conn.close()
    else:
        hotel_details = None

    if hotel_details:
        details_window = tk.Toplevel(root)
        details_window.title("Hotel Details")
        details_window.geometry("400x300")

        details_text = tk.Text(details_window, font=("Arial", 14))
        details_text.pack(pady=20, padx=20, fill='both', expand=True)

        details_text.insert(tk.END, f"Hotel Name: {hotel_details[1]}\nCity: {hotel_details[3]}\nRating: {hotel_details[2]}\nNo. of Rooms Available: {hotel_details[4]}")

        book_button = tk.Button(details_window, text="Book Now", command=lambda: show_amenities(hotel_details), font=("Arial", 14), bg="#FF0000", fg="#FFFFFF")
        book_button.pack(pady=10)

        close_button = tk.Button(details_window, text="Close", command=details_window.destroy, font=("Arial", 14), bg="#FF0000", fg="#FFFFFF")
        close_button.pack(pady=10)
    else:
        messagebox.showerror("Error", "No details found for this hotel")

def show_amenities(hotel_details):
    amenities_window = tk.Toplevel(root)
    amenities_window.title("Select Amenities")
    amenities_window.geometry("400x300")

    tk.Label(amenities_window, text="Select Room Type:", font=("Arial", 14)).pack(pady=10)
    
    room_type_var = tk.StringVar(value="Single")
    tk.Radiobutton(amenities_window, text="Single", variable=room_type_var, value="Single", font=("Arial", 14)).pack(anchor='w')
    tk.Radiobutton(amenities_window, text="Double", variable=room_type_var, value="Double", font=("Arial", 14)).pack(anchor='w')
    tk.Radiobutton(amenities_window, text="Suite", variable=room_type_var, value="Suite", font=("Arial", 14)).pack(anchor='w')

    tk.Label(amenities_window, text="Select Facilities:", font=("Arial", 14)).pack(pady=10)
    
    wifi_var = tk.BooleanVar()
    parking_var = tk.BooleanVar()
    gym_var = tk.BooleanVar()
    breakfast_var = tk.BooleanVar()
    
    tk.Checkbutton(amenities_window, text="WiFi", variable=wifi_var, font=("Arial", 14)).pack(anchor='w')
    tk.Checkbutton(amenities_window, text="Parking", variable=parking_var, font=("Arial", 14)).pack(anchor='w')
    tk.Checkbutton(amenities_window, text="Gym", variable=gym_var, font=("Arial", 14)).pack(anchor='w')
    tk.Checkbutton(amenities_window, text="Breakfast", variable=breakfast_var, font=("Arial", 14)).pack(anchor='w')

    def book_now():
        selected_room_type = room_type_var.get()
        selected_facilities = []
        if wifi_var.get():
            selected_facilities.append("WiFi")
        if parking_var.get():
            selected_facilities.append("Parking")
        if gym_var.get():
            selected_facilities.append("Gym")
        if breakfast_var.get():
            selected_facilities.append("Breakfast")

        messagebox.showinfo("Booking Info", f"Room Type: {selected_room_type}\nFacilities: {', '.join(selected_facilities)}\nBooking Confirmed!")

    book_button = tk.Button(amenities_window, text="Book Now", command=book_now, font=("Arial", 14), bg="#FF0000", fg="#FFFFFF")
    book_button.pack(pady=10)

    close_button = tk.Button(amenities_window, text="Close", command=amenities_window.destroy, font=("Arial", 14), bg="#FF0000", fg="#FFFFFF")
    close_button.pack(pady=10)

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

    def on_hotel_select(event):
        selected_hotel = hotel_listbox.get(hotel_listbox.curselection())
        show_hotel_details(selected_hotel)

    hotel_listbox.bind('<<ListboxSelect>>', on_hotel_select)

    close_button = tk.Button(hotels_window, text="Close", command=hotels_window.destroy, font=("Arial", 14), bg="#FF0000", fg="#FFFFFF")
    close_button.pack(pady=10)

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
        
        search_entry = tk.Entry(search_frame, font=("Arial", 14), width=30)
        search_entry.pack(side='left', padx=10)
        
        search_button = tk.Button(search_frame, text="Search", command=lambda: messagebox.showinfo("Info", "Search button clicked!"), font=("Arial", 14), bg="#FF0000", fg="#FFFFFF")
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
        
        home_button = tk.Button(taskbar_frame, text="Home", image=home_icon, compound='left', command=lambda: messagebox.showinfo("Info", "Home button clicked!"), font=("Arial", 14), bg="#FFFFFF", fg="#000000", width=100)
        home_button.pack(side='left', padx=5, pady=5)
        
        bookings_button = tk.Button(taskbar_frame, text="Bookings", image=bookings_icon, compound='left', command=lambda: messagebox.showinfo("Info", "Bookings button clicked!"), font=("Arial", 14), bg="#FFFFFF", fg="#000000", width=100)
        bookings_button.pack(side='left', padx=5, pady=5)
        
        search_button = tk.Button(taskbar_frame, text="Search", image=search_icon, compound='left', command=lambda: messagebox.showinfo("Info", "Search button clicked!"), font=("Arial", 14), bg="#FFFFFF", fg="#000000", width=100)
        search_button.pack(side='left', padx=5, pady=5)
        
        oyo_serviced_button = tk.Button(taskbar_frame, text="OYO Serviced", image=oyo_serviced_icon, compound='left', command=lambda: messagebox.showinfo("Info", "OYO Serviced button clicked!"), font=("Arial", 14), bg="#FFFFFF", fg="#000000", width=100)
        oyo_serviced_button.pack(side='left', padx=5, pady=5)
        
        need_help_button = tk.Button(taskbar_frame, text="Need Help", image=need_help_icon, compound='left', command=lambda: messagebox.showinfo("Info", "Need Help button clicked!"), font=("Arial", 14), bg="#FFFFFF", fg="#000000", width=100)
        need_help_button.pack(side='left', padx=5, pady=5)
        
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
