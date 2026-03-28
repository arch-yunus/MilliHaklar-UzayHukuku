import time
import random

class SSADetectionEngine:
    """
    Uzay Durumsal Farkndalk (SSA) ve Hukuki ihlal Tespit Motoru - POC
    """
    def __init__(self, satellite_name, protected_coords):
        self.satellite_name = satellite_name
        self.protected_coords = protected_coords # (Lat, Lon)
        self.legal_db = {
            "proximity_infringement": "Liability Convention 1972 - Article II",
            "frequency_jamming": "ITU Radio Regulations - Article 15",
            "unauthorized_observation": "National Space Law - Article 5"
        }

    def monitor_orbit(self, intruder_name, intruder_coords, signal_strength):
        print(f"\n[MONITORING] {intruder_name} yaklayor...")
        
        # Basit mesafe hesaplama (Örnekleme)
        distance = self._calculate_distance(self.protected_coords, intruder_coords)
        
        if distance < 50: # 50km alt kritik eik
            self.trigger_legal_alert("proximity_infringement", intruder_name, distance)
            
        if signal_strength < 15: # Jamming tespiti
            self.trigger_legal_alert("frequency_jamming", intruder_name, f"SNR: {signal_strength}dB")

    def _calculate_distance(self, c1, c2):
        # Basit Öklid uzakl (Demo amaldr)
        return ((c1[0]-c2[0])**2 + (c1[1]-c2[1])**2)**0.5

    def trigger_legal_alert(self, violation_type, actor, detail):
        treaty = self.legal_db.get(violation_type, "Unknown Treaty")
        print("!" * 50)
        print(f"HUKUKi iHLAL TESPit EDiLDi!")
        print(f"Varlk: {self.satellite_name}")
        print(f"ihlal Tr: {violation_type.upper()}")
        print(f"Aktör: {actor}")
        print(f"Detay: {detail}")
        print(f"Dayanak: {treaty}")
        print("!" * 50)

if __name__ == "__main__":
    print("--- Milli Uzay Haklar Kalkan SSA Simulator Balatlyor ---")
    turksat_shield = SSADetectionEngine("TURKSAT-6A", (31.0, 42.0))
    
    # Simüle edilmi veriler
    scenarios = [
        ("Unknown_SAT_X", (31.1, 42.1), 20), # Yaknlama ihlali
        ("Jammer_Station_Z", (35.0, 45.0), 5), # Jamming ihlali
    ]
    
    for actor, coords, snr in scenarios:
        turksat_shield.monitor_orbit(actor, coords, snr)
        time.sleep(1)
