from dataclasses import dataclass

@dataclass(frozen=True)
class PostCreateResponse:
    name: str
    job: str
    id: str
    createdAt: str