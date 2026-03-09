#!/usr/bin/env python3
"""
Estimate Pi using Monte Carlo method
Each run uses different random seed for parallel execution
"""

import argparse
import numpy as np
import time
import json
from pathlib import Path

def estimate_pi(num_samples, seed=None):
    """
    Estimate Pi by throwing random darts at a square
    
    Args:
        num_samples: Number of random points to generate
        seed: Random seed for reproducibility
    
    Returns:
        dict with results
    """
    if seed is not None:
        np.random.seed(seed)
    
    # Generate random points in unit square [0,1] x [0,1]
    x = np.random.uniform(0, 1, num_samples)
    y = np.random.uniform(0, 1, num_samples)
    
    # Check if points fall inside quarter circle
    distances = x**2 + y**2
    inside_circle = np.sum(distances <= 1.0)
    
    # Pi ≈ 4 * (points inside circle / total points)
    pi_estimate = 4.0 * inside_circle / num_samples
    
    return {
        'pi_estimate': float(pi_estimate),
        'num_samples': num_samples,
        'inside_circle': int(inside_circle),
        'error': abs(pi_estimate - np.pi),
        'seed': seed
    }

def simulate_work(duration=1):
    """Simulate some computational work"""
    time.sleep(duration)

def main():
    parser = argparse.ArgumentParser(description='Estimate Pi using Monte Carlo')
    parser.add_argument('--task-id', type=int, required=True,
                       help='Task ID (used as seed)')
    parser.add_argument('--samples', type=int, default=1000000,
                       help='Number of samples to generate')
    parser.add_argument('--work-time', type=int, default=5,
                       help='Seconds of simulated work')
    parser.add_argument('--output-dir', type=str, default='results',
                       help='Output directory for results')
    
    args = parser.parse_args()
    
    print(f"Starting Task {args.task_id}")
    print(f"Using {args.samples:,} samples")
    print(f"Random seed: {args.task_id}")
    
    # Run estimation
    start_time = time.time()
    result = estimate_pi(args.samples, seed=args.task_id)
    
    # Simulate some computational work
    print(f"Simulating {args.work_time} seconds of work...")
    simulate_work(args.work_time)
    
    elapsed = time.time() - start_time
    result['elapsed_time'] = elapsed
    result['task_id'] = args.task_id
    
    # Print results
    print(f"\nResults for Task {args.task_id}:")
    print(f"  Pi estimate: {result['pi_estimate']:.6f}")
    print(f"  True Pi:     {np.pi:.6f}")
    print(f"  Error:       {result['error']:.6f}")
    print(f"  Time:        {elapsed:.2f} seconds")
    
    # Save results
    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)
    
    output_file = output_dir / f'result_{args.task_id:03d}.json'
    with open(output_file, 'w') as f:
        json.dump(result, f, indent=2)
    
    print(f"\nResults saved to {output_file}")
    print(f"Task {args.task_id} completed!")

if __name__ == "__main__":
    main()