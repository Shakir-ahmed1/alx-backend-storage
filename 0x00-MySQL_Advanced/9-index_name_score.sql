-- indexing using names and it's first letter and score
CREATE INDEX idx_name_first_score ON names (name(1), score);
