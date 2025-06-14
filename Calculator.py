import tkinter as tk
from tkinter import font as tkfont

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")
        self.root.resizable(0, 0)  # Disable resizing
        
        # Custom font
        self.custom_font = tkfont.Font(size=15)
        
        # Create display
        self.display_var = tk.StringVar()
        self.display_var.set("0")
        
        self.display = tk.Entry(
            root, 
            textvariable=self.display_var, 
            font=self.custom_font, 
            bd=10, 
            insertwidth=1,
            width=14, 
            borderwidth=4, 
            justify='right',
            readonlybackground='white',
            state='readonly'
        )
        self.display.grid(row=0, column=0, columnspan=4)
        
        # Button layout
        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            'C', '0', '.', '+',
            '=', '⌫'  # Added backspace button
        ]
        
        # Create buttons
        row = 1
        col = 0
        for button_text in buttons:
            if button_text == '=':
                btn = tk.Button(
                    root, 
                    text=button_text, 
                    padx=20, 
                    pady=20, 
                    font=self.custom_font,
                    command=self.calculate,
                    bg='#4CAF50',  # Green color
                    fg='white'
                )
                btn.grid(row=5, column=2, columnspan=2, sticky="nsew")
                continue
            elif button_text == '⌫':
                btn = tk.Button(
                    root, 
                    text=button_text, 
                    padx=20, 
                    pady=20, 
                    font=self.custom_font,
                    command=self.backspace,
                    bg='#FF9800',  # Orange color
                    fg='white'
                )
            elif button_text == 'C':
                btn = tk.Button(
                    root, 
                    text=button_text, 
                    padx=20, 
                    pady=20, 
                    font=self.custom_font,
                    command=self.clear,
                    bg='#f44336',  # Red color
                    fg='white'
                )
            elif button_text in ['+', '-', '*', '/']:
                btn = tk.Button(
                    root, 
                    text=button_text, 
                    padx=20, 
                    pady=20, 
                    font=self.custom_font,
                    command=lambda op=button_text: self.set_operation(op),
                    bg='#2196F3',  # Blue color
                    fg='white'
                )
            else:
                btn = tk.Button(
                    root, 
                    text=button_text, 
                    padx=20, 
                    pady=20, 
                    font=self.custom_font,
                    command=lambda text=button_text: self.button_click(text)
                )
            
            btn.grid(row=row, column=col, sticky="nsew")
            col += 1
            if col > 3:
                col = 0
                row += 1
        
        # Configure grid weights to make buttons expandable
        for i in range(4):
            root.grid_columnconfigure(i, weight=1)
        for i in range(1, 6):
            root.grid_rowconfigure(i, weight=1)
        
        # Initialize calculator state
        self.current_input = ""
        self.operation = None
        self.previous_value = None
        self.reset_display = False
    
    def button_click(self, text):
        if self.reset_display:
            self.display_var.set("0")
            self.reset_display = False
        
        current_value = self.display_var.get()
        
        # Handle decimal point
        if text == '.':
            if '.' in current_value:
                return  # Only allow one decimal point
            if current_value == "0" or current_value == "":
                self.display_var.set("0.")
                self.current_input = "0."
                return
        
        if current_value == "0" and text != '.':
            self.display_var.set(text)
            self.current_input = text
        else:
            self.display_var.set(current_value + text)
            self.current_input += text
    
    def clear(self):
        self.current_input = ""
        self.display_var.set("0")
        self.operation = None
        self.previous_value = None
        self.reset_display = False
    
    def backspace(self):
        current_value = self.display_var.get()
        if len(current_value) == 1 or current_value == "Error":
            self.display_var.set("0")
            self.current_input = ""
        else:
            new_value = current_value[:-1]
            self.display_var.set(new_value)
            self.current_input = new_value
    
    def set_operation(self, op):
        try:
            if self.current_input or self.previous_value:
                if self.operation and self.previous_value is not None and self.current_input:
                    self.calculate()
                
                self.previous_value = float(self.display_var.get())
                self.operation = op
                self.current_input = ""
                self.reset_display = True
        except:
            self.display_var.set("Error")
            self.clear()
    
    def calculate(self):
        try:
            if self.operation and self.previous_value is not None:
                current_value = float(self.display_var.get())
                result = None
                
                if self.operation == '+':
                    result = self.previous_value + current_value
                elif self.operation == '-':
                    result = self.previous_value - current_value
                elif self.operation == '*':
                    result = self.previous_value * current_value
                elif self.operation == '/':
                    if current_value == 0:
                        self.display_var.set("Error: Div/0")
                        self.clear()
                        return
                    result = self.previous_value / current_value
                
                # Format result to remove unnecessary decimal places
                if result is not None:
                    if result.is_integer():
                        result = int(result)
                    self.display_var.set(str(result))
                    self.current_input = str(result)
                    self.reset_display = True
                self.operation = None
        except Exception as e:
            self.display_var.set("Error")
            self.clear()

if __name__ == "__main__":
    root = tk.Tk()
    calc = Calculator(root)
    root.mainloop()