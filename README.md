# TranslateCura_sandbox
Python script for automatin Cura translation using googletrans and polib

# Limitations
Will blindly translate XML tags (fixing manually is ok for now since there's only 29 of these in all 4 files)
googletrans wil die sometimes (json.decoder.JSONDecodeError) because Google doesn't like it. Wait a few days or use VPN.

# TODO
Save translated texts into txt file so I don't translate same thing twice over multiple sessions.