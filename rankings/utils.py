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
