from prefect.infrastructure.kubernetes import KubernetesJob


from prefect.filesystems import GitHub


def load_or_create_github_block(name: str = "urimandujano-repro-10620") -> GitHub:
    try:
        block = GitHub.load(name)
    except ValueError:
        print("Creating new Github block")
        block = GitHub(repository="https://github.com/urimandujano/repro-10620")
        block.save(name)
    return block


def load_or_create_k8s_job(
    name: str = "urimandujano-repro-10620", overwrite: bool = False
) -> KubernetesJob:
    try:
        job: KubernetesJob | None = KubernetesJob.load(name)
    except ValueError:
        job = None

    if overwrite or job is None:
        print("Creating new Kubernetes block")
        job = KubernetesJob(
            namespace="default-mem-example", image="prefecthq/prefect:2.11-python3.8"
        )
        job.save(name, overwrite=True)

    return job
