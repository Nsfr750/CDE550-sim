@ECHO OFF
@REM CDE-Simulator
@x:
@cd "x:/GitHub/CDE550-sim"
@ECHO
@C:\Users\guara\AppData\Local\Programs\Python\Python312\python -m nuitka ^
--onefile ^
--mingw64 ^
--output-dir=x:/GitHub/CDE550-sim ^
--output-filename=CDE-Simulator.exe ^
--windows-icon-from-ico=x:/GitHub/CDE550-sim/icon.ico ^
--plugin-enable=pyqt6 ^
--follow-imports ^
--show-progress ^
--windows-company-name=Tuxxle ^
--copyright="(c)2025 by Nsfr750" ^
--windows-product-name="CDE550 Simulator" ^
--windows-product-version=0.0.1 ^
--windows-file-version=0.0.1 ^
x:/GitHub/CDE550-sim/main.py
@pause
