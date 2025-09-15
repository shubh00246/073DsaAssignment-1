# WeatherRecord ADT

class WeatherRecord:
    # Constructor: creates a new record
    def __init__(self, date, city, temperature):
        self.date = date
        self.city = city
        self.temperature = temperature

    # Insert or update a record
    def insert(self, date, city, temperature):
        self.date = date
        self.city = city
        self.temperature = temperature
        print(f"Inserted record: {self.city}, {self.date}, {self.temperature}°C")

    # Delete a record
    def delete(self):
        print(f"Deleting record for {self.city} on {self.date}")
        self.date = None
        self.city = None
        self.temperature = None

    # Retrieve record based on city + year
    def retrieve(self, city, year):
        record_year = self.date.split("/")[-1] if self.date else None
        if self.city == city and record_year == str(year):
            return f"Temperature in {self.city} ({year}) was {self.temperature}°C"
        else:
            return "No record found"



record1 = WeatherRecord("05/09/2025", "Delhi", 32.5)

record1.insert("06/09/2025", "Delhi", 33.0)

print(record1.retrieve("Delhi", 2025))

record1.delete()

print(record1.retrieve("Delhi", 2025))


class DataStorage:
    def __init__(self, years, cities):
        self.years = years
        self.cities = cities
        # Create a 2D array (years x cities) initialized with None
        self.data = [[None for _ in range(len(cities))] for _ in range(len(years))]

    # Fill array with values
    def populateArray(self):
        for i in range(len(self.years)):
            for j in range(len(self.cities)):
                # Example values: (just random demo temperatures)
                self.data[i][j] = 25 + i + j  # base 25 + offsets

    # Row-major traversal
    def rowMajorAccess(self):
        print("\nRow-Major Access:")
        for i in range(len(self.years)):
            for j in range(len(self.cities)):
                print(f"Year: {self.years[i]}, City: {self.cities[j]}, Temp: {self.data[i][j]}")

    # Column-major traversal
    def columnMajorAccess(self):
        print("\nColumn-Major Access:")
        for j in range(len(self.cities)):
            for i in range(len(self.years)):
                print(f"Year: {self.years[i]}, City: {self.cities[j]}, Temp: {self.data[i][j]}")

    # Handle sparse data 
    def handleSparseData(self):
        print("\nHandling Sparse Data:")
        for i in range(len(self.years)):
            for j in range(len(self.cities)):
                if self.data[i][j] is None:
                    self.data[i][j] = -999  # sentinel value

    
    def analyzeComplexity(self):
        print("\nComplexity Analysis:")
        print("Insert: O(1)")
        print("Delete: O(1)")
        print("Retrieve: O(1)")
        print("Space Complexity: O(n*m) where n=years, m=cities")


years = [2023, 2024, 2025]
cities = ["Delhi", "Mumbai", "Chennai"]

storage = DataStorage(years, cities)

storage.populateArray()
storage.rowMajorAccess()
storage.columnMajorAccess()
storage.handleSparseData()
storage.analyzeComplexity()
