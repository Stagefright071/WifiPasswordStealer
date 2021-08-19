mkdir compile
cp this.py compile
cp upx.exe compile
cd compile
pyinstaller --onefile this.py
cp .\dist\this.exe ..\runthis.exe
cd ..
Remove-Item .\compile\ -Recurse -Force -Confirm:$false