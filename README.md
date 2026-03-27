# Advanced Calculator with GUI

## Overview

This project is a Python-based advanced calculator that combines both basic and scientific operations within a graphical user interface (GUI). Built using Tkinter, it provides a structured and interactive way to perform calculations without relying on the command line.

The application emphasizes clean design, modular logic, and user-friendly interaction.

---

## Features

### Core Operations

* Addition, subtraction, multiplication, and division
* Power/exponentiation

### Scientific Functions

* Square and cube
* Square root and cube root
* Logarithmic function (base 10)
* Trigonometric functions (sin, cos, tan)

### System Capabilities

* Input validation and error handling
* Protection against invalid operations (e.g., division by zero, invalid logarithms)
* Modular operation handling using function mapping
* Responsive GUI built with Tkinter

---

## Interface

The calculator includes:

* Input fields for numerical values
* A structured grid of operation buttons
* A result display section
* Clear and simple layout for ease of use

---

## Requirements

To run this project, ensure you have:

* Python 3.8 or higher
* Tkinter (included with most Python installations)

---

## Installation

Clone the repository:

```bash
git clone https://github.com/stephenombuya/Python_Calculator.git
cd advanced-calculator-gui
```

---

## Usage

Run the application:

```bash
main.py
```

---

## How It Works

1. Enter a value in the first input field
2. Enter a second value if required by the operation
3. Click the desired operation button
4. View the result instantly in the display area

---

## Project Structure

```
Python_Calculator/

├── src.py
    ├── main.py         # Main application (UI + logic)
├── README.md           # Documentation
```

---

## Design Improvements

Compared to a basic implementation, this version introduces:

* Separation of logic and UI components
* Use of operation mapping instead of long conditional chains
* Improved input validation
* Structured layout using grid positioning

---

## Future Improvements

* Calculation history panel
* Keyboard input support
* Theme customization (dark/light mode)
* Scientific mode toggle (basic vs advanced)
* Packaging as a standalone desktop application

---

## License

This project is open-source and available under the GNU General Public License.

---

## Contributions

Contributions are welcome:

1. Fork the repository
2. Create a new branch

   ```bash
   git checkout -b feature-branch
   ```
3. Make your changes
4. Commit your changes

   ```bash
   git commit -m "Add feature or improvement"
   ```
5. Push to your branch

   ```bash
   git push origin feature-branch
   ```
6. Open a pull request
