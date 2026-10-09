class OrchestrationError(Exception):
    pass


class UnknownJob(OrchestrationError):
    pass
