# =========================
# file: rules.py
# =========================

from experta import Rule
from facts import Symptom


# Hardware Rules
class HardwareRules:

    @Rule(Symptom(power="no"))
    def no_power(self):
        print("\n🔌 No power detected.")
        print("💡 Check power cable or battery.")


    @Rule(Symptom(power="yes", display="no"))
    def no_display(self):
        print("\n🖥️ Display issue detected.")
        print("💡 Check monitor or graphics card.")


# Performance Rules
class PerformanceRules:

    @Rule(Symptom(power="yes", display="yes", slow="yes"))
    def slow_pc(self):
        print("\n🐌 Computer is slow.")
        print("💡 Close apps or upgrade RAM.")


# Network Rules
class NetworkRules:

    @Rule(Symptom(power="yes", display="yes", internet="no"))
    def no_internet(self):
        print("\n🌐 Internet problem detected.")
        print("💡 Restart router or reconnect Wi-Fi.")
# Safe Rules
class SafeRules:

    @Rule(Symptom(power="yes", display="yes", slow="no", internet="yes"))
    def no_problem(self):
        print("\n✅ No problem detected.")
