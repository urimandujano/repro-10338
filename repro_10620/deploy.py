from prefect.deployments import Deployment

from repro_10620.flows import k8s_job_flow
from repro_10620.blocks import load_or_create_github_block, load_or_create_k8s_job

# run this first: prefect work-pool create repro-10620

deployment = Deployment.build_from_flow(
    version=1,
    flow=k8s_job_flow,
    name="repro-10620-deployment",
    work_queue_name="repo-10620-queue",
    work_pool_name="repro-10620",
    storage=load_or_create_github_block(),
    infrastructure=load_or_create_k8s_job(overwrite=True),
    apply=True,
)
deployment.apply()
