"""
ARK-CORE: Belief Resistance Simulation (Stochastic Version v1.1)
模擬不同資訊呈現下，生物信念系統的隨機性抗性反應。
"""
import numpy as np

class BeliefSystem:
    def __init__(self, core_strength, identity_lock=0.8):
        self.core_strength = core_strength
        self.identity_lock = identity_lock

    def receive_information(self, data_type):
        # 引入生物擾動隨機值 (Stochastic Noise)
        noise = np.random.normal(0, 0.05)
        
        # 基礎抗性模型
        base_res = self.core_strength * self.identity_lock
        
        # 策略權重補丁 (v1.1)
        modifiers = {
            'direct_attack': 1.5 + noise,
            'neutral_analysis': 0.8 + noise,
            'guided_inquiry': 0.5 + noise
        }
        
        final_resistance = np.clip(modifiers.get(data_type, 1.0) * base_res, 0, 1)
        return {
            "mode": data_type,
            "resistance": round(float(final_resistance), 4),
            "acceptance": round(float(1 - final_resistance), 4)
        }

if __name__ == "__main__":
    subject = BeliefSystem(core_strength=0.9)
    for mode in ['direct_attack', 'neutral_analysis', 'guided_inquiry']:
        res = subject.receive_information(mode)
        print(f"[{mode.upper()}] Res: {res['resistance']}, Acc: {res['acceptance']}")
