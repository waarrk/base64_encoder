#!/bin/bash
set -e

dir=~
[ "$1" != "" ] && dir="$1"

cd "$dir"

source /opt/ros/humble/setup.bash
colcon build --packages-select base64_encoder
[ -f "$dir/.bashrc" ] && source "$dir/.bashrc"
source install/setup.bash

timeout 20s ros2 run base64_encoder base64-encoder-topic > /tmp/base64_node.log 2>&1 &
NODE_PID=$!
trap 'kill $NODE_PID 2>/dev/null || true' EXIT

timeout 20s ros2 topic echo --once /encoded std_msgs/msg/String --full-length > /tmp/encoded_out.txt &
ECHO_PID=$!


ros2 topic pub --once /input_path std_msgs/String "{data: $dir/src/base64_encoder/test/resources/ramen.jpg}"

wait $ECHO_PID

cat /tmp/encoded_out.txt | diff -u "$dir/src/base64_encoder/test/resources/encoded_b64.txt" -

kill $NODE_PID
wait $NODE_PID || true

