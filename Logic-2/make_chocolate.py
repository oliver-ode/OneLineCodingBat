def make_chocolate(small, big, goal):
    return (goal-big*5 if goal>=big*5 else goal%5) if (goal-big*5 if goal>=big*5 else goal%5) <= small else -1