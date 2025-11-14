#!/bin/bash
# Profiling script for HRM model
# Runs with minimal epochs and batch size for performance profiling

set -e

echo "Starting HRM Profiling Pipeline..."
echo "=================================="

# Clean up any existing profile files
echo "Cleaning up old profile files..."
rm -f trace.json profile.prof *.lprof

# Run profiling with line profiler
echo "Running profiling with line profiler..."
uv run kernprof -l profiling.py

# Run normal profiling (generates trace.json and profile.prof)
echo "Running standard profiling..."
uv run python profiling.py

# Analyze results
echo "Profiling complete! Results:"
echo "- CPU profile: profile.prof"
echo "- GPU profile: trace.json"
echo "- Line profile: profile.py.lprof"
echo ""
echo "To view results:"
echo "  CPU: uv run snakeviz profile.prof"
echo "  GPU: Open trace.json in chrome://tracing"
echo "  Line: uv run python -m line_profiler profile.py.lprof"