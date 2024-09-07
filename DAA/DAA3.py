class Item:
    def __init__(self, profit, weight):
        self.profit = profit
        self.weight = weight

def fractionalKnapsack(W, arr):
    # Sorting array on basis of profit/weight ratio in descending order
    arr.sort(key=lambda x: (x.profit / x.weight), reverse=True)
    
    # Result value in Knapsack
    final_value = 0.0
    
    for item in arr:
        if item.weight <= W:
            # Take the whole item
            W -= item.weight
            final_value += item.profit
        else:
            # Take the fraction of the remaining item
            final_value += item.profit * W / item.weight
            break
    
    return final_value

if __name__ == "__main__":
    W = 50
    arr = [Item(60, 10), Item(100, 20), Item(120, 30)]
    
    # Function call
    max_val = fractionalKnapsack(W, arr)
    print(f"Maximum value in Knapsack: {max_val}")
