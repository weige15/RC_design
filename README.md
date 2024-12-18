\documentclass[a4paper,12pt]{article}
\usepackage{amsmath}
\usepackage{amssymb}
\usepackage{geometry}
\usepackage{hyperref}
\geometry{margin=1in}

\begin{document}

\title{Reinforced Concrete Design Program}
\author{}
\date{}
\maketitle

\section{Overview}
The \textbf{Reinforced Concrete Design Program} is a Python-based tool to assist structural engineers in designing and analyzing reinforced concrete beams and columns. It integrates computational logic, engineering design principles, and a user-friendly graphical interface for enhanced usability.

The tool adheres to industry standards like \textbf{ACI 318} or similar international codes for structural design.

\subsection*{Key Features:}
\begin{itemize}
    \item Calculation of moment capacity, axial load capacity, and reinforcement areas.
    \item Support for \textbf{rectangular beams}, \textbf{T-beams}, and \textbf{columns}.
    \item Graphical User Interface (GUI) for input/output.
    \item Interactive \textbf{PMM (axial-moment interaction)} diagrams for columns.
    \item Modular and extensible code structure.
\end{itemize}

\section{Project Structure}
\begin{verbatim}
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
\end{verbatim}

\section{Program Flow}
The application follows the \textbf{Model-View-Controller (MVC)} architecture:
\begin{itemize}
    \item \textbf{Model:} Core logic for calculations (rc\_\*\_base.py files).
    \item \textbf{View:} GUI components (e.g., ui\_rc\_\* and widget\_rc\_\* files).
    \item \textbf{Controller:} Navigation logic (menu\_controller.py).
\end{itemize}
The starter.py script launches the main menu where users can select the desired functionality. The menu directs users to specific design modules (beam, column, etc.), which connect to backend calculations and display the results.

\section{Metrics Calculation in Detail}

\subsection{Beam Design Metrics}
\textbf{Files:}
\begin{itemize}
    \item beam\_function.py
    \item rc\_beamdsgn\_base.py
    \item rc\_recbeamcal\_base.py
    \item rc\_tbeamcal\_base.py
\end{itemize}

\subsubsection*{Moment Capacity ($M_u$):}
\begin{equation}
M_u = A_s f_y \left( d - \frac{a}{2} \right)
\end{equation}
\begin{itemize}
    \item $A_s$: Steel reinforcement area
    \item $f_y$: Steel yield strength
    \item $d$: Effective depth of beam
    \item $a$: Depth of equivalent rectangular stress block
\end{itemize}

\subsubsection*{Calculation of $a$:}
\begin{equation}
a = \frac{A_s f_y}{0.85 f'_c b}
\end{equation}

\subsubsection*{Rectangular vs T-Beam Design:}
\begin{itemize}
    \item \textbf{Rectangular Beam:} Compression zone limited to beam width ($b$).
    \item \textbf{T-Beam:} Includes flange with effective width:
    \begin{equation}
    b_{\text{effective}} = \min(b_f, \text{design width})
    \end{equation}
\end{itemize}

\subsubsection*{Reinforcement Area ($A_s$):}
\begin{equation}
A_s = \frac{M_u}{f_y \left( d - \frac{a}{2} \right)}
\end{equation}

\subsection{Column Design Metrics}
\textbf{Files:}
\begin{itemize}
    \item column\_function.py
    \item rc\_columncal\_base.py
\end{itemize}

\subsubsection*{Axial Capacity ($P_n$):}
\begin{equation}
P_n = 0.85 f'_c (A_g - A_s) + f_y A_s
\end{equation}
\begin{itemize}
    \item $A_g$: Gross cross-sectional area
    \item $A_s$: Area of steel reinforcement
\end{itemize}

\subsubsection*{Combined Axial \& Bending (PMM Interaction):}
\begin{equation}
\frac{P_u}{P_n} + \frac{M_u}{M_n} \leq 1.0
\end{equation}
\begin{itemize}
    \item PMM curve ensures the column does not fail under combined loads.
    \item Computed and visualized in widget\_rc\_pmm.py.
\end{itemize}

\subsection{Validation and Checks}
The program ensures:
\begin{enumerate}
    \item \textbf{Reinforcement Limits:} Prevent over-reinforcement (brittle failure).
    \item \textbf{Deflection Limits:} Serviceability checks.
    \item \textbf{Strength Reduction Factors ($\phi$):}
    \begin{itemize}
        \item Flexure: $\phi = 0.9$
        \item Axial-bending: $\phi = 0.75$
    \end{itemize}
    \item \textbf{Cracking Control:} Limits on maximum crack width.
\end{enumerate}

\section{Example Use Cases}
\subsection{Beam Design}
\begin{enumerate}
    \item \textbf{User inputs:} Span, width, depth, concrete strength $f'_c$, and steel yield strength $f_y$.
    \item \textbf{Program calculates:} Required $A_s$ and moment capacity $M_u$.
    \item \textbf{Output:} Reinforcement details displayed in GUI.
\end{enumerate}

\subsection{Column Design}
\begin{enumerate}
    \item \textbf{User inputs:} Axial load $P$, moment $M$, and column dimensions.
    \item \textbf{Program:}
    \begin{itemize}
        \item Calculates axial-bending capacity.
        \item Plots PMM interaction curve.
    \end{itemize}
    \item \textbf{Output:} Safe or unsafe design result.
\end{enumerate}

\section{GUI Description}
\begin{itemize}
    \item \textbf{Main Menu:} Navigate to beam or column design modules.
    \item \textbf{Beam GUI:} Input fields for beam dimensions, material properties, and load.
    \item \textbf{Column GUI:} Input fields and PMM curve visualization.
    \item \textbf{Rectangular \& T-Beam Widgets:} Specialized input forms and results.
\end{itemize}

\section{Installation}
\subsection*{Dependencies:}
\begin{verbatim}
pip install numpy pandas
\end{verbatim}

\subsection*{Run the Program:}
\begin{verbatim}
python starter.py
\end{verbatim}

\section{Contributing}
\begin{enumerate}
    \item Fork the repository.
    \item Open a Pull Request with your changes.
    \item Include clear documentation for any new features.
\end{enumerate}

\section{License}
This project is licensed under the \textbf{MIT License}.

\section{Contact}
For any queries or suggestions, feel free to open an issue or contribute directly to the repository.

\end{document}
