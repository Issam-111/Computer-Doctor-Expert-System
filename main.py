import collections
import collections.abc

# Python 3.10+ Fix
collections.Mapping = collections.abc.Mapping
collections.MutableMapping = collections.abc.MutableMapping

from experta import KnowledgeEngine, Fact, DefFacts

from facts import Symptom

from Rules import (
    HardwareRules,
    PerformanceRules,
    NetworkRules,
    SafeRules
)


# Main Engine
class ComputerDoctor(
    HardwareRules,
    PerformanceRules,
    NetworkRules,
    SafeRules,
    KnowledgeEngine
):

    @DefFacts()
    def startup(self):
        yield Fact(action="diagnose")


# --- Run System ---
engine = ComputerDoctor()
engine.reset()

power = input("Does the computer turn on? (yes/no): ").lower()

if power == "yes":

    display = input("Is the display working? (yes/no): ").lower()

    if display == "yes":

        slow = input("Is the computer slow? (yes/no): ").lower()
        internet = input("Does internet work? (yes/no): ").lower()

        engine.declare(
            Symptom(
                power=power,
                display=display,
                slow=slow,
                internet=internet
            )
        )

    else:

        engine.declare(
            Symptom(
                power=power,
                display=display
            )
        )

else:

    engine.declare(
        Symptom(power=power)
    )

engine.run()