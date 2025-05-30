def vacuum_cleaner():
    print("Vacuum Cleaner World (Two Rooms: A and B)")
    
    location = input("Enter initial location of vacuum (A/B): ").strip().upper()
    status_A = input("Enter status of room A (D for Dirty / C for Clean): ").strip().upper()
    status_B = input("Enter status of room B (D for Dirty / C for Clean): ").strip().upper()

    if location not in ['A', 'B'] or status_A not in ['D', 'C'] or status_B not in ['D', 'C']:
        print("Invalid input. Use A/B for location and D/C for status.")
        return

    print("\n--- Cleaning Process ---")

    def clean(location, status_A, status_B):
        if location == 'A':
            if status_A == 'D':
                print("Vacuum is at Location A. A is Dirty.")
                print("Action: Suck → A is now Clean.")
                status_A = 'C'
            else:
                print("Vacuum is at Location A. A is already Clean.")
            print("Moving to Location B.")
            location = 'B'
            if status_B == 'D':
                print("Location B is Dirty.")
                print("Action: Suck → B is now Clean.")
                status_B = 'C'
            else:
                print("Location B is already Clean.")
        else:  
            if status_B == 'D':
                print("Vacuum is at Location B. B is Dirty.")
                print("Action: Suck → B is now Clean.")
                status_B = 'C'
            else:
                print("Vacuum is at Location B. B is already Clean.")
            print("Moving to Location A.")
            location = 'A'
            if status_A == 'D':
                print("Location A is Dirty.")
                print("Action: Suck → A is now Clean.")
                status_A = 'C'
            else:
                print("Location A is already Clean.")
        print("\nFinal State: A =", status_A, ", B =", status_B)

    clean(location, status_A, status_B)

if __name__ == "__main__":
    vacuum_cleaner()
