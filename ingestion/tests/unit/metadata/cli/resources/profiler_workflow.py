"""
This file has been generated from dag_runner.j2
"""
from airflow import DAG
from openmetadata.workflows import workflow_factory

workflow = workflow_factory.WorkflowFactory.create(
    "/airflow/dag_generated_configs/local_redshift_profiler_e9AziRXs.json"
)
workflow.generate_dag(globals())
