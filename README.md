# AI
Repo for providing public access to AI tools and services.


NEED TO REMOVE FUNCTIONS THAT AREN'T ABSOLUTELY REQUIRED/STANDARD
WILL HAVE TO DEEP DIVE EVERY SINGLE FUNCTION/DESIGN UNTIL WE GET IT RIGHT.

File Guide:

hivemind.py
- Central brain for data collection/processing
- The robots themselves should be kept fairly weak so they don't go rogue
- Worried about single point of failure risk, but we can probably compartmentalize, or even create internal adversaries... like a group of advisors

Core/core.py
- Emergency Shut Off for safety purposes.
- Status Check for data, longevity, and safety.
- Environmental sensing for gathering data and productivity.
- Wireless Networking for data and productivity.
- Recharging/ Service for longevity/ productivity.
- Owner checks for safety/fairness.
- On/Off/Restart for longevity/productivity.
- Update for future proofing/ longevity/ productivity.

constructor_protocol.py
Coming soon...

EMERGENCY SAFETY CONCERNS:

# Note: may need to use smart contract functionality to ensure some kind of immutable state for this. OR potentially some governance structure.
# Abort conditions:
# 1.) temperature anomaly (electrical fire/ etc) Reason: minimize chance of fire/damage. Other mitigation: onboard firefighting capabilities.
# 2.) AWOL protocol (AI somehow becomes self aware/ damaging) Reason: minimize chance of human loss. Other mitigation: protocols for network, etc.
# 3.) Low power (power source depleted/malfunction) Reason: minimize money loss/ accidents due to poor timing.
# 4.) Lost (cant find a network and cant figure out where it is) Reason: minimize losses/accidents due to failures/ environmental variables.
# 5.) Damage/unforseen anomoly (shit happens...) Reason: need to make sure they are useful. broken robots not knowing they're broken would be bad.
# 6.) Tampering with internals (opening proprietary access ports/ machine) Reason: don't want bad actors reprogramming the bot :D
