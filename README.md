⚡ Matrix Calculator CLI ⚡A powerful, interactive command-line Linear Algebra calculator built with Python, NumPy, and SciPy.🌟 OverviewWelcome to Matrix Calculator CLI! 🚀 Whether you are standardizing matrices, computing decompositions, or solving complex linear systems, this tool provides a sleek interactive menu packed with robust mathematical capabilities.🔥 Key FeaturesCategoryFeatures Included🛠️ Matrix GenerationCustom $N \times M$ input, Identity matrices 🆔, Random matrix generation 🎲🧮 Core OperationsMatrix Multiplication ✖️, Transposition 🔄, Inverse Calculation 🔁, Determinants 📊, Matrix Rank 📈🧩 Advanced FactorizationsLU Decomposition 📐QR Decomposition 📉Singular Value Decomposition (SVD) 🌌Eigendecomposition ⚡Cholesky Decomposition 💎📐 Linear Systems & RREFCustom Gauss-Jordan RREF algorithm 🔍Direct System Solver ($Ax = b$) 🎯⚡ Quick Start1️⃣ PrerequisitesMake sure you have Python installed along with the required libraries:pip install numpy scipy
2️⃣ Clone & Run# Clone the repository 
git clone https://github.com/your-username/matrix-calculator.git

# Navigate into the project directory
cd matrix-calculator

# Launch the calculator 🎉
python matrix.py
🕹️ Interactive CLI Menu================ WELCOME TO MATRIX CALCULATOR ================
1. 🆔 Make Identity Matrix
2. ✍️  Create Custom Matrix
3. 🎲 Generate Random Matrix
4. ✖️  Multiply Two Matrices
5. 📊 Determinant of Matrix
6. 🔍 Reduced Row Echelon Form (RREF)
7. 📐 Extract Upper / Lower Triangular Part
8. 📈 Rank of Matrix
9. 🧩 Matrix Decomposition (LU, QR, SVD, Eigen, Cholesky)
10. 🔄 Transpose of Matrix
11. 🔁 Inverse of Matrix
12. 🎯 Solve Linear System (Ax = b)
13. 🚪 Exit
✨ Features Highlight🛡️ Robust Validation: Never worry about crashes from non-square matrices or zero-determinants!🧮 Precision Thresholding: Eliminates floating-point noise (e.g., -0.0 or 1e-16) during RREF eliminations.💬 User-Friendly Prompts: Input numeric values seamlessly with continuous inline error-checking.🤝 ContributingContributions, issues, and feature requests are welcome!Feel free to check the issues page if you want to contribute.📜 LicenseDistributed under the MIT License. See LICENSE for details. 🌟
