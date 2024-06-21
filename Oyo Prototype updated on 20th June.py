import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import mysql.connector
from mysql.connector import Error

def create_connection():
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Saurav121@__",
            database="OYO"
        )
        return conn
    except Error as e:
        print(f"Error: {e}")
        return None
    
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import mysql.connector
from mysql.connector import Error

def create_connection():
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Saurav121@__",
            database="OYO"
        )
        return conn
    except Error as e:
        print(f"Error: {e}")
        return None

def show_bookings(cid):
    bookings_window = tk.Toplevel(root)
    bookings_window.title("Your Bookings")
    bookings_window.geometry("400x300")

    conn = create_connection()
    if conn:
        try:
            cursor = conn.cursor()
            cursor.execute("""
                SELECT Booking.BID, Hotel.HID, Hname, Booking.Check_In, Booking.Check_Out 
                FROM Booking 
                JOIN Hotel ON Booking.HID = Hotel.HID 
                WHERE Booking.CID = %s
            """, (cid,))
            bookings_list = cursor.fetchall()
        except Error as e:
            print(f"Error: {e}")
            bookings_list = []
        finally:
            cursor.close()
            conn.close()
    else:
        bookings_list = []

    bookings_listbox = tk.Listbox(bookings_window, font=("Arial", 14))
    for booking in bookings_list:
        bookings_listbox.insert(tk.END, f"Hotel: {booking[2]}, Room: {booking[1]}, Check-in: {booking[3]}, Check-out: {booking[4]}")
    bookings_listbox.pack(pady=20, padx=20, fill='both', expand=True)

    close_button = tk.Button(bookings_window, text="Close", command=bookings_window.destroy, font=("Arial", 14), bg="#FF0000", fg="#FFFFFF")
    close_button.pack(pady=10)

def continue_button_clicked():
    username = mobile_entry.get()
    password = password_entry.get()
    
    conn = create_connection()
    if conn:
        try:
            cursor = conn.cursor()
            cursor.execute("SELECT CID FROM Customer WHERE username = %s AND passwords = %s", (username, password))
            result = cursor.fetchone()
            
            if result:
                cid = result[0]
                root.withdraw()
                open_home_page(cid)
            else:
                tk.messagebox.showerror("Login Failed", "Invalid username or password.")
                
        except Exception as e:
            tk.messagebox.showerror("Error", f"An error occurred: {e}")
        finally:
            conn.close()
    else:
        messagebox.showerror("Error", "Invalid username or password")

def open_home_page(cid):
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

    bookings_button = tk.Button(taskbar_frame, text="Bookings", image=bookings_icon, compound='left', command=lambda: show_bookings(cid), font=("Arial", 14), bg="#FFFFFF", fg="#000000", width=100)
    bookings_button.pack(side='left', padx=5, pady=5)

    search_button = tk.Button(taskbar_frame, text="Search", image=search_icon, compound='left', command=lambda: messagebox.showinfo("Info", "Search button clicked!"), font=("Arial", 14), bg="#FFFFFF", fg="#000000", width=100)
    search_button.pack(side='left', padx=5, pady=5)

    oyo_serviced_button = tk.Button(taskbar_frame, text="OYO Serviced", image=oyo_serviced_icon, compound='left', command=lambda: messagebox.showinfo("Info", "OYO Serviced button clicked!"), font=("Arial", 14), bg="#FFFFFF", fg="#000000", width=100)
    oyo_serviced_button.pack(side='left', padx=5, pady=5)

    need_help_button = tk.Button(taskbar_frame, text="Need Help", image=need_help_icon, compound='left', command=lambda: messagebox.showinfo("Info", "Need Help button clicked!"), font=("Arial", 14), bg="#FFFFFF", fg="#000000", width=100)
    need_help_button.pack(side='left', padx=5, pady=5)

    home_page_window.mainloop()

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
mobile_entry.insert(0, "")
mobile_entry.pack(pady=5)

password_label = tk.Label(login_frame, text="Password", font=("Arial", 14), fg="#000000")
password_label.pack()
password_entry = tk.Entry(login_frame, font=("Arial", 14), width=20, show="*")
password_entry.insert(0, "")
password_entry.pack(pady=5)

continue_button = tk.Button(login_frame, text="Continue", command=continue_button_clicked, font=("Arial", 14), bg="#FF0000", fg="#FFFFFF", width=20, height=2)
continue_button.pack(pady=10)

