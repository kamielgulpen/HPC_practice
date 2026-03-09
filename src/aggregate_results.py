#!/usr/bin/env python3
"""
Aggregate results from parallel Pi estimation runs
"""

import json
import numpy as np
import pandas as pd
from pathlib import Path

def load_results(results_dir='results'):
    """Load all result files"""
    results_path = Path(results_dir)
    results = []
    
    for result_file in sorted(results_path.glob('result_*.json')):
        with open(result_file, 'r') as f:
            result = json.load(f)
            results.append(result)
    
    return results

def analyze_results(results):
    """Analyze and display results"""
    if not results:
        print("No results found!")
        return
    
    df = pd.DataFrame(results)
    
    print("\n" + "="*60)
    print("PARALLEL PI ESTIMATION RESULTS")
    print("="*60)
    
    print(f"\nTotal tasks completed: {len(results)}")
    print(f"Total samples: {df['num_samples'].sum():,}")
    
    print(f"\n{'Task':<6} {'Pi Estimate':<12} {'Error':<12} {'Time (s)':<10}")
    print("-" * 60)
    for _, row in df.iterrows():
        print(f"{row['task_id']:<6} {row['pi_estimate']:<12.6f} {row['error']:<12.6f} {row['elapsed_time']:<10.2f}")
    
    print("\n" + "="*60)
    print("AGGREGATE STATISTICS")
    print("="*60)
    
    # Combined estimate (average of all estimates)
    combined_estimate = df['pi_estimate'].mean()
    combined_error = abs(combined_estimate - np.pi)
    
    print(f"\nCombined Pi estimate: {combined_estimate:.6f}")
    print(f"True Pi value:        {np.pi:.6f}")
    print(f"Combined error:       {combined_error:.6f}")
    print(f"\nMean error:           {df['error'].mean():.6f}")
    print(f"Std dev of estimates: {df['pi_estimate'].std():.6f}")
    print(f"Min estimate:         {df['pi_estimate'].min():.6f}")
    print(f"Max estimate:         {df['pi_estimate'].max():.6f}")
    
    print(f"\nTotal computation time: {df['elapsed_time'].sum():.2f} seconds")
    print(f"Mean time per task:     {df['elapsed_time'].mean():.2f} seconds")
    
    # Convergence
    if len(results) > 1:
        cumulative_estimates = df['pi_estimate'].expanding().mean()
        cumulative_errors = np.abs(cumulative_estimates - np.pi)
        
        print(f"\nConvergence: Error decreased from {cumulative_errors.iloc[0]:.6f} to {cumulative_errors.iloc[-1]:.6f}")
    
    return df

def main():
    print("Loading results...")
    results = load_results()
    
    if not results:
        print("No results found. Make sure jobs have completed.")
        return
    
    df = analyze_results(results)
    
    print("\n" + "="*60)
    print("Analysis complete!")
    print("="*60)

if __name__ == "__main__":
    main()
```

### Create `requirements.txt`:
```
numpy>=1.21.0
pandas>=1.3.0