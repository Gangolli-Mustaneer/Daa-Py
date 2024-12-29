def fractional_knapsack(capacity, weights, values):
    items = [(values[i] / weights[i], weights[i], values[i]) for i in range(len(weights))]
    items.sort(reverse=True, key=lambda x: x[0])
    
    total_value = 0
    
    for ratio, weight, value in items:
        if capacity >= weight:
            capacity -= weight
            total_value += value
        else:
            total_value += ratio * capacity
            break
    
    return total_value

weights = [10, 20, 30]
values = [60, 100, 120]
capacity = 50

max_value = fractional_knapsack(capacity, weights, values)
print(f"Maximum value in the knapsack: {max_value}")