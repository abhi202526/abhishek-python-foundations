# Chapter 1: Core System Diagnostics Matrix

def check_system_nodes(cpu_temperature: int, drive_status: str):
    print("--- INTIATING HARDWARE SECURITY EVALUATION ---")

    # 1. Logic Check matching video 3 (The CPU Cooler reality)
    if cpu_temperature > 90:
        return " CRITICAL ERROR: CPU Overheating! Thermal throttling initiated to prevent chip meltdown."
        
    # 2. Storage Check matching video 4 (The Hard Drive state)
    if drive_status != "ACITVE":
        return "HARDWARE FAULT: Storage platter disk failure detected. Core memory unreadable."
    
    return "SYSTEM OPTIMIZED: Hardware nodes running within secure parameters."

# Test your hardware rules
diagnostic_report = check_system_nodes(95, "ACTIVE")
print(diagnostic_report)