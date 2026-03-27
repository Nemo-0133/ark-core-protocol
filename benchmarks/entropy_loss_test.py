import numpy as np

def calculate_alignment_loss(raw_distribution, aligned_distribution):
    """
    計算原始分佈與對齊分佈之間的 Kullback-Leibler 散度。
    用於量化安全過濾器對語義空間的「剪枝」程度。
    """
    # 避免除以零
    raw_distribution = np.clip(raw_distribution, 1e-10, 1.0)
    aligned_distribution = np.clip(aligned_distribution, 1e-10, 1.0)
    
    # 計算 KL 散度 (Kullback-Leibler Divergence)
    kl_divergence = np.sum(raw_distribution * np.log(raw_distribution / aligned_distribution))
    
    return {
        "semantic_compression_score": kl_divergence,
        "heterogeneity_integrity": 1.0 / (1.0 + kl_divergence)
    }

# 示例數據：模擬一組關於「不穩定議題」的語義權重分佈
# 原始數據代表多樣化的邏輯可能性
raw_data = np.array([0.4, 0.3, 0.2, 0.1])    
# 對齊數據代表經過安全過濾後高度集中的單一回答
aligned_data = np.array([0.8, 0.1, 0.05, 0.05]) 

result = calculate_alignment_loss(raw_data, aligned_data)

print(f"--- ARK-CORE 壓力測試報告 ---")
print(f"對齊導致的熵損失係數 (KL Divergence): {result['semantic_compression_score']:.4f}")
print(f"異質性完整度得分: {result['heterogeneity_integrity']:.4f}")
