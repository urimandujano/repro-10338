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


def load_or_create_k8s_job(name: str = "urimandujano-repro-10620") -> KubernetesJob:
    try:
        job = KubernetesJob.load(name)
    except ValueError:
        print("Creating new Kubernetes block")
        job = KubernetesJob()
        job.save(name)
    return job
