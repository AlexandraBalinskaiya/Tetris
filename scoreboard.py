import json
import os

# Файл для збереження найкращих результатів
SCORE_FILE = 'highscore.json'

def load_highscore():
    if os.path.exists(SCORE_FILE):
        with open(SCORE_FILE, 'r') as f:
            return json.load(f)
    return 0

def save_highscore(score):
    with open(SCORE_FILE, 'w') as f:
        json.dump(score, f)

def update_highscore(score):
    highscore = load_highscore()
    if score > highscore:
        save_highscore(score)
        return score
    return highscore
