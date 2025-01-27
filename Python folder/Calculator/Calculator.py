import tkinter as tk  # Import the tkinter module for building the graphical user interface

class CalculatorApp:
    def __init__(self, root):
        self.root = root  # Reference to the root window
        self.root.title("Calculator")  # Set the window title

        # Input field for displaying and entering expressions
        self.entry = tk.Entry(root, width=20, font=("Arial", 18), borderwidth=5, relief="ridge", justify="right")
        self.entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)  # Position the entry field at the top

        # Layout for calculator buttons (text, row, column)
        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),  # Row 1: numbers and division
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),  # Row 2: numbers and multiplication
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),  # Row 3: numbers and subtraction
            ('C', 4, 0), ('0', 4, 1), ('=', 4, 2), ('+', 4, 3),  # Row 4: clear, zero, equals, addition
        ]

        # Loop to create and position each button in the UI
        for (text, row, col) in buttons:
            button = tk.Button(root, text=text, font=("Arial", 18), width=5, height=2,  # Button styling
                               command=lambda t=text: self.on_button_click(t))  # Assign click behavior
            button.grid(row=row, column=col, padx=5, pady=5)  # Place the button on the grid

    # Event handler for button clicks
    def on_button_click(self, char):
        if char == "C":  # Clear the input field if "C" is clicked
            self.entry.delete(0, tk.END)
        elif char == "=":  # Evaluate the expression if "=" is clicked
            try:
                expression = self.entry.get()  # Get the current input from the field
                result = eval(expression)  # Evaluate the mathematical expression
                self.entry.delete(0, tk.END)  # Clear the input field
                self.entry.insert(tk.END, str(result))  # Display the result
            except Exception:  # Handle errors (e.g., invalid expressions)
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, "Error")  # Display an error message
        else:  # For numbers and operators, append the character to the input field
            self.entry.insert(tk.END, char)

# Entry point of the application
if __name__ == "__main__":
    root = tk.Tk()  # Create the root window
    app = CalculatorApp(root)  # Instantiate the CalculatorApp
    root.mainloop()  # Start the Tkinter event loop
