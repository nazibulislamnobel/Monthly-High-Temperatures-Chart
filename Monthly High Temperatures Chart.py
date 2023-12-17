import matplotlib.pyplot as plt

def main():
    city = input("Enter city: ")
    year = input("Enter year: ")

    try:
        year = int(year)
    except ValueError:
        print("Please enter a valid year.")
        return

    temperatures = input("Enter average high temperature for each month of the year: \n").split()
    temperatures = [float(temp) for temp in temperatures]

    if len(temperatures) != 12:
        print("Please enter exactly 12 temperatures for each month.")
        return

    months = [
        "Jan", "Feb", "Mar", "Apr",
        "May", "Jun", "Jul", "Aug",
        "Sep", "Oct", "Nov", "Dec"
    ]

    plt.figure(figsize=(10, 6))
    plt.plot(months, temperatures, marker='o', linestyle='-', color='b')
    plt.title(f"{year} Average Monthly High Temperatures - {city}")
    plt.xlabel("Months")
    plt.ylabel("Temperature")
    plt.grid(True)
    plt.ylim(0, 95)
    plt.yticks(range(0, 96, 5))

    plt.show()

if __name__ == "__main__":
    main()