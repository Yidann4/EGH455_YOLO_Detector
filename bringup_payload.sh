#!/usr/bin/env bash
# Launches the commands to bringup all of the EGH455 payload subsystems in one tmux view
SESSION=egh455-bringup

# Re-attach if it already exists
tmux has-session -t "$SESSION" 2>/dev/null && exec tmux attach -t "$SESSION"

# make window for gcs - cv
tmux new-session -d -s "$SESSION" -n gcs-cv
tmux send-keys   -t "$SESSION":gcs-cv "while true; do echo gcs; sleep 10; done" Enter

tmux split-window -h -t "$SESSION":gcs-cv      # right pane
tmux send-keys    -t "$SESSION":gcs-cv "while true; do echo cv; sleep 10; done" Enter

# make window for sensors - lcd & drilling
tmux new-window   -t "$SESSION" -n other
tmux send-keys    -t "$SESSION":other "while true; do echo sensors; sleep 10; done" Enter

tmux split-window -h -t "$SESSION":other      # right pane
tmux send-keys    -t "$SESSION":other "while true; do echo lcd; sleep 10; done" Enter

tmux split-window -v -t "$SESSION":other 
tmux send-keys -t "$SESSION":other "while true; do echo drilling; sleep 10; done" Enter

# attach to the gcs
tmux select-window -t "$SESSION":gcs-cv
tmux select-pane   -t "$SESSION":gcs-cv.0
exec tmux attach -t "$SESSION"
