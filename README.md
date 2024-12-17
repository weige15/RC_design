# RC_design
This program analyzes RC sections strength including RC beam and RC column with GUI provided by pyqt5. Strength calculations are based on ACI-318 code.

# Reinforced Concrete Design Program

## 1. Overview
The **Reinforced Concrete Design Program** is a Python-based tool to assist structural engineers in designing and analyzing reinforced concrete beams and columns. It integrates computational logic, engineering design principles, and a user-friendly graphical interface for enhanced usability.

The tool adheres to industry standards like **ACI 318** or similar international codes for structural design.

### Key Features:
- Calculation of moment capacity, axial load capacity, and reinforcement areas.
- Support for **rectangular beams**, **T-beams**, and **columns**.
- Graphical User Interface (GUI) for input/output.
- Interactive **PMM (axial-moment interaction)** diagrams for columns.
- Modular and extensible code structure.

---

## 2. Project Structure
```
📦 Reinforced-Concrete-Design-Program
│
├── starter.py                 # Main entry point
├── menu_controller.py         # Controller for navigation
│
├── beam_function.py           # Beam calculation logic
├── column_function.py         # Column calculation logic
├── dataframe_model.py         # Data management logic
│
├── rc_beamdsgn_base.py        # Base logic for beam design
├── rc_columncal_base.py       # Base logic for column design
├── rc_recbeamcal_base.py      # Rectangular beam design
├── rc_tbeamcal_base.py        # T-beam design logic
│
├── ui_menu.py                 # Menu GUI
├── ui_rc_beamdsgn.py          # Beam design GUI
├── ui_rc_columncal.py         # Column design GUI
├── ui_rc_recbeamcal.py        # Rectangular beam GUI
├── ui_rc_tbeamcal.py          # T-beam GUI
│
├── widget_rc_beamdsgn.py      # Beam widgets
├── widget_rc_column.py        # Column widgets
├── widget_rc_pmm.py           # PMM interaction widgets
├── widget_rc_recbeam.py       # Rectangular beam widgets
└── widget_rc_tbeam.py         # T-beam widgets
```

---

## 3. Program Flow
The application follows the **Model-View-Controller (MVC)** architecture:
- **Model:** Core logic for calculations (`rc_*_base.py` files).
- **View:** GUI components (e.g., `ui_rc_*` and `widget_rc_*` files).
- **Controller:** Navigation logic (`menu_controller.py`).

The `starter.py` script launches the main menu where users can select the desired functionality. The menu directs users to specific design modules (beam, column, etc.), which connect to backend calculations and display the results.

---

## 4. Metrics Calculation in Detail

### 4.1 Beam Design Metrics
**Files:**
- `beam_function.py`
- `rc_beamdsgn_base.py`
- `rc_recbeamcal_base.py`
- `rc_tbeamcal_base.py`

#### Moment Capacity (\( M_u \)):

$$
M_u = A_s f_y \left( d - \frac{a}{2} \right)
$$

- \( A_s \): Steel reinforcement area  
- \( f_y \): Steel yield strength  
- \( d \): Effective depth of beam  
- \( a \): Depth of equivalent rectangular stress block  

#### Calculation of \( a \):

\[
a = \frac{A_s f_y}{0.85 f'_c b}
\]

#### Rectangular vs T-Beam Design:

- **Rectangular Beam**: Compression zone limited to beam width (\( b \)).
- **T-Beam**: Includes flange with effective width:

\[
b_{\text{effective}} = \min(b_f, \text{design width})
\]

#### Reinforcement Area (\( A_s \)):

\[
A_s = \frac{M_u}{f_y \left( d - \frac{a}{2} \right)}
\]

---

### 4.2 Column Design Metrics
**Files:**
- `column_function.py`
- `rc_columncal_base.py`

#### Axial Capacity (\( P_n \)):

\[
P_n = 0.85 f'_c (A_g - A_s) + f_y A_s
\]

- \( A_g \): Gross cross-sectional area  
- \( A_s \): Area of steel reinforcement  

#### Combined Axial & Bending (PMM Interaction):

\[
\frac{P_u}{P_n} + \frac{M_u}{M_n} \leq 1.0
\]

- PMM curve ensures the column does not fail under combined loads.  
- Computed and visualized in `widget_rc_pmm.py`.

---

### 4.3 Validation and Checks

The program ensures:

1. **Reinforcement Limits**: Prevent over-reinforcement (brittle failure).  
2. **Deflection Limits**: Serviceability checks.  
3. **Strength Reduction Factors (\( \phi \))**:  
   - Flexure: \( \phi = 0.9 \)  
   - Axial-bending: \( \phi = 0.75 \)  
4. **Cracking Control**: Limits on maximum crack width.


---

## 5. Example Use Cases
### Beam Design
1. **User inputs:** Span, width, depth, concrete strength \( f'_c \), and steel yield strength \( f_y \).
2. **Program calculates:** Required \( A_s \) and moment capacity \( M_u \).
3. **Output:** Reinforcement details displayed in GUI.

### Column Design
1. **User inputs:** Axial load \( P \), moment \( M \), and column dimensions.
2. **Program:**
   - Calculates axial-bending capacity.
   - Plots PMM interaction curve.
3. **Output:** Safe or unsafe design result.

---

## 6. GUI Description
- **Main Menu:** Navigate to beam or column design modules.
- **Beam GUI:** Input fields for beam dimensions, material properties, and load.
- **Column GUI:** Input fields and PMM curve visualization.
- **Rectangular & T-Beam Widgets:** Specialized input forms and results.

---

## 7. Installation

### Dependencies:
```bash
pip install numpy pandas
```

### Run the Program:
```bash
python starter.py
```

---

## 8. Contributing
1. Fork the repository.
2. Open a Pull Request with your changes.
3. Include clear documentation for any new features.

---

## 9. License
This project is licensed under the **MIT License**.

---

## 10. Contact
For any queries or suggestions, feel free to open an issue or contribute directly to the repository.

---

Happy Designing! 🏗️
