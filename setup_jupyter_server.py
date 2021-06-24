# Import OS and Spark Dependencies
import os, posixpath, socket
from pyspark import SparkConf, SparkContext


# General Settings
SPARK_EXECIMAGE = 'code.oak-tree.tech:5005/courseware/oak-tree/dataops-examples/spark245-k8s-minio-base'
K8S_SERVICEACCOUNT = 'spark-driver'
K8S_NAMESPACE = 'jupyterhub'
SPARK_EXECUTORS = 2
    

# Set python versions explicitly using the PySpark environment variables
# to prevent the executors from using the wrong version of Pytho9
os.environ['PYSPARK_PYTHON'] = 'python3'
os.environ['PYSPARK_DRIVER_PYTHON'] = 'python3'

# Spark Configuration
conf = SparkConf()

# Set Spark Master to the local Kubernetes Driver
conf.setMaster('k8s://https://kubernetes.default.svc')

# Configure executor image and runtime options
conf.set('spark.kubernetes.container.image', SPARK_EXECIMAGE)
conf.set("spark.kubernetes.authenticate.driver.serviceAccountName", K8S_SERVICEACCOUNT) 
conf.set("spark.kubernetes.namespace", K8S_NAMESPACE)

# Spark on K8s works ONLY in client mode (driver runs on client)
conf.set('spark.submit.deployMode', 'client')

# Executor instances and settings
conf.set('spark.executor.instances', SPARK_EXECUTORS)

# Application Name
conf.setAppName('sparkui-k8s-example')

# Set IP of driver. This is always the user pod. The socket methods
# dynamically fetch the IP address.
conf.set('spark.driver.host', socket.gethostbyname(socket.gethostname()))
