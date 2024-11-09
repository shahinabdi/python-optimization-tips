import random
import time
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from examples.lookup_optimization import (
    find_common_elements_list,
    find_common_elements_set
)

def run_lookup_tests():
    print("Testing Lookup Optimization:")
    print("-" * 50)
    
    # Generate test data
    random.seed(42)  # For reproducible results
    search_values = random.sample(range(1000000), 1000)
    
    # Test Program 1
    start_time = time.time()
    result1 = find_common_elements_list(search_values)
    time1 = (time.time() - start_time) * 1000
    print(f"List lookup took: {time1:.2f} ms")
    
    # Test Program 2
    start_time = time.time()
    result2 = find_common_elements_set(search_values)
    time2 = (time.time() - start_time) * 1000
    print(f"Set lookup took: {time2:.2f} ms")
    
    # Verify Results
    print("\nTesting Correctness:")
    print("-" * 50)
    results_match = sorted(result1) == sorted(result2)
    print("Both approaches give same results:", results_match)
    
    print("\nSample Results:")
    print(f"First 5 found values: {sorted(result1)[:5]}")
    print(f"Number of values found: {len(result1)}")
    
    # Calculate Improvement
    improvement = ((time1 - time2) / time1) * 100
    print(f"\nImprovement: {improvement:.1f}% faster")
    
    # Additional Insights
    print("\nComplexity Analysis:")
    print("-" * 50)
    print("List Lookup: O(n) - must scan entire list")
    print("Set Lookup: O(1) - constant time using hash table")
    print(f"Actual time ratio: {time1/time2:.1f}x faster with sets")

if __name__ == "__main__":
    run_lookup_tests()