import time
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from examples.list_optimization import (
    calculate_squares_loop,
    calculate_squares_comprehension
)

def run_list_tests():
    print("Testing List Optimization:")
    print("-" * 50)
    numbers = range(1000000)

    # Test Program 1
    start_time = time.time()
    result1 = calculate_squares_loop(numbers)
    time1 = (time.time() - start_time) * 1000
    print(f"Loop approach took: {time1:.2f} ms")
    
    # Test Program 2
    start_time = time.time()
    result2 = calculate_squares_comprehension(numbers)
    time2 = (time.time() - start_time) * 1000
    print(f"Comprehension approach took: {time2:.2f} ms")
    
    # Verify Results
    print("\nTesting Correctness:")
    print("-" * 50)
    print("Both approaches give same results:", result1 == result2)
    print(f"First 5 elements: {result1[:5]}")
    print(f"Length of result: {len(result1)}")
    
    # Calculate Improvement
    improvement = ((time1 - time2) / time1) * 100
    print(f"\nImprovement: {improvement:.1f}% faster")

if __name__ == "__main__":
    run_list_tests()