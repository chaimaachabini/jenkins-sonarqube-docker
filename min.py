def calculate_sum(numbers):
    """
    Cette fonction calcule la somme des nombres dans une liste.
    :param numbers: Liste des nombres
    :return: Somme des nombres
    """
    if not numbers:
        return 0
    
    return sum(numbers)

if __name__ == "__main__":
    # Exemple de liste
    numbers = [1, 2, 3, 4, 5]
    total = calculate_sum(numbers)
    print(f"La somme des nombres est : {total}")
