data_filename = 'data.csv'
num_of_steps = 3
report_template = """Report
We have made {observations_count} observations from tossing a coin:
{tails_count} of them were tails, and {heads_count} of them were heads.
The probabilities are {tails_chance:.2f}% and {heads_chance:.2f}%, respectively.
Our forecast is that in the next {num_of_steps} observations we will have: {tails_pred} and {heads_pred}.
"""