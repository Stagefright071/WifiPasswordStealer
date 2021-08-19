mkdir compile
cp final.py compile
cp upx.exe compile
cp notazip.zip compile
cd compile
pyinstaller --clean -y --onefile --add-data="notazip.zip;zips" final.py
cp .\dist\final.exe ..\final.exe
cd ..
Remove-Item .\compile\ -Recurse -Force -Confirm:$false