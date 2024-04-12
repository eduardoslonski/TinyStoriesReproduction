from dataclasses import dataclass

@dataclass
class GPTConfig():
    vocab_size: int
    context_length: int = 512
    n_embed: int = 512
    n_heads: int = 4
    n_layers: int = 8
    lr: float = 6e-4
    batch_size: int = 128
    batch_size_val: int = 128
    device: str = "cuda"
    n_epochs: int = 1
    eval_every: int = 1_000
    checkpoint_every: int = 1_000