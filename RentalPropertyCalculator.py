class RentalPropertyCalculator:
    def __init__(self, monthly_rent_small, monthly_rent_medium, monthly_rent_large, monthly_rent_delux, laundry_mat, storage, 
                boat_slip, covered_parking, num_small_units, num_medium_units, num_large_units, num_delux_units, num_storage,
                num_boat_slip, num_covered_parking,
                mortgage, taxes, insurance, electric, water, sewer, gas, garbage, gate_guard, 
                hoa_board, lawn_ground_maintenance,
                property_manager, repair_fund, vacancy, capex,
                purchase_price, holding_period):
        # rent from Incomes
        self.monthly_rent_small = monthly_rent_small
        self.monthly_rent_medium = monthly_rent_medium
        self.monthly_rent_large = monthly_rent_large
        self.monthly_rent_delux = monthly_rent_delux
        self.laundry_mat = laundry_mat
        self.storage = storage
        self.boat_slip = boat_slip
        self.covered_parking = covered_parking
        # number of units or conveniences
        self.num_small_units = num_small_units
        self.num_medium_units = num_medium_units
        self.num_large_units = num_large_units
        self.num_delux_units = num_delux_units
        self.num_storage_units = num_storage  # Corrected attribute name
        self.num_boat_slip = num_boat_slip
        self.num_covered_parking = num_covered_parking
        # expenses
        self.mortgage = mortgage
        self.taxes = taxes
        self.insurance = insurance
        self.electric = electric
        self.water = water
        self.sewer = sewer
        self.gas = gas
        self.garbage = garbage
        self.gate_guard = gate_guard
        self.hoa_board = hoa_board
        self.lawn_ground_maintenance = lawn_ground_maintenance
        # expenses client security 
        self.property_manager = property_manager  # 10% of rent
        self.repair_fund = repair_fund  # tenant broke things recommend $50-$100 a month per unit
        self.vacancy = vacancy  # 5% of rental income
        self.capex = capex  # replacing things fund recommend $100 a month for each unit

        self.holding_period = holding_period
        self.purchase_price = purchase_price
    # box 1
    def income_details(self):
        # number of things
        self.num_small_units = int(input("Enter the number of small units: "))
        self.num_medium_units = int(input("Enter the number of medium units: "))
        self.num_large_units = int(input("Enter the number of large units: "))
        self.num_delux_units = int(input("Enter the number of deluxe units: "))
        self.num_storage_units = int(input("Enter the number of storage units: "))  # Corrected attribute name
        self.num_boat_slip = int(input("Enter the number of boat slips: "))
        self.num_covered_parking = int(input("Enter the number of covered parking spaces: "))
        # rent on those things
        self.monthly_rent_small = float(input("Enter monthly rent for small units: "))
        self.monthly_rent_medium = float(input("Enter monthly rent for medium units: "))
        self.monthly_rent_large = float(input("Enter monthly rent for large units: "))
        self.monthly_rent_delux = float(input("Enter monthly rent for deluxe units: "))
        self.storage = float(input("Enter monthly rent for storage units: "))
        self.boat_slip = float(input("Enter monthly rent for boat slip: "))
        self.covered_parking = float(input("Enter monthly rent for covered parking space: "))

    def calculate_total_income(self):
        # Calculate total income based on the number of units or conveniences and their monthly rents
        total_income = (
            self.num_small_units * self.monthly_rent_small +
            self.num_medium_units * self.monthly_rent_medium +
            self.num_large_units * self.monthly_rent_large +
            self.num_delux_units * self.monthly_rent_delux +
            self.num_storage_units * self.storage +  # Corrected attribute name
            self.num_boat_slip * self.boat_slip +
            self.num_covered_parking * self.covered_parking
        )
        return total_income
    # box 2
    def input_expenses(self):
        # Gather input for various expense fields
        self.mortgage = self.get_input("Enter mortgage: ")
        self.taxes = self.get_input("Enter taxes: ")
        self.insurance = self.get_input("Enter insurance: ")
        self.electric = self.get_input("Enter electric: ")
        self.water = self.get_input("Enter water expense: ")
        self.sewer = self.get_input("Enter sewer expense: ")
        self.gas = self.get_input("Enter gas expense: ")
        self.garbage = self.get_input("Enter garbage expense: ")
        self.gate_guard = self.get_input("Enter gate guard expense: ")
        self.hoa_board = self.get_input("Enter HOA board expense: ")
        self.lawn_ground_maintenance = self.get_input("Enter lawn/ground maintenance expense: ")

    def skip_expenses(self):
        # Allow users to skip input for various expense fields
        skip_mortgage = input("Skip mortgage expense? (yes/no): ").lower() == 'yes'
        if not skip_mortgage:
            self.mortgage = self.get_input("Enter mortgage: ")

        skip_gas = input("Skip gas expense? (yes/no): ").lower() == 'yes'
        if not skip_gas:
            self.gas = self.get_input("Enter gas expense: ")

        skip_gate_guard = input("Skip gate guard expense? (yes/no): ").lower() == 'yes'
        if not skip_gate_guard:
            self.gate_guard = self.get_input("Enter gate guard expense: ")

        skip_hoa_board = input("Skip HOA board expense? (yes/no): ").lower() == 'yes'
        if not skip_hoa_board:
            self.hoa_board = self.get_input("Enter HOA board expense: ")

        skip_lawn_ground_maintenance = input("Skip lawn/ground maintenance expense? (yes/no): ").lower() == 'yes'
        if not skip_lawn_ground_maintenance:
            self.lawn_ground_maintenance = self.get_input("Enter lawn/ground maintenance expense: ")

    def get_input(self, prompt, multiplier=None):
        # Helper function to get input with validation
        while True:
            try:
                value = float(input(prompt))
                if multiplier is not None:
                    value *= multiplier  # Apply the multiplier if provided
                return value
            except ValueError:
                print("Invalid input. Please enter a valid number.")

    def input_security_expenses(self):
        # Gather input for property management, repair fund, vacancy, and capex
        self.property_manager = self.get_input("Enter property manager expense (10% of rent recommended): ", multiplier=0.1)
        self.repair_fund = self.get_input("Enter repair fund expense (per unit $50 - $100 a month): ")
        self.vacancy = self.get_input("Enter vacancy expense (5% of rental income recommended): ", multiplier=0.05)
        self.capex = self.get_input("Enter capital expenditures expense (per unit recommend $100 a month): ")

    def skip_security_expenses(self):
        # Allow users to skip input for property management, repair fund, vacancy, and capex
        skip_property_manager = input("Skip property manager expense? (yes/no): ").lower() == 'yes'
        if not skip_property_manager:
            self.property_manager = self.get_input("Enter property manager expense (10% of rent): ", multiplier=0.1)

        skip_repair_fund = input("Skip repair fund expense? (yes/no): ").lower() == 'yes'
        if not skip_repair_fund:
            self.repair_fund = self.get_input("Enter repair fund expense (per unit): ")

        skip_vacancy = input("Skip vacancy expense? (yes/no): ").lower() == 'yes'
        if not skip_vacancy:
            self.vacancy = self.get_input("Enter vacancy expense (5% of rental income): ", multiplier=0.05)

        skip_capex = input("Skip capital expenditures expense? (yes/no): ").lower() == 'yes'
        if not skip_capex:
            self.capex = self.get_input("Enter capital expenditures expense (per unit): ")

    def calculate_total_expenses_group1(self):
    # Calculate total expenses for the first group
        total_expenses_group1 = (
        self.mortgage +
        self.taxes +
        self.insurance +
        self.electric +
        self.water +
        self.sewer +
        self.gas +
        self.garbage +
        self.gate_guard +
        self.hoa_board +
        self.lawn_ground_maintenance
        )
        return total_expenses_group1
    
    def calculate_total_security_expenses(self):
    # Calculate total security expenses
        total_security_expenses = (
        self.property_manager +
        self.repair_fund +
        self.vacancy +
        self.capex
        )
        return total_security_expenses

    def calculate_total_expenses(self):
        # Calculate total expenses by adding expenses from both groups
        total_expenses = (
            self.calculate_total_expenses_group1() +
            self.calculate_total_security_expenses()
        )
        return total_expenses
    # box 3
    def calculate_cash_flow(self):
        # Calculate cash flow by subtracting total expenses from total income
        total_income = self.calculate_total_income()
        total_expenses = self.calculate_total_expenses()
        cash_flow = total_income - total_expenses
        return cash_flow
    # box 4
    def input_investment_details(self):
        # Gather input for property details
        self.down_payment = self.get_input("Enter down payment or purchase price: ")
        self.closing_costs = self.get_input("Enter closing costs: ")
        self.rehab_budget = self.get_input("Enter rehab budget: ")
        self.appraisal = self.get_input("Enter appraisal cost: ")
        self.inspection = self.get_input("Enter inspection cost: ")

    def calculate_total_investment(self):
        # cal total investment
        total_investment = (
            self.down_payment +
            self.closing_costs +
            self.rehab_budget +
            self.appraisal +
            self.inspection
        )
        return total_investment
    
    def calculate_roi(self):
    # Calculate Return on Investment (ROI)
        cash_flow = self.calculate_cash_flow()
        total_investment = self.calculate_total_investment()

        if total_investment == 0:
            return "Cannot calculate ROI with zero total investment."

        roi = (cash_flow / total_investment) * 100
        return roi

    def print_investment_summary(self):
        total_income = self.calculate_total_income()
        total_expenses = self.calculate_total_expenses()
        total_investment = self.calculate_total_investment()
        roi = self.calculate_roi()

        print(f"\nTotal Income: ${total_income:.2f}")
        print(f"Total Expenses: ${total_expenses:.2f}")
        print(f"Total Investment: ${total_investment:.2f}")
        print(f"ROI: {roi:.2f}%")

        if roi > 7:
            print("This is a good investment.")
        elif 3 <= roi <= 7:
            print("This is an average investment.")
        else:
            print("This is a bad investment.")

    # Create an instance
calculator = RentalPropertyCalculator(
    monthly_rent_small=0, monthly_rent_medium=0, monthly_rent_large=0, monthly_rent_delux=0,
    laundry_mat=0, storage=0, boat_slip=0, covered_parking=0,
    num_small_units=0, num_medium_units=0, num_large_units=0, num_delux_units=0,
    num_storage=0, num_boat_slip=0, num_covered_parking=0,
    mortgage=0, taxes=0, insurance=0, electric=0, water=0, sewer=0, gas=0, garbage=0,
    gate_guard=0, hoa_board=0, lawn_ground_maintenance=0,
    property_manager=0, repair_fund=0, vacancy=0, capex=0,
    purchase_price=0, holding_period=0
)

# Input details
calculator.income_details()
calculator.input_expenses()
calculator.input_security_expenses()
calculator.input_investment_details()

# Calculate and print the summary
calculator.print_investment_summary()
