data_set = None
split_config = 15 # the range of options for data configurations of the test data set. will need to supercharge this later to be more flexible.

def split_data_set(type, configs, dataset):
    """Take a data set and split it up into different combinations of metrics to test which works best."""
    
    # Need to figure out how to test this all effectively and to iterate through it efficiently.
    # Most likely going to have some sort of weird case thing or lit lambda function?
    # May need to be supercharged with ML to handle multimodal data, more use cases, and superparameter optmization enhancement.
    
    if type == "news":
        if isinstance(dataset, dict):
            print("Dictionary detected (likely JSON data)")
            for i in range(configs):
                print(i)
                # Need to create a dictionary of data set rows that represents all the combinations.
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