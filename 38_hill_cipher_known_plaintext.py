# Question 38: Hill Cipher and Known Plaintext Attack Demonstration
# Uses a 2x2 Hill cipher key matrix.

def mod_inverse(a, m):
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return None


def matrix_inverse_2x2(matrix):
    a, b = matrix[0]
    c, d = matrix[1]

    determinant = (a * d - b * c) % 26
    determinant_inverse = mod_inverse(determinant, 26)

    if determinant_inverse is None:
        return None

    return [
        [(d * determinant_inverse) % 26, (-b * determinant_inverse) % 26],
        [(-c * determinant_inverse) % 26, (a * determinant_inverse) % 26]
    ]


def matrix_multiply(A, B):
    return [
        [
            sum(A[i][k] * B[k][j] for k in range(2)) % 26
            for j in range(2)
        ]
        for i in range(2)
    ]


def text_to_numbers(text):
    return [ord(c.upper()) - ord('A') for c in text if c.isalpha()]


def main():
    print("Hill Cipher Known Plaintext Attack Demonstration")
    print("Use two plaintext blocks and corresponding ciphertext blocks.")
    print("Example plaintext matrix can be formed from 4 letters.")

    plaintext = input("Enter 4 plaintext letters: ").upper()
    ciphertext = input("Enter 4 corresponding ciphertext letters: ").upper()

    p = text_to_numbers(plaintext)
    c = text_to_numbers(ciphertext)

    if len(p) != 4 or len(c) != 4:
        print("Please enter exactly 4 alphabetic characters for each.")
        return

    # Arrange as 2x2 matrices using column vectors
    P = [[p[0], p[2]], [p[1], p[3]]]
    C = [[c[0], c[2]], [c[1], c[3]]]

    P_inverse = matrix_inverse_2x2(P)

    if P_inverse is None:
        print("Plaintext matrix is not invertible modulo 26.")
        print("Choose a different plaintext pair.")
        return

    # K = C * P^-1 mod 26
    K = matrix_multiply(C, P_inverse)

    print("\nRecovered Hill Cipher Key Matrix:")
    print(K[0])
    print(K[1])

    print("\nThis demonstrates a known plaintext attack:")
    print("K = C × P^-1 (mod 26)")


if __name__ == "__main__":
    main()
