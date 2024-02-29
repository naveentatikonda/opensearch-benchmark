from enum import Enum


class ClusterConfigType(str, Enum):
    CLUSTER_CONFIG = "cluster-config"
    MIXIN = "mixin"
