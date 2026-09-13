#!/bin/bash

for file in /run/user/1000/gvfs/google-drive:host=admin.sd.belajar.id,user=muhammad.fadlian138/0AI_DfUNoU6IcUk9PVA/1hm1RH1wyalxxfNMFy35dG-TYlyXW2aOl/1TTz7t4pe-V6Gpm1nBGbVvWCjpKg-ejYc/1S_17SBDMZapcz_aCc_d7ga01A6Gm6L1a/* ; do
	python /d/Works/pi/py/pillow.py "$file"
done
