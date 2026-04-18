# Kenneth Ly and Kenneth Cho
def couples_swap(couples):
    swaps = 0
    
    for i in range(0, len(couples), 2):
        first_partner = couples[i]
        
        # Checks if partner is even or odd
        # Example: 1 should be with 0, not 2 so it becomes (1 - 1)
        if first_partner % 2 == 0:
            second_partner = first_partner + 1
        else:
            second_partner = first_partner - 1
            
        # Couple is already together, skip
        if couples[i + 1] == second_partner:
            continue
        
        # Search for their partner, start at the second couple
        for j in range(i + 2, len(couples)):
            if couples[j] == second_partner:
                
                # Swap in place
                couples[i + 1], couples[j] = couples[j], couples[i + 1]
                swaps += 1
                break 
            
    return swaps            

if __name__ == "__main__":
    print(couples_swap([0, 2, 1, 3]))
    print(couples_swap([3, 2, 0, 1]))