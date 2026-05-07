import pandas as pd

def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
    salaries = employee["salary"].sort_values(ascending= False ).unique()
    df = pd.DataFrame()
    df["SecondHighestSalary"] = [salaries[1] if len(salaries) > 1 else np.nan]
    return df