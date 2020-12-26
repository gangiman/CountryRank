import pandas as pd
from sklearn import preprocessing

class IndividualRanking:
    """
    Abstract class for individual ranking
    """

    @property
    def higher_is_better(self):
        """

        :return: bool
        """
        return NotImplementedError()

    def get_ranking(self):
        raise NotImplementedError()

    def get_norm_ranking(self) -> pd.Series:
        ranking = self.get_ranking()
        # normalazing ranking
        # as.numpy(ranking)
        min_max_scaler = preprocessing.MinMaxScaler()
        x_scaled = min_max_scaler.fit_transform(ranking.to_numpy().reshape(1,-1))
        return pd.Series(x_scaled[0], index=ranking.index)
