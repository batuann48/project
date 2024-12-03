from visualization import plot_carbon_footprint, show_table
import subprocess

def main():
    while True:
        print("\n1. Open GUI for Calculation")
        print("2. Show Graphs")
        print("3. Show Data Table")
        print("4. Exit")
        choice = input("Enter Your choice:")


        if choice == "1":
            subprocess.run(["python","gui.py"])
        elif choice == "2":
            plot_carbon_footprint()
        elif choice == "3":
            show_table()
        elif choice == "4":
            print("Exiting program.")
            break
        else:
            print("Invalid choice! Try again.")

if __name__ == "__main__":
    main()
