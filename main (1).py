data_set = None

def split_data_set(type, dataset):
    """Take a data set and split it up into different combinations of metrics to test which works best."""
    if type == "news":
        if isinstance(dataset, dict):
            print("Dictionary detected (likely JSON data)")
        else:
            print("Dataset is not a dictionary")
        # need to clean data to have these combinations:
        # 1.) headline and ranking
        # 2.) headline, ranking, and source
        # 3.) headline, ranking, and author
        # 4.) headline, ranking, and date
        # 5.) headline, ranking, and description
        # 6.) headline, ranking, source, and author
        # 7.) headline, ranking, source, and date
        # 8.) headline, ranking, source, and description
        # 8.) headline, ranking, author, and date
        # 9.) headline, ranking, author, and description
        # 10.) headline, ranking, date, and description
        # 11.) headline, ranking, source, author, and date
        # 12.) headline, ranking, source, author and description
        # 13.) headline, ranking, source, date, and description
        # 14.) headline, ranking, author, date, and description
        # 15.) headline, ranking, source, author, date, and description
        return dataset # temporary. need to change once the real variable exists.


def prepare_models(type, data):
    """Builds models using various ML libraries to compare results."""
    pass