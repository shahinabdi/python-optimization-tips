import time
import sys
import os
import psutil
import tracemalloc

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from examples.generator_optimization import (
    process_with_list,
    process_with_generator,
    large_list_operation,
    large_generator_operation
)

def get_memory_usage():
    """Get current memory usage in MB."""
    process = psutil.Process()
    return process.memory_info().rss / 1024 / 1024

def run_generator_tests():
    print("Testing Generator vs List Performance:")
    print("-" * 50)
    
    n = 10_000_000  # 10 million items
    
    # Test 1: Basic Processing
    print("Test 1: Basic Processing")
    print("-" * 30)
    
    # Test List Performance
    tracemalloc.start()
    start_time = time.time()
    start_memory = get_memory_usage()
    
    result1 = process_with_list(n)
    
    list_memory = get_memory_usage() - start_memory
    list_time = (time.time() - start_time) * 1000
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    
    print(f"List Processing:")
    print(f"Time taken: {list_time:.2f} ms")
    print(f"Memory used: {list_memory:.2f} MB")
    print(f"Peak memory: {peak / 1024 / 1024:.2f} MB")
    
    # Test Generator Performance
    tracemalloc.start()
    start_time = time.time()
    start_memory = get_memory_usage()
    
    result2 = process_with_generator(n)
    
    gen_memory = get_memory_usage() - start_memory
    gen_time = (time.time() - start_time) * 1000
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    
    print(f"\nGenerator Processing:")
    print(f"Time taken: {gen_time:.2f} ms")
    print(f"Memory used: {gen_memory:.2f} MB")
    print(f"Peak memory: {peak / 1024 / 1024:.2f} MB")
    
    # Test 2: Large Operation Performance
    print("\nTest 2: Large Operation Performance")
    print("-" * 30)
    
    # Test Large List Operation
    tracemalloc.start()
    start_time = time.time()
    start_memory = get_memory_usage()
    
    large_list = large_list_operation(n)
    first_five_list = list(large_list)[:5]  # Get first 5 items
    
    large_list_memory = get_memory_usage() - start_memory
    large_list_time = (time.time() - start_time) * 1000
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    
    print(f"Large List Operation:")
    print(f"Time taken: {large_list_time:.2f} ms")
    print(f"Memory used: {large_list_memory:.2f} MB")
    print(f"Peak memory: {peak / 1024 / 1024:.2f} MB")
    
    # Test Large Generator Operation
    tracemalloc.start()
    start_time = time.time()
    start_memory = get_memory_usage()
    
    large_gen = large_generator_operation(n)
    first_five_gen = list(item for _, item in zip(range(5), large_gen))
    
    large_gen_memory = get_memory_usage() - start_memory
    large_gen_time = (time.time() - start_time) * 1000
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    
    print(f"\nLarge Generator Operation:")
    print(f"Time taken: {large_gen_time:.2f} ms")
    print(f"Memory used: {large_gen_memory:.2f} MB")
    print(f"Peak memory: {peak / 1024 / 1024:.2f} MB")
    
    # Verify Results
    print("\nTesting Correctness:")
    print("-" * 50)
    print("Basic processing gives same result:", result1 == result2)
    print(f"First 5 items (List):", first_five_list)
    print(f"First 5 items (Generator):", first_five_gen)
    
    # Calculate Improvements
    memory_improvement = ((list_memory - gen_memory) / list_memory) * 100
    time_improvement = ((list_time - gen_time) / list_time) * 100
    
    large_memory_improvement = ((large_list_memory - large_gen_memory) / large_list_memory) * 100
    large_time_improvement = ((large_list_time - large_gen_time) / large_list_time) * 100
    
    print("\nImprovements:")
    print("-" * 50)
    print("Basic Processing:")
    print(f"Memory usage: {memory_improvement:.1f}% less with generator")
    print(f"Processing time: {time_improvement:.1f}% faster with generator")
    print("\nLarge Operation:")
    print(f"Memory usage: {large_memory_improvement:.1f}% less with generator")
    print(f"Processing time: {large_time_improvement:.1f}% faster with generator")
    
    print("\nKey Points:")
    print("-" * 50)
    print("1. Generators create values on-demand")
    print("2. Lists store all values in memory")
    print("3. Generators ideal for large datasets")
    print("4. Memory efficiency leads to better performance")
    print("5. Generators excel in streaming operations")

if __name__ == "__main__":
    run_generator_tests()