or_label = tk.Label(login_frame, text="OR", font=("Arial", 14), fg="#000000")
or_label.pack()

google_button = tk.Button(login_frame, text="Continue with Google", command=lambda: messagebox.showinfo("Info", "Google login not implemented"), font=("Arial", 14), bg="#4285F4", fg="#FFFFFF", width=30, height=2)
google_button.pack(pady=5)

    
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
            cursor.fetchall() # Ensure all results are fetched
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
            cursor.fetchall() # Ensure all results are fetched
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

        details_text.insert(tk.END, f"Hotel Name: {hotel_details[1]}\nCity: {hotel_details[3]}\nRating: {hotel_details[2]}\nNo. of Rooms Available: {hotel_details[4]}\nContact Details: {hotel_details[5]}")

        proceed_button = tk.Button(details_window, text="Proceed to Payment", command=lambda: show_amenities(hotel_details), font=("Arial", 14), bg="#FF0000", fg="#FFFFFF")
        proceed_button.pack(pady=10)

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

    def proceed_to_payment():
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
        
        payment_info = {
            "room_type": selected_room_type,
            "facilities": selected_facilities
        }
        show_payment_page(payment_info)

    proceed_button = tk.Button(amenities_window, text="Proceed to Payment", command=proceed_to_payment, font=("Arial", 14), bg="#FF0000", fg="#FFFFFF")
    proceed_button.pack(pady=10)

    close_button = tk.Button(amenities_window, text="Close", command=amenities_window.destroy, font=("Arial", 14), bg="#FF0000", fg="#FFFFFF")
    close_button.pack(pady=10)

def show_payment_page(payment_info):
    payment_window = tk.Toplevel(root)
    payment_window.title("Payment")
    payment_window.geometry("400x300")

    tk.Label(payment_window, text="Select Payment Option:", font=("Arial", 14)).pack(pady=10)

    payment_option_var = tk.StringVar(value="Credit Card")
    tk.Radiobutton(payment_window, text="Credit Card", variable=payment_option_var, value="Credit Card", font=("Arial", 14)).pack(anchor='w')
    tk.Radiobutton(payment_window, text="Debit Card", variable=payment_option_var, value="Debit Card", font=("Arial", 14)).pack(anchor='w')
    tk.Radiobutton(payment_window, text="UPI", variable=payment_option_var, value="UPI", font=("Arial", 14)).pack(anchor='w')
    tk.Radiobutton(payment_window, text="Pay On Visit", variable=payment_option_var, value="Pay On Visit", font=("Arial", 14)).pack(anchor='w')

    card_details_frame = tk.Frame(payment_window)
    card_details_frame.pack(pady=10)

    def update_payment_options(*args):
        for widget in card_details_frame.winfo_children():
            widget.destroy()
        
        if payment_option_var.get() in ["Credit Card", "Debit Card"]:
            tk.Label(card_details_frame, text="Card Number:", font=("Arial", 14)).pack(anchor='w')
            tk.Entry(card_details_frame, font=("Arial", 14)).pack(anchor='w')
            tk.Label(card_details_frame, text="Expiry Date (MM/YY):", font=("Arial", 14)).pack(anchor='w')
            tk.Entry(card_details_frame, font=("Arial", 14)).pack(anchor='w')
            tk.Label(card_details_frame, text="CVV:", font=("Arial", 14)).pack(anchor='w')
            tk.Entry(card_details_frame, font=("Arial", 14)).pack(anchor='w')
        elif payment_option_var.get() == "UPI":
            tk.Label(card_details_frame, text="UPI ID:", font=("Arial", 14)).pack(anchor='w')
            tk.Entry(card_details_frame, font=("Arial", 14)).pack(anchor='w')
    
    payment_option_var.trace("w", update_payment_options)
    update_payment_options()

    def confirm_booking():
        messagebox.showinfo("Booking Confirmed", "Your booking has been confirmed!")

    confirm_button = tk.Button(payment_window, text="Confirm Booking", command=confirm_booking, font=("Arial", 14), bg="#FF0000", fg="#FFFFFF")
    confirm_button.pack(pady=10)

    close_button = tk.Button(payment_window, text="Close", command=payment_window.destroy, font=("Arial", 14), bg="#FF0000", fg="#FFFFFF")
    close_button.pack(pady=10)

root.mainloop()