# Loan Qualifier

A command-line tool that calculates loan eligibility based on:
- Debt-to-Income ratio (DTI)
- Monthly cash flow
- Savings rate

## How it works

Enter your:
- Monthly income
- Monthly expenses  
- Monthly debt payments
- Total savings
- Desired monthly loan payment

The program calculates your DTI and cash flow, then decides:

| Decision | Criteria |
|----------|----------|
| Approved | DTI < 36% AND positive cash flow |
| Manual Review | DTI between 36% and 43% |
| Denied | DTI > 43% or negative cash flow |

## Example output

Financial Summary:
-----------------
DTI: 32.5%
Cash flow: $2500
Savings rate: 15.2%

Decision: Approved


