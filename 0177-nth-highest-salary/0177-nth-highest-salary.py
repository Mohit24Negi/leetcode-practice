import pandas as pd

def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:
    salaries = employee["salary"].sort_values(ascending= False).unique()
    df = pd.DataFrame(
        {f"getNthHighestSalary({N})" : [salaries[N-1] if N > 0 and len(salaries) >= N else np.nan]}
    )
    
    return df
