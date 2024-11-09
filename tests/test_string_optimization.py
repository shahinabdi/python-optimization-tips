import time
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from examples.string_optimization import (
    concatenate_with_plus,
    concatenate_with_join,
    concatenate_with_fstring,
    concatenate_with_format
)

def run_string_tests():
    print("Testing String Concatenation Methods:")
    print("-" * 50)
    
    # Test data
    items = list(range(10000))
    
    # Test concatenation with +
    start_time = time.time()
    result1 = concatenate_with_plus(items)
    time1 = (time.time() - start_time) * 1000
    print(f"+ operator took: {time1:.2f} ms")
    
    # Test concatenation with join
    start_time = time.time()
    result2 = concatenate_with_join(items)
    time2 = (time.time() - start_time) * 1000
    print(f"join() method took: {time2:.2f} ms")
    
    # Test concatenation with f-string
    start_time = time.time()
    result3 = concatenate_with_fstring(items)
    time3 = (time.time() - start_time) * 1000
    print(f"f-string took: {time3:.2f} ms")
    
    # Test concatenation with format
    start_time = time.time()
    result4 = concatenate_with_format(items)
    time4 = (time.time() - start_time) * 1000
    print(f".format() took: {time4:.2f} ms")
    
    # Verify Results
    print("\nTesting Correctness:")
    print("-" * 50)
    all_same = (result1 == result2 == result3 == result4)
    print("All methods produce the same result:", all_same)
    print(f"\nSample output (first 50 chars):\n{result1[:50]}...")
    
    # Calculate Improvements
    base_time = time1  # Using + operator as baseline
    print("\nPerformance Improvements:")
    print("-" * 50)
    print(f"join() method: {((base_time - time2) / base_time) * 100:.1f}% faster")
    print(f"f-string: {((base_time - time3) / base_time) * 100:.1f}% faster")
    print(f"format(): {((base_time - time4) / base_time) * 100:.1f}% faster")
    
    # Memory Usage Note
    print("\nMemory Usage Note:")
    print("-" * 50)
    print("+ operator creates new string objects in each iteration")
    print("join() method allocates memory once")
    print("Both f-string and format() methods are optimized for string formatting")

if __name__ == "__main__":
    run_string_tests()