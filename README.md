# Parallel Pi Estimation on HPC Cluster

Monte Carlo estimation of Pi using Slurm job arrays for parallel processing.

## Project Structure
```
.
├── src/
│   ├── estimate_pi.py      # Main estimation script
│   └── aggregate_results.py # Results analysis
├── logs/                    # Slurm output logs (created automatically)
├── results/                 # JSON results (created automatically)
├── run_array.sh            # Slurm job array script
├── setup_env.sh            # Environment setup script
├── requirements.txt        # Python dependencies
└── README.md              # This file
```

## Local Development

### Test locally (optional):
```bash
# Create virtual environment
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Test single run
python src/estimate_pi.py --task-id 0 --samples 100000 --work-time 2
```

## Cluster Deployment

### 1. Clone repository on cluster:
```bash
ssh username@dta.university.country
git clone https://github.com/yourusername/pi-estimation-cluster.git
cd pi-estimation-cluster
```

### 2. Setup environment:
```bash
./setup_env.sh
```

### 3. Submit jobs:
```bash
sbatch run_array.sh
```

### 4. Monitor jobs:
```bash
squeue -u $USER
watch -n 2 squeue -u $USER  # Auto-refresh every 2 seconds
```

### 5. Analyze results:
```bash
source venv/bin/activate
python src/aggregate_results.py
```

## Configuration

### Adjust number of tasks:
Edit `run_array.sh` and change:
```bash
#SBATCH --array=0-9    # Change to 0-99 for 100 tasks
```

### Adjust samples per task:
Edit the `--samples` parameter in `run_array.sh`:
```bash
--samples 10000000    # More samples = better accuracy
```

### Adjust resources:
Edit the SBATCH directives in `run_array.sh`:
```bash
#SBATCH --mem=2G           # More memory
#SBATCH --time=01:00:00    # Longer time limit
```

## Useful Commands
```bash
# Check job status
squeue -u $USER

# Cancel jobs
scancel JOBID
scancel -u $USER  # Cancel all your jobs

# Check resource usage
seff JOBID_0

# View logs
tail -f logs/task_*_0.out

# Clean up
rm -rf results/* logs/*
```

## Expected Results

With default settings (10 tasks, 1M samples each):
- Total samples: 10,000,000
- Expected error: ~0.0001-0.001
- Runtime: ~5-10 minutes (depending on cluster load)