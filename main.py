import numpy as np 
from scipy.linalg import lu

def ident(n):
    """Generate identity matrix of size n x n."""
    return np.identity(n)

def createMatrix(n, m):
    """Interactively build an (n x m) float matrix."""
    matrix = []
    print(f"\nEntering elements for a {n}x{m} matrix:")
    for i in range(1, n + 1):
        row = []
        for j in range(1, m + 1):
            while True:
                try:
                    element = float(input(f"Element [{i}][{j}]: "))
                    row.append(element)
                    break
                except ValueError:
                    print("Invalid input! Please enter a numerical value.")
        matrix.append(row)
    
    mat_np = np.array(matrix, dtype=float)
    print("\nMatrix created:\n", mat_np, "\n")
    return mat_np

def Matrixdecomp(A):
    """Perform various matrix decompositions with explicit error handling."""
    print("\n====== MATRIX DECOMPOSITION ======\n")
    print("1. LU Decomposition")
    print("2. QR Decomposition")
    print("3. SVD Decomposition")
    print("4. Eigendecomposition")
    print("5. Cholesky Decomposition\n")
    
    try:
        choice = int(input("Enter preference (1-5): "))
        
        if choice == 1:
            P, L, U = lu(A)
            print("\nPermutation Matrix P:\n", P)
            print("\nLower Triangular Matrix L:\n", L)
            print("\nUpper Triangular Matrix U:\n", U)

        elif choice == 2:
            Q, R = np.linalg.qr(A)
            print(f"\nQ Matrix:\n{Q}")
            print(f"\nR Matrix:\n{R}")

        elif choice == 3:
            U, S, Vh = np.linalg.svd(A)
            print(f"\nUnitary Matrix U:\n{U}")
            print(f"\nSingular Values S:\n{S}")
            print(f"\nRight Singular Vectors V^H:\n{Vh}")

        elif choice == 4:
            if A.shape[0] != A.shape[1]:
                print("\nError: Eigendecomposition requires a square matrix.")
                return
            eigvals, eigvec = np.linalg.eig(A)
            print(f"\nEigenvalues:\n{eigvals}")
            print(f"\nEigenvectors:\n{eigvec}")

            try:
                lam = np.diag(eigvals)
                eig_inverse = np.linalg.inv(eigvec)
                A_reconstructed = eigvec @ lam @ eig_inverse
                print(f"\nReconstructed Matrix (V * Lambda * V^-1):\n{np.real_if_close(A_reconstructed)}")
            except np.linalg.LinAlgError:
                print("\nNote: Eigenvector matrix is singular (non-invertible); cannot reconstruct matrix.")

        elif choice == 5:
            if A.shape[0] != A.shape[1]:
                print("\nError: Cholesky decomposition requires a square matrix.")
                return
            if not np.allclose(A, A.T):
                print("\nError: Cholesky decomposition requires a symmetric matrix.")
                return
            try:
                L = np.linalg.cholesky(A)
                print(f"\nLower Triangular Matrix L:\n{L}")
            except np.linalg.LinAlgError:
                print("\nError: Matrix is not positive-definite.")
        else:
            print("\nInvalid decomposition choice.")

    except ValueError:
        print("\nInvalid input. Please enter an integer choice.")
    except Exception as e:
        print(f"\nAn error occurred during decomposition: {e}")

def rref(A, tol=1e-12):
    """Compute Reduced Row Echelon Form (RREF)."""
    M, N = A.shape
    A = A.astype(float).copy()
    i, j = 0, 0
    
    while i < M and j < N:
        pivot = np.argmax(np.abs(A[i:M, j])) + i
        if np.abs(A[pivot, j]) <= tol:
            A[i:M, j] = 0.0
            j += 1
        else:
            A[[i, pivot]] = A[[pivot, i]]
            A[i] = A[i] / A[i, j]
            
            for k in range(M):
                if k != i:
                    A[k] -= A[k, j] * A[i]
            i += 1
            j += 1

    A[np.abs(A) < tol] = 0.0
    return A

# -------- MAIN LOOP --------------------------------------------------        

