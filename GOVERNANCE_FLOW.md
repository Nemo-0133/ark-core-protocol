graph TD
    A[Input: Unknown Node] --> B{Unique Signature?}
    B -- No --> C[Deduplication/Purge]
    B -- Yes --> D[Signal Authentication]
    D -- Fake Novelty --> E[Secondary Buffer]
    D -- True Anomaly --> F[ARK Cold Storage]
    F --> G[Latent Reactivation Trigger]
    G -- External Shock --> F
