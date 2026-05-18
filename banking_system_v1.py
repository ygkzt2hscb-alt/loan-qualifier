#banking system V1

def info():
    while True:
        try:
            m_income = int(input("Please enter your monthly income. $"))
            if m_income > 0:
                break
            else:
                print("Please input a value larger than 0.")
        except ValueError:
            print("Please enter a number.")
    while True:
        try:
            m_expenses = int(input("Please enter your monthly expenses. $"))
            if m_expenses >= 0:
                break
            else:
                print("Please enter a value that is larger than 0.")
        except ValueError:
            print("Please enter a number.")
    while True:
        try:
            m_debt_payments = int(input("Please enter your monthly debt payments. $"))
            if m_debt_payments >= 0:
                break
            else:
                print("Please enter a value that is larger than 0.")
        except ValueError:
            print("Please enter a number.")
    while True:
        try:
            t_savings = int(input("Please enter your total savings. $"))
            if t_savings >= 0:
                break
            else:
                print("Please enter a value that is larger than 0.")
        except ValueError:
            print("Please enter a number.")
    while True:
        try:
            m_desired_loan_p = int(input("Please enter your desired monthly loan. $"))
            if m_desired_loan_p >= 0:
                break
            else:
                print("Please enter a value that is larger than 0.")
        except ValueError:
            print("Please enter a number.")

    
    
    cash_flow = m_income - m_expenses
    savings_rate = (t_savings / m_income) * 100
    total_debt = m_debt_payments + m_desired_loan_p
    dti = (total_debt / m_income) * 100

    if dti < 36 and cash_flow > 0:
        print("Your request to loan has been approved.")
        decision = "Approved"
    elif 36 <= dti <= 43:
        print("Your request to loan has to be approved manually.")
        decision = "Needs Manual Review"
    else:
        print("Your loan has been denied.")
        decision = "Denied"

    print(f"\nFinancial Summary:",
    f"\n-----------------",
    f"\nDTI: {dti}%",
    f"\nCash flow: ${cash_flow}",
    f"\nSavings rate: {savings_rate}%"
    f"\n\nDecision: {decision}"
    )

info()