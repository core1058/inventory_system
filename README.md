# inventory_system
A GUI-based inventory management system developed with Python and Tkinter, adopting OOP and modular design, with user permission control and complete product inventory operations.

📖**Table of Contents**
1. Project Overview
2. Core Features
3. Project Structure
4. Quick Start
5. Usage Instructions
6. Permission System
7. Troubleshooting
8. Technical Highlights
9. License
## Project Overview
The inventory management system provides an intuitive graphical interface for small businesses or personal use to manage product stock. It requires no external dependencies, runs on standard Python environments, and implements complete inventory control with data validaiton and use access restrictions.
## Core Features
- Add, delete,update product information
- Real-time inventory quantity management
- Automatic calculation of total inventory value
- Role-based permission control(Admin/Manager/Staff)
- Strict data validation for price and quantity
- User-friendly GUI with automatic table refresh
- No thrid-party libraries required
## Project Structure
inventory_system/
--- project.py
---inventory.py
---user.py
---gui.py
---main.py
## Preparatory work
- Python 3.6 or higher installed
- Tkinter
## Instruction
1. Make sure you have all 5 files in the same folder
2. Check environment requirement
3. function work: 
   -  Add a product (ID, Name, Price, Quantity)
   -  Delete a product (ID, Click Remove buttom)
   -  Update Quantity (ID, Click Update button)
   -  View total value (The total inventory value is shown at the bottom of the window)
4. Permission:
   - Administrator: All enabled
   - Manager: Update & View enabled
   - visitor: View only
## 📃License
This project is for learing and educational use only.




