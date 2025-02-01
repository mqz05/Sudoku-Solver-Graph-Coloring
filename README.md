# **Sudoku Solver using Graph Coloring**  
**A Python-based project to solve Sudoku puzzles using graph theory and chromatic polynomials**  

## **Overview**  
This project solves **Sudoku puzzles** by modeling them as **graph coloring problems**. It uses the `networkx` library to generate graphs, `matplotlib` to visualize Sudoku boards and graphs, and computes **chromatic polynomials** to determine the number of valid solutions for a given Sudoku puzzle.  [Preview screenshots](#screenshots)

This project was developed as part of my **IB Diploma Program Internal Assessment** in **Analysis and Approaches (Higher Level)**. This project demonstrates the application of graph theory and combinatorics to solve classic puzzles like Sudoku. You can view the complete document (in Spanish) here:  [Download PDF Document](https://github.com/user-attachments/files/18630026/TI_AnalisisyEnfoques_NS_Mayo23.pdf)

---

## **Features**  
- **Sudoku Solving:** Solves 4x4 and 9x9 Sudoku puzzles using graph coloring.  
- **Graph Visualization:** Generates and plots graphs representing Sudoku puzzles.  
- **Chromatic Polynomials:** Computes the number of valid Sudoku solutions using chromatic polynomials.  
- **Custom Input:** Modify the `sudoku_board.py` file to input custom Sudoku puzzles.  
- **Research Integration:** Includes a research paper (in Spanish) analyzing the mathematical foundations and results of the project.  

---

## **How It Works**  
1. **Graph Representation:**  
   - Each cell in the Sudoku grid is represented as a node in a graph.  
   - Edges connect nodes that cannot have the same number (i.e., nodes in the same row, column, or block).  
2. **Graph Coloring:**  
   - The Sudoku puzzle is solved by assigning colors (numbers) to nodes such that no two connected nodes share the same color.  
3. **Chromatic Polynomials:**  
   - The `polinomio_cromatico.py` file computes the chromatic polynomial for a given Sudoku graph, determining the number of valid solutions.  

---

## **Screenshots**   <a name="screenshots"></a> 
Here are some visualizations of the project:  

- 9x9 Sudoku Graph:
<p align="center">
  <img src="https://github.com/user-attachments/assets/22dbf25a-9817-41eb-8b3a-1404687a610f" width="45%">&nbsp;&nbsp;&nbsp;&nbsp;
  <img src="https://github.com/user-attachments/assets/90be764d-bc96-4cb9-bf9b-2241ae42f9ab" width="45%">
</p>

- 4x4 Sudoku Graph:
<p align="center">
  <img src="https://github.com/user-attachments/assets/fb099c81-52e9-4954-8739-4c8fdfd0b95b" width="45%">&nbsp;&nbsp;&nbsp;&nbsp;
  <img src="https://github.com/user-attachments/assets/186d16fd-d37e-48bd-ad95-51368193fa53" width="45%">
</p>


---

## **Technologies Used**  
- **Programming Language:** Python  
- **Libraries:**  
  - `networkx` for graph generation and manipulation.  
  - `matplotlib` for plotting Sudoku boards and graphs.  
  - `numpy` for numerical computations.  

---

## **Installation**  
To run this project locally, follow these steps:  
1. Clone the repository:  
   ```bash  
   git clone https://github.com/mqz05/Sudoku-Solver-Graph-Coloring.git
   ```
2. Navigate to the project directory:
   ```bash  
   cd Sudoku-Solver-Graph-Coloring  
   ```
3. Install the required libraries:
   ``` bash
   pip install networkx matplotlib numpy
   ```
4. Modify the sudoku_board.py file to input your Sudoku puzzle.
5. Run the solver (*note, it might take a couple minutes to run, if so, try changing input sudoku*):
   ```bash
   python main.py
   ```
6. To compute chromatic polynomials, set up the input sudoku in the file and run :
   ``` bash
   python polinomio_cromatico.py
   ```

---

## **Credits**  
- Developed by Muqi Zhang
- Inspired by the blog post: [Sudoku Solver using Graph Coloring](https://medium.com/code-science/sudoku-solver-graph-coloring-8f1b4df47072)  

