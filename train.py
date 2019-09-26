import autocomplete
from autocomplete import models

with open('one_year_subject_lines.txt', 'r') as file:
    data = file.read().replace('\n', '')
models.train_models(data)

