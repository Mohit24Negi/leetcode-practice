import pandas as pd

def order_scores(scores: pd.DataFrame) -> pd.DataFrame:
    scores["rank"] = scores["score"].rank(method= "dense", ascending= False)
    scores.drop(columns= "id", inplace= True)
    return scores.sort_values(by="score", ascending= False)