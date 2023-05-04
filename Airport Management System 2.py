import tkinter as tk
import cx_Oracle

# Set up the connection
connection = cx_Oracle.connect(user="system", password="123", dsn="localhost:1521/orcl")

# Create a cursor object
cursor = connection.cursor()

# Define the Tkinter GUI window
window = tk.Tk()
window.title("Airport Management System")

# Define the functions for inserting, deleting, updating, and displaying data
def insert_data():
    # Get the user input from the Tkinter GUI form
    flight_name = entry1.get()
    flight_number = entry2.get()
    gate_number = entry3.get()
    terminal_number = entry4.get()

    # Insert the data into the Airports table
    cursor.execute("INSERT INTO Airports (flight_number, flight_name, gate_number, terminal_number) VALUES (:1, :2, :3, :4)",
                   (flight_number, flight_name, gate_number, terminal_number))
    connection.commit()

    # Get the passenger data from the Tkinter GUI form
    passenger_name = entry5.get()
    seat_number = entry6.get()

    # Insert the data into the FlightPassengers table
    cursor.execute("INSERT INTO FlightPassengers (passenger_name, seat_number, flight_number) VALUES (:1, :2, :3)",
                   (passenger_name, seat_number, flight_number))
    connection.commit()

    status_label.config(text="Data inserted successfully")

def delete_data():
    # Get the user input from the Tkinter GUI form
    flight_number = entry2.get()

    # Delete the data from the FlightPassengers table
    cursor.execute("DELETE FROM FlightPassengers WHERE flight_number = :1", (flight_number,))
    connection.commit()

    # Delete the data from the Airports table
    cursor.execute("DELETE FROM Airports WHERE flight_number = :1", (flight_number,))
    connection.commit()

    status_label.config(text="Data deleted successfully")

def update_data():
    # Get the user input from the Tkinter GUI form
    flight_name = entry1.get()
    flight_number = entry2.get()
    gate_number= entry3.get()
    terminal_number = entry4.get()

    # Update the data in the Airports table
    cursor.execute("UPDATE Airports SET flight_name = :1, gate_number = :2, terminal_number = :3 WHERE flight_number = :4",
                   (flight_name, gate_number, terminal_number, flight_number))
    connection.commit()

    # Get the passenger data from the Tkinter GUI form
    passenger_name = entry5.get()
    seat_number = entry6.get()

    # Update the data in the FlightPassengers table
    cursor.execute("UPDATE FlightPassengers SET passenger_name = :1, seat_number = :2 WHERE flight_number = :3",
                   (passenger_name, seat_number, flight_number))
    connection.commit()

    status_label.config(text="Data updated successfully")

def display_data():
    # Get the data from the Airports and FlightPassengers tables
    cursor.execute("SELECT a.flight_number, a.flight_name, a.gate_number, a.terminal_number, p.passenger_name, p.seat_number FROM Airports a LEFT JOIN FlightPassengers p ON a.flight_number = p.flight_number")
    result = cursor.fetchall()

    # Clear the current contents of the display listbox
    display_listbox.delete(0, tk.END)

    # Display the data in the display listbox
    for row in result:
        display_listbox.insert(tk.END, f"{row[0]} - {row[1]}, {row[2]}, {row[3]}, {row[4]}, {row[5]}")

# Define the Tkinter GUI form elements
label1 = tk.Label(window, text="Flight Name:")
entry1 = tk.Entry(window)
label2 = tk.Label(window, text="Flight Number:")
entry2 = tk.Entry(window)
label3 = tk.Label(window, text="Gate Number:")
entry3 = tk.Entry(window)
label4 = tk.Label(window, text="Terminal Number:")
entry4 = tk.Entry(window)
label5 = tk.Label(window, text="Passenger Name:")
entry5 = tk.Entry(window)
label6 = tk.Label(window, text="Seat Number:")
entry6 = tk.Entry(window)
insert_button = tk.Button(window, text="Insert Data", command=insert_data)
delete_button = tk.Button(window, text="Delete Data", command=delete_data)
update_button = tk.Button(window, text="Update Data", command=update_data)
display_button = tk.Button(window, text="Display Data", command=display_data)
display_listbox = tk.Listbox(window)
status_label = tk.Label(window, text="")

# Add the Tkinter GUI form elements to the window
label1.grid(row=0, column=0)
entry1.grid(row=0, column=1)
label2.grid(row=1, column=0)
entry2.grid(row=1, column=1)
label3.grid(row=2, column=0)
entry3.grid(row=2, column=1) 
label4.grid(row=3, column=0)
entry4.grid(row=3, column=1)
label5.grid(row=4, column=0)
entry5.grid(row=4, column=1)
label6.grid(row=5, column=0)
entry6.grid(row=5, column=1)
insert_button.grid(row=6, column=0)
delete_button.grid(row=6, column=1)
update_button.grid(row=6, column=2)
display_button.grid(row=7, column=0)
display_listbox.grid(row=8, column=0, columnspan=3)
status_label.grid(row=9, column=0, columnspan=3)

connection.commit()

window.mainloop()

connection.close()
