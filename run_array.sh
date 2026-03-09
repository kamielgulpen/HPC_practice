#!/bin/bash
#SBATCH --job-name=practice_pi
#SBATCH --output=logs/task_%A_%a.out
#SBATCH --error=logs/task_%A_%a.err
#SBATCH --array=0-9
#SBATCH --time=00:10:00
#SBATCH --mem=1G
#SBATCH --cpus-per-task=1

# Print job info
echo "=========================================="
echo "Job ID: $SLURM_JOB_ID"
echo "Array Task ID: $SLURM_ARRAY_TASK_ID"
echo "Running on node: $(hostname)"
echo "Starting at: $(date)"
echo "=========================================="

# Load Python module (adjust version if needed)
module load python/3.9

# Activate virtual environment
source venv/bin/activate

# Run the Python script
python src/estimate_pi.py \
    --task-id $SLURM_ARRAY_TASK_ID \
    --samples 1000000 \
    --work-time 5 \
    --output-dir results

# Check exit status
EXIT_CODE=$?
echo "=========================================="
echo "Task completed with exit code: $EXIT_CODE"
echo "Finished at: $(date)"
echo "=========================================="

exit $EXIT_CODE