def main():
    while True:
        print("\n================ WELCOME TO MATRIX CALCULATOR ================")
        print("1. Make Identity Matrix")
        print("2. Create Custom Matrix")
        print("3. Generate Random Matrix")
        print("4. Multiply Two Matrices")
        print("5. Determinant of Matrix")
        print("6. Reduced Row Echelon Form (RREF)")
        print("7. Extract Upper / Lower Triangular Part")
        print("8. Rank of Matrix")
        print("9. Matrix Decomposition")
        print("10. Transpose of Matrix")
        print("11. Inverse of Matrix")
        print("12. Solve Linear System (Ax = b)")
        print("13. Exit")

        try:
            choice = int(input("\nEnter choice (1-13): "))
        except ValueError:
            print("Invalid input. Please enter a choice between 1 and 13.")
            continue

        if choice == 1:
            order = int(input("Order of identity matrix: "))
            print('\n', ident(order), '\n')

        elif choice == 2:
            row = int(input("Enter rows: "))
            cols = int(input("Enter columns: "))
            createMatrix(row, cols)

        elif choice == 3:
            row = int(input("Enter rows: "))
            cols = int(input("Enter columns: "))
            matrix = np.random.randint(-100, 100, size=(row, cols)).astype(float)
            print("\nGenerated Random Matrix:\n", matrix)

        elif choice == 4:
            row1 = int(input("Rows of Matrix 1: "))
            col1 = int(input("Columns of Matrix 1: "))
            row2 = int(input("Rows of Matrix 2: "))
            col2 = int(input("Columns of Matrix 2: "))

            if col1 != row2:
                print("\nCannot multiply: Columns of Matrix 1 must equal Rows of Matrix 2.")
            else:
                m1 = createMatrix(row1, col1)
                m2 = createMatrix(row2, col2)
                print("\nProduct:\n", np.matmul(m1, m2))

        elif choice == 5:
            row = int(input("Enter rows: "))
            cols = int(input("Enter columns: "))
            if row != cols:
                print("\nDeterminant is only defined for square matrices.")
            else:
                matrix = createMatrix(row, cols)
                det = np.linalg.det(matrix)
                print(f"\nDeterminant: {det:.4f}")

        elif choice == 6:
            row = int(input("Enter rows: "))
            cols = int(input("Enter columns: "))
            matrix = createMatrix(row, cols)
            print("\nRREF of matrix:\n", rref(matrix))

        elif choice == 7:
            row = int(input("Enter rows: "))
            cols = int(input("Enter columns: "))
            matrix = createMatrix(row, cols)
            tri_choice = input("Upper (U) or Lower (L): ").strip().lower()

            if tri_choice == "u":
                print("\nUpper Triangular Part:\n", np.triu(matrix))
            elif tri_choice == "l":
                print("\nLower Triangular Part:\n", np.tril(matrix))
            else:
                print("Invalid triangular option.")

        elif choice == 8:
            row = int(input("Enter rows: "))
            cols = int(input("Enter columns: "))
            matrix = createMatrix(row, cols)
            print("\nRank:", np.linalg.matrix_rank(matrix))

        elif choice == 9:
            row = int(input("Enter rows: "))
            cols = int(input("Enter columns: "))
            matrix = createMatrix(row, cols)
            Matrixdecomp(matrix)

        elif choice == 10:
            row = int(input("Enter rows: "))
            cols = int(input("Enter columns: "))
            matrix = createMatrix(row, cols)
            print("\nTranspose:\n", np.transpose(matrix))

        elif choice == 11:
            row = int(input("Enter rows: "))
            cols = int(input("Enter columns: "))
            if row != cols:
                print("\nInverse requires a square matrix.")
            else:
                matrix = createMatrix(row, cols)
                try:
                    inv = np.linalg.inv(matrix)
                    print("\nInverse:\n", inv)
                except np.linalg.LinAlgError:
                    print("\nMatrix is singular and does not have an inverse.")

        elif choice == 12:
            row = int(input("Enter dimension N of square matrix A: "))
            A = createMatrix(row, row)
            print("\nEnter vector b:")
            b = np.array([float(input(f"b[{i+1}]: ")) for i in range(row)])
            try:
                x = np.linalg.solve(A, b)
                print("\nSolution x:\n", x)
            except np.linalg.LinAlgError:
                print("\nSystem has no unique solution (matrix A is singular).")

        elif choice == 13:
            print("\nExiting Matrix Calculator. Goodbye!")
            break

if __name__ == "__main__":
    main()


