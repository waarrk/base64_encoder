# SPDX-FileCopyrightText: 2025 Yusaku Washio <s22c1704za@s.chibakoudai.jp>
# SPDX-License-Identifier: BSD-3-Clause

from __future__ import annotations

from typing import Optional

import rclpy
from rclpy.node import Node
from rclpy.qos import QoSProfile
from std_msgs.msg import String

from . import encode


class PathToBase64Node(Node):
    def __init__(self) -> None:
        super().__init__('base64_encoder_topic')

        qos = QoSProfile(depth=1)
        self._pub = self.create_publisher(String, 'encoded', qos)
        self.create_subscription(String, 'input_path', self._on_path, qos)

        self.get_logger().info('Ready')

    def _on_path(self, msg: String) -> None:
        path = msg.data.strip()
        if not path:
            self.get_logger().warn('Empty path')
            return
        try:
            with open(path, 'rb') as handle:
                data = handle.read()
        except OSError as exc:
            self.get_logger().error(f'Failed to read {path}: {exc}')
            return

        encoded = encode(data)
        self._pub.publish(String(data=encoded))
        self.get_logger().info(f'Published Base64 {path}')


def main(args: Optional[list[str]] = None) -> None:
    rclpy.init(args=args)
    node: Optional[PathToBase64Node] = None
    try:
        node = PathToBase64Node()
        rclpy.spin(node)
    finally:
        if node is not None:
            node.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()
