# Calculator Application

This is a simple calculator application built using Python and the Tkinter library. It provides basic arithmetic operations such as addition, subtraction, multiplication, and division, as well as a clear button to reset the input field.

## Features
- Basic arithmetic operations: `+`, `-`, `*`, `/`
- Clear button (`C`) to reset the input field
- Equal button (`=`) to evaluate the entered expression
- User-friendly graphical interface

## Prerequisites
- Python 3.x installed on your system

## How to Run the Application
1. Clone or download this repository.
2. Ensure you have Python 3.x installed.
3. Run the Python script `calculator.py` using the following command:
   ```bash
   python calculator.py
   ```
4. The calculator window will open, and you can start using the application.

## Code Structure
- **Input Field**: The `tk.Entry` widget is used for entering numbers and operations.
- **Buttons**: Each button is created dynamically using a loop and tied to a specific operation using the `on_button_click` method.
- **Event Handling**: The `on_button_click` method processes button clicks, evaluates expressions, and displays results.

## Usage
1. Enter a mathematical expression using the buttons.
2. Press `=` to evaluate the expression.
3. Press `C` to clear the input field.

## Example
- Input: `12 + 8`
- Press `=`
- Output: `20`

## Screenshots
(No screenshots are provided in this README. You can run the application to see its interface.)

## Known Issues
- The application uses Python's built-in `eval()` function, which may pose security risks if untrusted input is provided.
- Does not support advanced operations like square root, power, or trigonometric functions.

## Future Enhancements
- Add support for advanced operations like square root, power, and percentage.
- Improve error handling for invalid inputs.

## License
This project is licensed under the MIT License. Feel free to use, modify, and distribute it.

---

### Author
Created by [Your Name]. Feel free to contribute or suggest improvements!
