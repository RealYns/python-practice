def make_sandwich(*items):
    for item in items:
        print("-" + item.title())

make_sandwich('cheese', 'ham', 'eggs', 'lettuce', 'mustard')